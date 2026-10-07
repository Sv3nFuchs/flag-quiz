import random
#Dictionary of countries and emojis (max five for every letter, based on the influence and population).
countries = {"Afghanistan":"🇦🇫", "Algeriet":"🇩🇿", "Angola":"🇦🇴", "Argentina":"🇦🇷", "Australien":"🇦🇺",
             "Bangladesh":"🇧🇩", "Belgien":"🇧🇪", "Bolivia":"🇧🇴", "Brasilien":"🇧🇷", "Bulgarien":"🇧🇬",
             "Chile":"🇨🇱", "Colombia":"🇨🇴", "Costa Rica":"🇨🇷", "Cypern":"🇨🇾",
             "Danmark":"🇩🇰", "Djibouti":"🇩🇯", "Dominica":"🇩🇲", "Dominikanska republiken":"🇩🇴",
             "Ecuador":"🇪🇨", "Egypten":"🇪🇬", "El Salvador":"🇸🇻", "Estland":"🇪🇪", "Etiopien":"🇪🇹",
             "Filippinerna":"🇵🇭", "Finland":"🇫🇮", "Frankrike":"🇫🇷", "Förenade Arabemiraten":"🇦🇪", "Förenta staterna":"🇺🇸",
             "Georgien":"🇬🇪", "Ghana":"🇬🇭", "Grekland":"🇬🇷", "Guatemala":"🇬🇹", "Guinea":"🇬🇳",
             "Haiti":"🇭🇹", "Honduras":"🇭🇳",
             "Indien":"🇮🇳", "Indonesien":"🇮🇩", "Irak":"🇮🇶", "Iran":"🇮🇷", "Italien":"🇮🇹",
             "Jamaica":"🇯🇲", "Japan":"🇯🇵", "Jemen":"🇾🇪", "Jordanien":"🇯🇴",
             "Kanada":"🇨🇦", "Kazakstan":"🇰🇿", "Kenya":"🇰🇪", "Kina":"🇨🇳", "Kongo":"🇨🇩",
             "Lettland":"🇱🇻", "Libanon":"🇱🇧", "Libyen":"🇱🇾", "Litauen":"🇱🇹", "Luxemburg":"🇱🇺",
             "Malaysia":"🇲🇾", "Marocko":"🇲🇦", "Mexiko":"🇲🇽", "Moçambique":"🇲🇿", "Myanmar":"🇲🇲",
             "Nederländerna":"🇳🇱", "Nepal":"🇳🇵", "Nigeria":"🇳🇬", "Norge":"🇳🇴", "Nya Zeeland":"🇳🇿",
             "Oman":"🇴🇲",
             "Pakistan":"🇵🇰", "Palestina":"🇵🇸", "Peru":"🇵🇪", "Polen":"🇵🇱", "Portugal":"🇵🇹",
             "Qatar":"🇶🇦",
             "Saudiarabien":"🇸🇦", "Spanien":"🇪🇸", "Storbritannien":"🇬🇧", "Sverige":"🇸🇪", "Sydkorea":"🇰🇷",
             "Taiwan":"🇹🇼", "Thailand":"🇹🇭", "Tjeckien":"🇨🇿", "Turkiet":"🇹🇷", "Tyskland":"🇩🇪",
             "Uganda":"🇺🇬", "Ukraina":"🇺🇦", "Ungern":"🇭🇺", "Uruguay":"🇺🇾", "Uzbekistan":"🇺🇿",
             "Venezuela":"🇻🇪", "Vietnam":"🇻🇳", "Vitryssland":"🇧🇾",
             "Zambia":"🇿🇲", "Zimbabwe":"🇿🇼",
             "Österrike":"🇦🇹", "Östtimor":"🇹🇱"
}

def flag_quiz():
    #Keep score.
    user_score = 0
    #How many answered.
    questions_answered = 0
    print("Varmt välkommen till denna frågesport om världens flaggor!\n")
    #Asks the user how many questions they want to answer (and checks if valid).
    while True:
        try:
            how_many = int(input("Hur många frågor vill du besvara? "))
            break
        except ValueError:
            print("Ej giltig! Försök igen.\n")
    for i in range(how_many):
        #Randomly select a coutry and emoji from dictionary.
        country, emoji = random.choice(list(countries.items()))
        #Ask the user for the country that a given emoji/flag represents.
        user_question = input("Vilket land är representerad med denna flagga: " + emoji + "  ").capitalize()
        #Remove the instance of that country so that it doesn't repeat during the quiz.
        countries.pop(country)
        #Checks if the user's answer is right. If so, their score increases by one. Either way, their current score is printed.
        if user_question == country:
            user_score += 1
            questions_answered += 1
            print(f"Det svaret var rätt! Hittills har du fått {user_score} av {questions_answered} rätt.\n")
        elif user_question != country:
            questions_answered += 1
            print(f"Tyvärr var det svaret fel. Hittills har du fått {user_score} av {questions_answered} rätt.")
            print(f"Det rätta svaret var: {country}\n")
    #The user's final percentage is calculated, which is printed at the end of the quiz.
    percentage = round(((user_score/questions_answered) * 100), 2)
    print(f"Grattis till att du klarade denna frågesporten! Du fick {user_score} av {questions_answered} rätt.")
    print(f"Detta motsvarar ett betyg av {percentage}%. Tack för att du spelade!\n")
    return percentage