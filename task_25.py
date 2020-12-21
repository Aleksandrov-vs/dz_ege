def main():
    L = 174457
    R = 174505
    result = []
    for i in range(L, R+1):
        dividers = []
        count = 0
        print(i)
        for i1 in range(2, i):
            print(i1)
            if i % i1 == 0:
                dividers.append(i1)
                count += 1

        print(dividers)
        if count == 2:
            result.append(dividers)
        dividers = []
    print(result)


main()