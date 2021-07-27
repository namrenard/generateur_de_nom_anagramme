'''
1) trouver l'anagramme d'un mot  = ok
2) verifier que c'est un mot et non des chiffres = bug car si les deux mixer programme continue.
3) fonction pour relancer avec le même mot ou choisir un nouveau = ok
3.1) fonction pour un shuffle de x fois le mot  = ok
4) interface gui : kivi md pour mobile
4.1) faire un input ou text pour le mot, un bouton pour le shuffle et un bouton pour le nombre de recherche
4.2) mettre un logo du jeu.
4.3) mettre de la couleur en bandeau et arrière plan de l'appli.
4.4) bouton pour relancer le programme en effacant les données
5) compiler sous apk
'''

from random import shuffle
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton

# GUI kivi MD

class AnagramApp(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Click here to Shuffle",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen



# definition class word_programme

class Word:

    def __init__(self, word, token=0):
        self.word = word
        self.token = token


    # function shuffle for a word
    def anagramme(self):
        a = list(self.word)
        shuffle(a)
        return "".join(a)

    # choice of shuffle
    def anagramme_multiple(self,token):
        nombre_de_recherche = ''
        y = 1
        while nombre_de_recherche == '' or nombre_de_recherche.isdigit() == False:
            nombre_de_recherche = input("Choisissez le nombre d'anagramme à générer:")
        nombre_de_recherche_int = int(nombre_de_recherche)
        print(f"Voici les résultats pour {nombre_de_recherche} anagrammes du mot ({self.word}):")
        print()
        while y <= nombre_de_recherche_int:
            print("".join(self.anagramme()))
            y = y+1
        if token == 0:
            self.relance_anagramme()
        else:
            exit()

    # again a shuffle of shutdown the program?
    def relance_anagramme(self):
        question = input("Relancez le générateur avec le même mot ? o/n")
        if question.lower() == "o":
            self.anagramme_multiple(1)
        elif question.lower() == "n":
             print("Ok. Programme Terminé")
        else:
            print("Vous n'avez pas donné de réponse valide. Programme Terminé")
            self.relance_anagramme()


    # check if it's a word or number // miss to block the mixture of word+number
    def verification_anagramme(self):

        if self.word.isdigit():
            print(f"Erreur, {self.word} n'est pas un mot, recommencez s'il vous plait.")
            self.word = input("Quel est votre mot ? :")
            self.verification_anagramme()
        else:
            return



#---------------------------program-----------------------------
if __name__ == '__main__':
       AnagramApp().run()

'''print("Bonjour, ceci est un petit programme pour trouver un anagramme aléatoirement.")
print()
mot = ''
while mot == '':
    mot = input("Veuillez donner un mot :")

mot_str = Word(mot)
mot_str.verification_anagramme()
mot_str.anagramme_multiple(0)'''
