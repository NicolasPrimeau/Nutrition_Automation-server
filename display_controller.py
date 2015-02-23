import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.uix.progressbar import ProgressBar
from kivy.uix.label import Label
from kivy.uix.listview import ListView, ListItemLabel, ListItemButton
from kivy.adapters.listadapter import ListAdapter
from kivy.clock import Clock
import database_interface



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
        super(MessagesList, self).__init__(**kwargs)

        concerns = database_interface.get_data(database_interface.DETECTED_CONCERNS)
        msgs = list()
        msgs.append(" ")

        if len(concerns) != 0:
            concerns = concerns[0]['info']
            for c in concerns:
                for msg in c:
                    msgs.append(msg['message']['plain'])

        self.adapter = ListAdapter(data=msgs, cls=ListItemLabel)


class FoodScreen(Screen):
    pass


class FoodGrid(GridLayout):
    pass


class DataGrid(GridLayout):
    def __init__(self, **kwargs):
        super(DataGrid, self).__init__(**kwargs)

        for bin in database_interface.get_data(database_interface.CONFIG.BINS):
            b = GridLayout(cols=1,rows=2)

            b.add_widget(Label(text=bin['name'], size_hint=(0.2, 0.2)))

            last_entry = database_interface.get_data(database_interface.FOOD, query={'bin': bin['bin']}, sort="date")

            if len(last_entry) == 0:
                prog = 0
            else:
                prog = last_entry[0]['quantity']

            pb = ProgressBar(max=100, value=prog, padding=20, size_hint=(0.8, 0.8))
            b.add_widget(pb)

            self.add_widget(b)


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


class SettingAreasList(ListView):
    def __init__(self, **kwargs):
        super(SettingAreasList, self).__init__(**kwargs)

        bins = database_interface.get_data(database_interface.CONFIG.BINS)
        areas = list()

        for bin in bins:
            areas.append('Bin ' + str(bin['bin']) + ': ' +bin['name'])
            areas.append('a_buffer')

        list_item_args_converter = lambda row_index, info: {'text': info}
        self.adapter = ListAdapter(data=areas,
                                   args_conerter=list_item_args_converter,
                                   cls=CustomBinListButton)


class CustomBinListButton(ListItemButton):
    def buttonCallback(instance):
	MANAGER.current = "setting_update_bin_screen"

    def __init__(self, **kwargs):
        super(CustomBinListButton, self).__init__(**kwargs)

        if self.text == "a_buffer":
            self.background_normal = "Images/blank.png"
            self.selected_color = [0, 0, 0, 1.]
            self.deselected_color = [0, 0, 0, 1.]
            self.color = [0, 0, 0, 1]
            self.background_color = [0, 0, 0, 1]
            self.size = (10, 10)

        else:
            self.background_normal = "Images/blank.png"
            self.selected_color = [0, .5, .5, 1.]
            self.deselected_color = [1, 1, 1, 1.]
            self.color = [0, 0, 0, 1]
            self.background_color = [1, 1, 1, 1]
            self.size = (100, 100)
            self.bind(on_press=self.buttonCallBack)


class UpdateBinScreen(Screen):
    pass


class UpdateBinGrid(GridLayout):
    pass


class UpdateBinCatergoryList(ListView):
    def __init__(self, **kwargs):
        super(UpdateBinCategoryList, self).__init__(**kwargs)

	categories = list()

	for entry in database_interface.get_data(database_interface.GUIDELINES.SHELF_TIME):

            if entry['type'] not in categories:
                categories.append(entry['type'].capitalize())
                categories.append('a_buffer')

        list_item_args_converter = lambda row_index, info: {'text': info}
        self.adapter = ListAdapter(data=categories,
                                   args_converter=list_item_args_converter,
                                   cls=CustomBinCategoryButton)		


class CustomBinCategoryButton(ListItemButton):
    def buttonCallback(instance):
	# clear UpdateBinTypeList
	# add names
	names = list()
	type_list = MANAGER.get_screen(MANAGER.current).children[-1]
        type_list.clear_widgets()
        for entry in database_interface.get_data(database_interface.GUIDELINES.SHELF_TIME, query={'type': instance.text.lower()}):
            if entry['name'] not in names:
                names.append(entry['name'].capitalize())
                names.append("a_buffer")
        list_item_args_converter = lambda row_index, info: {'text': info}
        type_list.adapter = ListAdapter(data=names,
                                        args_converter=list_item_args_converter,
                                        cls=CustomBinNameButton)

    def __init__(self, **kwargs):
        super(CustomBinCategoryButton, self).__init__(**kwargs)

        if self.text == "a_buffer":
            self.background_normal = "Images/blank.png"
            self.selected_color = [0, 0, 0, 1.]
            self.deselected_color = [0, 0, 0, 1.]
            self.color = [0, 0, 0, 1]
            self.background_color = [0, 0, 0, 1]
            self.size = (10, 10)

        else:
            self.background_normal = "Images/blank.png"
            self.selected_color = [0, .5, .5, 1.]
            self.deselected_color = [1, 1, 1, 1.]
            self.color = [0, 0, 0, 1]
            self.background_color = [1, 1, 1, 1]
            self.size = (100, 100)
            self.bind(on_press=self.buttonCallBack)



class UpdateBinTypeList(ListView):
    def __init__(self, **kwargs):
	super(UpdateBinTypeList(ListView)).__init__(**kwargs)


class CustomBinNameButton(ListItemButton):
	pass


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
        sm.add_widget(UpdateBinScreen(name="setting_upate_bin_screen"))
        sm.current = "main"
        MANAGER = sm

        return sm

