__author__ = 'Nixon'


from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('../Kivy_Layouts/SettingContacts.kv')


class SettingContactScreen(Screen):
    pass


class SettingContactGrid(GridLayout):
    pass


class SettingContactNittyGrid(GridLayout):
    pass
