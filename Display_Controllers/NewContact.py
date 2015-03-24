

from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen
import database_interface
import display_controller as controller
from kivy.uix.textinput import TextInput

Builder.load_file('Kivy_Layouts/NewContact.kv')


class NewContactScreen(Screen):

    def add_contact(self):
        info = controller.MANAGER.get_screen("new_contact").children[0].children[0]
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

        if len(database_interface.get_data(database_interface.CONTACT, {'name': contact['name']}))== 0:
            database_interface.store_data(database_interface.CONTACT, contact)

        controller.MANAGER.get_screen("setting_contact").children[0].children[0].children[0].update_contacts()

        controller.MANAGER.transition.direction = 'right'
        controller.MANAGER.current = "setting_contact"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class NewContactGrid(GridLayout):
    pass


class NewContactDetailGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(ContactTextInput(hint_text="Name", multiline=False))
        self.add_widget(ContactTextInput(hint_text="Email", multiline=False))
        self.add_widget(ContactTextInput(hint_text="Phone", multiline=False))


class ContactTextInput(TextInput):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = 30

class SpaceGrid(GridLayout):
    pass
