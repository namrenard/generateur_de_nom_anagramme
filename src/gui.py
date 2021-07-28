from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar

# GUI kivi MD

class AnagramApp(MDApp):
    def build(self):
        screen = MDScreen()

        # screen Widgets
        screen.add_widget(Image(
            source="img/logo_black.png",
            pos_hint={ "center_x" : 0.5, "center_y" : 0.9}
        ))
        # label 1 and 2
        self.label1 = MDLabel(
            text="Bienvenue sur Anagram",
            halign="center",
            pos_hint={"center_x" :0.5, "center_y": 0.7},
            font_style="H5",
            theme_text_color="Primary",
        )
        self.label2 = MDLabel(
            text="*Entrez un mot puis un nombre et cliquez sur lancer*.",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.65},
            font_style="Caption",
            theme_text_color="Secondary",
        )
        screen.add_widget(self.label1)
        screen.add_widget(self.label2)

        # collect user input

        self.input = MDTextField(
            text="Veuillez entrer un mot",
            halign="center",
            size_hint=(0.6,1),
            pos_hint={"center_x": 0.5, "center_y": 0.45},
            font_size= 22)

        screen.add_widget(self.input)

        self.label3 = MDLabel(
            text="Résultat :",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            font_style="Caption",
            theme_text_color="Primary")
        screen.add_widget(self.label3)

        return screen
