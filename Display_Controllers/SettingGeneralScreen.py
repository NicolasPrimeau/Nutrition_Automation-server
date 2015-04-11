__author__ = 'Nixon'


from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
import database_interface as db

Builder.load_file('Kivy_Layouts/SettingGeneral.kv')


class SettingGeneralScreen(Screen):
    def set_general_settings(self):
        pass


class SettingGeneralGrid(GridLayout):
    pass


class BackButtonGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class SettingPanel(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        i = 0
        for entry in db.get_data(db.CONFIG.BINS):
            self.add_widget(BinGrid(entry['bin'], entry['settings']['display_type'], name=entry['name']))
            i += 1

        for entry in range(6-i):
            self.add_widget(GridLayout(rows=1, cols=3))

class BinGrid(GridLayout):
    def __init__(self, bin, type, name="", **kwargs):
        super().__init__(**kwargs)
        self.rows = 1
        self.cols = 3
        self.add_widget(Label(text="Bin "+str(bin) + (len(name)>0)*(": " + name.capitalize())))
        if type == 0:
            self.add_widget(ToggleButton(text="Weight", group="bin"+str(bin), state="down"))
        else:
            self.add_widget(ToggleButton(text="Weight", group="bin"+str(bin)))

        if type == 1:
            self.add_widget(ToggleButton(text="Unit", group="bin"+str(bin), state="down"))
        else:
            self.add_widget(ToggleButton(text="Unit", group="bin"+str(bin)))

