__author__ = 'Nixon'


from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen
import display_controller as controller


Builder.load_file('Kivy_Layouts/MainScreen.kv')


class MainScreen(Screen):
    def go_to_food(self):
        controller.update_and_view_food()

    def go_to_report(self):
        controller.MANAGER.get_screen("setting_update_bin").children[-1].children[0].update()
        controller.MANAGER.transition.direction = 'up'
        controller.MANAGER.current = "report"

class MainGrid(GridLayout):
    pass


class MainMidGrid(GridLayout):
    pass
