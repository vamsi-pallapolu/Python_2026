# For loop

n = 4
for i in range(0, n):
    print(i)

# Find min
n = [10, 2, 3, 7]
min =  n[0]
for i in n:
    if i <= min:
        min = i
print(f"Minimum:{min}")


for element in range(len(n)):
    if element <= min:
        min = element

# While loop
count = 0
while count < 3:
    count +=1
    print("Hello World")

# Infinite while loop
# while True:
#     print("hello world")


# Nested Loop
"""
1
2 2
3 3 3
4 4 4 4
"""

for i in range(1, 5):
    for j in range(i):
        print(i, end= ' ')
    print()