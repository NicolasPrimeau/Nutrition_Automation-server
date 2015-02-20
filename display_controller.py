import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.base import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import database_interface


Builder.load_file('Kivy_Layouts/AlertScreen.kv')
Builder.load_file('Kivy_Layouts/FoodScreen.kv')
Builder.load_file('Kivy_Layouts/MainScreen.kv')
Builder.load_file('Kivy_Layouts/SettingScreen.kv')


class MainScreen(Screen):
    def alert_callback(self):
        pass


class MainGrid(GridLayout):
    pass


class AlertScreen(Screen):
    pass


class AlertGrid(GridLayout):
    pass

class MessagesGrid(GridLayout):
    pass


class FoodScreen(Screen):
    pass


class FoodGrid(GridLayout):
    pass


class DataGrid(GridLayout):
    def __init__(self, **kwargs):
        super(DataGrid, self).__init__(**kwargs)

        for bin in database_interface.get_data(database_interface.CONFIG.BINS):
            self.add_widget(Button(text=bin['name']))
            self.add_widget(Button(text=bin['name']))



class SettingsScreen(Screen):
    pass


class SettingsGrid(GridLayout):
    pass

class SettingGrid(GridLayout):
    pass


class MainApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(AlertScreen(name="alert"))
        sm.add_widget(FoodScreen(name="food"))
        sm.add_widget(SettingsScreen(name="settings"))
        sm.current = "main"
        return sm

