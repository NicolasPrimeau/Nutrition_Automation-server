__author__ = 'Nixon'

from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.base import Builder


Builder.load_file('Kivy_Layouts/SettingAlerts.kv')


class SettingAlertScreen(Screen):
    pass


class SettingAlertGrid(GridLayout):
    pass


class SettingAlertNittyGrid(GridLayout):
    pass

