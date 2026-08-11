
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Python Hangman game that uses string manipulation, loops, conditionals, and user input to let the player guess a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Word Selection and Setup

#### Description
Create the initial game setup by selecting a random target word from a predefined list and preparing the display for hidden letters.

#### Requirements
Completed program should:

- Define a list of possible words inside the program.
- Select a random word from the list using the `random` module.
- Create a hidden representation of the word using underscores for each letter.
- Display the initial game state to the player.

### 🛠️ Guess Handling and Progress Display

#### Description
Build the main game loop that accepts letter guesses, updates the hidden word display, and tracks letters already guessed.

#### Requirements
Completed program should:

- Prompt the player to guess a single letter each turn.
- Reveal letters in the hidden word display when the guess is correct.
- Track incorrect guesses and show the current progress in `_ _ _` format.
- Prevent repeated guesses from counting against remaining attempts.

### 🛠️ Win/Lose Conditions

#### Description
Implement the game end conditions so the player wins when the word is fully guessed and loses when attempts run out.

#### Requirements
Completed program should:

- End the game when the player guesses all letters correctly.
- End the game when the player uses up the allowed number of incorrect guesses.
- Display a clear win message or lose message with the correct word.
- Show the number of remaining attempts after each guess.
