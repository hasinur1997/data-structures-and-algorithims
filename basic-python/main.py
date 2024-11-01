"""
1. Print
2. Variable
3. Condition
4. Loop
5. Function
6. Data structure (lists, dictionary, set, tuple)
"""

# Print someting

print("Hello World")

# Variable

name = "John Doe"
age = 60
is_younger = False
wealth = 200.50

print(name, age, is_younger, wealth)


# Condition
is_rainy_day = True

if is_rainy_day:
    print("Cook hotchpotch")

noodles = "sdf"

if noodles == "Maggi":
    print("Buy maggi noodles")
elif noodles == "Cocola":
    print("Buy cocola")
elif noodles == "Kulsum":
    print("Buy Kulsum")
else:
    print("Buy whatever you want")


if noodles == "Maggi":
    print("Buy maggi")
else:
    print("Whatever you want")



# For loop
# While loop

# for i in range(1, 100+1, 23):
#     print(i)

k = 10
n = 100
while k <= n:
    print(k)
    k = k + 10
