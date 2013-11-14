# Name: Sam Goldsmith
# Evergreen Login: Golsam27
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3

def f(n):
    curent = 1
    oldnum = 1
    awns = 1
    while (awns < n):
        curent, oldnum, awns = curent+oldnum, curent, awns+1
    return curent

for awns in range(10):
    print(f(awns))