import csv

fileName = input()
with open(fileName, encoding='utf-8-sig') as r_file:
    file = csv.reader(r_file, delimiter=",")
    count = 0
    array = []
    for line in file:
        if count == 0:
            print(line)
            lineLen = len(line)
            count += 1
        else:
            if len(line) != lineLen:
                continue
            if '' in line:
                continue
            array.append(line)
    print(array)