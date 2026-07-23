eng = "abcdefghijklmnopqrstuvwxyz"
rus = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
symbols = [" ", ",", ".", "!", "?"]
lang = input("Выберите язык (а - англ.; р - русс.) ")
chs = input("Шифрование (ш) или дешифрование (д)? ")
k = int(input("Какой сдвиг? "))
text = input("Введите текст: ")
def process_shifra(n, langg, shifr, phrase):
    phrase = phrase.lower()
    if langg == "р":
        alphabet = rus
        mochnost = 32
    else:
        alphabet = eng
        mochnost = 26
    if shifr == 'д':
        n = -n
    result = ""
    for char in phrase:
        if char in alphabet:
            x = alphabet.index(char)
            y = (x + n) % mochnost
            result += alphabet[y]
        else:
            result += char
    return result
final_text = process_shifra(k, lang, chs, text)
print("Результат:", final_text)
