__author__ = 'Nixon'


from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen


Builder.load_file('Kivy_Layouts/SettingGeneral.kv')


class SettingGeneralScreen(Screen):
    pass


class SettingGeneralGrid(GridLayout):
    pass


class SettingGeneralNittyGrid(GridLayout):
    pass
