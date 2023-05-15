'''final project'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('Uom88dgP12KqnUbtA73RzAWA1FKvZfqsAdZsd1VczV2b')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com/instances/72ff0e6d-75bc-4148-a1e7-dde6b8db2d34')

#function to translate English to French
def english_to_french(english_text):
    '''write the code here'''
    translation = language_translator.translate(
    english_text,
    model_id='en-fr').get_result()
    french_text = translation["translations"][0]["translation"]
    return french_text

#function to translate French to English
def french_to_english(french_text):
    '''write the code here'''
    translation = language_translator.translate(
    french_text,
    model_id='fr-en').get_result()
    english_text = translation["translations"][0]["translation"]
    return english_text
