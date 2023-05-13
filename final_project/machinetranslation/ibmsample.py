import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('Uom88dgP12KqnUbtA73RzAWA1FKvZfqsAdZsd1VczV2b')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com/instances/72ff0e6d-75bc-4148-a1e7-dde6b8db2d34')

translation = language_translator.translate(
    text=['ten', 'how', 'are', 'you', 'today?'],
    model_id='en-es').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))
x = []
for i in translation:
    for j in 
    x = translation["translations"][0:]
print (x.values())