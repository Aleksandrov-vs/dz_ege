
DATA = []


def load_data():
    with open('./26.txt') as f:
        size, count = f.readline().split(' ')
        size = int(size)
        count = int(count)
        for line in f:
            DATA.append(int(line))
    return size, count


def main():
    size, count = load_data()
    DATA.sort()
    sum = 0
    count = 0
    max_el = int
    # количество элементов которые влезут
    for i in range(0, len(DATA)):
        if DATA[0] <= size:
            count += 1
            el = DATA.pop(0)
            max_el = el
            size -= el
    # берем сумму последнего элемента и оставшйся памяти и сотрим какой наибольший элемент влезет
    rest_disk_space = max_el + size
    for i in range(0, len(DATA)):
        if rest_disk_space > DATA[i]:
            max_el = DATA[i]
    print(count, max_el)


main()