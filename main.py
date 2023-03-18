def mainfunc1():
    listq = ["Q.1}In which type of change a new substance is formed?\n(a) In physical change\n(b) In chemical change\n(c) In both (a) and (b)\n(d) In neither of these",
             "Q.2}Which among the following is a physical change?\n(a) Cutting a log of wood in small pieces\n(b) Burning of wood\n(c) Ripening of fruit\n(d) Cooking of food",
             "Q.3}Which of the following is a chemical change?\n(a) Bursting of a fire cracker\n(b) Germination of seed\n(c) Coal formation from buried trees\n(d) All of these",
             "Q.4}Which is a method to prevent rust?\n(a) Crystallization\n(b) Sedimentation\n(c) Galvanisation\n(d) None of these",
             "Q.5}How crystal of pure substances are obtained?\n(a) By crystallization\n(b) By chromatography\n(c) By peptization\n(d) By all these methods",
             "Q.6}What will happen if carbon dioxide gas is passed through lime water?\n(a) Calcium carbonate is formed\n(b) The lime water turns milky\n(c) Both of these\n(d) None of these",
             "Q.7}Galvanisation is a process used to prevent the rusting of which of the following?\n(a) Iron\n(b) Zinc\n(c) Aluminium\n(d) Copper"]

    lista = ["b","a","d","c","a","c","a"]

    prizemoney = 0

#MAIN CODE OF mainfunc1():
    while True:

        print(listq[0])
        q1input = input("Enter the correct option:")
        if q1input == lista[0]:
            prizemoney += 1
            print("Congratulations, your answer is correct and you won Rs.",prizemoney,"Crore")
        else:
            print("Your answer is wrong, Game is over")
            break
        
        print(listq[1])
        q1input = input("Enter the correct option:")
        if q1input == lista[1]:
            prizemoney += 1
            print("Congratulations, your answer is correct and you won Rs.",prizemoney,"Crores")
        else:
            print("Your answer is wrong, Game is over")
            break

        print(listq[2])
        q1input = input("Enter the correct option:")
        if q1input == lista[2]:
            prizemoney += 1
            print("Congratulations, your answer is correct and you won Rs.",prizemoney,"Crores")
        else:
            print("Your answer is wrong, Game is over")
            break

        print(listq[3])
        q1input = input("Enter the correct option:")
        if q1input == lista[3]:
            prizemoney += 1
            print("Congratulations, your answer is correct and you won Rs.",prizemoney,"Crores")
        else:
            print("Your answer is wrong, Game is over")
            break

        print(listq[4])
        q1input = input("Enter the correct option:")
        if q1input == lista[4]:
            prizemoney += 1
            print("Congratulations, your answer is correct and you won Rs.",prizemoney,"Crores")
        else:
            print("Your answer is wrong, Game is over")
            break

        print(listq[5])
        q1input = input("Enter the correct option:")
        if q1input == lista[5]:
            prizemoney += 1
            print("Congratulations, your answer is correct and you won Rs.",prizemoney,"Crores")
        else:
            print("Your answer is wrong, Game is over")
            break

        print(listq[6])
        q1input = input("Enter the correct option:")
        if q1input == lista[6]:
            prizemoney += 1
            print("Congratulations, your answer is correct and you won Rs.",prizemoney,"Crores")
        else:
            print("Your answer is wrong, Game is over")
            break
        break

        
    print("You can take Rs.",prizemoney,"Crores with you")
    print("Thank you for playing our game")

#Main code
print("WELCOME TO KBC (Fake)")

playername = input("ENTER YOUR NAME:\n")

print("HELLO", playername)

print("Do you wish to proceed\nPress 1(to continue) and 2(to exit):")
reply1 = int(input())
if reply1 == 1:
    print("All the best!!!\n")
    print("Please give all answers only in 'a','b','c' and 'd'")
    mainfunc1()
elif reply1 == 2:
    print("We hope you liked the game\nThank You")