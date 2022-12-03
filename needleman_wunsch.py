from PAM250 import PAM250
# ---------------------
# Score points settings
m = 1  # match
r = -2  # replacement
d = -1  # gap
# ---------------------


def tab_creating(seq1: str, seq2: str):
    seq1, seq2 = seq1.upper(), seq2.upper()
    tab = [[-1] * len(seq2) for _ in range(len(seq1))]
    for i in range(0, len(seq1)):
        tab[i][0] = i * d
    for j in range(0, len(seq2)):
        tab[0][j] = j * d
    mode = 0
    for elem in seq1:
        if elem not in ['A', 'T', 'G', 'C', ' ']:
            mode += 1
            break
    for elem in seq2:
        if elem not in ['A', 'T', 'G', 'C', ' ']:
            mode += 1
            break
    for i in range(1, len(seq1)):
        for j in range(1, len(seq2)):
            if mode == 0:
                if seq1[i] == seq2[j]:
                    s = m
                else:
                    s = r
            else:
                s = PAM250[seq1[i]][seq2[j]]
            tab[i][j] = max(tab[i-1][j] + d, tab[i][j-1] + d, tab[i-1][j-1] + s)
    if mode == 0:
        print('\033[94mNucleotide mode is used', end='')
    else:
        print('\033[94mProtein mode is used', end='')
    return tab


def printer(seq1: str, seq2: str, tab):
    seq1, seq2 = seq1.upper(), seq2.upper()
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
          '\n\033[0mThe second sequence :\033[92m', ''.join(reversed(ans2)),
          '\n\033[0mThe numer of gaps   :\033[91m', (''.join(reversed(ans1))+''.join(reversed(ans2))).count('-'))


if __name__ == '__main__':
    from fasta_reader import *
    sequence1 = ' ' + str(fasta(choose_file()))
    sequence2 = ' ' + str(fasta(choose_file()))
    table = tab_creating(sequence1, sequence2)
    printer(sequence1, sequence2, table)
