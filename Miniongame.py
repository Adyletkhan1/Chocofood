


def minion_game():
    # your code goes here
    s = input()
    vowels, L = 'AEIOU', len(s)
    K = sum([L - i for i in range(L) if s[i] in vowels])
    S = sum([L - i for i in range(L) if s[i] not in vowels])
    return (['Stuart ' + str(S), ['Kevin ' + str(K), 'Draw'][K == S]][K >= S])


