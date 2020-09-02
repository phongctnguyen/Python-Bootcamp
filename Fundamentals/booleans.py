print(20 > 15)
print(20 == 20)
print(20 < 15)

age = int(input("Enter your age: "))

can_learn = age > 0 and age < 100
print(can_learn)

not_working = age < 18 or age > 60
print(not_working)
