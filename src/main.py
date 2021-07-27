'''
1) trouver l'anagramme d'un  = ok
2) verifier que c'est un mot et non des chiffres = bug
3) fonction pour relancer avec le même mot ou choisir un nouveau = ok
3.1) fonction pour un shuffle de 5, 10 ou 20 mots ?
4) interface gui : kivi md pour mobile
4.1) faire un input pour le mot, un bouton pour le shuffle x1, shuffle x 5 et shuffle x 10
4.2) bandeau
'''

from random import shuffle
# from kivy.uix.screenmanager import Screen
# from kivymd.app import MDApp
# from kivymd.uix.button import MDRectangleFlatButton

# GUI kivi MD

'''class AnagramApp(MDApp):
    def build(self):
        screen = MDScreen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen
'''


# definition class word_programme

class Word:
    def __init__(self, word):
        self.word = word

    def anagramme(self):
        a = list(self.word)
        shuffle(a)
        return "".join(a)

    def relance_anagramme(self):
        question = input("Relancez le générateur avec le même mot ? o/n")
        if question.lower() == "o":
            print(mot_str.anagramme())
        elif question.lower() == "n":
            print("Ok. Programme Terminé")
            exit()
        else:
            print("Vous n'avez pas donné de réponse valide. Programme Terminé")
            self.relance_anagramme()

    def verification_anagramme(self):

        if self.word.isdigit() == True:
           print(f"Erreur, {self.word} n'est pas un mot, recommencez s'il vous plait.")
           self.word = input("Quel est votre mot ? :")
           self.verification_anagramme()
        else:
            return



#---------------------------program-----------------------------
# if __name__ == '__main__':
#       AnagramApp().run()

print("Bonjour, ceci est un petit programme pour trouver un anagramme aléatoirement.")
print()
mot = ''
while mot == '':
    mot = input("Veuillez donner un mot :")

mot_str = Word(mot)
mot_str.verification_anagramme()
print(mot_str.anagramme())
mot_str.relance_anagramme()






