import sys

def mobile ():
    a = input("Which OS?\n"
              "In case iOS, press - '1'\n"
              "In case Android, press - '2'\n")
    l = ["2","1"]
    if a not in l:
        print("Value error, try again \n,\n,\n")
        return mobile()
    if a == "1":
        a = "y"
        obj_c(a)
    elif a == "2":
        a = "y"
        java(a)


def favorite_toy ():
    a  = input("When you were a kid, what was your favorite toy?\n"
               "In case 'Lego' press - 1\n"
               "In case 'Plasticine' press - 2\n"
               "In case you have old and ugly toy, but you love it so much press - 3\n")
    l = ["3", "1", "2"]
    if a not in l:
        print("Value error, try again \n,\n,\n")
        favorite_toy()
    if a == "1":
        print("Your choice,as mine is Phyton ")
        sys.exit()
    elif a == "2":
        print("Your choice is Ruby")
        sys.exit()
    elif a == "3":
        print("Your choice is php")
        sys.exit()


def only_money ():
    a = "y"
    java(a)


def gaming():
    a = "y"
    c_plus(a)

def enterprise():
    a = input("What is your opinion about 'Microsoft'? \n"
              "In case you like it press - '1'\n"
              "In case you don't like it press - '2'\n"
              "In case it suck press - '3'\n")
    l = ["2", "3", "1"]
    if a not in l:
        print("Value error, try again \n,\n,\n")
        return enterprise()
    if a == "1":
        a = "y"
        c_sh(a)
    elif a == "2":
        a = "y"
        java(a)
    elif a == "3":
        a = "y"
        java(a)

def web():
    a = input("Does your WEB app provides info in real time like twitter?")
    l = ["n", "y"]
    if a not in l:
        print ("Value error, try again \n,\n,\n")
        return web()

    if a == "y":
        js(a)
    else:
        a = input("So you want to try something new with huge potential, but less mature?")
        l = ["n", "y"]
        if a not in l:
            print ("Value error, try again \n,\n,\n")
            return web()
        if a == "y":
            js(a)
        if a == "n":
            favorite_toy()

def java (a):
    if a == "y":
        print ("Your choice is java")
        sys.exit()


def c (a):
    if a == "y":
        print ("Your choice is C")
        sys.exit()


def php (a):
    if a == "y":
        print ("Your choice is php")
        sys.exit()


def obj_c (a):
    if a == "y":
        print ("Your choice is objective-C")
        sys.exit()


def ruby (a):
    if a == "y":
        print( "Your choice is Ruby")
        sys.exit()


def corporation ():
    a = input("In case your dream is work place a 'Facebook', press - '1'\n"
              "In case your dream is work place a 'Apple', press - '2'\n"
              "In case your dream is work place a 'Microsoft', press - '3'\n"
              "In case your dream is work place a 'Google', press - '4'\n")
    l = ["1", "2", "3", "4"]
    if a not in l:
        print("Value error, try again \n,\n,\n")
        return corporation()
    if a == "1":
        a = "y"
        phy(a)
    if a == "2":
        a = "y"
        obj_c(a)
    if a == "3":
        a = "y"
        c_sh(a)
    if a == "4":
        a = "y"
        phy(a)


def js (a):
    if a == "y":
        print( "Your choice is Java script")
        sys.exit()


def c_plus (a):
    if a == "y":
        print ("Your choice is C ++")
        sys.exit()


def c_sh (a):
    if a =="y":
        print ("Your choice,as mine is C# ")
        sys.exit()

def phy (a):
    if a =="y":
        print ("Your choice,as mine is Phyton ")
        sys.exit()

def idea ():
    a = input("Have a brilliant idea/platform in a mind ?")
    l = ["n", "y", "ololo"]
    if a not in l:
        print("Value error, try again \n,\n,\n")
        return idea()
    if a == "y":
        wich_platform_1 ()
    if a != "y":
        learn ()

