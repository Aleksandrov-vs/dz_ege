def load_data():
    data = ''
    with open('./24.txt') as f:
        for line in f:
            data = data + line
    return data


def main():
    data = load_data()
    n = len(data)
    max_count = 0
    count = 0
    for i in range(0, n-2):
        if data[i+1] != data[i]:
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 0
    print(max_count + 1)   # так как мы считаем количество совпадений а не количество символов


main()