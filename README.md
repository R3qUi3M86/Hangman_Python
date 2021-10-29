# Hangman

## Story

Let's hang somebody! Implement the popular [Hangman](<https://en.wikipedia.org/wiki/Hangman_(game)>)
game. Add a full fledged game flow with a main menu and optionally some cool graphics
in the console! Some online examples:

- https://www.gamestolearnenglish.com/hangman/
- https://www.coolmathgames.com/0-hangman

## What are you going to learn?

- Use lists and strings.
- Handle files.
- Use and validate user input.
- Handle normal and edge cases.
- Create ASCII art.

## Tasks

1. Implement the `play(word, lives)` function as a basic hangman game.
    - The function uses the `word` parameter as the word to guess and the `lives` parameter as the number of available mistakes.
    - The initial game state is displayed as `_ _ _ _ _ _ _ _` (one underscore for each letter in `word`).
    - The game state is displayed as `_ o d _ _ o o _` if letters 'd' and 'o' are revealed.
    - It is possible to make guesses, and letters that occur in the word are revealed.
    - When a guessed letter does not occur in `word`, the player loses one life.
    - When a guess is repeated (regardless of its occurrences), the player is notified, and nothing happens.
    - When a guess is wrong (either a new or a repeated letter), the previous wrong letters are shown to the user.
    - The player wins when all letters in `word` are revealed.
    - The player loses when the number of wrong guesses is higher than the value of `lives` (not counting repeated guesses).
    - When the player types `'quit'` as input, the program says good-bye and terminates.

2. The gameplay is case insensitive, the word display is case sensitive.
    - Both uppercase and lowercase letters are considered valid input.
    - Uppercase and lowercase letter guesses reveal the same letters (e.g. both `c` and `C` guesses reveal all the `c`s in the word, regardless of their case).
    - Letters of different cases behave as if they were the same when checking repetitions (e.g. entering `c` after a `C` would count as a repetition).
    - On the displaying side, however, letters are revealed as they originally appear in `word` (e.g. successfully guessing `c` shows `C _ _ _ c _ _ _` for `Codecool`).

3. Add ASCII art to visualize lives left.
    - The game state display is accompanied by an ASCII art depending on the number of lives left.
    - The art sequence is adapted to the starting value of the `lives` parameter (at least between 3 and 7) – this means that the game over art is always the same.

4. The game uses a random word from a pre-defined word collection.
    - The game randomly picks a word at each run.
    - The game randomly picks a country from `countries-and-capitals.txt`.

5. The program allows the user to play on different levels.
    - The game starts with a menu for picking a difficulty level. The `play()` function is not changed.
    - The word-pool and the number of lives depend on the chosen level.

## General requirements

None

## Hints

- Store the state of the game (such as the revealed and missed letters) with the help
  of mutable structures (such as lists or sets).
- Use a `set` data structure when you have a collection that cannot have duplicate elements.
- Try to create a few (3-6) functions for features that are somewhat separated from the
  main process (such as dealing with the inputs, parts of the display, or the menu).
  Think of the input requirements and the results of these units! Add the necessary
  inputs as parameters, and return the results that is needed by the caller side!
- Ideal team size is 2. Maximum team size is 3.

## Background materials

- <i class="far fa-exclamation"></i> [Strings](project/curriculum/materials/competencies/python-basics/python-strings.md.html)
- <i class="far fa-exclamation"></i> [User input](project/curriculum/materials/competencies/python-basics/python-io.md.html)
- <i class="far fa-exclamation"></i> [File handling](project/curriculum/materials/competencies/python-basics/python-file-handling.md.html)
- <i class="far fa-book-open"></i> [Sets](project/curriculum/materials/competencies/python-data-structures/python-sets.md.html)

