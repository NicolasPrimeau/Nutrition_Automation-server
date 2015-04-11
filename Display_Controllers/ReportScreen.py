__author__ = 'Nixon'

from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen
import Report

Builder.load_file('Kivy_Layouts/ReportScreen.kv')


class ReportScreen(Screen):
    pass


class ReportGrid(GridLayout):
    pass


class ReportLowerGrid(GridLayout):
    def update(self):
        data = Report.generate_consumption_report(1)
        print(data)


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update()

