from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Goto settings'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Calender'
            
            on_press:
                root.manager.transition.direction = 'right' 
                root.manager.current = 'analysis'
        Button:
            text: 'Description'
            
            on_press:
                root.manager.transition.direction = 'left' 
                root.manager.current = 'feast'                              
        Button:
            text: 'Quit'
            on_press: TestApp.stop()
<PlaceHolder>:
    BoxLayout:
        
        orientation: 'vertical'
        
        Button:
            
            text: 'Back to Menu'
            on_press:
                root.manager.transition.direction = 'left'  
                root.manager.current = 'menu'
        Button:
            
            text: 'Place 1'
        Button:
            
            text: 'Place 2'
        Button:
            
            text: 'Place 3'
        Button:
            
            text: 'Place 4'
        Button:
            
            text: 'Place 5'            
<Calender>:
    BoxLayout:  
        orientation: 'vertical'
        
        Button:
            
            text: 'Back to Menu'
            on_press: root.manager.current = 'menu'            
        BoxLayout:  
            orientation: 'horizontal'
            
            Button:
                
                text: 'January'            
            Button:
                
                text: 'February'
            Button:
                
                text: 'March'
            Button:
                
                text: 'April' 
        BoxLayout:  
            orientation: 'horizontal'
            
            Button:
                
                text: 'May'            
            Button:
                
                text: 'July'
            Button:
                
                text: 'June'
            Button:
                
                text: 'August' 
        BoxLayout:  
            orientation: 'horizontal'
            
            Button:
                
                text: 'September'            
            Button:
                
                text: 'October'
            Button:
                
                text: 'November'
            Button:
                
                text: 'December'
        Button:
            
            text: 'Exit'
            on_press: TestApp.stop()    
          
<Feast>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'This is a simple calender application'
            size_hint_y: '3.8'
            size: self.texture_size
            pos_hint: {'center': 1}
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'                    
<SettingsScreen>:

    BoxLayout:
        orientation: 'horizontal'
        Button:
            text: 'View Events'
            on_press: root.manager.current = 'placeholder'
        Button:            
            text: 'Create Event'
        Button:            
            text: 'Update Event' 
        Button:            
            text: 'Delete Event'              
        Button:
            text: 'Back to menu'
            on_press: 
                root.manager.transition.direction = 'left'  
                root.manager.current = 'menu'
""")

# Declare both screens


class MenuScreen(Screen):
    pass


class PlaceHolder(Screen):
    pass


class SettingsScreen(Screen):
    pass


class Calender(Screen):
    pass


class Feast(Screen):
    pass


class CalenderApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(PlaceHolder(name='placeholder'))
        sm.add_widget(Calender(name='analysis'))
        sm.add_widget(Feast(name='feast'))

        return sm


if __name__ == '__main__':

    CalenderApp().run()
