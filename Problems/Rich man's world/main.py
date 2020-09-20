deposit = int(input())
n = 0
while deposit <= 700000:
    deposit = deposit * 1.071
    n += 1
print(n)