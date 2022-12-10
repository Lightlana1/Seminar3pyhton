res = 0
lst = ['qwe', 'asd', 'zxc', 'ertqwe', 'qwe']
ask = 'qwe'
count = 0
for i in range(len(lst)):
    if lst[i] == ask:
        count += 1
        print(count)

    if count == 2:
        res = i
        break
print(res)