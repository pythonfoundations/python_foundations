import sys


def my_dec(function_to_decorate):
    def wrapper (a=""):
        while True:
            try:
                function_to_decorate(a)
            except Exception as e:
                return function_to_decorate(a)
    return wrapper


def my_dec_1(function_to_decorate):
    while True:
        def wrapper ():
            try:
                function_to_decorate()
            except Exception as e:
                return function_to_decorate()
        return wrapper


def mobile ():
    a = input("Which OS?\n"
              "In case iOS, press - '1'\n"
              "In case Android, press - '2'\n")
    assert (a == "2" or a == "1")
    if a == "1":
        a = "y"
        obj_c(a)
    if a == "2":
        a = "y"
        java(a)


def favorite_toy ():
    a  = input("When you were a kid, what was your favorite toy?\n"
               "In case 'Lego' press - 1\n"
               "In case 'Plasticine' press - 2\n"
               "In case you have old and ugly toy, but you love it so much press - 3\n")
    assert (a == '2' or a == '1' or a == "3")
    if a == "1":
        print("Your choice,as mine is Phyton ")
        sys.exit()
    if a == "2":
        print("Your choice is Ruby")
        sys.exit()
    if a == "3":
        print("Your choice is php")
        sys.exit()


def only_money ():
    a = "y"
    java(a)


def gaming():
    a = "y"
    c_plus(a)


@my_dec
def enterprise():
    a = input("What is your opinion about 'Microsoft'? \n"
              "In case you like it press - '1'\n"
              "In case you don't like it press - '2'\n"
              "In case it suck press - '3'\n")
    assert (a == '2' or a == '1' or a == "3")
    if a == 1:
        a = "y"
        c_sh(a)
    if a == 2:
        a = "y"
        java(a)
    if a == 3:
        a = "y"
        java(a)


@my_dec
def web():
    a = input("Does your WEB app provides info in real time like twitter?")
    assert (a == 'n' or a == 'y')
    if a == "y":
        js(a)
    else:
        a = input("Do you want to try something new with huge potential, but less mature?")
        if a == "y":
            js(a)
        if a == "n":
            ##@my_dec
            favorite_toy()
    raise AssertionError


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


@my_dec_1
def corporation ():
    a = input("In case your dream is work place a 'Facebook', press - '1'\n"
              "In case your dream is work place a 'Apple', press - '2'\n"
              "In case your dream is work place a 'Microsoft', press - '3'\n"
              "In case your dream is work place a 'Google', press - '4'\n")
    assert (a == '2' or a == '1' or a == "3" or a == "4")
    if a == 1:
        a = "y"
        phy(a)
    if a == 2:
        a = "y"
        obj_c(a)
    if a == 3:
        a = "y"
        c_sh(a)
    if a == 4:
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

#@my_dec_1
def phy (a):
    if a =="y":
        print ("Your choice,as mine is Phyton ")
        sys.exit()

@my_dec_1
def idea ():
    a = input("Have a brilliant idea/platform in a mind ?")
    assert (a == 'n' or a == 'y')
    if a == "y":
        wich_platform_1 ()
    if a != "y":
        learn ()

@my_dec_1
def wich_platform_1 ():
    a = input ("In case you are interested in WEB press - '1'\n "
               "In case you are interested in Enterprise press - '2'\n"
               "In case you are interested in Mobile press - '3'\n"
               "In case you are interested in 3D Gaming ? press - '4'\n")
    assert (a == '1' or a == '2' or a == '3' or a == '4')
    if a == "1":
        ##@my_dec
        web ()
    if a == "2":
        ##@my_dec
        enterprise()
    if a == "3":
        ##@my_dec
        mobile()
    if a == "4":
        ##@my_dec
        gaming()

@my_dec_1
def wich_platform_2 ():
    a = input("In case your are choice are  3D Gaming, press - '1'\n"
              "In case your choice are Enterprise, press - '2'\n"
              "In case your choice are Mobile, press - '3'\n"
              "In case you came to programming only for money, press - '4'\n"
              "In case your choice are working in big corporation, press - '5'\n"
              "In case your choice is WEB, press - '6'\n")
    assert (a == '1' or a == '2' or a == '3' or a == '4' or a == '5' or a == '6')
    if a == "1":
        ##@my_dec
        gaming()
    if a == "2":
        ##@my_dec
        enterprise()
    if a == "3":
        ##@my_dec
        mobile()
    if a == "4":
        ##@my_dec
        only_money()
    if a == "5":
        ##@my_dec
        corporation ()
    if a == "6":
        #@my_dec
        web_1 ()

@my_dec_1
def web_1 ():
    a = input("In case you want to make WEB Front-end (WEB - interface),press - '1'"
              "In case you want to make WEB back-end (WEB - brain) in corporate ,press - '2'"
              "In case you want to make WEB back-end (WEB - brain) in startup ,press - '3'")
    assert (a == '1' or a == '2' or a == '3')
    if a == "1":
        a = "y"
        js(a)
    if a == "2":
        a = "y"
        #@my_dec
        enterprise()
    if a == "3":
        #@my_dec
        web()

@my_dec_1
def learn ():
    a = input ("So you prefere to learn things... \n"
               "In case you prefer easy way press - '1'\n"
               "In case you prefer best way press - '2'\n"
               "The slightly harder way press - '3'\n"
               "The really HARD way, (but easier to study other languages in the future) - '4'\n"
               )
    assert (a == '1' or a == '2' or a == '3' or a == '4')
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


@my_dec_1
def make_monay():
    a = input("In case you want make monay by job, press - '1'\n"
              "In case you want make monay by implementation of startup, press - '2'")
    assert (a == '1' or a == '2')
    if a == "1":
        #@my_dec
        wich_platform_2()
    if a == "2":
        #@my_dec
       wich_platform_1()


#@my_dec_1
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
    print(a)
    print(a not in list(map(str, range(1, 7))))
#    assert (a == '1' or a == '2' or a == '3' or a == '4' or a == '5' or a == '6')
    if a not in list(map(str, range(1, 7))):
        print('fghjkl;lgfdfkgflfkflglgklglfk')
        return True
    if a =='1' or a == "2":
        a = "y"
        phy (a)
    if a == "3":
        make_monay()
    if a == "4" or a =="5" or a == "6":
        idea()


def aaa():
    b = True
    while b:
        print('77777777777777777777777777777777777777777777777777777777777')
        b = learn_programming()
        print(b)

aaa ()

#learn_programming()
# d = my_dec(learn_programming)
# d()
