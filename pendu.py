'''importation des librairie:
random:il permet de choisir de facon aleatoire des valeurs
time:permet de matquer les pauses avec l afonction sleep()'''
import random
import time
'''khoudia et penda
 charge les mots en fonction du niveau choisi en fonction par l'utilisateur'''
def choisirNiveau(niveau):
    with open('words.txt', 'r') as mon_fichier:
           liste=mon_fichier.read().split(",")
    mots_de_quatre=[]
    mots_de_six=[]
    mots_de_dix=[]
    print("Chargement des mots...")
    time.sleep(2)
    print(str(len(liste))+"mots charges")
    time.sleep(2)
    for i in range(len(liste)):
            if(len(liste[i])==4):
                mots_de_quatre.append(liste[i])
            elif(len(liste[i])==6):
                mots_de_six.append(liste[i])
            else:
                mots_de_dix.append(liste[i])
    if niveau==1:
        print("vous avez choisi le niveau "+str(niveau))
        return mots_de_quatre
            
    elif niveau==2:
        print("vous avez choisi le niveau"+str(niveau))
        return mots_de_six
    else:
        print("vous avez choisi le niveau"+str(niveau))
        return mots_de_dix
'''khoudia
renvoit un mot aleatoirement en fonction de la liste de mots chargee'''
def motAleatoire(listeMots):
     mot=random.choice(listeMots)
     return mot

'''penda
c'est la fonction principale qui gere chaque partie du jeu,elle controle la lettre devinee par l'utilisateur'''
def pendu(mot,erreurs,tentatives,chaine,lettresTrouvees):
    lettres_unique=0
    lettreDisponibles="abcdefghijklmnopqrstuvwxyz" 
    while mot!=chaine:
        print("Il vous reste"+str(tentatives)+"tentatives")
        print("Lettres disponibles: "+lettreDisponibles)
        lettre=input("Je penses a un mot de 4 lettres a vous de le devinez")
        while lettre.isdigit():
            lettre=input("Veuilez entrer une lettre valide")
        lettre=lettre.lower()
        alphabet="abcdefghijklmnopqrstuvwxyz"
        voyelles="aoiue" 
        if lettre in alphabet:
            if lettre in mot:
                if lettre in lettreDisponibles:
                      lettresTrouvees.append(lettre)
                      chaine=placerLettre(mot,lettresTrouvees)
                      print("Bon essai: "+str(chaine))
                      lettreDisponibles=lettreDispo(lettreDisponibles,lettre)
                      print(80*"#"+"\n")
                else:
                      print("Oups! Vous avez déjà deviné cette lettre.")
                      erreurs=erreurs-1
                      print("Il vous reste "+str(erreurs)+" avertisements: "+chaine)
                      print(80*"#"+"\n")
                      
            else:
                if lettre not in lettreDisponibles :
                    erreurs=erreurs-1
                    print("Vous avez deja devine cette lettre")
                    print("Il vous reste"+str(erreurs)+"avertisements") 
                else:
                    if lettre in voyelles:
                        lettreDisponibles=lettreDispo(lettreDisponibles,lettre)
                        tentatives=tentatives-2
                        print("Oups! Cette lettre n'est pas dans le mot secret: "+chaine)
                        print(80*"#"+"\n")
                        
                    else:
                        print("Oups! Cette lettre n'est pas dans le mot secret")
                        print("tentative actuelle: "+chaine)
                        tentatives=tentatives-1
                        lettreDisponibles=lettreDispo(lettreDisponibles,lettre)
                        print(80*"#"+"\n")
                                      
        else:
            print("Oups! Ce n'est pas une lettre valide.\n Il vous reste"+str(erreurs)+"avertissements")
        if(erreurs==0):
            print("Vous n\'avez aucun avertissement donc vous perdez une tentative")
            tentatives=tentatives-1
            erreurs=3
        if(tentatives==0):
            print("Pendu! vous avez perdu!")
            break
    for l in mot:
        if mot.count(l)==1:
            lettres_unique+=1
    if(tentatives!=0):
            print("felicitation vous avez trouver le mot secret")
    print("votre score est: "+str(tentatives*lettres_unique))
    return tentatives*lettres_unique
   
'''khoudia
elle contient les lettres dont l'utilisateur n'a pas encore devinee'''
def lettreDispo(chaine,lettre):
       i=0
       while len(chaine)>0:
           if chaine[i]==lettre:
               chaine=chaine[:i]+chaine[i+1:]
               break
           i=i+1
       return chaine

'''penda
  elle permet de placer chaque lettre aux bon endroit'''
def placerLettre(mot,lettres):
    mot_masque = ""
    for lettre in mot:
        if lettre in lettres:
            mot_masque += lettre
        else:
            mot_masque += "_"
    return mot_masque

'''khoudia'''
print(80*"#"+"\n")
print(25*"#"+"BIENVENUE DANS LE JEU HANGMAN"+25*"#"+"\n")
    
niveau=int(input("choisissez un niveau entre 1 et 3"))
while((niveau<=0 and niveau>3)):
        niveau=int(input("choisissez un niveau entre 1 et 3"))
scores=[]
reponse="oui"
while reponse=="oui":
    mot=motAleatoire(choisirNiveau(niveau))
    chaine=""
    lettresTrouvees=[]
    erreurs=3
    tentatives=6
    print("vous pouvez commencer une nouvelle partie")
    print("Il vous reste "+str(erreurs)+" points erreurs")
    print(80*"#"+"\n")
    time.sleep(2)
    score=pendu(mot,erreurs,tentatives,chaine,lettresTrouvees)
    scores.append(score)
    reponse=input("voulez vous commencer une nouvelle partie? oui/non")
    print(80*"#"+"\n")
print("votre meilleur score est: "+str(max(scores)))
            


