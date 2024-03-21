# region Task 1
'''def get_errors(*arguments):
    result_ = []
    array_arguments = arguments
    errors = {"out": "Вы вышли из системы",
              "noaccess": "У вас нет доступа к этому разделу",
              "unknown": "Неизвестная ошибка",
              "timeout": "Система долго не отвечает",
              "robot": "Ваши действия похожи на робота"}

    for key, value in errors.items():
        for elements_array in array_arguments:
            if key == elements_array:
                result_.append(value)

    return result_


result = get_errors("out", "robot", "unknown")
print(result)'''

# endregion
# region Task 2
"""def draw_carpet(w, h):
    if h <= 5:
        for i in range(h):
            print("*" * 5 + " - " * 2 + " - " * w + " - " * 2 + "*" * 5)
        for i in range(h):
            print("*" * 5 + " - " * 2 + " - " * w + " - " * 2 + "*" * 5)
    else:
        for i in range(h):
            print("*" * 5 + " - " * 2 + " - " * w + " - " * 2 + "*" * 5)
        for i in range(h):
            print("*" * 5 + " - " * 2 + " + " * w + " - " * 2 + "*" * 5)
        for i in range(h):
            print("*" * 5 + " - " * 2 + " - " * w + " - " * 2 + "*" * 5)


draw_carpet(6, 6)"""


# endregion
# region Task 3
def shift_encoding(string):
    dictionary_encoding = {"a":"b", "b":"c", "c":"d", "d":"e", "e":"f", "f":"g",
                           "g":"h", "h":"i", "i":"j", "j":"k", "k":"l", "l":"m",
                           "m":"n", "n":"o", "o":"p", "p":"q", "q":"r", "r":"s",
                           "s":"t", "t":"u", "u":"v", "v":"w", "w":"x", "x":"y",
                           "y":"z", "z":"0"}

    result_text = ""
    # TODO Decompositions text line on words
    for k, v in dictionary_encoding.items():
        for decompositions in string.split(" "):
            for e in decompositions:
                if e == k:
                    e = v
                    result_text += e

    print(result_text)


shift_encoding("hello world")
# endregion
