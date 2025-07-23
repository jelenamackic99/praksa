from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar
from kivy.uix.boxlayout import BoxLayout

class SliderAndProgressBarExample(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)
        
        # Slider example
        def on_slider_value(instance, value):
            label.text = f'Slider Value: {value:.2f}'
        slider = Slider(min=0, max=50, value=25)
        slider.bind(value=on_slider_value)
        layout.add_widget(slider)
        
        label = Label(text='Slider Value: 50.00')
        layout.add_widget(label)
        
        # Progressbar example
        def update_progressbar(dt):
            if progressbar.value < 100:
                progressbar.value += 1
            else:
                label.text = f'Vrednost slajdera: {slider.value:.2f}'
                progressbar.value = 0
        progressbar = ProgressBar(max=100)
        Clock.schedule_interval(update_progressbar, 0.1)
        layout.add_widget(progressbar)
        
        return layout

if __name__ == '__main__':
    SliderAndProgressBarExample().run()
