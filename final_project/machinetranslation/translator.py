'''final project'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('url')

#function to translate English to French 
def english_to_french(english_text):
    '''write the code here'''
    translation = language_translator.translate(
    englishText,
    model_id='en-fr').get_result()
    french_text = translation("translations")
    return french_text

#function to translate French to English
def french_to_english(french_text):
    '''write the code here'''
    translation = language_translator.translate(
    french_text,
    model_id='fr-en').get_result()
    french_text = translation("translations")
    return english_text
