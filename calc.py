numbers = [1,2,3,4,5,6,7,8,9]
amount = 0
for number in numbers:
    amount += number
print(amount)
amount = 1
for number in numbers:
    amount *= number
print(amount)
amount = 1
for number in numbers:
    amount /= number
print(amount)
amount = 0
for number in numbers:
    amount -= number
print(amount)