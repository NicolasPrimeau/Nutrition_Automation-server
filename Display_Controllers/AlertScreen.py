__author__ = 'Nixon'


from kivy.uix.gridlayout import GridLayout
from kivy.base import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.listview import ListView, ListItemLabel
from kivy.adapters.listadapter import ListAdapter
import database_interface
import re

Builder.load_file('Kivy_Layouts/AlertScreen.kv')


class AlertScreen(Screen):
    pass


class AlertGrid(GridLayout):
    pass


class MessagesList(ListView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        concerns = database_interface.get_data(database_interface.DETECTED_CONCERNS)
        msgs = list()
        #msgs.append(" ")
        flag = True
        try:
            concerns[0]
        except IndexError as e:
            flag = False


        if flag:
            concerns = concerns[0]['info']
            for msg in concerns:
                msg = msg['message']['plain'].split(" ")
                while len(msg) > 0:
                    line = msg.pop(0)
                    if len(msg) == 0:
                        msgs.append(line)
                        msgs.append(" ")
                        break
                    while (len(line) + 1 + len(msg[0])) < 40:
                        line += " " + msg.pop(0)
                        if len(msg) == 0:
                            break
                    msgs.append(line)
                msgs.append(" ")

        msgs.pop()
        list_item_args_converter = lambda row_index, text: {
            'text': text,
            'height': 15,
            'font_size': 30
        }

        self.adapter = ListAdapter(data=msgs,
                                   args_converter=list_item_args_converter,
                                   cls=ListItemLabel)
