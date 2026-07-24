lang = input("Выберите язык (а - англ.; р - русс.): ").lower()
choose = input("Шифрование (ш) или дешифрование (д)? ").lower()
k = int(input("Какой сдвиг? "))
text = input("Введите текст: ")
def process_shifra(n, lang, answer, phrase):
    if answer == 'д':
        n = -n
    result = ""
    for char in phrase:
        if lang == "а":
            if 'A' <= char <= 'Z':
                start = ord('A')
                result += chr((ord(char) - start + n) % 26 + start)
            elif 'a' <= char <= 'z':
                start = ord('a')
                result += chr((ord(char) - start + n) % 26 + start)
            else:
                result += char
        elif lang == "р":
            if 'А' <= char <= 'Я':
                start = ord('А')
                result += chr((ord(char) - start + n) % 32 + start)
            elif 'а' <= char <= 'я':
                start = ord('а')
                result += chr((ord(char) - start + n) % 32 + start)
            else:
                result += char
        else:
            result += char 
    return result
final_text = process_shifra(k, lang, choose, text)
print("Результат:", final_text)
