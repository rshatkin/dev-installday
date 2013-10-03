# it seems that the value of o1, 010, 0100 and 01000 respectively are: 1, 8, 64, and 512
# each is the number before multipled by 8
# if we are dealing with octal number systems, only the numbers 1-7 are valid, 
# which is why 02492 is invalid (9 is not octal)

# so the first number '0' is the number of 1's (0), then the next is the number of 'eights' (2) (8 columm), 
# followed by 'eight' times the 'number of eights in 8 column' (one 8 * 8) = 64
# followed by one 8 * 8 * 8 (the 4th number is "3" denoting three 8's) 64, 64*8 = 512
# the fifth and final number is '2', 2*1

(2*512)+(1*64)+(3*8)+(2*1)
# 02132, is like saying "2 'ones', 3 'eights', 1 '64', and 2 '512s', and zero is '0' 
# Hence, 1114

#2.2
# >>> 5
# 5
# >>> x = 5
# >>> x + 1
# 6

5
x = 5
x + 1

print 5
x = 5
print x + 1

# By running the commands in script format, I do not recieved an (visually) automatic response back
# The output for the script directly above would be:
# 5
# 6


#2.3


