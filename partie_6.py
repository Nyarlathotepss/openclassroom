liste_oui = ["oui","o","yes"]
liste_non = ["non","n","no"]

reponse_uti = "oui"

while reponse_uti not in liste_non :
    if reponse_uti in liste_oui :
        reponse_uti = input("Veuillez saisir votre reponse :")
    else :
        print("Mauvaise saisie Recommencer")
        reponse_uti = input("Veuillez saisir votre reponse :")
