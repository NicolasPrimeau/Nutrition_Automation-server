__author__ = 'Nixon'

from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.progressbar import ProgressBar
from kivy.uix.label import Label
import database_interface
import display_controller as controller

Builder.load_file('Kivy_Layouts/FoodScreen.kv')


class FoodScreen(Screen):
    pass


class FoodGrid(GridLayout):
    pass


class DataGrid(GridLayout):
    def update(self):
        self.clear_widgets()

        bins = controller.sort_bin(database_interface.get_data(database_interface.CONFIG.BINS))

        for bin in bins:
            b = GridLayout(cols=1, rows=3)

            b.add_widget(Label(text=bin['name'].capitalize(), font_size=30, size_hint_y=0.2))

            last_entry = database_interface.get_data(database_interface.FOOD, query={'bin': bin['bin']}, sort="date")

            if len(last_entry) == 0:
                prog = 0
            else:
                prog = last_entry[-1]['quantity']

            b.add_widget(Label(text=("{0:.1f}".format(prog)+" Kg"), size_hint_y=0.2, font_size=20))

            pb = ProgressBar(max=10000, value=prog, padding=20, size_hint_y=0.6)
            b.add_widget(pb)

            self.add_widget(b)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update()
