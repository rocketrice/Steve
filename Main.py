from Response import Response

class Main(object):
    Steven = Response()
    print Steven.getRep("hello")

    #response... this is a reocurring name if you haven't already noticed...
    rep = ""
    myInput = ""

    print "\nYour wish is my command."

    #this is the main loop for the program
    while rep != "\nAlright, see you later Rice.":
        myInput = raw_input()
        rep = Steven.getRep(myInput)
        print rep
        
        
    
