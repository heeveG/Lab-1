import copy


def first_part(file):
    """
    :param file: srt
    :return: (str, str)
    Adds line by line from file followed by vowels from that line to the result string
    """
    f = open(file)
    cp = ''
    res = ''
    for line in f:
        if cp == '':
            cp = copy.deepcopy(line)
        vow_dict = dict()
        lst = []
        for char in line:
            if char in vowels:
                if char not in vow_dict.keys():
                    vow_dict[char] = 1
                else:
                    vow_dict[char] += 1
        for k, v in vow_dict.items():
            lst.append((k, v))
        lst = sorted(lst, key=lambda x: x[1])
        res += line[:-1] + "".join([l[0] for l in lst])
        res += '\n'
    f.close()
    return (res, cp)


def second_part(res, cp, file):
    """
    :param res: str
    :param cp: str
    :param file: str
    :return: str
    Adds consonant letters in columns to a result string
    """
    f = open(file)
    lines = f.readlines()
    letters = []
    for i in range(len(cp)):
        change = []
        for line in lines:
            change.append(line[i])
        letters.append(change)
    for i in range(len(letters)):
        n = sorted(letters[i])
        n = list(set(n))
        m = []
        for j in range(len(n)):
            if n[j] in vowels or n[j] == '' or n[j] == ' ':
                pass
            else:
                m.append(n[j])
        m = sorted(m)
        if len(m) != len(letters[i]):
            num = len(letters[i]) - len(m)
            for bl in range(num):
                m.append('')
        letters[i] = m
    for i in range(len(letters[0])):
        for j in range(len(letters)):
            if letters[j][i] == '':
                res += ' '
            else:
                if letters[j][i] == '\n':
                    pass
                else:
                    res += letters[j][i]
        res += '\n'
    f.close()
    return res


if __name__ == "__main__":
    vowels = {'a', 'e', 'i', 'o', 'u'}
    res_1 = first_part('text_1.txt')
    res = second_part(res_1[0], res_1[1], 'text_1.txt')
    new_f = open('new.txt', 'w')
    new_f.write(res)
    new_f.close()