from time import sleep, clock

n =  0
def calculating (n):
    try:
        while True:
            a = clock()
            n = n + 1
            assert a<=30, "Houston we've got a problem"
    except AssertionError:
        print("time is out n ==", n)
    except KeyboardInterrupt:
        print("the program was interrupted prematurely ==", n)

if __name__ == "__main__":
    calculating(n)





