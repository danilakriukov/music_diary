import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.core.window import Window
import mysql.connector

my_db = mysql.connector.connect(
    host = 'b500u5coeyqxe74jtgz2-mysql.services.clever-cloud.com',
    user = 'u4guu7kkgslrpafp',
    database = 'b500u5coeyqxe74jtgz2',
    passwd = 'FstTZJ6TJJTxmEChRjMB',
    port = 3306
) 


my_cursor = my_db.cursor(buffered=True,dictionary=True)
my_cursor.execute("SELECT * FROM listoftasks")
tasksforoutputlist = my_cursor.fetchall()
tasksforoutput = str(tasksforoutputlist)

class Hogweed(App):
    def build(self):
        #self.window.load_file('background_color.kv')
        Window.clearcolor = (1,1,1,1)
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6,0.7)
        self.window.pos_hint = {'center_x': 0.5, 'center_y':0.5}
        #add widgets to window

        # image widget
        #self.window.add_widget(Image(source="hogweed.png"))
        # label widget
        self.greeting = Label(
                        text='Домашнее задание:',
                        font_size = 18,
                        color='#123456'
                        )
        self.window.add_widget(self.greeting)
        self.tasks = Label(
                        text=tasksforoutput,
                        font_size = 12,
                        color='#123456'
                        )
        self.window.add_widget(self.tasks)
 

        return self.window


    def callback(self,instance):
        self.greeting.text = "You favourite plant is " + self.user.text + ", buddy"   
        

if __name__ == "__main__":
    Hogweed().run()