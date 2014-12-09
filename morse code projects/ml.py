import RPi.GPIO as GP,time 
GP.setmode(GP.BOARD)
GP.setup(11,GP.OUT)

#creates the dash
def dash() :
    GP.output(11,GP.HIGH)
    time.sleep(1)
    GP.output(11,GP.LOW)
    time.sleep(0.5)

dash()

#creates the dot
def dot () :
    GP.output(11,GP.HIGH)
    time.sleep(0.5)
    GP.output(11,GP.LOW)
    time.sleep(0.5)

dot()


#the alphabet in morse code, using the dots and dashes (used above)
def MORSELETTER (char):
    if char == ("a"):
        dot() 
        dash()
        print ("a")
        
    elif char == ("b"):
        dash()
        dot()
        dot()
        dot()
        print ("b")

    elif char == ("c"):
        dash()
        dot()
        dash()
        dot()
        print ("c")
        

    elif char == ("d"):
        dash()
        dot()
        dot()
        print ("d")
        
    elif char == ("e"):
        dot()
        print ("e")

    elif char == ("f"):
        dot()
        dash()
        dot()
        print ("f")

    elif char == ("g"):
        dash()
        dash()
        dot()
        print ("g")

    elif char == ("h"):
        dot()
        dot()
        dot()
        dot()
        print ("h")

    elif char == ("i"):
        dot()
        dot()
        print ("i")

    elif char == ("j"):
        dot()
        dash()
        dash()
        dash()
        print ("j") 

    elif char == ("k"):
        dash()
        dot()
        dash()
        print ("k")
        

    elif char == ("l"):
        dot()
        dash()
        dot()
        dot()
        print ("l")

    elif char == ("m"):
        dash()
        dash()
        print ("m")

    elif char == ("n"):
        dash()
        dot()
        print ("n")
        
    elif char == ("o"):
        dash()
        dash()
        dash()
        print ("o")

    elif char == ("p"):
        dot()
        dash()
        dash()
        dot()
        print ("p")

    elif char == ("q"):
        dash()
        dash()
        dot()
        dash()
        print ("q")

    elif char == ("r"):
        dot()
        dash()
        dot()
        print ("r")

    elif char == ("s"):
        dot()
        dot()
        dot()
        print ("s")

    elif char == ("t"):
        dash()
        print ("t")

    elif char == ("u"):
        dot()
        dot()
        dash()
        print ("u")

    elif char == ("v"):
        dot()
        dot()
        dot()
        dash()
        print ("v")

    elif char == ("w"):
        dot()
        dash()
        dash()
        print ("w")

    elif char == ("x"):
        dash()
        dot()
        dot()
        dash()
        print ("w")

    elif char == ("y"):
        dash()
        dot
        dash()
        dash()
        print ("y")

    elif char == ("z"):
        dash()
        dash()
        dot()
        dot()
        print ("z")

    #adds a few extra things such as full-stops, commas etc. so it dosen't
    #confuse the user
    elif char == (" "):
        print (" ")

    elif char == ("?"):
        print ("?")

    elif char == ("!"):
        print ("!")

    elif char == (","):
        print (",")

    elif char == ("."):
        print (".")

    #if any other letters are used, which is impossible, it will say the below 
    else:
        print ("You have a strange alphabet")

#this is what the script will say when it's ready for you to enter your word/
#sentence
msg = input ("what do you want your pi to say?: ")
for each in msg:
    MORSELETTER(each)
                 


