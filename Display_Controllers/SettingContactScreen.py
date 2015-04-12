__author__ = 'Nixon'


from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.listview import ListView, ListItemButton
from kivy.adapters.listadapter import ListAdapter
import display_controller as controller
import database_interface

Builder.load_file('Kivy_Layouts/SettingContacts.kv')


class SettingContactScreen(Screen):
    pass


class SettingContactGrid(GridLayout):
    pass


class SettingContactSubGrid(GridLayout):
    def update_contacts(self):
        self.clear_widgets(children=0)
        self.add_widget(SettingContactList())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class SettingContactList(ListView):

    def update_contacts(self):
        names = controller.database_interface.get_data(database_interface.CONTACT)
        li = list()

        for name in names:
            li.append(controller.DataItem(str(name['name'])))

        list_item_args_converter = lambda row_index, obj: {
            'text': obj.text,
            'font_size': 30,
            'height': 100,
            'selected_color': [0.2, 5, 0.5, 1.],
            'deselected_color': [1, 1, 1, 1.],
            'background_color': [1, 1, 1, 0.],
            'background_normal': "Images/Box.png",
            'color': [0, 0, 0, 1.],
            'padding': (5, 5)
        }
        self.adapter = ListAdapter(data=li,
                                   args_converter=list_item_args_converter,
                                   propagate_selection_to_data=True,
                                   cls=ListItemButton)
        self.adapter.bind(on_selection_change=controller.go_to_contact)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_contacts()

