# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

timezones = {
    "London": "UTC+1:00",
    "Manila": "UTC+8:00"
}

class ActionShowTimezone(Action):

    def name(self) -> Text:
        return "action_show_timezone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot("city")
        timezone = timezones.get(city)

        output = "Sorry, I couldn't find the timezone of {}.".format(city)
        if timezone:
            output = "The timezone of {} is {}.".format(city, timezone)
        
        dispatcher.utter_message(text=output)

        return []
