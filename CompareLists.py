#CompareLists
def compare(list_one, list_two):
    if list_one == list_two:
        print "The lists are the same"
    else:
        print "The lists are NOT the same"
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

compare(list_one, list_two)
#try1 = ([1,2,5,6,2],[1,2,5,6,2])
#try2 = ([1,2,5,6,5],[1,2,5,6,5,3])
#try3 = ([1,2,5,6,5,16],[1,2,5,6,5])
#try4 = (['celery','carrots','bread','milk'],['celery','carrots','bread','cream'])