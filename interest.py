x = input ("quel capital ? :")
t = input ("quelle durée ? :")
i = 0.045

#intérêt simple et composés
if float(t) <= 1 :
	print("Simple Interest :",int(x) + int(x) * i * float(t))
elif int(t) >= 1:
	print("Coumpound interest",int(x) * (1+i) ** int(t))

