__author__ = 'Nixon'

from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.progressbar import ProgressBar
from kivy.uix.label import Label
import database_interface
import display_controller as controller
import math

Builder.load_file('Kivy_Layouts/FoodScreen.kv')


class FoodScreen(Screen):
    pass


class FoodGrid(GridLayout):
    pass


class DataGrid(GridLayout):
    def update(self):
        self.clear_widgets()

        bins = controller.sort_bin(database_interface.get_data(database_interface.CONFIG.BINS, {}))
        temp = list()
        for b in bins:
            temp.append(b)
        bins = temp

        if len(bins) <= 3:
            self.rows = 1
            self.cols = len(bins)
        else:
            self.rows = 2
            self.cols = 3

        for area in bins:
            b = GridLayout(cols=1, rows=3)

            b.add_widget(Label(text=area['name'].capitalize(), font_size=40, size_hint_y=0.2))

            last_entry = database_interface.get_data(database_interface.FOOD, query={'bin': area['bin']}, sort="date",
                                                     single=True)

            try:
                if last_entry is None:
                    prog = 0
                else:
                    prog = last_entry['quantity']
            except IndexError:
                prog = 0

            if area['display_type'] == 0:
                b.add_widget(Label(text=("{0:.1f}".format(prog)+" g"), size_hint_y=0.2, font_size=30))
                pb = ProgressBar(max=100, value=prog/100, padding=20, size_hint_y=0.6)
                b.add_widget(pb)
            elif area['display_type'] == 1:
                gui = database_interface.get_data(database_interface.GUIDELINES.SHELF_TIME,
                                                  {'name': area['name']})[0]
                b.add_widget(Label(text=str(int(math.floor(prog/gui['unit']))) + " Units", font_size=30))
                b.add_widget(Label(text=""))

            self.add_widget(b)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update()
