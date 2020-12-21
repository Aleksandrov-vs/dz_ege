def main():
    count = int(0)
    max = int(0)

    for number in range(1016, 7938):
        if (number % 3) == 0:
            if (number % 7) != 0 and (number % 17) != 0 and (number % 19) != 0 and (number % 27) != 0:
                count = count + 1
                if max < number:
                    max = number
    print(count, max)


main()
