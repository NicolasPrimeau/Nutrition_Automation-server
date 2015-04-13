

from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen
import database_interface
import display_controller as controller
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label


Builder.load_file('Kivy_Layouts/NewAlert.kv')


class NewAlertScreen(Screen):

    def add_alert(self):

        info = controller.MANAGER.get_screen("new_alert").children[0].children[0]
        alarm = dict()
        alarm['description'] = ""
        alarm['type'] = "quantity"
        alarm['flag'] = dict()
        alarm['flag']['max'] = 0
        alarm['flag']['min'] = 0
        alarm['target_bins'] = []

        if len(info.children[-1].text) > 200:
            alarm['description'] = info.children[-1].text[0:200].lstrip().rstrip()
        else:
            alarm['description'] = info.children[-1].text.lstrip().rstrip()

        try:
            temp = float(info.children[-2].text.lstrip().rstrip())
            if temp < 0:
                temp = 0
            elif temp > 10000:
                temp = 10000
            alarm['flag']['min'] = temp
        except ValueError as e:
            alarm['flag']['min'] = 0

        try:
            temp = float(info.children[-3].text.lstrip().rstrip())
            if temp < alarm['flag']['min']:
                temp = alarm['flag']['min']
            elif temp < 0:
                temp = 0
            elif temp > 10000:
                temp = 10000
            alarm['flag']['max'] = temp
        except ValueError as e:
            alarm['flag']['max'] = 0

        bin_boxes_root = info.children[-4]
        for child in bin_boxes_root.children:
            if child.children[0].active:
                alarm['target_bins'].append(int(child.children[-1].text.split(" ")[-1]))

        database_interface.store_data(database_interface.ALERT, alarm)

        controller.MANAGER.get_screen("setting_alerts").children[0].children[0].children[0].update_alerts()
        controller.MANAGER.transition.direction = 'right'
        controller.MANAGER.current = "setting_alerts"
        info.reset()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class NewAlertGrid(GridLayout):
    pass


class NewAlertDetailGrid(GridLayout):
    def reset(self):
        self.clear_widgets()
        self.add_widget(AlertTextInput(hint_text="Description", multiline=False))
        self.add_widget(AlertTextInput(hint_text="Minimum", multiline=False))
        self.add_widget(AlertTextInput(hint_text="Maximum", multiline=False))
        self.add_widget(BinGrid())


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reset()


class BinGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.rows = 2
        self.padding = 10

        for i in range(database_interface.count(database_interface.CONFIG.BINS)):
            self.add_widget(BinChoice(text="Bin "+str(i+1)))


class BinChoice(GridLayout):
    def __init__(self, text="", **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.rows = 1
        self.padding = 10
        self.add_widget(Label(text=text, font_size=30))
        self.add_widget(BinCheckBox())


class BinCheckBox(CheckBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (100, 100)


class AlertTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = 30


class SpaceGrid(GridLayout):
    pass
