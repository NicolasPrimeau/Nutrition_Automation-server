

from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
import database_interface
import display_controller as controller

Builder.load_file('Kivy_Layouts/UpdateAlert.kv')


class UpdateAlertScreen(Screen):
    
    def add_alert(self):
        info = controller.MANAGER.get_screen("new_alert").children[0].children[0]
        contact = dict()
        if len(info.children[-1].text)>30:
            contact['name'] = info.children[-1].text[0:30].lstrip().rstrip()
        else:
            contact['name'] = info.children[-1].text.lstrip().rstrip()
        if len(info.children[-2].text)>40 and '@' in info[-2]:
            contact['email'] = info.children[-2].text[0:40].lstrip().rstrip()
        elif '@' in info.children[-2].text:
            contact['email'] = info.children[-2].text.lstrip().rstrip()
        if len(info.children[-3].text)>10:
            contact['phone'] = info.children[-3].text[0:10].lstrip().rstrip()
        else:
            contact['phone'] = info.children[-3].text.lstrip().rstrip()
        database_interface.update(database_interface.CONTACT, {'name': contact['name']}, contact)

        controller.MANAGER.get_screen("setting_alerts").children[0].children[0].children[0].update_contacts()
        controller.MANAGER.transition.direction = 'right'
        controller.MANAGER.current = "setting_alerts"

    def delete_alert(self):
        alert = controller.MANAGER.get_screen("setting_alerts").children[0].children[0].children[0]

        alert = alert.adapter
        if len(alert.selection) > 0:
            alert = alert.selection[0].text
            alert = database_interface.get_data(database_interface.ALERT, {'name': alert})
            alert = alert[0]
            database_interface.delete_alert(alert)

        controller.MANAGER.get_screen("setting_alerts").children[0].children[0].children[0].update_contacts()
        controller.MANAGER.transition.direction = 'right'
        controller.MANAGER.current = "setting_alerts"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class UpdateAlertGrid(GridLayout):
    pass


class UpdateAlertDetailGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(AlertTextInput(hint_text="Name", multiline=False))
        self.add_widget(AlertTextInput(hint_text="Email", multiline=False))
        self.add_widget(AlertTextInput(hint_text="Phone", multiline=False))


class AlertTextInput(TextInput):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = 30


class SpaceGrid(GridLayout):
    pass
