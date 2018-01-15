num = input()
k = input()

while k:
    modified = False
    for i in range(len(num)):
        if num[i] > num[i+1]:
            num = num[:i] + num[i+1:]
            k -= 1
            modified = True
            continue

    if not modified:
        num = num[:len(num)-1]
        k -= 1
        modified = True

if num[0] == '0':
    num = num[1:]

print(num)
