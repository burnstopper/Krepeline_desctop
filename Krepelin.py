import json
import time
import random
import datetime

answers = []
correct_answers = []
questions = []
time_of_given_question = []

class Answers:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def game_with_sum():
    start_time = time.perf_counter()
    first_digit = random.randint(1, 9)
    second_digit = random.randint(1, 9)
    while(time.perf_counter() - start_time < 600):
        time_of_given_question.append(datetime.datetime.now().isoformat())
        print(str(first_digit) + ' + ' + str(second_digit) + f' осталось веремени {round(600 - time.perf_counter() + start_time)} секунд. Для выхода из игры нажмите q')
        result = input()
        if(result == 'q'):
            return

        answers.append(result)
        correct_answers.append((first_digit + second_digit) % 10)
        questions.append((first_digit, second_digit))
        first_digit = random.randint(1, 9)
        second_digit = random.randint(1, 9)

def game_with_multiply():
    start_time = time.perf_counter()
    first_digit = random.randint(1, 9)
    second_digit = random.randint(1, 9)
    while (time.perf_counter() - start_time < 600):
        time_of_given_question.append(datetime.datetime.now().isoformat())
        print(str(first_digit) + ' * ' + str(
            second_digit) + f' осталось веремени {round(600 - time.perf_counter() + start_time)} секунд. Для выхода из игры нажмите q')
        result = input()
        if (result == 'q'):
            return

        answers.append(result)
        correct_answers.append((first_digit * second_digit) % 10)
        questions.append((first_digit, second_digit))
        first_digit = random.randint(1, 9)
        second_digit = random.randint(1, 9)


print(
    "Необходимо складывать или умножать числа.\n" +
    "Если результат состоит из двух цифр, то вводим только последнюю.\n" +
    "Пример:\n"
    "2+2=4\n"
    "3*3=9\n"
    "4*5=0\n"
    "7*8=6\n"
    "3+9=2\n" +
    "На весь тест дается 10 минут.  Если вы хотите закончить раньше в ответе на вопрос нажмите q. Спасибо за участие!\n" +
    "P.S. Не пытайтесь сломать программу, пожалуйста, это демоверсия для сбора данных!")
answer = Answers()
game_type = input("Выберите тип игры сложение или умножение. 1 - для умножения, 2 - для сложения \n")
answer.game_type = int(game_type) - 1
if (game_type == '2'):
    print("Выбрано сложение")
    game_with_sum()
elif (game_type == '1'):
    print("Выбрано умножение")
    game_with_multiply()
answer.time_of_given_question = time_of_given_question
answer.question_digits = questions
answer.user_answer = answers
answer. correct_number = correct_answers
datetime_to_write = datetime.datetime.now().time().strftime("%H_%M_%S")
with open(f"./Game_results_{datetime_to_write}.json", "w") as text_file:
    text_file.write(answer.toJSON())
