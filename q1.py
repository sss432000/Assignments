# man,goat,grass,tiger puzzle

bank1 = []
bank2 = []
boat = []

#initially

bank1.append("goat") #index 0
bank1.append("grass")  #index 1
bank1.append("tiger")  #index 2
boat.append("man")   # man on index 0 in boat

print("Initial conditions -->\n")
print("On bank1 :", bank1)
print("On boat :" ,boat)
print("On bank2 :" ,bank2)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

print("Trip 1: Man takes goat with him\n")
boat.append("goat")
print("On boat :", boat)
print("After 1st trip:")
bank2.append(bank1.pop(0)) #popping goat from bank1 and appending it to bank2 -- now grass -0 tiger -1 index
print("On bank1 :\n", bank1)
print("On bank2 :\n", bank2)

boat.pop(1) #goat popped from goat
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

print("Trip 2(bank1 to bank2): Man takes grass with him\n")
boat.append("grass")
print("On boat :", boat)
print("After 2nd trip :")
bank2.append(bank1.pop(0)) #grass popped from bank1 and appended in bank2
print("On bank1 :\n", bank1)
print("On bank2 :\n", bank2)

boat.pop(1) #grass popped from boat
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

print("Trip 2(bank2 to bank1) -- Man takes goat with him in boat\n")
boat.append("goat")
print("On boat :" ,boat)
print("After second trip of boat from bank 2 to bank 1:")
bank2.pop(0)  #goat popped from bank2
bank1.append("goat")  #goat appended in bank1
print("On bank 1:\n",bank1)
print("On bank 2:\n",bank2)

boat.pop(1) #goat popped from boat
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

print("Trip 3: Man takes tiger with him\n")
boat.append("tiger")
print("On boat :", boat)
print("After 3rd trip :")
bank2.append(bank1.pop(0)) #tiger popped from bank1 and appended in bank2
print("On bank1 :\n" ,bank1)
print("On bank2 :\n", bank2)

boat.pop(1) #tiger popped from boat
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

print("Trip 4: Man takes goat with him\n")
boat.append("goat")
print("On boat :", boat)
print("After 4th trip :")
bank2.append(bank1.pop(0)) #goat popped from bank1 and appended in bank2
print("On bank1 :\n" ,bank1)
print("On bank2 :\n" ,bank2)

boat.pop(1) #goat popped from boat
print("On boat:\n", boat)

print("Now, man goes on bank2 from boat\n")
bank2.append(boat.pop(0))
print("On boat:\n", boat)
print("On bank1 :\n" ,bank1)
print("On bank2 :\n" ,bank2)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")



