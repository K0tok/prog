l = []
l.append([int(input()), "Петя"])
l.append([int(input()), "Вася"])
l.append([int(input()), "Толя"])
print(l)
l = sorted(l, key=lambda x: x[0])


for i in range(3):
    print(f"{i+1}. {l[i][1]}")
