from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.menu import MDDropdownMenu
from time import sleep
import pytube
import youtube_downloader
from kivymd.uix.snackbar import Snackbar
from kivy.properties import ListProperty, StringProperty


class CustomSnackbar(Snackbar):
    icon = StringProperty()
class YT_DOWNLODER(MDApp):
    def build(self):
        loader = Builder.load_file("main.kv")
        return loader
    def dropme(self):        
        menu_items = [{"icon": "quality-high", "text": "High"},{"icon": "quality-medium", "text": "Medium"},{"icon": "quality-low", "text": "Low"} ]
        self.smenu = MDDropdownMenu(
            caller=self.root.ids.drop_item,
            items=menu_items,
            position="center",
            callback=self.set_item,
            width_mult=4.5,
        )
        self.smenu.open()
 
    def set_item(self, instance):
        # print(instance.text,"----------this is instance")
        gender = instance.text
        mm=self.root.ids.drop_item.set_item(gender)
        self.root.ids.drop_item.text = gender
        self.smenu.dismiss()
        
    def download_video(self,url, resolution):
        youtube_downloader.download_video(url, resolution)
        print(url,resolution)
        self.root.ids.url.text = ""
        self.root.ids.drop_item.text = "Quality"
        print("download done...")
        
    def error(self,msg):
        Snackbar(
        text= msg           
    ).show()

YT_DOWNLODER().run()
