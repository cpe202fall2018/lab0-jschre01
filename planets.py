def weight_on_planets():
   # write your code here

   #setting mulitpliers abd user inputs
    mamu = .38
    jumu = 2.34

    weight = input("What do you weigh on earth? ")
    weight = int(weight)

    #setting weights on jupiter and saturn
    jupiter = (weight*jumu)
    mars = (weight*mamu)


    #print
    print('\nOn Mars you would weigh %g pounds.\nOn Jupiter you would weigh %g pounds.'% (mars,jupiter)) 
   
if __name__ == '__main__':
   weight_on_planets()
