reponse_client = "oui"

while reponse_client != "non" and reponse_client != "n":
    reponse_client = input("Voulez vous continuer ? :")
    if reponse_client == "oui" or reponse_client == "o" :
        continue
    elif reponse_client is not "non" and reponse_client is not "oui":
        print("saisie incorrecte :")
        continue
