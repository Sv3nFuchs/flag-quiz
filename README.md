# Flag Quiz:

Console flag quiz in Python with Swedish output. Features score-tracking across multiple rounds (up to user discretion). Based on a random flag emoji shown, the user answers with the corresponding country.

## How it works:

- `final_score.py`: When the program begins, the user is asked how many rounds they would like to play.
- `flagga_quiz.py`: This file contains the quiz itself. For each round, the user chooses how many questions to answer and is then shown a random flag emoji for each one.
- Each flag emoji is paired with its country name in a dictionary of 90+ countries.
- After each answer, the user is shown whether they were correct, along with their current score.
- At the end of each round, the user is given their percentage score. Through `final_score.py`, the user is then asked if they would like to see their percentages from all previous rounds.

## Concepts used:

- Dictionaries.
- Functions.
- Modules and imports.
- Loops.
- Input validation with try/except (numeric input).
- String methods (`.capitalize()`).
- F-strings.

## Running it:

```
python final_score.py
```

Requires Python 3. The quiz is run in Swedish.

## Possible improvements:

- Multiplayer mode, allowing users to play against another.
- English version of the program.
- Varying difficulty levels.
- Saving scores to a file so results last between sessions.
