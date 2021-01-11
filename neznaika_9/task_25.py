def main():
    A = []
    N = 30
    for i in range(0, N):
        chsl = int(input())
        A.append(chsl)
    max = -1001
    for i in range(0, N):
        if A[i] % 10 == 5 and A[i] > -1:
            max = A[i]

    if max == -1001:
        print('не найдено')
    else:
        print(max)


main()
