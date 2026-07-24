print("Результат:", final_text)
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
