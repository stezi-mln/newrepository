def without_five():
    count = 0
    num = []
    for x in range(a, b + 1):
        if str(i) not in str(x):
            count += 1
            num.append(x)

    return count, num


#rint("Задача рахує кількість чисел в діапазоні,окрім чисел які містять певну цифру а також виводить сам діапазон з чисел які вводить користувач")
#a = int(input("Введіть початок діапазону:"))
#b = int(input("Введіть кінець діапазону:"))
#i = input("Введіть число яке не має міститись у діапазоні:")

#number = list(without_five())

#print(f"Кількість:{number[0]}")
#print(f"Список чисел:{number[1]}")




n = lambda x:print(x**2)
n(5)

def power(n):
    def inner(x):
        return x**n
    return inner
