__author__ = 'Nixon'


from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
import database_interface as db
import display_controller as controller

Builder.load_file('Kivy_Layouts/SettingGeneral.kv')


class SettingGeneralScreen(Screen):
    def set_general_settings(self):
        info = controller.MANAGER.get_screen("setting_general").children[-1].children[0]
        for bin_grid in info.children:
            if isinstance(bin_grid, BinGrid):
                if isinstance(bin_grid.children[-1], Label) and len(bin_grid.children) > 2:
                    bin = bin_grid.children[-1].text.split(":")[0]
                    bin = int(bin.split(" ")[-1])
                    if bin_grid.children[0].state == "down":
                        db.update(db.CONFIG.BINS, {'bin':  bin}, {'$set': {'display_type': 1}})
                    elif bin_grid.children[1].state == "down":
                        db.update(db.CONFIG.BINS, {'bin':  bin}, {'$set': {'display_type': 0}})

        controller.MANAGER.transition.direction = 'right'
        controller.MANAGER.current = "main"

class SettingGeneralGrid(GridLayout):
    pass


class BackButtonGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class SettingPanel(GridLayout):
    def update(self):
        self.clear_widgets()
        i = 0
        for entry in db.get_data(db.CONFIG.BINS):
            gui = db.get_data(db.GUIDELINES.SHELF_TIME, {'name': entry['name']})[0]
            self.add_widget(BinGrid(entry['bin'], entry['display_type'],
                                    dual=(gui['unit'] is not None), name=entry['name']))
            i += 1

        for entry in range(6-i):
            self.add_widget(GridLayout(rows=1, cols=3))


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update()

class BinGrid(GridLayout):
    def __init__(self, bin, type, dual, name="", **kwargs):
        super().__init__(**kwargs)
        self.rows = 1
        self.cols = 3
        self.add_widget(Label(text="Bin "+str(bin) + (len(name)>0)*(": " + name.capitalize())))


        if not dual:
            self.add_widget(Label(text="Weight Only"))
        elif type == 0:
            self.add_widget(ToggleButton(text="Weight", group="bin"+str(bin), state="down"))
        else:
            self.add_widget(ToggleButton(text="Weight", group="bin"+str(bin)))

        if type == 1 and dual:
            self.add_widget(ToggleButton(text="Unit", group="bin"+str(bin), state="down"))
        elif dual:
            self.add_widget(ToggleButton(text="Unit", group="bin"+str(bin)))
