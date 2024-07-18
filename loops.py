# a loop is a iteration
# loop a string, a list, dict (key-worded)
# types: for-loop and the while


"""
FOR-LOOP
 
 syntax:
    for i in <iterable|range>:
        <block of code>
    """

# for i in range(15): [0, 1, 2, ..., 14]
#     print(f"{i}: hello world")

lst = ["banana", "mango", "pawpaw", "mellow"]
for fruit in lst:
    print(fruit)

price_dict = {
    "pencil": 10,
    "Biro": 10,
    "eraser": 5,
    "book": 130
}

for key, val in price_dict.items():
    print(f"{key} is sold at Ksh {val}")

# while 
"""syntax

    while <condition>:
        <blocks of code>
"""
# all odd numbers from 1 - 10
# i = 1

# while i <= 10:
#     print(i)
#     i += 1

# control intrunctions
# break statement - terminate/ stop a loop
# continue - control jump 

for j in range(10):
    # stop at j = 5
    if j == 5:
        break
    print(j)

print(" ------- ")
for k in range(10):
    if k == 5:
        continue
    print(k)

print("--while--")
l = 0
while l < 10:
    if l == 5:
        break
    print(l)
    l += 1
print("--while--")
p = 0
while p < 10:
    if p == 5:
        continue
    print(p)
    p += 1
