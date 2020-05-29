inputNum = int(input("숫자를 입력하세요 : "))

result = 0

for i in range(1, inputNum + 1):
    for j in range(1, i):
        if i % j == 0:
            result += j

    if result == i:
        print("%d" % (result))

    result = 0
