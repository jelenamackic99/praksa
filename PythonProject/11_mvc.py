from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

# Model
class CounterModel:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

# View
class CounterView(BoxLayout):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller

        # Create widgets
        self.label = Label(text='0', font_size=48, size_hint_y=None, height=100)
        self.increment_button = Button(text='Increment', size_hint_y=None, height=50)
        self.decrement_button = Button(text='Decrement', size_hint_y=None, height=50)

        # Add widgets to layout
        self.add_widget(self.label)
        self.add_widget(self.increment_button)
        self.add_widget(self.decrement_button)

    def update_label(self, count):
        self.label.text = str(count)

# Controller
class CounterController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.update_label(self.model.count)

    def increment(self, instance):
        self.model.increment()
        self.view.update_label(self.model.count)

    def decrement(self, instance):
        self.model.decrement()
        self.view.update_label(self.model.count)

class CounterApp(App):
    def build(self):
        model = CounterModel()
        view = CounterView(controller=None)
        controller = CounterController(model, view)
        view.controller = controller
        # Set up the controller after assigning it to the view
        if view.controller:
            view.increment_button.bind(on_press=view.controller.increment)
            view.decrement_button.bind(on_press=view.controller.decrement)
        return view

if __name__ == '__main__':
    CounterApp().run()
