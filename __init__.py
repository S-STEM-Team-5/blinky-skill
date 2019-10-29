from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler


class Blinky(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('blinky.intent')
    def handle_blinky(self, message):
        self.speak_dialog('blinky')


def create_skill():
    return Blinky()

 // Should stop the blinking of the light. 

def stop(self):
    pass


