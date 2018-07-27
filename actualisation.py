#Actualisatio,
#Actualisationà intérêt simple et capi
x = input ("quel capital ? :")
t = input ("quelle durée ? :")
i = 0.05
if float (t) <= 1:
	print("Valeur actuelle simple :",int(x) / (1 + i * float(t)))
elif int(t) >= 1: 
	print("Valeur actuelle composée :",int(x) / (1 +i)**float(t))

