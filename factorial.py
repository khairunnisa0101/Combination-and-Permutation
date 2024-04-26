#Code to calculate combination or permutation
#Combination formula: C(n, r) = n!/(r! (n – r)!)
#Permutation formula: P(n,r) = n! ÷ (n-r)!

import math
 
def factorial(n):
    return(math.factorial(n))

#Initial number x, y
#n = x
#r = y
x= int(input("Factorial number x = "))
y= int(input("Factorial number y = "))

#Type Combination/ Permutation
#comb_formula
comb_formula = factorial(x)/(factorial(y)*(factorial(x-y)))

#perm_formula
perm_formula = factorial(x)/(factorial(x-y))


types= input("Combinatiaon (comb) or Permutatioan (perm)?" )
if types == "comb":
    print ("Result= ", comb_formula)
if types == "perm":
    print ("Result=", perm_formula)