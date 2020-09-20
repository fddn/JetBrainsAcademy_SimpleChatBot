initial = int(input())
quantity = int(input())

half_life_days = 12
day_counter = 0

while initial >= quantity:
    initial //= 2
    day_counter += 1

print(day_counter * half_life_days)