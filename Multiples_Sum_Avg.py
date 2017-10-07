#Multiples, Sum, Average Assignmnent

#Multiples
#Part 1
# for i in range(1, 1000, 2):
#     print i

#Part 2
# for i in range(5, 1000000, 5):
#     print i

#Sum List
# sum = 0
# for a in [1, 2, 5, 10, 255, 3]:
#     sum = sum + a
# print sum

# Another way to do the Sum List
# a = [1, 2, 5, 10, 255, 3]
# sum = 0
# for x in a:
#     sum = sum + x
# print sum

#Average List
a = [1, 2, 5, 10, 255, 3]
alength = len(a)
print alength
sum = 0 

for i in a:
    sum = sum + i
    avg = sum/alength
print avg