# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from translate import Translator
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import emoji


class ActionTranslateToLang(Action):

    def name(self) -> Text:
        return "action_translate_to_lang"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #text to be translated 
        translate_text=next(tracker.get_latest_entity_values("translate_text"),None)

        #language the text should be translated into 
        target_language=next(tracker.get_latest_entity_values("target_language"),None)

        #if we have language but missing the text 
        if not translate_text:
            msg=f"give me a translate_text to translate"
            dispatcher.utter_message(text=msg)
            translate_text=next(tracker.get_latest_entity_values("translate_text"), None)
            return[]

        #if we know text but not the target language 
        if not target_language:
            msg=f"Give me a target language"
            dispatcher.utter_message(text=msg)
            target_language=next(tracker.get_latest_entity_values("target_language"), None)
            return []
        
        #call on python translate module to define translations 
        translator=Translator(from_lang="english", to_lang=target_language)

        #translate + return translated text 
        translation=translator.translate(translate_text)
        msg=f"translation: {translation}"
        dispatcher.utter_message(text=msg)
        return[]
