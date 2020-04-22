from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recycleview import RecycleView 
from kivy.uix.label import Label




class Display(TabbedPanel):
    def __init__(self, **kwargs):
        super(Display, self).__init__(**kwargs)
    

class AircraftTitle(GridLayout):
    pass
 
class AircraftList(RecycleView):
    def __init__(self, **kwargs):
        super(AircraftList, self).__init__(**kwargs)
        self.data = [{"text": str(x)} for x in range(100)]

class AMToolApp(App):
    def build(self):
        return Display()
