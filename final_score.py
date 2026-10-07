from flagga_quiz import flag_quiz

def final_scores():
    #Previous scores as a list.
    scores_list = []
    #Asks the user how many times they want to play (and checks if valid).
    while True:
        try:
            times_play = int(input("Hur många gånger vill du spela? "))
            break
        except ValueError:
            print("Ej giltig! Försök igen.\n")
    #Based on the user's input, runs the game a certain number of times. Their final percentage is added to the list.
    for i in range(times_play):
        percentage = flag_quiz()
        scores_list.append(percentage)
    #Asks the user if they would like to view their previous scores.
    user_input = (input("Vill du se dina tidigare resultat? "))
    if user_input.capitalize() == "Ja":
        print(f"Här finns dina tidigare resultat: {scores_list}")
    elif user_input.capitalize() == "Nej":
        print("Programmet slut.")
    else:
        print("Ej giltig!")
final_scores()