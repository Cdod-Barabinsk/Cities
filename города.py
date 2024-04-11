import random

# Чтение городов из файла
with open('cities.txt', 'r', encoding='utf-8') as f:
    cities_list = [line.strip() for line in f]

cities_list_answer = []


# Первый ход бота
bot_answer = random.choice(cities_list)
cities_list_answer.append(bot_answer)
print(bot_answer)
print()

game_over = False
count = 0

while not game_over:
    if bot_answer[-1].lower() in ["ё", "ь", "ъ", "ы"]:
        arg_letters = bot_answer[0].lower()
    else:
        arg_letters = bot_answer[-1].lower()

    player_answer = input(f"Введите город на букву '{arg_letters}':\n")

    if player_answer[0].lower() != arg_letters:
        count += 1
        print(f"Неверно. Город должен начинаться на букву '{arg_letters}', попробуйте еще раз.")
    elif player_answer.lower() in [city.lower() for city in cities_list_answer]:
        print("Такой город уже был назван, попробуйте еще раз.")
        count += 1
    elif player_answer.lower() not in [city.lower() for city in cities_list]:
        print("Возможно, такого города не существует, попробуйте еще раз.")
        count += 1
    else:
        cities_list_answer.append(player_answer)

        # Поиск возможных городов для бота
        if player_answer[-1].lower() in ["ё", "ь", "ъ", "ы"]:
            possible_cities = [city for city in cities_list if city[0].lower() == player_answer[0].lower() and city.lower() not in [ans.lower() for ans in cities_list_answer]]
        else:
            possible_cities = [city for city in cities_list if city[0].lower() == player_answer[-1].lower() and city.lower() not in [ans.lower() for ans in cities_list_answer]]

        if not possible_cities:
            print("Компьютер не смог найти подходящий город. Вы победили!")
            break

        bot_answer = random.choice(possible_cities)
        cities_list_answer.append(bot_answer)
        print(bot_answer)

    if count == 5:
        game_over = True
        print("Количество попыток закончилось, Вы проиграли!")

while True:
    answer = input(" ответ (или 'exit' для завершения): ")
    if answer.lower() == 'exit':
        break
    cities_list_answer.append(answer)

with open('answers.txt', 'w' , encoding='utf-8') as file:
    for answer in cities_list_answer:
        file.write(answer + '\n')

print("Ответы успешно сохранены в файле 'answers.txt'.")