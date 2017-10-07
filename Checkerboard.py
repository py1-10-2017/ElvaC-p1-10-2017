#Find checkerBoard
def checkerboard():
    for x in range (0, 8):
        if x%2 == 0:
            print "* " * 4
        else:
            print " *" * 4

checkerboard()