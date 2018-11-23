import sys

a = ['--opt3', '2', '--files', '*.c', '*.java', '--opt1', 'True']
b = ['--opt3', '2', '--opt1=True', '--files', '*.c', '*.java']
c = ['--opt1', 'False', '--opt3', '2', '--files', '*.c', '*.java']
d = ['--opt1=False', '--opt3', '2', '--files', '*.c', '*.java']
e = d = ['--opt3', '2', '--files', '*.c', '*.java']

def cw_12 (list_0, list_1, list_2, list_3, list_4):
    ololo = None
    choice = input("input number of line you want to choose")
    l = ["a", "b", "c", "d", "e"]
    if choice in l:
        if choice == "a":
            for i in a:
                if i == "--opt1=False":
                    print("<p>opt1 is False</p>")
                    sys.exit()
                if i == "--opt1=True" or i == "--opt1" and a [a.index(i)+1] == "True" in a:
                    ololo = True
                    if ololo == True:
                        print("<p>opt1 is True!</p>")
                        sys.exit()
                else:
                    ololo = False
        if ololo == False:
            print("<p>opt1 is False</p>")
            sys.exit()

        if choice == "b":
            for i in b:
                if i == "--opt1=False":
                    ololo = False
                if i == "--opt1=True" or i == "--opt1" and b [b.index(i)+1] == "True" in b:
                    ololo = True
                    if ololo == True:
                        print("<p>opt1 is True!</p>")
                        sys.exit()
                else:
                    ololo = False
        if ololo == False:
            print("<p>opt1 is False</p>")
            sys.exit()

        if choice == "c":
            for i in c:
                if i == "--opt1=False":
                    print("<p>opt1 is False</p>")
                    sys.exit()
                if i == "--opt1=True" or i == "--opt1" and c [c.index(i)+1] == "True" in c:
                    ololo = True
                    if ololo == True:
                        print("<p>opt1 is True!</p>")
                        sys.exit()
                else:
                    ololo = False
        if ololo == False:
            print("<p>opt1 is False</p>")
            sys.exit()

        if choice == "d":
            for i in d:
                if i == "--opt1=False":
                    print("<p>opt1 is False</p>")
                    sys.exit()
                if i == "--opt1=True" or i == "--opt1" and d [d.index(i)+1] == "True" in d:
                    ololo = True
                    if ololo == True:
                        print("<p>opt1 is True!</p>")
                        sys.exit()
                else:
                    ololo = False
        if ololo == False:
            print("<p>opt1 is False</p>")
            sys.exit()

        if choice == "e":
            for i in e:
                if i == "--opt1=False":
                    print("<p>opt1 is False</p>")
                    sys.exit()
                if i == "--opt1=True" or i == "--opt1" and e[e.index(i) + 1] == "True" in e:
                    ololo = True
                    if ololo == True:
                        print("<p>opt1 is True!</p>")
                        sys.exit()
                else:
                    ololo = False
        if ololo == False:
            print("<p>opt1 is False</p>")
            sys.exit()

    else: print("Value error, please try again")
    return cw_12(a, b, c, d, e)

cw_12 (a, b, c, d, e)