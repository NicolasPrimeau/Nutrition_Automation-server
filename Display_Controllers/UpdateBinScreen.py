

from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.listview import ListView, ListItemButton
from kivy.adapters.listadapter import ListAdapter
import datetime
import database_interface
import display_controller as controller

Builder.load_file('Kivy_Layouts/UpdateBin.kv')


class UpdateBinScreen(Screen):
    def config_bin(self):

        name_list = self.children[0].children[0].children[0]
        type_list = self.children[0].children[0].children[1]

        if len(name_list.adapter.selection) == 0 or len(name_list.adapter.selection) == 0:
            return

        bin_list = controller.MANAGER.get_screen("setting_areas").children[0].children[0].children[0]

        area = bin_list.adapter.selection[0].text.split(":")[0].split(" ")[-1]

        new_bin = dict()
        new_bin['bin'] = int(area)
        new_bin['name'] = name_list.adapter.selection[0].text.lower()
        new_bin['type'] = type_list.adapter.selection[0].text.lower()
        new_bin['date'] = datetime.datetime.now()
        new_bin['display_type'] = 0

        controller.MANAGER.transition.direction = 'right'
        controller.MANAGER.current = 'main'

        database_interface.configure_bin(new_bin)

        controller.update_all_bins()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class UpdateBinGrid(GridLayout):
    pass


class UpdateBinDetailGrid(GridLayout):

    def show_bin_names(self, ad):
        # ad = self.children[0]
        if len(ad.selection) == 0:
            return

        type_list = controller.MANAGER.get_screen("setting_update_bin").children[-1]

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
            'font_size': 30,
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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        categories = list()
        words = list()

        for entry in database_interface.get_data(database_interface.GUIDELINES.SHELF_TIME, {}):

            if entry['type'].capitalize() not in words:
                categories.append(controller.DataItem(text=entry['type'].capitalize()))
                words.append(entry['type'].capitalize())

        list_item_args_converter = lambda row_index, obj: {
            'text': obj.text,
            'height': 100,
            'font_size': 30,
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

        ad.bind(on_selection_change=self.show_bin_names)
        self.add_widget(ListView(adapter=ad))
        self.add_widget(ListView())