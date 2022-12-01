#Set up
gn = "Bibo"
print ("\nWelcome Adventurer to ", gn,"!\nHere you can play all sorts of text based puzzle-adventure games related to rusty lake!\n")

error = ("I don't quite understand it. Please answer it again.") #for incorrect entries

#Intro
while True:
    q1 = str(input("Are you familiar with the plot of rusty lake? [Y(es)/N(o)]\n"))
    if q1 == "N":
        print ("Rusty lake is a surrealistical game series connected to the history of the Eilanders and the Vanderbooms, which both lived by rusty lake in the 1890s.\nGood Luck!")
        #To give info about rusty lake
        break  
    elif q1 != "Y":
        print (error)
    else:
        print ("Alright then, you should get going on your unique journey.")
        break

while True:
    pn = str(input("What's your name?\n"))
    q = str(input("Are you sure that is your name? [Y(es)/N(o)]\n"))
    if q == "N":
        print (pn)
    elif q != "Y":
        print (error)
    else:
        break
print("Ok", pn)

#Game starting
print("Short Story begins!")
print(pn, "You are now trapped in the centre of an unfamiliar room facing NORTH in the middle of nowhere!")
print("The room is nicely furnished in a Vintage European Style with four walls in the shade of Luxury Green around you\n")
print("You are now going to escape this room and find out what is happening!\n")
while True: 
    c1 = str(input("In front of you, there's a door. Do you want to: \nA)try to open it? \nB)or take a look around?\n"))
    if c1 == "A":
        print("It's LOCKED! Go look a round ")
        c2 = str(input("Which way do you want to turn?\n[E(ast)/W(est)/S(outh)]\n"))
        break
    elif c1 != "B":
        print(error)
    else:
        c2 = str(input("Which way do you want to turn?\n[E(ast)/W(est)/S(outh)]\n"))
        break

