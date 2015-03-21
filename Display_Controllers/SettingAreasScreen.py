__author__ = 'Nixon'

from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.listview import ListView, ListItemButton
from kivy.adapters.listadapter import ListAdapter
import database_interface
import display_controller as controller


Builder.load_file('../Kivy_Layouts/SettingAreas.kv')


class SettingAreasScreen(Screen):
    pass


class SettingAreasGrid(GridLayout):
    pass


class SettingListGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(SettingAreasList())

class SettingAreasList(ListView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        bins = controller.sort_bin(database_interface.get_data(database_interface.CONFIG.BINS))
        areas = list()

        for bin in bins:
            areas.append(controller.DataItem('Bin ' + str(bin['bin']) + ': ' + bin['name'].capitalize()))

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
        self.adapter.bind(on_selection_change=controller.go_to_update)

