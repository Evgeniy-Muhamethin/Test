print(f"Привет! Предлагаю проверить свои знания английского!")
print(f"Расскажи, как тебя зовут!")

name = str(input("Введите имя: "))

questions = ["My name __ Vova", "I __ a doctor", "I live __ Moscow"]
answers = ["is", "am", "in"]

print(f"Привет! {name}. Предлагаю проверить свои знания английского!")

enter_text = str(input("Наберите 'ready', чтобы начать: "))

if enter_text == "ready":

    count_failing = 3
    count = 0
    true_cuestion = 0
    false_question = 0

    print(f"Первый вопрос: {questions[0]}'")

    while count_failing > 0:
        first_question = str(input("Ответ: "))
        if first_question == answers[0]:
            print("Ответ верный")
            true_cuestion += 1
            if count_failing == 3:
                count += 3
            elif count_failing == 2:
                count += 2
            else:
                count += 1
            break
        elif first_question != answers[0] and count_failing != 0:
            count_failing -= 1
            if count_failing > 0:
                print(f"Осталось попыток: {count_failing}, попробуйте еще раз!")
            else:
                print(f"Увы но нет. Верный ответ {answers[0]}")

    print(f"Второй вопрос: {questions[1]}")

    if count_failing < 3:
        count_failing = 3
    while count_failing > 0:
        second_question = str(input("Ответ: "))

        if second_question == answers[1]:
            print("Ответ верный")
            true_cuestion += 1
            if count_failing == 3:
                count += 3
            elif count_failing == 2:
                count += 2
            else:
                count += 1
            break
        elif second_question != answers[1] and count_failing != 0:
            count_failing -= 1
            if count_failing > 0:
                print(f"Осталось попыток: {count_failing}, попробуйте еще раз!")
            else:
                print(f"Увы но нет. Верный ответ {answers[1]}")

    print(f"Третий вопрос: {questions[2]}")

    if count_failing < 3:
        count_failing = 3
    while count_failing > 0:
        last_question = str(input("Ответ: "))
        if last_question == answers[2]:
            print("Ответ верный")
            true_cuestion += 1
            if count_failing == 3:
                count += 3
            elif count_failing == 2:
                count += 2
            else:
                count += 1
            break
        elif last_question != answers[2] and count_failing != 0:
            count_failing -= 1
            if count_failing > 0:
                print(f"Осталось попыток: {count_failing}, попробуйте еще раз!")
            else:
                print(f"Увы но нет. Верный ответ {answers[2]}")

    print(f"Вот и все, {name}!")
    print(f"Вы ответили {true_cuestion} вопросов из {len(questions)} верно.")
    print(f"Вы заработали {count} баллов")
    print(f"Это {(true_cuestion / 3) * 100} процентов")
else:
    print(f"Кажется, вы не хотите играть. Очень жаль")