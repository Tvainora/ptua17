import random
import logging
import sqlite3
from typing import List, Optional


logging.basicConfig(filename='hangman.log', level=logging.INFO, format='%(asctime)s %(message)s')


DB_NAME = 'hanging_man.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            word TEXT,
            won INTEGER,
            guesses INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.id: Optional[int] = None

    def save(self):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)', 
                  (self.name, self.email))
        conn.commit()
        c.execute('SELECT id FROM users WHERE email=?', (self.email,))
        self.id = c.fetchone()[0]
        conn.close()
        logging.info(f"User registered: {self.name} ({self.email})")

class hanging:
    def __init__(self, user: User, word_list: List[str]):
        self.user = user
        self.word = random.choice(word_list).lower()
        self.guessed_letters: List[str] = []
        self.max_attempts = 10
        self.attempts_left = self.max_attempts
        self.guesses_made = 0
        self.won = False

    def display_word(self) -> str:
        return ' '.join([c if c in self.guessed_letters else '_' for c in self.word])

    def guess(self, guess: str) -> bool:
        guess = guess.lower()
        self.guesses_made += 1
        if len(guess) == 1:
            if guess in self.word and guess not in self.guessed_letters:
                self.guessed_letters.append(guess)
                logging.info(f"Letter guessed: {guess}")
                return True
            else:
                self.attempts_left -= 1
                logging.info(f"Incorrect letter: {guess}. Attempts left: {self.attempts_left}")
                return False
        elif len(guess) == len(self.word):
            if guess == self.word:
                self.guessed_letters = list(self.word)
                self.won = True
                logging.info(f"Word guessed: {guess}")
                return True
            else:
                self.attempts_left -= 1
                logging.info(f"Incorrect word: {guess}. Attempts left: {self.attempts_left}")
                return False
        else:
            self.attempts_left -= 1
            logging.info(f"Invalid guess: {guess}. Attempts left: {self.attempts_left}")
            return False

    def is_finished(self) -> bool:
        if set(self.word) <= set(self.guessed_letters):
            self.won = True
            return True
        if self.attempts_left <= 0:
            return True
        return False

    def save_game(self):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('INSERT INTO games (user_id, word, won, guesses) VALUES (?, ?, ?, ?)',
                  (self.user.id, self.word, int(self.won), self.guesses_made))
        conn.commit()
        conn.close()
        logging.info(f"Game saved for user {self.user.email}: word={self.word}, won={self.won}, guesses={self.guesses_made}")

def show_stats():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        SELECT u.name, u.email, COUNT(g.id) as games_played,
               SUM(g.won) as games_won, SUM(1-g.won) as games_lost, SUM(g.guesses) as guesses_made
        FROM users u
        LEFT JOIN games g ON u.id = g.user_id
        GROUP BY u.id
    ''')
    rows = c.fetchall()
    print("User Stats:")
    print("Name" \
    "\tEmail    " \
    "\tGames    " \
    "\tPlayed   " \
    "\tGames Won    " \
    "\tGames Lost   " \
    "\tGuesses Made  ")
    for row in rows:
        print('\t'.join(str(x) for x in row))
    conn.close()

def main():
    init_db()
    print("Welcome to Hangman game!\n")
    name = input("Enter your name or gamer tag: ")
    email = input("Enter your email: ")
    user = User(name,  email)
    user.save()
#spėjami žodžiau
    word_list = ['python', 
                 'apple', 
                 'cherry', 
                 'car', 
                 'tower', 
                 'doctor', 
                 'mouse']
    game = hanging(user, word_list)

    while not game.is_finished():
        print(f"\nWord: {game.display_word()}")
        print(f"Attempts left: {game.attempts_left}")
        guess = input("Guess a letter or the whole word: ")
        game.guess(guess)
        if set(game.word) <= set(game.guessed_letters):
            print(f"Congratulations! You guessed the word: {game.word}")
            break
        elif game.attempts_left == 0:
            print(f"Game over! The word was: {game.word}")
            break

    game.save_game()
    show_stats()

if __name__ == "__main__":
    main()
    