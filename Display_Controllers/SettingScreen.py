__author__ = 'Nixon'

from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen
import display_controller as controller

Builder.load_file('Kivy_Layouts/SettingScreen.kv')


class SettingsScreen(Screen):

    def go_to_general(self):
        controller.MANAGER.get_screen("setting_general").children[0].children[0].update()
        controller.MANAGER.transition.direction = 'left'
        controller.MANAGER.current = 'setting_general'


class SettingsGrid(GridLayout):
    pass


class SettingGrid(GridLayout):
    pass


class BackButtonGrid(GridLayout):
    pass