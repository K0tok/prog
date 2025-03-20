a = input()
b = int(input())
c = int(input())
d = int(input())

print("================Чек================")
print("Товар:" + a.rjust(29))
print("Цена:" + (str(c) + "кг * " + str(b) + "руб/кг").rjust(30))
