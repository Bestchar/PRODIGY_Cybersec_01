# Liste des lettres de l'alphabet
liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Demande à l'utilisateur d'entrer un message et une clé
message = input("Entrez votre message: ").lower()  # Convertit le message en minuscules
clef = int(input("Entrez la clef: "))


def Chiffrage_lettre(lettre, liste, clef):
    if lettre == ' ':  # Vérifie si la lettre est un espace
        return ' '
    if lettre in liste:
        index = liste.index(lettre)  # Trouve l'index de la lettre
        # Calcule le nouvel index avec un retour à zéro si on dépasse la longueur de la liste
        new_index = (index + clef) % len(liste)
        return liste[new_index]  # Retourne la lettre chiffrée
    return '?'  # Retourne un point d'interrogation si la lettre n'est pas trouvée

message_chiffré = str()

# Chiffre chaque lettre du message
for lettre in message:
    message_chiffré += Chiffrage_lettre(lettre, liste, clef)

print("Message chiffré:", message_chiffré)
