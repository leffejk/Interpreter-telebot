def tr_def(tr: list):
    ''' Используется для пункта "Перевод" '''
    main_string = ""
    main_string += "Перевод: "  # Перевод:
    for _ in tr:
        main_string = main_string + "<b>" + _["text"] + "</b>" + " <i>("  # Перевод: word (
        try:
            main_string += (_["pos"] + ";")  # Перевод: word (часть_речи;
        except:
            pass
        try:
            main_string += (_["gen"] + ";")  # Перевод: word (часть_речи;род;
        except:
            pass
        try:
            main_string += (_["num"] + ";")  # Перевод: word (часть_речи;род;число;
        except:
            pass
        main_string += ")</i>; "  # Перевод: word (часть_речи;род;число;);
    main_string += "\n"  # + переход на новую строку
    return main_string


def syn_def(syn: list):
    ''' Используется для пункта "Синонимы" '''
    main_string = ""
    main_string += "Синонимы: "  # Синонимы:
    for _ in syn:
        main_string = main_string + _["text"] + " <i>("  # Синонимы: word (
        try:
            main_string += (_["pos"] + ";")  # Синонимы: word (часть_речи;
        except:
            pass
        try:
            main_string += (_["gen"] + ";")  # Синонимы: word (часть_речи;род;
        except:
            pass
        try:
            main_string += (_["num"] + ";")  # Синонимы: word (часть_речи;род;число;
        except:
            pass
        main_string += ")</i>; "  # Синонимы: word (часть_речи;род;число;);
        if "tr" in _:  # Если есть раздел "Перевод", то добавить его
            main_string += "\n"
            main_string += tr_def(_["tr"])

    main_string += "\n"  # + переход на новую строку
    return main_string


def mean_def(mean: list):
    ''' Используется для пункта "Значения" '''
    main_string = ""
    main_string += "Значения: "  # Значения:
    for _ in mean:
        main_string = main_string + _["text"] + " <i>("  # Значения: word (
        try:
            main_string += (_["pos"] + ";")  # Значения: word (часть_речи;
        except:
            pass
        try:
            main_string += (_["gen"] + ";")  # Значения: word (часть_речи;род;
        except:
            pass
        try:
            main_string += (_["num"] + ";")  # Значения: word (часть_речи;род;число;
        except:
            pass
        main_string += ")</i>; "  # Значения: word (часть_речи;род;число;);
        if "tr" in _:  # Если есть раздел "Перевод", то добавить его
            main_string += "\n"
            main_string += tr_def(_["tr"])
    main_string += "\n"  # + переход на новую строку
    return main_string


def ex_def(ex: list):
    ''' Используется для пункта "Примеры" '''
    main_string = ""
    main_string += "Примеры: "
    for _ in ex:
        main_string = main_string + _["text"] + " <i>("  # Примеры: word (
        try:
            main_string += (_["pos"] + ";")  # Примеры: word (часть_речи;
        except:
            pass
        try:
            main_string += (_["gen"] + ";")  # Примеры: word (часть_речи;род;
        except:
            pass
        try:
            main_string += (_["num"] + ";")  # Примеры: word (часть_речи;род;число;
        except:
            pass
        main_string += ")</i>; "  # Примеры: word (часть_речи;род;число;);
        if "tr" in _:
            main_string += "\n"
            main_string += tr_def(_["tr"])
    main_string += "\n"  # + переход на новую строку
    return main_string


def main_function(translations):
    '''Главная функция, отвечающая за формативание всего списка с информацией о переводе.'''
    main_str = ""
    if str(type(translations)) == "<class 'list'>":
        for _ in translations:
            # Форматирование раздела "Переводе"
            main_str += ("Перевод: " + "<b>" + _["text"] + "</b>" + " <i>(")
            try:
                main_str += (_["pos"] + ";")
            except:
                pass
            try:
                main_str += (_["gen"] + ";")
            except:
                pass
            try:
                main_str += (_["num"] + ";")  # Перевод: привет( существительное м ):
            except:
                pass
            main_str += ")</i>:\n"

            # Добавление (при наличии) пунктов: синонимы, значения, примеры
            try:
                main_str += syn_def(_["syn"])
            except:
                pass
            try:
                main_str += mean_def(_["mean"])
            except:
                pass
            try:
                main_str += ex_def(_["ex"])
            except:
                pass
        return main_str
    else:
        return ""


exem = [{'text': 'что', 'pos': 'местоимение', 'syn': [{'text': 'какой', 'pos': 'местоимение'}],
     'mean': [{'text': 'which'}]}, {'text': 'каков', 'pos': 'местоимение', 'mean': [{'text': 'what kind'}]},
    {'text': 'кто', 'pos': 'местоимение'}]
# print(main_function(exem))
