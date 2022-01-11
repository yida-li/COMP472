from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-", "%", "//", "**"]
        self.prevOperator = None
        self.prevClickedButton = None
        main_layout = BoxLayout(orientation="vertical")
        colors = [[1, 105/255, 180/255, 1], [251/255, 245 /
                                             255, 48/255, 1], [111/255, 69/255, 148/255, 1]]
        buttons = [
            ["1", "2", "3", "4"],
            ["5", "6", "7", "8"],
            ["9", "0", "1.618", "3.14"],
            [".", "+", "-", "/"],
            ["*", "**", "%", "//"],
            ["Clear", "Exit","Clear All"],
            ["Copy to Cache 1", "Clear Cache 1"],
            ["Copy to Cache 2", "Clear Cache 2"],
            ["Copy to Cache 3", "Clear Cache 3"],
            ["Copy to Cache 4", "Clear Cache 4"],
        ]
        self.answer = TextInput(
            multiline=False, readonly=True, halign="right", font_size=30, background_color=[168/255, 245/255, 200/255, 1]
        )
        main_layout.add_widget(self.answer)
        self.answer1 = TextInput(
            multiline=False, readonly=True, halign="right", font_size=30, background_color=[168/255, 245/255, 200/255, 1]
        )
        main_layout.add_widget(self.answer1)
        self.answer2 = TextInput(
            multiline=False, readonly=True, halign="right", font_size=30, background_color=colors[2]
        )
        main_layout.add_widget(self.answer2)
        self.answer3 = TextInput(
            multiline=False, readonly=True, halign="right", font_size=30, background_color=colors[2]
        )
        main_layout.add_widget(self.answer3)
        self.answer4 = TextInput(
            multiline=False, readonly=True, halign="right", font_size=30, background_color=colors[2]
        )
        main_layout.add_widget(self.answer4)
        self.answer5 = TextInput(
            multiline=False, readonly=True, halign="right", font_size=30, background_color=colors[2]
        )
        main_layout.add_widget(self.answer5)
        # hex color selection

        counter = 0
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                if counter <= 11:
                    button = Button(
                        text=label,
                        pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=colors[0]
                    )
                elif counter <= 21:
                    button = Button(
                        text=label,
                        pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=colors[1]
                    )
                else:
                    button = Button(
                        text=label,
                        pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=colors[2]
                    )
                counter = counter+1
                # if (counter % 2) == 0:
                #     button = Button(
                #         text=label,
                #         pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=colors[1]
                #     )
                # else:
                #     button = Button(
                #         text=label,
                #         pos_hint={"center_x": 0.5, "center_y": 0.5}, background_color=colors[0]
                #     )
                # counter = counter+1
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}, size_hint=(1, 1), background_color=[168/255, 245/255, 200/255, 1]
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        whatIsCurrentlyInRam = self.answer.text
        button_chosen = instance.text

        if button_chosen == "X":
            # hard reset
            app.stop()
        if button_chosen == "Copy to Cache 1":

            self.answer2.text = self.answer1.text
            return
        if button_chosen == "Clear Cache 1":

            self.answer2.text = ""
            return
        if button_chosen == "Copy to Cache 2":

            self.answer3.text = self.answer1.text
            return
        if button_chosen == "Clear Cache 2":

            self.answer3.text = ""
            return
        if button_chosen == "Copy to Cache 3":

            self.answer4.text = self.answer1.text
            return
        if button_chosen == "Clear Cache 3":

            self.answer4.text = ""
            return
        if button_chosen == "Copy to Cache 4":

            self.answer5.text = self.answer1.text
            return
        if button_chosen == "Clear Cache 4":

            self.answer5.text = ""
            return            
        if button_chosen == "Clear":
            # hard reset
            self.answer.text = ""
            self.answer1.text = ""
        if button_chosen == "Clear All":
            # hard reset
            self.answer.text = ""
            self.answer1.text = ""
            self.answer2.text = ""
            self.answer3.text = "" 
            self.answer4.text = ""
            self.answer5.text = ""                         
        else:
            if whatIsCurrentlyInRam and (
                    self.prevOperator and button_chosen in self.operators):
                return

            elif whatIsCurrentlyInRam == "" and button_chosen in self.operators:
                return

            else:
                self.answer.text = whatIsCurrentlyInRam + button_chosen
            #    "23/434"        =   "23/"              +    "434"

        self.prevClickedButton = button_chosen
        self.prevOperator = self.prevClickedButton in self.operators

    def on_solution(self, instance):
        text = self.answer.text
        if text:
            pythonCalculator = str(eval(self.answer.text))
            # essentially the bread and butter of the calculator because the eval method evaluates expression dynamically
            # even sum of multiple set of numbers or true false, etc etc
            # unlike coen 316 where I had to design an actual CPU let alone an ALU for basic arthmetic expression lol
            self.answer1.text = pythonCalculator
            # 3434/242 is gonna get calculated by itself boringgggg


if __name__ == "__main__":
    app = MainApp()
    app.run()
