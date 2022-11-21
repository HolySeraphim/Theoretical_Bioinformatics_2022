# ---------------------
# Score points settings
m = 1  # match
r = -1  # replacement
d = -1  # gap
# ---------------------


def tab_creating(seq1: str, seq2: str):
    tab = [[-1] * len(seq2) for _ in range(len(seq1))]
    for i in range(0, len(seq1)):
        tab[i][0] = i * d
    for j in range(0, len(seq2)):
        tab[0][j] = j * d
    for i in range(1, len(seq1)):
        for j in range(1, len(seq2)):
            if seq1[i] == seq2[j]:
                s = m
            else:
                s = r
            tab[i][j] = max(tab[i-1][j] + d, tab[i][j-1] + d, tab[i-1][j-1] + s)
    return tab


def printer(seq1: str, seq2: str, tab):
    ans1, ans2 = '', ''
    i, j = len(seq1) - 1, len(seq2) - 1
    while i + j != 0:
        if tab[i-1][j-1] >= max(tab[i-1][j], tab[i][j-1]):
            ans1 += seq1[i]
            ans2 += seq2[j]
            i, j = i - 1, j - 1
        else:
            if tab[i-1][j] >= tab[i][j-1]:
                ans1 += seq1[i]
                ans2 += '-'
                i = i - 1
            else:
                ans1 += '-'
                ans2 += seq2[j]
                j = j - 1
    print('\n\033[0mThe first sequence  :\033[92m', ''.join(reversed(ans1)),
          '\n\033[0mThe second sequence :\033[92m', ''.join(reversed(ans2)))


if __name__ == '__main__':
    sequence1 = ' ' + input('Enter the first sequence: ')
    sequence2 = ' ' + input('Enter the second sequence: ')
    table = tab_creating(sequence1, sequence2)
    printer(sequence1, sequence2, table)
