mot = ["règles","ventre","seigne"]
regle = ["a","b","c"]
ventre = ["e","f","g"]
seigne = ["h","i","j"]
a = input ("quel est votre question :")
if str(a) == mot[0]:
	print("essaie 1")	
elif a == mot[1]:
	print("essaie 2")
else :
	print("essaie 3")
b = input ("Quel est votre choix ? :")

if str(b) == regle [0]:
	print ("essaie 4")
elif str(b) == regle [1]:
	print("essaie 5")
else:
	print ("essaie 6")
if str(a) == mot[0] and str(b) == regle[0]:
	print("essaie 7")
if str(a) == mot [1] and str (b) == regle [1]:
	print("essaie 8")
if str(a) == mot[2] and str (b) == regle [2]:
	print("essaie 9")

