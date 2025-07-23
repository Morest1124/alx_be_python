#Task 2
"""for num in range(1, 11):
    total = 0
    if num > 0 < 11:
        total += num
        print(total)"""

number = int(input("Enter a number to see its multiplication table: "))


for num in range(1, 11):
    product = number * num
    print(f"{number} * {num} = {product}")

