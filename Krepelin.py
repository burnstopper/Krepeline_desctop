import json
import time
import random

answers = []
answers_user = []
questions = []
intervals_between_answers = []

class Answers:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def game_with_sum():
    start_time = time.perf_counter()
    game_timestamp = start_time
    first_digit = random.randint(1, 9)
    second_digit = random.randint(1, 9)
    questions.append(first_digit)
    while(time.perf_counter() - start_time < 600):
        print(str(first_digit) + ' + ' + str(second_digit) + f' осталось веремени {round(600 - time.perf_counter() + start_time)} секунд')
        questions.append(second_digit)
        result = input()
        answers_user.append(result)
        if(result == 'q'):
            return
        if(int(result) == (first_digit + second_digit) % 10):
            answers.append(1)
        else:
            answers.append(0)
        intervals_between_answers.append(time.perf_counter() - game_timestamp)
        game_timestamp = time.perf_counter()
        first_digit = second_digit
        second_digit = random.randint(1, 9)

def game_with_multiply():
    start_time = time.perf_counter()
    game_timestamp = start_time
    first_digit = random.randint(0, 9)
    second_digit = random.randint(0, 9)
    questions.append(first_digit)
    while(time.perf_counter() - start_time < 600):
        print(str(first_digit) + ' * ' + str(second_digit) + f' осталось веремени {round(600 - time.perf_counter() + start_time)} секунд')
        questions.append(second_digit)
        result = input()
        answers_user.append(result)
        if(result == 'q'):
            return
        if(int(result) == (first_digit * second_digit) % 10):
            answers.append(1)
        else:
            answers.append(0)
        intervals_between_answers.append(time.perf_counter() - game_timestamp)
        game_timestamp = time.perf_counter()
        first_digit = second_digit
        second_digit = random.randint(0, 9)


print(
    "Вам предлагается пройти тест Крепелина. Есть два типа теста: с умножением и сложением, ответом является остаток от деления результата опреации на 10.\n" +
    "На весь тест дается 10 минут.  Если вы хотите закончить раньше в ответе на вопрос нажмите q. Спасибо за участие!\n" +
    "P.S. Не пытайтесь сломать программу, пожалуйста, это демоверсия для сбора данных!")
answer = Answers()
game_type = input("Выберите тип игры сложение или умножение. 1 - для умножения, 2 - для сложения \n")
answer.game_type = game_type
answer.user_answer = answers_user
if (game_type == '2'):
    print("Выбрано сложение")
    game_with_sum()
elif (game_type == '1'):
    print("Выбрано умножение")
    game_with_multiply()
answer.question_numbers = questions
answer.answers = answers
answer.intervals = intervals_between_answers
with open("./Game_results.json", "w") as text_file:
    text_file.write(answer.toJSON())
