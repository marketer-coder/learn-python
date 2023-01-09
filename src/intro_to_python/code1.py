# swapping normal
x = 1
y = 5
t = x
x = y
y = t

# swapping without temp variable
x = 1
y = 5
x = x + y
y = x - y
x = x - y

# swapping python
x, y = 1, 5
x, y = y, x

# printing table of 2
for x in range(1, 11):
    print(x*2)
