print("Hello Stephen this is Leo's homework")
print("I can solve ax^2+bx+c=0 for you !")
def delta(a, b, c):  #This part is to solve delta
    d = b ** 2 - 4 * a * c
    return d

while True:    #This part is to ask coefficient number a b c
      a=float(input("Please give me a coefficient"))
      b=float(input("Please give me b coefficient"))
      c=float(input("Please give me c coefficient"))

      if a == 0:      #This is to check a not zero
                print("Sorry but a can not be zero.")
                continue   #This is to check if a is 0, then go back to the while and ask again

      else:      # If a is not zero programming will go here to solve equation
          if delta(a, b, c) > 0:    # quadratic equation have three situation , here is to check which situation here is
              x1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
              x2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
              print("Thank you that is a valid input :) I will solve now")
              print(f"Root 1: {x1} Root 2 :{x2}")
              break   # if have root than stop the loop

          elif delta(a,b,c) == 0:      # situation : when delat is 0
              x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
              print("Thank you that is a valid input :) I will solve now")
              print(f"Root : {x1} ")
              break    # If have root than stop the loop

          else:     # situation : when delta smaller than 0 there is no real root
               print("Sorry but this equation have no real roots")

quit()



