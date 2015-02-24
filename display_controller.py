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
import datetime


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

# show bin names


def show_bin_names(ad):
    if len(ad.selection) == 0:
        return

    global MANAGER

    type_list = MANAGER.get_screen("setting_update_bin_screen").children[-1]

    type_list = type_list.children[0]
    type_list.remove_widget(type_list.children[0])

    names = list()

    for entry in database_interface.get_data(database_interface.GUIDELINES.SHELF_TIME,
                                             query={'type': ad.selection[0].text.lower()}):

        if entry['name'].capitalize() not in names:
            names.append(entry['name'].capitalize())

    list_item_args_converter = lambda row_index, info: {
        'text': info,
        'height': 100,
        'selected_color': [0.2, 5, 0.5, 1.],
        'deselected_color': [1, 1, 1, 1.],
        'background_color': [1, 1, 1, 0.],
        'background_normal': "Images/Box.png",
        'color': [0, 0, 0, 1.],
        'padding': (5, 5)
    }
    ad = ListAdapter(data=names,
                     args_converter=list_item_args_converter,
                     cls=ListItemButton)
    type_list.add_widget(ListView(adapter=ad))


def update_all_bins():
    bin_grid = MANAGER.get_screen("setting_areas").children[0].children[0]

    bin_grid.clear_widgets()
    bin_grid.add_widget(SettingAreasList())

    bin_grid = MANAGER.get_screen("food").children[0]
    bin_grid.children[1].update()


def sort_bin(bins):
    ar = [dict() for _ in range(len(bins))]

    for bin in bins:
        ar[bin['bin']-1] = bin
    bins = ar
    return bins


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

        list_item_args_converter = lambda row_index, text: {
            'text': text,
            'height': 100,
            'font_size': 30
        }

        self.adapter = ListAdapter(data=msgs,
                                   args_converter=list_item_args_converter,
                                   cls=ListItemLabel)


class FoodScreen(Screen):
    pass


class FoodGrid(GridLayout):
    pass


class DataGrid(GridLayout):
    def update(self):
        self.clear_widgets()

        bins = sort_bin(database_interface.get_data(database_interface.CONFIG.BINS))

        for bin in bins:
            b = GridLayout(cols=1, rows=2)

            b.add_widget(Label(text=bin['name'].capitalize(), size_hint=(0.2, 0.2)))

            last_entry = database_interface.get_data(database_interface.FOOD, query={'bin': bin['bin']}, sort="date")

            if len(last_entry) == 0:
                prog = 0
            else:
                prog = last_entry[0]['quantity']

            pb = ProgressBar(max=100, value=prog, padding=20, size_hint=(0.8, 0.8))
            b.add_widget(pb)

            self.add_widget(b)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update()


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


class BackButtonGrid(GridLayout):
    pass


class SettingListGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(SettingAreasList())


class SettingAreasList(ListView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        bins = sort_bin(database_interface.get_data(database_interface.CONFIG.BINS))
        areas = list()

        for bin in bins:
            areas.append(DataItem('Bin ' + str(bin['bin']) + ': ' + bin['name'].capitalize()))

        list_item_args_converter = lambda row_index, obj: {
            'text': obj.text,
            'height': 100,
            'selected_color': [0.2, 5, 0.5, 1.],
            'deselected_color': [1, 1, 1, 1.],
            'background_color': [1, 1, 1, 0.],
            'background_normal': "Images/Box.png",
            'color': [0, 0, 0, 1.],
            'padding': (5, 5)
        }
        self.adapter = ListAdapter(data=areas,
                                   args_converter=list_item_args_converter,
                                   propagate_selection_to_data=True,
                                   cls=ListItemButton)
        self.adapter.bind(on_selection_change=go_to_update)


def go_to_update(value):
    MANAGER.current = "setting_update_bin_screen"


class UpdateBinScreen(Screen):
    def config_bin(self):

        name_list = self.children[0].children[0].children[0]
        type_list = self.children[0].children[0].children[0]

        if len(name_list.adapter.selection) == 0 or len(name_list.adapter.selection) == 0:
            return

        global MANAGER

        bin_list = MANAGER.get_screen("setting_areas").children[0].children[0].children[0]

        bin = bin_list.adapter.selection[0].text.split(":")[0].split(" ")[-1]

        new_bin = dict()
        new_bin['bin'] = int(bin)
        new_bin['name'] = name_list.adapter.selection[0].text.lower()
        new_bin['type'] = type_list.adapter.selection[0].text.lower()
        new_bin['date'] = datetime.datetime.now()

        database_interface.configure_bin(new_bin)

        update_all_bins()
        MANAGER.current = "main"


    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class UpdateBinGrid(GridLayout):
    pass


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
            'background_normal': "Images/Box.png",
            'color': [0, 0, 0, 1.],
            'padding': (5, 5)
            }

        ad = ListAdapter(data=categories,
                         args_converter=list_item_args_converter,
                         propagate_selection_to_data=True,
                         cls=ListItemButton)

        ad.bind(on_selection_change=show_bin_names)
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