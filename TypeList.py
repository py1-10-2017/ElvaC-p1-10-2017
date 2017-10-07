#Typelist
mixed_list = ['magical unicorns',19,'hello',98.98,'world']
integer_list = [2,3,1,7,4,12]
string_list = ["magical", "unicorns", "majestic"]


def identify_list_type(lst):
    new_string = ''
    total = 0

    for value in lst:
            if isinstance(value, int) or isinstance(value, float):
                total += value
            elif isinstance(value, str):
                new_string += (value + " ")

                if new_string and total:
                    print "Mixed type"
                    print "String:", new_string
                    print "Total:", total

                elif new_string:
                    print "String type"
                    print "String:", new_string

                else:
                    print "Number(float or int) type"
                    print "Total:", total

print identify_list_type(mixed_list)
print identify_list_type(integer_list)
print identify_list_type(string_list)