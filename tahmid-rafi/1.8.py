total_student = int(input())
total_amount = 0
x = total_student

while x > 0:
    amount = int(input())
    total_amount += amount
    print(total_amount)
    x -= 1

print(f"Total Amount: {total_amount}")

