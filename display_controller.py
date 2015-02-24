import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.uix.progressbar import ProgressBar
from kivy.uix.label import Label
from kivy.uix.listview import ListView, ListItemLabel, ListItemButton
from kivy.adapters.listadapter import ListAdapter
import database_interface
import re
from kivy.adapters.models import SelectableDataItem


Builder.load_file('Kivy_Layouts/AlertScreen.kv')
Builder.load_file('Kivy_Layouts/FoodScreen.kv')
Builder.load_file('Kivy_Layouts/MainScreen.kv')
Builder.load_file('Kivy_Layouts/SettingScreen.kv')
Builder.load_file('Kivy_Layouts/SettingAlerts.kv')
Builder.load_file('Kivy_Layouts/SettingAreas.kv')
Builder.load_file('Kivy_Layouts/SettingContacts.kv')
Builder.load_file('Kivy_Layouts/SettingGeneral.kv')
Builder.load_file('Kivy_Layouts/UpdateBin.kv')

MANAGER = None


class MainScreen(Screen):
    def alert_callback(self):
        pass


class MainGrid(GridLayout):
    pass


class MainMidGrid(GridLayout):
    pass


class AlertScreen(Screen):
    pass


class AlertGrid(GridLayout):
    pass


class MessagesList(ListView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        concerns = database_interface.get_data(database_interface.DETECTED_CONCERNS)
        msgs = list()
        msgs.append(" ")

        if len(concerns) != 0:
            concerns = concerns[0]['info']
            for c in concerns:
                for msg in c:
                    msgs.append(re.sub("(.{40})", "\\1\n", msg['message']['plain'], 0, re.DOTALL))

        list_item_args_converter = lambda row_index, info: {
            'text': info,
            'font_size': 22
        }

        self.adapter = ListAdapter(data=msgs,
                                   args_converter=list_item_args_converter,
                                   cls=ListItemLabel)


class FoodScreen(Screen):
    pass


class FoodGrid(GridLayout):
    pass


class DataGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for bin in database_interface.get_data(database_interface.CONFIG.BINS):
            b = GridLayout(cols=1, rows=2)

            b.add_widget(Label(text=bin['name'], size_hint=(0.2, 0.2)))

            last_entry = database_interface.get_data(database_interface.FOOD, query={'bin': bin['bin']}, sort="date")

            if len(last_entry) == 0:
                prog = 0
            else:
                prog = last_entry[0]['quantity']

            pb = ProgressBar(max=100, value=prog, padding=20, size_hint=(0.8, 0.8))
            b.add_widget(pb)

            self.add_widget(b)


class SettingsScreen(Screen):
    pass


class SettingsGrid(GridLayout):
    pass


class SettingGrid(GridLayout):
    pass


class SettingContactScreen(Screen):
    pass


class SettingContactGrid(GridLayout):
    pass


class SettingContactNittyGrid(GridLayout):
    pass


class SettingAlertScreen(Screen):
    pass


class SettingAlertGrid(GridLayout):
    pass


class SettingAlertNittyGrid(GridLayout):
    pass


class SettingGeneralScreen(Screen):
    pass


class SettingGeneralGrid(GridLayout):
    pass


class SettingGeneralNittyGrid(GridLayout):
    pass


class SettingAreasScreen(Screen):
    pass


class SettingAreasGrid(GridLayout):
    pass


class SettingAreasList(ListView):
    def __init__(self, **kwargs):
        super(SettingAreasList, self).__init__(**kwargs)

        bins = database_interface.get_data(database_interface.CONFIG.BINS)
        areas = list()

        for bin in bins:
            areas.append('Bin ' + str(bin['bin']) + ': ' + bin['name'])
            areas.append('a_buffer')

        list_item_args_converter = lambda row_index, info: {'text': info}
        self.adapter = ListAdapter(data=areas,
                                   args_converter=list_item_args_converter,
                                   cls=CustomBinListButton)


def go_to_update(value):
    MANAGER.current = "setting_update_bin_screen"


class CustomBinListButton(ListItemButton):

    def __init__(self, **kwargs):
        super(CustomBinListButton, self).__init__(**kwargs)

        if self.text == "a_buffer":
            self.background_normal = "Images/blank.png"
            self.selected_color = [0, 0, 0, 1.]
            self.deselected_color = [0, 0, 0, 1.]
            self.color = [0, 0, 0, 1]
            self.background_color = [0, 0, 0, 1]
            self.size = (10, 10)

        else:
            self.background_normal = "Images/blank.png"
            self.selected_color = [1, 1, 1, 1.]
            self.deselected_color = [1, 1, 1, 1.]
            self.color = [0, 0, 0, 1]
            self.background_color = [1, 1, 1, 1]
            self.size = (100, 100)
            self.bind(on_press=go_to_update)


class UpdateBinScreen(Screen):
    pass


class UpdateBinGrid(GridLayout):
    pass



def show_names(ad):
    return
    # what has changed

    ad.selection

    # clear UpdateBinTypeList
    # add names
    global MANAGER

    type_list = MANAGER.get_screen("setting_update_bin_screen").children[-1]

    type_list = type_list.children[0]
    type_list.remove_widget(type_list.children[0])

    names = list()

    for entry in database_interface.get_data(database_interface.GUIDELINES.SHELF_TIME,
                                             query={'type': self.text.lower()}):

        if entry['name'].capitalize() not in names:
            names.append(entry['name'].capitalize())



class UpdateBinDetailGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        categories = list()
        words = list()

        for entry in database_interface.get_data(database_interface.GUIDELINES.SHELF_TIME):

            if entry['type'].capitalize() not in words:
                categories.append(DataItem(text=entry['type'].capitalize()))
                words.append(entry['type'].capitalize())

        list_item_args_converter = lambda row_index, obj: {
            'text': obj.text,
            'height': 100,
            'selected_color': [0.2, 5, 0.5, 1.],
            'deselected_color': [1, 1, 1, 1.],
            'background_color': [1, 1, 1, 0.],
            'background_normal': "Images/blank.png",
            'color': [0, 0, 0, 1.],
            'padding': (5, 5)
            }

        ad = ListAdapter(data=categories,
                                   args_converter=list_item_args_converter,
                                   propagate_selection_to_data=True,
                                   cls=ListItemButton)

        ad.bind(on_selection_change=show_names)

        self.add_widget(ListView(adapter=ad))
        self.add_widget(ListView())

class DataItem(SelectableDataItem):
    text = ""

    def __init__(self, text="", **kwargs):
        super().__init__(**kwargs)
        self.text = text


class MainApp(App):
    def build(self):
        Config.set('graphics', 'fullscreen', '1')
        global MANAGER
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(AlertScreen(name="alert"))
        sm.add_widget(FoodScreen(name="food"))
        sm.add_widget(SettingsScreen(name="settings"))
        sm.add_widget(SettingAlertScreen(name="setting_alerts"))
        sm.add_widget(SettingContactScreen(name="setting_contact"))
        sm.add_widget(SettingAreasScreen(name="setting_areas"))
        sm.add_widget(SettingGeneralScreen(name="setting_general"))
        sm.add_widget(UpdateBinScreen(name="setting_update_bin_screen"))
        sm.current = "main"
        MANAGER = sm

        return sm