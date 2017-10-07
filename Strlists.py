# words = "It's thanksgiving day. It's my birthday, too!"
# print words.find('day')
# print words.replace("day", "month")

#min
# x = [2,54,-2,7,12,98]
# print min(x)

#max
# x = [2,54,-2,7,12,98]
# print max(x)

#First and Last
# x = ["hello",2,54,-2,7,12,98,"world"]
# print x[0], x[-1]

#New List
x2 = [19,2,54,-2,7,12,98,32,10,-3,6]
x2.sort()
# print x2

y = x2[:len(x2)/2]
z = len(x2)/2
result = x2[z:]
print y
print z

print y.append(result)