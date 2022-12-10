# найти число и вернуть
lst = ['ble', 'abc', '56']
f = False
for i in range(len(lst)):
    if '2' in lst[i]:
        f = True
        break
print(f)