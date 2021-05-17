friends=["tom","dick","harry","rick","tim"]
print(friends)
print(friends[2])
print(friends[-1]) #no from the back
print(friends[1:3]) #all elements upto but not 3
friends[1]="dom"
print(friends[1])
enemies=["emienem","rocky","rambo",50,"gaga",69,"gaga"]
print(enemies)
friends.extend(enemies)
print(friends)
friends.append("dre")
print(friends)
friends.insert(2,"kesha")
print(friends)
friends.pop() #gets rid of last element
print(friends)
print(friends.index("rocky"))
print(friends.count("gaga"))
num=[76,45,72,34,53,56]
#print(num.sort())
#print(num.reverse())
num2=num.copy()
print(num2)
friends.clear
print(friends)