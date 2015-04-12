__author__ = 'Nixon'

from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.listview import ListView, ListItemLabel
from kivy.adapters.listadapter import ListAdapter
import Report

Builder.load_file('Kivy_Layouts/ReportScreen.kv')

def normalize(line, separator=' '):
    while(len(line) < 50):
        line = line + separator
    return line


class ReportScreen(Screen):
    pass


class ReportGrid(GridLayout):
    pass


class ReportLowerGrid(GridLayout):
    def update(self):
        self.clear_widgets()
        self.add_widget(ReportView())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update()


class ReportView(ListView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        report = Report.generate_consumption_report(8, hours=1)
        document = list()
        for section in report:
            document.append('-' * 50)
            document.append('Area: ' + str(section))
            document.append('Name: ' + str(report[section]['name']).capitalize())
            document.append('Type: ' + str(report[section]['type']).capitalize())
            if report[section]['date of purged'] is None:
                document.append('Purged: No')
            else:
                document.append('Purged: Yes (' +
                                report[section]['date of purged'] + " )")

            def print_consumption(con, title):
                document.append('-' * 30)
                document.append(title.capitalize())
                document.append('-' * 30)
                for decade in con:
                    document.append('Start: ' + decade['start time'].strftime('%H:%M %a %d/%b'))
                    document.append('End: ' + decade['end time'].strftime('%H:%M %a %d/%b'))
                    document.append('Decrease: ' + "{0:.2f}".format(decade['decrease']))
                    document.append('Increase: ' + "{0:.2f}".format(decade['increase']))
                    document.append('-'*20)
                document.pop()

            if 'hourly' in report[section]['consumption']:
                print_consumption(report[section]['consumption']['hourly'], 'hourly')

            if 'daily' in report[section]['consumption']:
                print_consumption(report[section]['consumption']['daily'], 'daily')

            if 'weekly' in report[section]['consumption']:
                print_consumption(report[section]['consumption']['weekly'], 'weekly')

            if 'monthly' in report[section]['consumption']:
                print_consumption(report[section]['consumption']['monthly'], 'monthly')

        list_adapter = ListAdapter(data=document, cls=ReportLine)
        self.adapter = list_adapter


class ReportLine(ListItemLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = 30
        self.height = 40
        self.padding = (10, 10)
