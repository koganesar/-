def Words_Game(used_words):
    import random
 
    wordlist = ["яблоко", "груша", "мандарин", "конфеты", "город", "телефон", "ноутбук", "книту", "колонки", "общежитие"]
 
    rand_word = random.choice(wordlist)
 
    while rand_word in used_words:
        rand_word = random.choice(wordlist)
 
    mistakes = 5
 
    wrong_ans = 0
 
    used_letters = []
 
    words_len_secret = "_" * len(rand_word)
 
    while wrong_ans < mistakes and words_len_secret != rand_word:
        print("Использованные буквы: ", used_letters)
        print("Ваше слово: ", words_len_secret)
 
        player_letter = input()
 
        while player_letter in used_letters:
            print("Вы уже выбирали эту букву:", player_letter)
            player_letter = input()
 
        used_letters.append(player_letter)
 
        if player_letter in rand_word:
            print("Вы угадали букву!", player_letter)
            letters_in_word = ''
            for i in range(len(rand_word)):
                if player_letter == rand_word[i]:
                    letters_in_word += player_letter
                else:
                    letters_in_word += words_len_secret[i]
            words_len_secret = letters_in_word
        else:
            print("Такой буквы нет в слове", player_letter)
            wrong_ans += 1
 
    if wrong_ans == mistakes:
        print("Ты проиграл!")
    else:
        print("Ты угадал слово!")
 
    print("Тебе загадали слово: ", rand_word)
    return rand_word
 
used_words = []
 
used_words.append(Words_Game(used_words))
 
 
 
while True:
    if len(used_words) == 10:
        print("Слова закончились")
        break
    print("Повторить? +/-")
    x = input()
    if x == "+":
        used_words.append(Words_Game(used_words))
    else:
        break
