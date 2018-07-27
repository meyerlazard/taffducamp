choix = ['yes','no']
print('Bonjour nous vous souhaitons la bienvenue chez LEONALMEYER, vous avez besoin de évaluer un projet dinvestissement,markusrobot va soccuper de vous')
a = input('voulez vous que markus soccupe de vous ?')
if a == choix[0]:
	n = input ('combien années : ')
	c = input('montant des cash flow : ')
	i = input ('quel taux ? :')
	r = int(i)/100
	m = int(n)
	A = int(c)
	ceof = (1-(1+r)**(-m))/r
	Actualisation = A * ceof
	print('votre séquence de',m,'cash flow valent actuellement',Actualisation)
else:
	print('Au revoir Monsieur')
