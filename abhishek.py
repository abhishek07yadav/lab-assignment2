


from itertools import product
import random




N=2  # no of dice
   
M= set(product([1,2,3,4,5,6] , repeat=N))  




print(M) # print sample space

print( len(M))   # print length ofsample space




E1={X for X in M if X[0]+X[1]==2} # sum of the no. on dices is 2

E2={X for X in M if X[0]+X[1]==3} # sum of the no. on dices is 3

E3={X for X in M if X[0]+X[1]==4} # sum of the no. on dices is 4

E4={X for X in M if X[0]+X[1]==5}  # sum of the no. on dices is 5

E5={X for X in M if X[0]+X[1]==6}  # sum of the no. on dices is 6

E6={X for X in M if X[0]+X[1]==7}  # sum of the no. on dices is 7

E7={X for X in M if X[0]+X[1]==8}  # sum of the no. on dices is 8

E8={X for X in M if X[0]+X[1]==9}   # sum of the no. on dices is 9

E9={X for X in M if X[0]+X[1]==10}  # sum of the no. on dices is 10

E10={X for X in M if X[0]+X[1]==11}  # sum of the no. on dices is 11

E11={X for X in M if X[0]+X[1]==12}  # sum of the no. on dices is 12




E1,E2,E3,E5,E6,E7,E8,E9,E10,E11  # print all possible event


P=[E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,E11]
Event= random.choice(P) # that select an event randomly from all possible event set


print(Event) # print randomly selected event
print(len(Event)) # print randomly selected event length


Probability=len(Event)/len(M)
print(Probability) # print required probability

