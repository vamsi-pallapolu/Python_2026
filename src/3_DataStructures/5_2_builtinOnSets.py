# Maximum and minimum 
s1 = {1, 2, 3}
print(max(s1))
print(min(s1))

# Using sorted
s1 = {3, 1, 2}
sorted_s1 = sorted(s1)
print(f"Minimum: {sorted_s1[0]}")
print(f"Maximum: {sorted_s1[-1]}")

# Using loops
s1 = {3, 1, 2}

min_value = float('inf')
max_value = float('-inf')

for value in s1:
    if value < min_value:
        min_value = value
    if value > max_value:
        max_value = value

print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")