'''final project'''
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['Uom88dgP12KqnUbtA73RzAWA1FKvZfqsAdZsd1VczV2b']
url = os.environ['https://api.us-east.language-translator.watson.cloud.ibm.com/instances/72ff0e6d-75bc-4148-a1e7-dde6b8db2d34']

authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('url')

### function to translate English to French 
def englishToFrench(englishText):
    #write the code here
    frenchText = language_translator.translate(
    englishText,
    model_id='en-fr').get_result()
    return frenchText

### function to translate French to English
def frenchToEnglish(frenchText):
    #write the code here
    englishText = language_translator.translate(
    frenchText,
    model_id='fr-en').get_result()
    return englishText

