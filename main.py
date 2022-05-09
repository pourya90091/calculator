from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import re


class Calculator(App):
    def build(self):
        # -------- header label --------
        header_label = Label(
            text="Enter Times : ",
            font_size="50sp",
            size_hint=(1, 0.2)
        )


        # -------- content layout --------
        inputs = GridLayout(cols=3)
        self.times = []
        while len(self.times) < 12:
            time = TextInput(multiline=False, font_size="50sp")
            self.times.append(time)
            inputs.add_widget(time)


        # -------- footer layout --------
        submitButton = Button(
            text="calculate",
            font_size="20sp",
            background_color=(1, 0, 1, 1)
        )

        submitButton.bind(on_press=self.press_key)

        response = Label(
            text="Response : ",
            font_size="20sp",
            color=[0, 1, 0, 1]
        )
        self.response = response
    
        footer_layout = GridLayout(cols=2, size_hint=(1, 0.2))
        footer_layout.add_widget(submitButton)
        footer_layout.add_widget(response)


        # -------- main layout --------
        box_layout = BoxLayout(orientation="vertical")
        box_layout.add_widget(header_label)
        box_layout.add_widget(inputs)
        box_layout.add_widget(footer_layout)

        return box_layout

    
    def press_key(self, event):
        taked_times = (self.times)

        times = []
        for time in taked_times:
            times.append(time.text)
        
        for i in range(len(times)):
            if type(times[i]) is str and len(times[i]) == 0:
                continue
            hour = re.findall(r"(\w{1,2}):\w{1,2}", times[i])[0]
            minute = re.findall(r"\w{1,2}:(\w{1,2})", times[i])[0]
            hour, minute = int(hour), int(minute)

            times[i] = (hour * 60) + minute

        total_time = 0
        for i in range(len(times)):
            if type(times[i]) is str and len(times[i]) == 0:
                continue
            total_time += times[i]

        hour = int(total_time / 60)

        minute = total_time - (hour * 60)

        self.response.text = f"{hour}:{minute}"


if __name__ == "__main__":
    Calculator().run()
