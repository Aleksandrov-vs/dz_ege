def main():
    N = int(input())
    mas = [0, 0, 0]
    l = 0
    m = 1
    r = 2
    for i in range(0, N):
        value = int(input())
        if value > mas[m]:
            if value > mas[r]:
                mas[l] = mas[m]
                mas[m] = mas[r]
                mas[r] = value
            elif value < mas[r]:
                mas[l] = mas[m]
                mas[m] = value

        elif value < mas[m]:
            if value > mas[l]:
                mas[l] = value

    if mas[l] == 0:
        print('#')
    else:
        print(mas[l])


main()
