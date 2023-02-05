def main():
    lines = [
        '3',
        'Hello #name',
        '2',
        '2',
        '#NAME Kenta',
        '#from America',
        '2',
        '#name Yuta',
        '#from America',
    ]
    temp = lines[1]

    # 追加①
    if not ('#' in temp):
        print("Error: Lack of data")
        exit()

    substitution = []
    for i in range(3, len(lines)):
        if len(lines[i]) == 1:
            substitution.append(lines[i+1:i+1+int(lines[i])])

    for v in substitution:
        substitution_num = len(v)  # 追加②
        temp_copy = temp
        for i in range(substitution_num):  # 追加③
            split = v[i].split()
            if split[0] in temp_copy:
                temp_copy = temp_copy.replace(split[0], split[1])

        # 追加④
        if '#' in temp_copy:
            print("Error: Lack of data")
            continue
        # 追加⑤
        print(temp_copy)

main()
