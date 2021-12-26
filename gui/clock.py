from kivy.app import App

from kivy.clock import Clock

from kivy.uix.label import Label


# The kivy App that extends from the App class

class ClockDemo(App):
    count = 0

    def build(self):
        self.myLabel = Label(text='Waiting for updates...')
        # Start the clock
        Clock.schedule_interval(self.Callback_Clock, 2)
        return self.myLabel

    def Callback_Clock(self, dt):
        self.count = self.count + 1
        self.myLabel.text = "Updated %d...times" % self.count


# Run the app

if __name__ == '__main__':
    ClockDemo().run()
