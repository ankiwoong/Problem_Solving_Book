def sumEachNum(n):
    sumValue = n
    while n > 0:
        sumValue += n % 10
        n //= 10
    return sumValue


# 제너레이터 설정
rangeNum = 15

# 제너레이터가 있는 숫자들의 합
generaterExist = [sumEachNum(i) for i in range(rangeNum)]
print(generaterExist)
generaterNotExist = [i for i in range(rangeNum) if not (i in generaterExist)]
print(generaterNotExist)
print(sum(generaterNotExist))
