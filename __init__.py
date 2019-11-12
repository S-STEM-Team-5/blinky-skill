from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler


class Blinky(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('blinky.intent')
    def handle_blinky(self, message):
        self.speak_dialog('blinky')
    
    @intent_handler('party.intent')
    def party_time(self, message):
        party_type = message.get.type('party'}
        if party_type is not None:
            self.speak_dialog('party.type',
                    {'party': party_type})
        else:
            self.speak_dialog('party.generic')




    def stop(self):
        pass



def create_skill():
    return Blinky()

 // Should stop the blinking of the light. 

