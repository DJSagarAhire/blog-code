def levenshtein_recursive(str1, str2):

    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)

    ins = levenshtein_recursive(str1[:-1], str2) + 1
    dlt = levenshtein_recursive(str1, str2[:-1]) + 1
    sub = levenshtein_recursive(str1[:-1], str2[:-1]) + (0 if str1[-1] == str2[-1] else 1)

    return min(ins, dlt, sub)

def levenshtein_dp(str1, str2):

    distances = []
    distances.append(list(range(len(str2)+1)))

    for i in range(1, len(str1)+1):
        distances.append([])
        distances[i].append(distances[i-1][0] + 1)

        for j in range(1, len(str2)+1):
            ins = distances[i-1][j] + 1
            dlt = distances[i][j-1] + 1
            sub = distances[i-1][j-1] + (0 if str1[i-1] == str2[j-1] else 1)

            distances[i].append(min(ins, dlt, sub))
    
    return distances[-1][-1]
