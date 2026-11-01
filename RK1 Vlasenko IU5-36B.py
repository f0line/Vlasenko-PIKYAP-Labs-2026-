from operator import itemgetter


class Language:
    """Язык программирования (Класс 1)"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Tool:
    """Средство разработки (Класс 2, сторона 'много')"""

    def __init__(self, id, name, price, lang_id):
        self.id = id
        self.name = name
        self.price = price  # количественный признак (цена лицензии)
        self.lang_id = lang_id  # для связи один-ко-многим


class LangTool:
    """Связь многие-ко-многим (Язык - Средство разработки)"""

    def __init__(self, lang_id, tool_id):
        self.lang_id = lang_id
        self.tool_id = tool_id


# --- Тестовые данные ---

# Языки программирования
languages = [
    Language(1, 'Python'),
    Language(2, 'Java'),
    Language(3, 'Ассемблер'),  # Начинается на 'А'
    Language(4, 'Ада'),  # Начинается на 'А'
    Language(5, 'C++'),
]

# Средства разработки
tools = [
    Tool(1, 'PyCharm', 10000, 1),
    Tool(2, 'IntelliJ IDEA', 15000, 2),
    Tool(3, 'Visual Studio', 20000, 5),
    Tool(4, 'Android Studio', 0, 2),  # Оканчивается на Studio
    Tool(5, 'Eclipse', 0, 2),
    Tool(6, 'Code::Blocks', 0, 5),
    Tool(7, 'GNAT Studio', 0, 4),  # Оканчивается на Studio
]

# Связь многие-ко-многим
lang_tools = [
    LangTool(1, 1),  # Python — PyCharm
    LangTool(1, 2),  # Python — IntelliJ IDEA
    LangTool(2, 2),  # Java — IntelliJ IDEA
    LangTool(2, 3),  # Java — Visual Studio
    LangTool(2, 4),  # Java — Android Studio
    LangTool(2, 5),  # Java — Eclipse
    LangTool(3, 6),  # Ассемблер — Code::Blocks
    LangTool(4, 7),  # Ада — GNAT Studio
    LangTool(4, 3),  # Ада — Visual Studio
    LangTool(5, 3),  # C++ — Visual Studio
    LangTool(5, 6),  # C++ — Code::Blocks
]


def main():
    # Соединение данных один-ко-многим
    # Получаем кортежи: (название средства, цена, название языка)
    one_to_many = [(t.name, t.price, l.name)
                   for l in languages
                   for t in tools
                   if t.lang_id == l.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(l.name, lt.lang_id, lt.tool_id)
                         for l in languages
                         for lt in lang_tools
                         if l.id == lt.lang_id]

    many_to_many = [(lang_name, t.name)
                    for lang_name, lang_id, tool_id in many_to_many_temp
                    for t in tools if t.id == tool_id]

    # ---------- Задание Д1 ----------
    print('Задание Д1')
    # Средства разработки на "Studio" и их языки (связь 1:M)
    res_1 = [(tool_name, lang_name)
             for tool_name, _, lang_name in one_to_many
             if tool_name.endswith('Studio')]
    print(res_1)

    # ---------- Задание Д2 ----------
    print('\nЗадание Д2')
    res_2_unsorted = []
    for l in languages:
        # Цены средств разработки для текущего языка
        prices = [price for _, price, lang_name in one_to_many if lang_name == l.name]
        if len(prices) > 0:
            avg_price = round(sum(prices) / len(prices), 2)
            res_2_unsorted.append((l.name, avg_price))

    # Сортировка по средней цене (по убыванию, как в примере)
    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    print(res_2)

    # ---------- Задание Д3 ----------
    print('\nЗадание Д3')
    res_3 = {}
    for l in languages:
        # Языки на букву "А"
        if l.name.startswith('А'):
            # Список средств разработки для этого языка (связь M:M)
            tool_names = [tool for lang_name, tool in many_to_many if lang_name == l.name]
            res_3[l.name] = tool_names
    print(res_3)


if __name__ == '__main__':
    main()
