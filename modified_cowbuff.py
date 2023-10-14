import tkinter as tk
from tkinter import messagebox
import random
import nltk
from nltk.corpus import words

class HomePage:
    def __init__(self, master):
        self.master = master
        self.bg_image = tk.PhotoImage(file="bg.png")
        self.bg_canvas = tk.Canvas(master, width=1250, height=800)
        self.bg_canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)
        self.bg_canvas.pack()

        self.digits_button = tk.Button(self.bg_canvas, text="Digits", font=("Arial", 16), command=self.start_bulls_and_cows_digits)
        self.digits_button.place(relx=0.4, rely=0.5, anchor=tk.CENTER)

        self.words_button = tk.Button(self.bg_canvas, text="Words", font=("Arial", 16), command=self.start_bulls_and_cows_words)
        self.words_button.place(relx=0.6, rely=0.5, anchor=tk.CENTER)

    def start_bulls_and_cows_digits(self):
        root.destroy()
        self.bulls_and_cows_game = BullsAndCowsGame(tk.Tk(), mode="digits")
        self.bulls_and_cows_game.mainloop()

    def start_bulls_and_cows_words(self):
        root.destroy()
        self.bulls_and_cows_game = BullsAndCowsGame(tk.Tk(), mode="words")
        self.bulls_and_cows_game.mainloop()

class BullsAndCowsGame:
    def __init__(self, master, mode):
        self.master = master
        self.mode = mode
        self.secret_code = self.generate_secret_code() if mode == "digits" else self.generate_secret_word()
        self.num_guesses = 0
        self.guess_history = []

        self.bg_image = tk.PhotoImage(file="bg.png")
        self.bg_canvas = tk.Canvas(master, width=1250, height=800)
        self.bg_canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)
        self.bg_canvas.pack()

        self.label_text = "Enter your guess (4-digit number):" if mode == "digits" else "Enter your guess (5-letter word):"
        self.label = tk.Label(self.bg_canvas, text=self.label_text, font=("Arial", 16), bg="white")
        self.label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.guess_entry = tk.Entry(self.bg_canvas, font=("Arial", 16))
        self.guess_entry.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        self.submit_button = tk.Button(self.bg_canvas, text="Submit Guess", font=("Arial", 16), command=self.check_guess)
        self.submit_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.result_label = tk.Label(self.bg_canvas, text="", font=("Arial", 16), bg="white")
        self.result_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.guess_history_text = tk.Text(self.bg_canvas, height=10, width=30, font=("Arial", 14))
        self.guess_history_text.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def generate_secret_code(self):
        return ''.join(random.sample('0123456789', 4))

    def generate_secret_word(self):
        nltk.download('words')
        word_list = words.words()
        while True:
            word = random.choice(word_list)
            if len(word) == 5:
                return word

    

    def check_guess(self):
        guess = self.guess_entry.get()
        if (self.mode == "digits" and (len(guess) != 4 or not guess.isdigit())) or (self.mode == "words" and len(guess) != 5):
            messagebox.showerror("Error", "Please enter a valid guess.")
            return

        self.num_guesses += 1
        if self.mode == "digits":
            bulls, cows = self.calculate_bulls_and_cows(guess)
        else:
            bulls, cows = self.calculate_bulls_and_cows_word(guess)
        self.guess_history.append((guess, bulls, cows))

        if bulls == 4 or (self.mode == "words" and guess == self.secret_code):
            messagebox.showinfo("Congratulations", f"You guessed the secret code/word in {self.num_guesses} tries!")
            self.master.destroy()
        else:
            self.result_label.config(text=f"Bulls: {bulls}, Cows: {cows}")
            self.update_guess_history()

    def calculate_bulls_and_cows(self, guess):
        bulls = sum(1 for i in range(4) if guess[i] == self.secret_code[i])
        cows = sum(1 for digit in guess if digit in self.secret_code) - bulls
        return bulls, cows

    def calculate_bulls_and_cows_word(self, guess):
        bulls = sum(1 for i in range(5) if guess[i] == self.secret_code[i])
        cows = sum(1 for letter in guess if letter in self.secret_code) - bulls
        return bulls, cows

    def update_guess_history(self):
        self.guess_history_text.delete('1.0', tk.END)
        for guess, bulls, cows in self.guess_history:
            self.guess_history_text.insert(tk.END, f"Guess: {guess}, Bulls: {bulls}, Cows: {cows}\n")

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Home Page")
    home_page = HomePage(root)
    root.mainloop()