def wich_platform_1 ():
    a = input ("In case you are interested in WEB press - '1'\n "
               "In case you are interested in Enterprise press - '2'\n"
               "In case you are interested in Mobile press - '3'\n"
               "In case you are interested in 3D Gaming ? press - '4'\n")
    l = ['1', '2', "3", "4"]
    if a not in l:
        print("Value error, try again \n,\n,\n")
        return wich_platform_1()
    if a == "1":
        web ()
    if a == "2":
        enterprise()
    if a == "3":
        mobile()
    if a == "4":
        gaming()

def wich_platform_2 ():
    a = input("In case your are choice are  3D Gaming, press - '1'\n"
              "In case your choice are Enterprise, press - '2'\n"
              "In case your choice are Mobile, press - '3'\n"
              "In case you came to programming only for money, press - '4'\n"
              "In case your choice are working in big corporation, press - '5'\n"
              "In case your choice is WEB, press - '6'\n")
    l = ["1", "2", "3", "4", "5", "6"]
    if a not in l:
        print("Value error, try again \n,\n,\n")
        return wich_platform_2()
    if a == "1":
        gaming()
    if a == "2":
        enterprise()
    if a == "3":
        mobile()
    if a == "4":
        only_money()
    if a == "5":
        corporation ()
    if a == "6":
        web_1 ()


def web_1 ():
    a = input("In case you want to make WEB Front-end (WEB - interface),press - '1'"
              "In case you want to make WEB back-end (WEB - brain) in corporate ,press - '2'"
              "In case you want to make WEB back-end (WEB - brain) in startup ,press - '3'")
    l = ["1", "2", "3"]
    if a not in l:
        print ("Value error, try again \n,\n,\n")
        return web_1()
    if a == "1":
        a = "y"
        js(a)
    if a == "2":
        a = "y"
        enterprise()
    if a == "3":
        web()

def learn ():
    a = input ("So you prefere to learn things... \n"
               "In case you prefer easy way press - '1'\n"
               "In case you prefer best way press - '2'\n"
               "The slightly harder way press - '3'\n"
               "The really HARD way, (but easier to study other languages in the future) - '4'\n"
               )
    l = ["1", "2", "3"]
    if a not in l:
        print("Value error, try again \n,\n,\n")
        return learn()
    if a == "1":
        a = "y"
        phy(a)
    if a=="2":
        a = "y"
        phy(a)
    if a =="3":
        a = input("Manual or Auto car?\n"
                   "Auto press - 'a'\n"
                   "Manual press - 'm'\n")
        if a == 'a':
            a = "y"
            java(a)
        if a == 'm':
            a = "y"
            c(a)
    if a == "4":
        a = "y"
        c_plus(a)


def make_monay():
    a = input("In case you want make monay by job, press - '1'\n"
              "In case you want make monay by implementation of startup, press - '2'")
    l = ["1", "2"]
    if a not in l:
        print ("Value error, try again \n,\n,\n")
        return make_monay()
    if a == "1":
        wich_platform_2()
    if a == "2":
       wich_platform_1()

def learn_programming ():
    print("'Why do you want to learn programming', \nThroughout the program, if your answer is 'yes',press 'y'\n"
      "if your answer is 'no' click - n.\n In case the program give other instructions, use it."
      "In another way, program probably will crashed \n \nLets start \nSo why did you decide to learn programming?")
    a = input("I don't know, just pick one for me, press - '1'\n"
          "For my kids, press - '2' \n"
          "To make money, press - '3'\n"
          "Just for fun, press - '4'\n"
          "I'm interested, press - '5'\n"
          "Improve  my self - '6'\n")
    l = ["1", "2", "3", "4", "5", "6"]
    if a not in l:
          print("Value error, try again \n,\n,\n")
          return learn_programming ()
    if a =='1' or a == "2":
        a = "y"
        phy (a)
    if a == "3":
        make_monay()
    if a == "4" or a =="5" or a == "6":
        idea()

learn_programming()
