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


        # -------- inputs layout --------
        inputs_layout = GridLayout(cols=3)
        self.times = []
        while len(self.times) < 12:
            time = TextInput(
                multiline=False,
                font_size="50sp",
                background_color="gray",
                cursor_color="red",
                foreground_color="white")
            self.times.append(time)
            inputs_layout.add_widget(time)


        # -------- footer layout --------
        calculate_button = Button(
            text="calculate",
            font_size="20sp",
            background_color=(1, 0, 1, 1)
        )

        calculate_button.bind(on_press=self.press_key)

        result_label = Label(
            text="result",
            font_size="20sp",
            color=[0, 1, 0, 1]
        )
        self.result_label = result_label
    
        footer_layout = GridLayout(cols=2, size_hint=(1, 0.2))
        footer_layout.add_widget(calculate_button)
        footer_layout.add_widget(result_label)


        # -------- main layout --------
        box_layout = BoxLayout(orientation="vertical")
        box_layout.add_widget(header_label)
        box_layout.add_widget(inputs_layout)
        box_layout.add_widget(footer_layout)

        return box_layout


    def press_key(self, event):
        times = []
        for time in self.times:
            times.append(time.text)

        for i in range(len(times)):
            if type(times[i]) is str and len(times[i]) == 0:
                continue

            try:
                hour = re.findall(r"^([0-9]{1,2}):[0-9]{1,2}$", times[i])[0]
                minute = re.findall(r"^[0-9]{1,2}:([0-9]{1,2})$", times[i])[0]

                hour, minute = int(hour), int(minute)

                if minute > 60:
                    raise IndexError
            except IndexError:
                self.result_label.text = "error"
                return 1

            times[i] = (hour * 60) + minute

        total_time = 0
        for i in range(len(times)):
            if type(times[i]) is str and len(times[i]) == 0:
                continue

            total_time += times[i]

        hour = int(total_time / 60)
        minute = total_time - (hour * 60)

        self.result_label.text = str(hour).zfill(2) + ":" + str(minute).zfill(2)

        return 0


if __name__ == "__main__":
    Calculator().run()
