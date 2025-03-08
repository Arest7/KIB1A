from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup


class MenuScreen(Screen):
    pass

class ModuloScreen(Screen):
    pass

class GCDScreen(Screen):
    pass




class ModExpScreen(Screen):
    pass

class ModInverseScreen(Screen):
    pass


def mod_inverse(e, n):
    g, x, _ = extended_gcd(e, n)
    if g != 1:
        return None  
    else:
        return x % n

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return g, x, y

def modular_exponentiation(a, e, n):
    return pow(a, e, n)

def modulo(a, n):
    return a % n

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class CalculationWindow(MDApp):
    def __init__(self, screen_name, **kwargs):
        super().__init__(**kwargs)
        self.screen_name = screen_name

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.root.current = self.screen_name

    def open_new_window(self, screen_name):
        self.root.current = screen_name

    def calculate_modulo(self, a, n):
        try:
            a = int(a)
            n = int(n)
            result = modulo(a, n)
            self.show_result(f"{a} mod {n} = {result}")
        except ValueError:
            self.show_result("Iltimos, butun son kiriting!")

    def calculate_gcd(self, a, b):
        try:
            a = int(a)
            b = int(b)
            result = gcd(a, b)
            self.show_result(f"EKUB({a}, {b}) = {result}")
        except ValueError:
            self.show_result("Iltimos, butun son kiriting!")

    def calculate_mod_exp(self, a, e, n):
        try:
            a = int(a)
            e = int(e)
            n = int(n)
            result = modular_exponentiation(a, e, n)
            self.show_result(f"{a}^{e} mod {n} = {result}")
        except ValueError:
            self.show_result("Iltimos, butun son kiriting!")

    def calculate_mod_inverse(self, e, n):
        try:
            e = int(e)
            n = int(n)
            result = mod_inverse(e, n)
            if result is None:
                self.show_result("Modular invers mavjud emas!")
            else:
                self.show_result(f"{e}^-1 mod {n} = {result}")
        except ValueError:
            self.show_result("Iltimos, butun son kiriting!")

    def show_result(self, message):
        popup = Popup(title='Natija',
                      content=MDLabel(text=message, halign='center',theme_text_color='Custom',
                        text_color=(1, 1, 1, 1),),
                      
                      size_hint=(None, None), size=(300, 200))
        popup.open()

    def go_back(self):
        self.root.current = 'menu' 

KV = '''
ScreenManager:
    MenuScreen:
    ModuloScreen:
    GCDScreen:
    ModExpScreen:
    ModInverseScreen:

<MenuScreen>:
    name: 'menu'
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDLabel:
            text: 'Matematik Kalkulyator'
            halign: 'center'
            font_style: 'H5'
        MDRaisedButton:
            text: 'a mod n'
            pos_hint: {'center_x': 0.5}
            on_press: app.open_new_window('mod')
        MDRaisedButton:
            text: 'EKUB(a, b)'
            pos_hint: {'center_x': 0.5}
            on_press: app.open_new_window('gcd')
        MDRaisedButton:
            text: 'a^e mod n'
            pos_hint: {'center_x': 0.5}
            on_press: app.open_new_window('modexp')
        MDRaisedButton:
            text: 'Modular Inverse'
            pos_hint: {'center_x': 0.5}
            on_press: app.open_new_window('modinv')

<GCDScreen>:
    name: 'gcd'
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDLabel:
            text: 'Greatest Common Divisor (GCD) Calculation'
            halign: 'center'
            font_style: 'H5'
        MDTextField:
            id: input_a
            hint_text: 'Enter a'
            input_filter: 'int'
        MDTextField:
            id: input_b
            hint_text: 'Enter b'
            input_filter: 'int'
        MDRaisedButton:
            text: 'Calculate'
            pos_hint: {'center_x': 0.5}
            on_press: app.calculate_gcd(input_a.text, input_b.text)
        MDRaisedButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5}
            on_press: app.go_back()


<ModuloScreen>:
    name: 'mod'
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDLabel:
            text: 'Modulo Calculation (a mod n)'
            halign: 'center'
            font_style: 'H5'
        MDTextField:
            id: input_a
            hint_text: 'Enter a'
            input_filter: 'int'
        MDTextField:
            id: input_n
            hint_text: 'Enter n'
            input_filter: 'int'
        MDRaisedButton:
            text: 'Calculate'
            pos_hint: {'center_x': 0.5}
            on_press: app.calculate_modulo(input_a.text, input_n.text)
        MDRaisedButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5}
            on_press: app.go_back()

<ModExpScreen>:
    name: 'modexp'
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDLabel:
            text: 'Modular Exponentiation (a^e mod n)'
            halign: 'center'
            font_style: 'H5'
        MDTextField:
            id: input_a
            hint_text: 'Enter a'
            input_filter: 'int'
        MDTextField:
            id: input_e
            hint_text: 'Enter e'
            input_filter: 'int'
        MDTextField:
            id: input_n
            hint_text: 'Enter n'
            input_filter: 'int'
        MDRaisedButton:
            text: 'Calculate'
            pos_hint: {'center_x': 0.5}
            on_press: app.calculate_mod_exp(input_a.text, input_e.text, input_n.text)
        MDRaisedButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5}
            on_press: app.go_back()

<ModInverseScreen>:
    name: 'modinv'
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(50)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDLabel:
            text: 'Modular Inverse Calculation (e^-1 mod n)'
            halign: 'center'
            font_style: 'H5'
        MDTextField:
            id: input_e
            hint_text: 'Enter e'
            input_filter: 'int'
        MDTextField:
            id: input_n
            hint_text: 'Enter n'
            input_filter: 'int'
        MDRaisedButton:
            text: 'Calculate'
            pos_hint: {'center_x': 0.5}
            on_press: app.calculate_mod_inverse(input_e.text, input_n.text)

        MDRaisedButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5}
            on_press: app.go_back()
'''

if __name__ == "__main__":
    CalculationWindow(screen_name='menu').run()
