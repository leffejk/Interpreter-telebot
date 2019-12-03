import requests
import format_string

def dictio(text, lang):
    '''Получение json перевода'''
    DICT_KEY = "dict.1.1.20191130T145952Z.5f121d459fa8cf6d.4e776d73c744dbfb37d199969fab8673acc46fbb"
    URL_DICT = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup"
    params = {
        "key": DICT_KEY,
        "lang": lang,
        "text": text,
        "ui": "ru"
    }
    response = requests.get(URL_DICT, params=params).json()
    return response


def format_text(translations_page):
    '''Форматирование json в str'''
    full_list = []
    for translate in translations_page:  # БЕРЕТ ПЕРЕВОДЫ
        dict_info = []
        for k, v in translate.items():  # ИНФУ О ТЕКСТЕ И ПЕРЕВОД
            dict_info.append(v)

        full_list.append(f'''{"📝 <b>" + dict_info[0] + " (" + ", ".join(dict_info[1:-1]) + "):" + "</b>"}
{format_string.main_function(dict_info[-1])}
''')
    return full_list

def main_functioin(text, lang):
    ''' Главная функция для перевода '''
    main_string = "\n".join([_ for _ in format_text(dictio(text, lang)["def"])])
    return main_string




# print(*(format_text(dictio("What", "en-ru")["def"])),sep="\n")
