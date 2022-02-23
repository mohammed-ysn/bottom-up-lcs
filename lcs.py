def table(s1, s2):
    # add an extra row and column for the empty string
    tbl = [[None for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0 or j == 0:
                # empty string
                tbl[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                # both end characters are the same
                tbl[i][j] = tbl[i - 1][j - 1] + 1
            else:
                # both end characters are different
                # get max of above and left cell
                tbl[i][j] = max(tbl[i - 1][j], tbl[i][j - 1])

    return tbl

def match_length(tbl):
    # the bottom-right number is the longest length
    return tbl[-1][-1]

def match_string(s1, s2, tbl):
    char_i = tbl[len(s1)][len(s2)] - 1

    subseq = ['' for _ in range(char_i + 1)]

    # start off at the bottom-right number
    i = len(s1)
    j = len(s2)

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            # common character
            subseq[char_i] = s1[i - 1]
            # go diagonally up and left
            i -= 1
            j -= 1
            char_i -= 1
        elif tbl[i - 1][j] >= tbl[i][j - 1]:
            # above value is greater than (or equal to) left value
            # go up
            i -= 1
        else:
            # left value is greater than above value
            # go left
            j -= 1

    return ''.join(subseq)

s1 = 'ABBA'
s2 = 'CACA'
tbl = table(s1, s2)
print(match_length(tbl))
print(match_string(s1, s2, tbl))