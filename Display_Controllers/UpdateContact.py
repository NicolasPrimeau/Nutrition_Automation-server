

from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
import database_interface
import display_controller as controller

Builder.load_file('Kivy_Layouts/UpdateContact.kv')

class UpdateContactScreen(Screen):
    
    def add_contact(self):
        info = controller.MANAGER.get_screen("new_contact_screen").children[0].children[0]
        contact = dict()
        if len(info.children[2].text)>30:
            contact['name'] = info.children[2].text[0:30].lstrip().rstrip()
        else:
            contact['name'] = info.children[2].text.lstrip().rstrip()
        if len(info.children[1].text)>40 and '@' in info[1]:
            contact['email'] = info.children[1].text[0:40].lstrip().rstrip()
        elif '@' in info.children[1].text:
            contact['email'] = info.children[1].text.lstrip().rstrip()
        if len(info.children[2].text)>10:
            contact['phone'] = info.children[0].text[0:10].lstrip().rstrip()
        else:
            contact['phone'] = info.children[0].text.lstrip().rstrip()
        database_interface.update(database_interface.CONTACT, {'name': contact['name']}, contact)

        controller.MANAGER.transition.direction = 'left'
        controller.MANAGER.current = "setting_update_contact_screen"


    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class UpdateContactGrid(GridLayout):
    pass


class UpdateContactDetailGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(ContactTextInput(hint_text="Name", multiline=False))
        self.add_widget(ContactTextInput(hint_text="Email", multiline=False))
        self.add_widget(ContactTextInput(hint_text="Phone", multiline=False))


class ContactTextInput(TextInput):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = 30
