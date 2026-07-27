import random

def game():
    number = random.randint(1, 100)
    def is_valid(num):
        if num.isdigit():
            num = int(num)
            return 1 <= num <= 100
        return False
    print("Угадайте число от 1 до 100")
    while True:
        question = input("Введите число от 1 до 100: ")
        if not is_valid(question):
            print("Введите именно число от 1 до 100")
            continue
        question = int(question)
        if question < number:
            print("Ваше число меньше загаданного")
        elif question > number:
            print("Ваше число больше загаданного")
        else:
            print("Вы угадали!")
            break
    print("Спасибо за игру...")

def game2():
    answers = ['Бесспорно', 'Мне кажется - да', 'Пока не ясно, попробуй снова', 'Даже не думай', 
    'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений', 
    'Хорошие перспективы', 'Лучше не рассказывать', 'По поим данным - нет', 'Определённо да', 
    'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 
    'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']
    print('Привет Мир, Я магический шар, и я знаю ответ на любой твой вопрос.')
    name = input('Как тебя зовут?')
    print('Привет,',  name)
    again = 'д'
    while again.lower() == 'д':
        question = input('Задай мне свой вопрос: ')
        print(random.choice(answers))
        again = input('Задать еще один вопрос? (д = да, н = нет): ')
        if not again.lower() == 'д':
            print('Возвращайся, если возникнут вопросы!')

def game3():
    lang = input("Выберите язык (а - англ.; р - русс.): ").lower()
    choose = input("Шифрование (ш) или дешифрование (д)? ").lower()
    k = int(input("Какой сдвиг? "))
    text = input("Введите текст: ")
    def process_shifra(n, lang, answer, phrase):
        if answer == 'д':
            n = -n
        result = ""
        for char in phrase:
            start = None
            alphabet_size = 26
            if lang == "а":
                if 'A' <= char <= 'Z':
                    start = ord('A')
                elif 'a' <= char <= 'z':
                    start = ord('a')
            elif lang == "р":
                alphabet_size = 32
                if 'А' <= char <= 'Я':
                    start = ord('А')
                elif 'а' <= char <= 'я':
                    start = ord('а')
            if start is not None:
                result += chr((ord(char) - start + n) % alphabet_size + start)
            else:
                result += char
        return result
    final_text = process_shifra(k, lang, choose, text)
    print("Результат:", final_text)

def game4():
    import random

    word_list = ['математика', 'геометрия', 'информатика', 'программирование', 'питон', 'образование', 'телефон', 'компьютер', 'алгоритм', 'функция', 'переменная', 'разработка', 'интернет', 'кибернетика', 'автоматизация', 'моделирование', 'симуляция', 'инженерия', 'архитектура', 'технология']
    def get_word():
        word = random.choice(word_list)
        return word.upper()
    def display_hangman(tries):
        stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                    ''',
                    # голова, торс, обе руки, одна нога
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / 
                       -
                    ''',
                    # голова, торс, обе руки
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |      
                       -
                    ''',
                    # голова, торс и одна рука
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|
                       |      |
                       |     
                       -
                    ''',
                    # голова и торс
                    '''
                       --------
                       |      |
                       |      O
                       |      |
                       |      |
                       |     
                       -
                    ''',
                    # голова
                    '''
                       --------
                       |      |
                       |      O
                       |    
                       |      
                       |     
                       -
                    ''',
                    # начальное состояние
                    '''
                       --------
                       |      |
                       |      
                       |    
                       |      
                       |     
                       -
                    '''
        ]
        return stages[tries]
    def play(word):
        word_completion = "_" * len(word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6

        print('Давайте играть в угадайку слов!')
        print(display_hangman(tries))
        print(word_completion)
        print()

        while not guessed and tries > 0:
            guess = input('Введите букву или слово целиком: ').upper()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print('Вы уже называли букву', guess)
                elif guess not in word:
                    print('Буквы', guess, 'нет в слове.')
                    tries -= 1
                    guessed_letters.append(guess)
                else:
                    print('Отличная работа, буква', guess, 'присутствует в слове!')
                    guessed_letters.append(guess)
                    word_as_list = list(word_completion)
                    indices = [i for i in range(len(word)) if word[i] == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = ''.join(word_as_list)
                    if '_' not in word_completion:
                        guessed = True
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print('Вы уже называли слово', guess)
                elif guess != word:
                    print('Слово', guess, 'не является верным.')
                    tries -= 1
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = word
            else:
                print('Введите букву или слово.')
            print(display_hangman(tries))
            print(word_completion)
            print()
        if guessed:
            print('Поздравляем, вы угадали слово! Вы победили!')
        else:
            print('Вы не угадали слово. Загаданным словом было ' + word + '. Может быть в следующий раз!')
            again = 'д'

    again = 'д'
    while again.lower() == 'д':
        word = get_word()
        play(word)
        again = input('Играем еще раз? (д = да, н = нет):')

def game5():
    import random

    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'

    chars = ''
    n = int(input('Введите количество паролей для генерации: '))
    length = int(input('Введите длину пароля: '))
    add_digit = input('Включить цифры? (д = да, н = нет) ').strip()
    add_lowercase = input('Включить прописные буквы? (д = да, н = нет) ').strip()
    add_uppercase = input('Включить строчные буквы? (д = да, н = нет) ').strip()
    add_punctuation = input('Включить символы, такие как !#$%&*+-=?@^_? (д = да, н = нет) ').strip()
    remove_badsymbols = input('Исключить символы il1Lo0O? (д = да, н = нет)').strip()
    if add_digit.lower() == 'д':
        chars += digits
    if add_lowercase.lower() == 'д':
        chars += lowercase_letters
    if add_uppercase.lower() == 'д':
        chars += uppercase_letters
    if add_punctuation.lower() == 'д':
        chars += punctuation
    if remove_badsymbols.lower() == 'д':
        for c in 'il1Lo0O':
            chars = chars.replace(c, '')
            
    def generate_password(length, chars):
        password = ''
        for j in range(length):
            password += random.choice(chars)
        return password
        
    for _ in range(n):
        print(generate_password(length, chars))

# Главное меню выбора игр
while True:
    print("Выберите игру:")
    print("1 - Угадайка чисел")
    print("2 - Магический шар")
    print("3 - Шифр Цезаря")
    print("4 - Угадайка слов (Виселица)")
    print("5 - Генератор паролей")
    print("0 - Выход")
    
    choice = input("Введите номер игры: ").strip()
    
    if choice == '1':
        while True:
            game()
            answer = input("Сыграем ещё раз? (да/нет): ")
            if answer.lower() not in ['да', 'lf', 'yes', 'y', 'д']:
                print("До свидания!")
                break
            print("\n" + "="*40 + "\n")
    elif choice == '2':
        game2()
    elif choice == '3':
        game3()
    elif choice == '4':
        game4()
    elif choice == '5':
        game5()
    elif choice == '0':
        print("До свидания!")
        break
    else:
        print("Неверный ввод, попробуйте еще раз.\n")