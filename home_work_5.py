import random

print("Сегодня мы потренируемся расшифровывать морзянку.\n"
      "Нажмите Enter и начнем.")
input()
words = ['ada', 'umbrella', 'jill', 'virus', 'gun']
answers = []


def print_statistics(answers_):
    answers_true = 0
    answers_false = 0
    print(f"Всего задачек: {len(answers_)}")
    for element in answers_:
        if element:
            answers_true += 1
        elif not element:
            answers_false += 1
    print(f'Отвечено верно: {answers_true}')
    print(f'Отвечено неверно: {answers_false}')


def morse_encoding(words_):
    """Перевод слов в азбуку морзе"""
    result_morse_encoding_ = ''
    morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
             'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
             'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
             'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
             'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
             'z': '--..'}

    for element_text in words_:
        for key, value in morse.items():
            if element_text == key:
                element_text = value
                result_morse_encoding_ += element_text

    return result_morse_encoding_


def get_word(words_):
    """Выбор случайного значения в массиве данных"""
    random_word_ = random.sample(words_, 1)

    return random_word_


count = 0
while count < len(words):
    random_word = get_word(words)
    result_morse_encoding = morse_encoding(str(random_word))  # Нехватало приведение типа
    print(result_morse_encoding)
    enter_answer = input("Введите ответ: ")
    if enter_answer == random_word:
        answers.append(True)
    else:
        answers.append(False)
    count += 1

print_statistics(answers)
