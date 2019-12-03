import requests

def translate_offers(text, lang):
    ''' Используется для перевода предложений '''
    URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    KEY = "trnsl.1.1.20191130T152747Z.f2879bdd4d9eba73.deccdb4c564b81195dc83da300ce2b70ef9dc624"

    def req():
        '''Запрос'''
        params = {
            "key": KEY,
            "text": text,
            "lang": lang
        }
        response = requests.get(URL, params=params)
        return response.json()

    return "📝 <b>" + ''.join(req()["text"]) + "</b>"

# print(translate_offers("What you see?", "en-ru"))