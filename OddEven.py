#Odd or Even
stringNumber = "Number is "
stringOdd = ". This is an odd number"
stringEven = ". This is an even number"
def oddEven(stringNumber, stringOdd, stringEven):
    for i in range(1, 2001):
        if not (i%2==0):
            print stringNumber + str(i) + stringOdd

        if (i%2==0):
            print stringNumber + str(i) + stringEven


oddEven(stringNumber, stringOdd, stringEven)