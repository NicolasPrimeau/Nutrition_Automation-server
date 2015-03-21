__author__ = 'Nixon'


from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen
import display_controller as controller


Builder.load_file('../Kivy_Layouts/MainScreen.kv')


class MainScreen(Screen):
    def go_to_food(self):
        controller.update_and_view_food()


class MainGrid(GridLayout):
    pass


class MainMidGrid(GridLayout):
    pass