# Kivy Imports:
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
# Get Window size
from kivy.core.window import Window
import functions
# Socket Import:
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 27020))


class MetroLogin(Screen):
    login_attempts = 0
    login_name = ObjectProperty(None)
    login_pass = ObjectProperty(None)
    logged = False

    def send_info(self):
        client_socket.send("1")
        client_socket.send(str(self.login_name.text).lower() + ";" + str(self.login_pass.text).lower())

        # Recv response:
        server_response = client_socket.recv(1024)

        # 0 = invalid login, show popup / 1 = logged on, redirect to main app screen.
        if server_response == "0":
            popup = invalid_login_popup()
            popup.open()
            self.logged = False

        elif server_response == "1":
            self.logged = True
        else:
            print server_response
        print self.logged

class MetroRegister(Screen):
    register_email = ObjectProperty(None)
    register_name = ObjectProperty(None)
    register_pass = ObjectProperty(None)

    def send_info(self):
        client_socket.send("0")
        client_socket.send(
            str(self.register_email.text).lower() + ";" + str(self.register_name.text).lower() + ";" + str(
                self.register_pass.text).lower())

        # Recv response:
        print client_socket.recv(1024)


class MetroChat(Screen):
    pass


class MetroWinmanager(ScreenManager):
    pass


class invalid_login_popup(Popup):
    pass


class MetroApp(App):
    def build(self):
        return Builder.load_file("main.kv")


def main():
    MetroApp().run()


main()

client_socket.close()
