mot = ["règles","ventre","seigne"]
regle = ["a","b","c"]
ventre = ["d","e","f"]
seigne = ["g","h","i"]
a = input ("quel est votre question :")
if str(a) == mot[0]:
	print("essaie 1")
	b = input ("question 2 :")
	if str(b) == regle [0]:
		print ("essaie 1.1")
	if str(b) == regle [1]:
		print("essaie 1.2")
	if str(b) == regle [2]:
		print("essaie 1.3")

if str(a) == mot[1]:
	print("essaie 2")
	b = input ("question 2 :")
	if str(b) == ventre [0]:
		print ("essaie 2.1")
	if str(b) == ventre [1]:
		print("essaie 2.2")
	if str (b) == ventre [2]:
		print("essaie 2.3")

if str(a) == mot[2]:
	print ("essaie 3")
	b = input ("question 2 :")
	if str(b) == seigne [0]:
		print ("essaie 3.1")
	if str(b) == seigne [1]:
		print ("essaie 3.2")
	if str(b) == seigne [2]:
		print ("essaie 3.3")

if str(a) == mot [0] and str (b) == regle [0]:
	print("essae 1.1.1")
elif str(a) == mot[0] and str(b) == regle [1]:
	print("essaie 1.2.1")
if str(a) == mot [0] and str (b) == regle [2]:
	print("essaie 1.3.1")
if str(a) == mot [1] and str (b) == ventre [1]:
	print("essae 2.1.1")
elif str(a) == mot [1] and str (b) == ventre [2]:
	print("essae 2.2.1")
else:
	print("essaie 2.3.1")
	print("essaie 2.3.1")