while True:
    if c2 == "E":
        print("You're now facing east")
        print("There's a picture hanging on the wall and a sewing mannequin standing in front of you.")
        c3 = str(input("Do you want to have a closer look at the items? [Y(es)/N(o)]\n"))
        if c3 == "Y":
            c4 = str(input("Which one do you want to look at? \nA)The picture \nB)The sewing mannequin\n"))
            if c4 == "A":
                print("There's a woman hanging upside down with her eyes tore out.")
                print("The woman seems familiar to you.\nBut you have no idea who she is.")
                print("Under the picture, you can see a label 'Laura Vanderboom'.")
                c3 = str(input("Do you want to keep looking? [Y(es)/N(o)]\n"))
            elif c4 != "B":
                print(error)
            else:
                print("The mannequin is wearing a BLUE formal tuxedo with premium wool.")
                print("On top of the mannequin, there're threads losing out.")
                c5 = str(input("Do you want to\n A) pull on the lose threads?\n B) just leave it there?\n"))
                if c5 == "A":
                    print("You pull on the lose threads.")
                    print("You accidentally fix the tuxedo.")
                    print("And the BLUE tuxedo magically appeared on your body.")
                    c3 = str(input("Do you still want to look at the picture or the sewing mannequin(Y/N)\n"))
                elif c5 == "B":
                    c2 = str(input("Which way do you want to turn?\n[E(ast)/W(est)/S(outh)]\n"))
                else:
                    print(error)
        elif c3 != "N":
            print(error)
        else:
            c2 = str(input("Which way do you want to turn?\n[E(ast)/W(est)/S(outh)]\n"))
    elif c2 == "W":
        print("You're now facing west.")
        print("There's a set of drawer and there's a clock and a telephone on top of it in front of you.")
        c7= str(input("Do you want to take a closer look? [Y(es)/N(o)]\n"))
        if c7 == "Y":
            c8 = str(input("Which one do you want to look at? \n A) the drawers\n B) the clock \n C) the telephone\n"))
            if c8 == "A":
                print("_________________")
                print("|       1       |")
                print("-----------------")
                print("|       2       |")
                print("-----------------")
                print("|       3       |")
                print("-----------------")
                print("|_______4_______|")
                c9 = int(input("Which drawer do you want to open? (1/2/3/4)\n"))
                if c9 == 1:
                    print ("There's nothing inside.")
                    c10 = str(input("Do you wanna keep looking? [Y(es)/N(o)]\n"))
                    if c10 == "Y":
                        print(c9)
                    elif c10 == "N":
                        c2 = str(input("Which way do you want to turn?\n[E(ast)/W(est)/S(outh)]\n"))
                    else:
                        print(error)
                elif c9 == 2:
                    print("It's locked")
                    c12 = str(input("Do you know the four digit password? [Y(es)/N(o)]\n"))
                    if c12 == "Y":
                        c13 = str(input("Please enter the password: _ _ _ _\n"))
                        if c13 == "1935":
                            print("There's two bottles of liquid.")
                            print("One has BLUE liquid inside with a label 'Harvey'")
                            print("The other one has RED liquid inside with a label 'Bloody Mary'")
                            c14 = str(input("*FINAL DECISION* Which liquid do you want to drink? [R(ed)/B(lue)]\n"))
                            if c14 == "R":
                                print("You're dead")
                                print("You transform to a person named 'Bob Hill'.")
                                print("You are transfered to a mental health faculty")
                                print("The White Door")
                                print("To be Continued...")
                                break
                            elif c14 == "B":
                                print("The door opens")
                                print("Mr.Owl is waiting for you.")
                                print("He says, 'Welcome to your memory'")
                                print("Harvey")
                                print("END")
                                break
                        else:
                            print("It's wrong, please try it again!")
                            print(c12)
                    elif c12 == "N": 
                        c10 = str(input("Do you wanna keep looking? [Y(es)/N(o)]\n"))
                        if c10 == "Y":
                            print(c9)
                        elif c10 == "N":
                            c2 = str(input("Which way do you want to turn?\n[E(ast)/W(est)/S(outh)]\n"))
                            break
                        else:
                            print(error)
                elif c9 == 3:
                    print("There's nothing there.")
                    c10 = str(input("Do you wanna keep looking? [Y(es)/N(o)]\n"))
                    if c10 == "Y":
                        print(c9)
                    elif c10 == "N":
                        c2 = str(input("Which way do you want to turn?\n[E(ast)/W(est)/S(outh)]\n"))
                        break
                elif c9 == 4:
                    print("There's a picture of a man figure in a tuxedo with an OWL head.")
                    c10 = str(input("Do you wanna keep looking? [Y(es)/N(o)]\n"))
                    if c10 == "Y":
                        print(c9)
                    elif c10 == "N":
                        c2 = str(input("Which way do you want to turn?\n[E(ast)/W(est)/S(outh)]\n"))
                        break
                else:
                    print("We don't have a {}th drawer".format(c9))
                    c10 = str(input("Do you wanna keep looking? [Y(es)/N(o)]\n"))
                    if c10 == "Y":
                        print(c9)
                    elif c10 == "N":
                        c2 = str(input("Which way do you want to turn?\n[E(ast)/W(est)/S(outh)]\n"))
                        break
            elif c8 == "B":
                print("The clock shows 19:35")
                c10 = str(input("Do you wanna keep looking? [Y(es)/N(o)]\n"))
                if c10 == "Y":
                    print(c2)
                elif c10 == "N":
                    print(c2)
                else:
                    print(error)
            elif c8 == "C":
                print("There's someone calling right now and ysou heard a familiar voice.")
                print("It says\nHello...This is Mr.Owl...\n'Some may find this place hard to leave'\n'There will be blood'\n'The past is never dead, it's not even the past.'\n")
                print("You get goosegumps all over your body, but the voice calms you down.")
                print("At last, he says\n'Find your *FATE*'\n")
                c10 = str(input("Do you wanna keep looking? [Y(es)/N(o)]\n"))
                if c10 == "Y":
                    print(c2)
                elif c10 == "N":
                    break
            else: 
                print(error)
        elif c7 == "N":
            print ("Ok, let's keep looking!")
            c2 = str(input("Which way do you want to turn?\n[E(ast)/W(est)/S(outh)]\n"))
    elif c2 == "S":
        print("You're now facing south.")
        print("There's a mirror in front of you.")
        c11 = str(input("Do you want to look at your face closely? [Y(es)/N(o)]\n"))
        if c11 == "Y":
            print("You have blue skin, blue eyes, blue lips, blue hair and a blue tongue.")
            print("Now, you wonder if your blood is also blue.")
            print("The blueness in your veins seems to remind you that you are something special.")
            c2 = str(input("Which way do you want to turn?\n[E(ast)/W(est)/S(outh)]\n"))
        elif c11 == "N":
             c2 = str(input("Which way do you want to turn?\n[E(ast)/W(est)/S(outh)]\n"))
        else:
            print(error)
    else:
        print(error)
        c2 = str(input("Which way do you want to turn?\n[E(ast)/W(est)/S(outh)]\n"))   

        






