#list comprehension
#1 - misol
lst_1 = [a**2 for a in range(1, 11)]
print(lst_1)

#2 - misol
lst_2 = [a for a in range(1, 21) if a % 2 == 0]
print(lst_2)

#3 - misol
lst_3 = [a for a in range(1, 31) if a % 2 != 0]
print(lst_3)

#4 - misol
roy = ["apple", "banana", "pear"]
lst_4 = [len(i) for i in roy]
print(lst_4)

#5 - misol
soz = "So'z"
lst_5 = [i for i in soz]
print(lst_5)

#6 - misol
lst_6 = [i**3 for i in range(1, 6)]
print(lst_6)
