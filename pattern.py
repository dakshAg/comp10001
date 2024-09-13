# Patterns for W5 Slides
for i in range(10):
    print(" "*(10-i) + "*"*(2*i))
    
for i in range(5):
    print("*"*(5-i)*2)
for i in range(3,-1,-1):
    print("*"*(5-i)*2)

for i in range(2):
    print("*"*10)
for i in range(2):
    print("*"*2)
for i in range(1):
    print("*"*10)
for i in range(2):
    print(" "*8+"*"*2)
for i in range(2):
    print("*"*10)


for i in range(4):
    print("*"*2+" "*6+"*"*2)
for i in range(1):
    print("*"*10)
for i in range(4):
    print("*"*2+" "*6+"*"*2)


def average_of_three(a, b, c):
    return (a + b + c) / 2

result = average_of_three(10, 20, 30)
print(f"The average is: {result}")