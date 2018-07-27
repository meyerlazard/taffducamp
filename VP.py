x = input("quel capital :")
t = input("quelle durée :")
i = 1.05
if int(x) > 0 and int(t) > 0:
	a = (int(x) /( i ** int(t)))
	print("VP = " ,round(a))