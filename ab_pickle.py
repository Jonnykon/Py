#this solution shows how to use the pickle module to convert python objects into bytes(binary) and
#how to convert it back from bytes to the object
#
# WARNING: using pickle can be dangerous, because it might sending harmful python objects
# read more at: https://docs.python.org/3/library/pickle.html
import pickle

A,B = 0,0

FILENAME = "data.pickle"

while 1:

    #print("a = {}; b = {}".format(a,b))
    print("A = %d; B = %d" % (A,B))

    print("""
    set (a)
    set (b)
    (s)ave
    (l)oad
    (q)uit
    
    """)

    option = input("Option: ").lower()

    if option == "a":
        A = int(input("enter new value for a:"))

    elif option == "b":
        B = int(input("enter new value for b:"))

    elif option == "s":
        f = open(FILENAME, "wb")
        pickle.dump([a,b], f)
        f.close()

    elif option == "l":
        f = open(FILENAME, "rb")
        a,b = pickle.load(f)
        f.close()
        '''
        x = pickle.load(FILENAME)
        a = x[0]
        b =  x[1]
        '''
    elif option == "q":
        break

    else:
        print("\ninvalid option!\n")





