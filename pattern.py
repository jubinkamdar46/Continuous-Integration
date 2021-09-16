# Python 3.x code to demonstrate star pattern


def pypart(n):

    for i in range(0, n):


        for j in range(0, i + 1):

            print("* ", end="")


        print("\r")



n = 3
pypart(n)
