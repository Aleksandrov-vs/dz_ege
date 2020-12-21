data = []


def load_data():
    with open('./18.csv', 'r', encoding='utf-8') as f:
        f.readline()
        for line in f:
            data.append(line.split(';'))


def main():
    pass


main()