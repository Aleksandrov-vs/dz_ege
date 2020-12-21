
def load_data(name):
    data = []
    with open(f'./{name}') as f:
        size = f.readline()
        size = int(size)
        sum = 0
        for line in f:
            try:
                f_v, s_v = line.split('  ')
            except:
                f_v, s_v = line.split(' ')
            f_v = int(f_v)
            s_v = int(s_v)
            difference = abs(f_v - s_v)
            data.append([f_v, s_v, difference])
            sum += max(f_v, s_v)
    return size, data, sum


def search_max_sum(name):
    size, data, sum = load_data(name)
    while (sum % 3) == 0:
        min_dif = 300000
        pair_index = 0
        for i in range(0, size):
            dif_pair = data[i][2]

            if min_dif > dif_pair and dif_pair % 3 != 0:
                min_dif = dif_pair
                pair_index = i
        f_v = data[pair_index][0]
        s_v = data[pair_index][1]
        sum -= max([f_v, s_v])
        sum += min([f_v, s_v])

        if sum % 3 == 0:
            data[pair_index][2] = 300000
            sum += max([f_v, s_v])
            sum -= min([f_v, s_v])
    print(sum)


def main():
    file_name = ['27-A.txt', '27-B.txt']
    for name in file_name:
        search_max_sum(name)


main()