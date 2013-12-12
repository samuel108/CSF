# Name: Sam Goldsmith
# Evergreen Login: golsam27
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

# import hw2_test

x = 0
for i in range(hw2_test.n):
    x = x + i
print x + hw2_test.n


###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

# for i in range (2, 11):
for i in range(2, 11):
    print 1 / i
###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

# n = 10
t = 0

for i in range (n+1):
    t = t + i
print "Tri num", n, "loop:", t
print "Tri num", n, "formula:", n*(n+1)/2
print

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

# num_factorial = input
num = 10
num2 = 1
for i in range (1, num + 1):
    num2 = num2 * i

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

# numberlines = 10

for i in range (1, numberlines + 1 ):
    f = (numberlines + 1) - i
    for i in range (1, f):
        f = f * i
    print (f)

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

# this problem threw me for a loop....

###
### Collaboration
###

# http://python-forum.org/,  http://stackoverflow.com/questions/203953/python-forums , http://forums.devshed.com/python-programming-11/ , and our text book
# ... as a comment (on a line starting with "#").

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
