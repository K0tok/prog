sum = 0
while True:
    n = int(input())
    print(n)
    if n == 0:
        print(sum)
        break
    else:
        if n < 500:
            sum += n
        else:
            sum += n * 0.9
