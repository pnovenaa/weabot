from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from typing import Any, Dict, List, Text, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    ActionExecuted,
    UserUttered,
)

class ActionWeather(Action):
	def name(self):
		return 'action_weather'
		
	def run(self, dispatcher: CollectingDispatcher, tracker:Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		import pyowm
		owm = pyowm.OWM('--yourOWMkey--')
		
		loc = tracker.get_slot('location')
		obs = owm.weather_at_place(loc)
		weather = obs.get_weather()

		temp = weather.get_temperature(unit='celsius')['temp']
		hum = weather.get_humidity()
		wind = weather.get_wind()['speed']

		response = "The temperature in {} is {}° C, the humidity is {}% and the wind speed is {} mph.".format(loc, temp, hum, wind)
						
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]