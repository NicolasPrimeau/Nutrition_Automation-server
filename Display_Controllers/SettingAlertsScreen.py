__author__ = 'Nixon'


from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.listview import ListView, ListItemButton
from kivy.adapters.listadapter import ListAdapter
import display_controller as controller
import database_interface


Builder.load_file('Kivy_Layouts/SettingAlerts.kv')


class SettingAlertScreen(Screen):
    pass


class SettingAlertGrid(GridLayout):
    pass


class SettingAlertSubGrid(GridLayout):
    def update_alerts(self):
        self.clear_widgets(children=0)
        self.add_widget(SettingAlertList())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class SettingAlertList(ListView):
    def update_alerts(self):
        names = controller.database_interface.get_data(database_interface.ALERT)
        li = list()

        for name in names:
            li.append(controller.DataItem(str(name['description'])))

        list_item_args_converter = lambda row_index, obj: {
            'text': obj.text,
            'height': 100,
            'select ed_color': [0.2, 5, 0.5, 1.],
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
        self.adapter.bind(on_selection_change=controller.go_to_alert)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_alerts()

