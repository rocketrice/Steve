class Response(object):
    response = ""


    #this is the method that is called when steven receives a command
    def getRep(self, rep):
        if rep == "hello" or rep == "hi":
            return "\nHello Rice."

        if rep == "power off" or rep == "poweroff" or rep == "shutdown":
            return "\nAlright, see you later Rice."


        #for future analysis, all unkown commands are saved in a file.    
        f = open('UnknownCommands.txt', 'r')
        fil = f.read()
        f.close()
        f = open('UnknownCommands.txt', 'w')
        f.write(fil + rep + "\n")
        f.close()
        return "I'm sorry, I didn't understand the statement."
