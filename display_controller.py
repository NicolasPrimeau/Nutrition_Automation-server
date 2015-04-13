import kivy
kivy.require('1.8.0')


from kivy.uix.screenmanager import ScreenManager
import database_interface
from kivy.adapters.models import SelectableDataItem
from kivy.app import App
from kivy.config import Config

MANAGER = None

# show bin names
from Display_Controllers.SettingAreasScreen import SettingAreasList
from Display_Controllers.AlertScreen import AlertScreen
from Display_Controllers.FoodScreen import FoodScreen
from Display_Controllers.MainScreen import MainScreen
from Display_Controllers.SettingAlertsScreen import SettingAlertScreen
from Display_Controllers.SettingAreasScreen import SettingAreasScreen
from Display_Controllers.SettingContactScreen import SettingContactScreen
from Display_Controllers.SettingGeneralScreen import SettingGeneralScreen
from Display_Controllers.SettingScreen import SettingsScreen
from Display_Controllers.UpdateBinScreen import UpdateBinScreen
from Display_Controllers.UpdateContact import UpdateContactScreen
from Display_Controllers.NewContact import NewContactScreen
from Display_Controllers.UpdateAlert import UpdateAlertScreen
from Display_Controllers.NewAlert import NewAlertScreen
from Display_Controllers.ReportScreen import ReportScreen


def update_all_bins():
    bin_grid = MANAGER.get_screen("setting_areas").children[0].children[0]

    bin_grid.clear_widgets()
    bin_grid.add_widget(SettingAreasList())

    bin_grid = MANAGER.get_screen("food").children[0]
    bin_grid.children[1].update()


def sort_bin(bins):
    ar = [dict() for _ in range(len(bins))]

    for bin in bins:
        ar[bin['bin']-1] = bin
    bins = ar
    return bins


def update_and_view_food():
    MANAGER.transition.direction = 'down'
    MANAGER.current="food"
    bin_grid = MANAGER.get_screen("food").children[0]
    bin_grid.children[1].update()


def go_to_update(value):
    MANAGER.transition.direction = 'left'
    MANAGER.current = "setting_update_bin"


def go_to_contact(value):
    global MANAGER
    contact = MANAGER.get_screen("setting_contact").children[0].children[0].children[0]

    contact = contact.adapter
    if len(contact.selection) > 0:
        contact = contact.selection[0].text

        update_cont = MANAGER.get_screen("setting_update_contact").children[0].children[0]
        contact = database_interface.get_data(database_interface.CONTACT, {'name': contact})
        contact = contact[0]
        update_cont.children[-1].text = contact['name']
        update_cont.children[-2].text = contact['email']
        update_cont.children[-3].text = contact['phone']

    MANAGER.transition.direction = 'left'
    MANAGER.current = "setting_update_contact"


def go_to_alert(value):
    global MANAGER
    MANAGER.get_screen("setting_update_alert").children[0].children[0].update()
    MANAGER.transition.direction = 'left'
    MANAGER.current = "setting_update_alert"

class DataItem(SelectableDataItem):
    text = ""

    def __init__(self, text="", **kwargs):
        super().__init__(**kwargs)
        self.text = text


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
        sm.add_widget(UpdateBinScreen(name="setting_update_bin"))
        sm.add_widget(UpdateContactScreen(name="setting_update_contact"))
        sm.add_widget(NewContactScreen(name="new_contact"))
        sm.add_widget(UpdateAlertScreen(name="setting_update_alert"))
        sm.add_widget(NewAlertScreen(name="new_alert"))
        sm.add_widget(ReportScreen(name="report"))
        sm.current = "main"
        MANAGER = sm

        return sm
