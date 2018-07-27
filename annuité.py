#A * a
#A = montant de l'annuité
#a = (1-(1+i)**(-n))/i
#i = taux de la periode
#n = periode : mensuelle, trimestrielle, semestrielle, annuelle
#i = (1+i)**(1/n)

# Si a == Annuelle --> n = 1 --> pas d'impact sur i
# Si a == Semestrielle --> n = 1/2 <=> n = 0.5 --> i_sem = (1+i_ann)**(1/n) -1
# Si a == Trimestrielle --> n = 1/4 <=> n = 0.25 --> i_trim = (1+i_ann)**(1/n) - 1
# Si a == mensuelle --> n = 1/12 <=> n = 0.8333 --> i_mens = (1+i_ann)**(1/n) - 1
#Periodicité du taux
periode = ['mensuelle', 'semestrielle', 'trimestrielle', 'annuelle']
valeur  = [0.0833, 0.5, 0.3333, 1]
i_annuel = 0.05
a = input('entrez une valeur : ')
if a == periode [0]:
	n = valeur[0]
	i_mens = ((1+i_annuel)**(n))  - 1
	b = input('Combien de mois ? :')
	i_mens_semidef = i_mens * int(b)
	print(i_mens_semidef)
if a == periode [1]:
	n = valeur[1]
	i_sem = ((1+i_annuel)**(n)) - 1
	print (i_sem)
if a == periode [2]:
	n = valeur[2]
	i_trim = ((1+i_annuel)**(n)) - 1
	print (i_trim)
if a == periode[3]:
	print (i_annuel)
