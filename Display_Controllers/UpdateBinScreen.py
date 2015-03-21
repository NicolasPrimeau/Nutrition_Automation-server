

from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.listview import ListView, ListItemButton
from kivy.adapters.listadapter import ListAdapter
import datetime
import database_interface
import display_controller as controller

Builder.load_file('../Kivy_Layouts/UpdateBin.kv')

class UpdateBinScreen(Screen):
    def config_bin(self):

        name_list = self.children[0].children[0].children[0]
        type_list = self.children[0].children[0].children[0]

        if len(name_list.adapter.selection) == 0 or len(name_list.adapter.selection) == 0:
            return

        bin_list = controller.MANAGER.get_screen("setting_areas").children[0].children[0].children[0]

        bin = bin_list.adapter.selection[0].text.split(":")[0].split(" ")[-1]

        new_bin = dict()
        new_bin['bin'] = int(bin)
        new_bin['name'] = name_list.adapter.selection[0].text.lower()
        new_bin['type'] = type_list.adapter.selection[0].text.lower()
        new_bin['date'] = datetime.datetime.now()

        database_interface.configure_bin(new_bin)

        controller.update_all_bins()
        controller.MANAGER.current = "main"


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
                categories.append(controller.DataItem(text=entry['type'].capitalize()))
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

        ad.bind(on_selection_change=controller.show_bin_names)
        self.add_widget(ListView(adapter=ad))
        self.add_widget(ListView())

