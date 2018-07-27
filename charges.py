a = input ("quel est votre chiffre d'affaire ? : ")
taux_charges = 0.2730
cotisation = int(a) * taux_charges
print("Le montant de vos charges s'élève à :",cotisation)
ca_charge = int(a) - cotisation
print("votre chiffre après chagrge est de :", ca_charge)
taux_imp = 0.18
montant_imp = ca_charge * taux_imp
print('le montant des impôts à payer est de :', montant_imp)
ca_net = ca_charge - montant_imp
print("votre chiffre net est de :", ca_net)
