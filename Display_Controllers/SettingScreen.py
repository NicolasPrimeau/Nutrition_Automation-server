__author__ = 'Nixon'

from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('../Kivy_Layouts/SettingScreen.kv')


class SettingsScreen(Screen):
    pass


class SettingsGrid(GridLayout):
    pass


class SettingGrid(GridLayout):
    pass


class BackButtonGrid(GridLayout):
    pass


