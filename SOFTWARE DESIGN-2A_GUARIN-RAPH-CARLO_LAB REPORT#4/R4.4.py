def reverse(S, start, stop):
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)


S = [44, 6, 8, 9, 2]
reverse(S, 0, 5)
print(S)
