import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import sys
import nltk


n=int
class HomePage:
    def __init__(self, master):
        self.master = master
        self.bg_image = tk.PhotoImage(file="bg.png")
        self.bg_canvas = tk.Canvas(master, width=1250, height=800)
        self.bg_canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)
        self.bg_canvas.pack()

        self.numbers_button = tk.Button(self.bg_canvas, text="Numbers", font=("Arial", 16), command=self.start_bulls_and_cows)
        self.numbers_button.place(relx=0.4, rely=0.5, anchor=tk.CENTER)

        self.words_button = tk.Button(self.bg_canvas, text="Words", font=("Arial", 16), command=self.words_button_click)
        self.words_button.place(relx=0.6, rely=0.5, anchor=tk.CENTER)

    def start_bulls_and_cows(self):
        root.destroy() 
        self.bulls_and_cows_game = tk.Tk()
        self.bulls_and_cows_game.title("Bulls and Cows Game")
        game = BullsAndCowsGame(self.bulls_and_cows_game)
        self.bulls_and_cows_game.mainloop()

    def words_button_click(self):
        messagebox.showinfo("Words Button Clicked", "You clicked the Words button.")
        root.destroy() 
        self.bulls_and_cows_game = tk.Tk()
        self.bulls_and_cows_game.title("Bulls and Cows Game")
        game = BullsAndCowsGameWords(self.bulls_and_cows_game)
        self.bulls_and_cows_game.mainloop()

class BullsAndCowsGame:
    def __init__(self, master):
        global n 
        n = simpledialog.askinteger("Enter n", "Enter the number of digits in the word:")

        self.master = master
        self.secret_code = self.generate_secret_code()
        self.num_guesses = 0
        self.guess_history = []

         

        self.bg_image = tk.PhotoImage(file="bg.png")
        self.bg_canvas = tk.Canvas(master, width=1250, height=800)
        self.bg_canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)
        self.bg_canvas.pack()

        self.label = tk.Label(self.bg_canvas, text="Enter your guess ("+str(n)+" -digit number):", font=("Arial", 16), bg="white")
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
        global n 
        return ''.join(random.sample('0123456789', n))

    def check_guess(self):
        global n 
        guess = self.guess_entry.get()
        if len(guess) != n or not guess.isdigit():
            messagebox.showerror("Error", "Please enter a valid"+str(n)+ "-digit number.")
            return

        self.num_guesses += 1
        bulls, cows = self.calculate_bulls_and_cows(guess)
        self.guess_history.append((guess, bulls, cows))

        if bulls == 4:
            messagebox.showinfo("Congratulations", f"You guessed the secret code {self.secret_code} in {self.num_guesses} tries!")
            self.master.destroy()
        else:
            self.result_label.config(text=f"Bulls: {bulls}, Cows: {cows}")
            self.update_guess_history()

    def calculate_bulls_and_cows(self, guess):
        global n 
        bulls = sum(1 for i in range(n) if guess[i] == self.secret_code[i])
        cows = sum(1 for digit in guess if digit in self.secret_code) - bulls
        return bulls, cows

    def update_guess_history(self):
        self.guess_history_text.delete('1.0', tk.END)
        for guess, bulls, cows in self.guess_history:
            self.guess_history_text.insert(tk.END, f"Guess: {guess}, Bulls: {bulls}, Cows: {cows}\n")






    #########################################################



class BullsAndCowsGameWords:
    def __init__(self, master):
        global n
        self.master = master
        self.secret_code = self.generate_secret_code()
        self.num_guesses = 0
        self.guess_history = []

        self.bg_image = tk.PhotoImage(file="bg.png")
        self.bg_canvas = tk.Canvas(master, width=1250, height=800)
        self.bg_canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)
        self.bg_canvas.pack()

        self.label = tk.Label(self.bg_canvas, text=f"Enter your guess ({n}-letter word):", font=("Arial", 16), bg="white")
        self.label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.guess_entry = tk.Entry(self.bg_canvas, font=("Arial", 16))
        self.guess_entry.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        self.submit_button = tk.Button(self.bg_canvas, text="Submit Guess", font=("Arial", 16), command=self.check_guess)
        self.submit_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.result_label = tk.Label(self.bg_canvas, text="", font=("Arial", 16), bg="white")
        self.result_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.guess_history_text = tk.Text(self.bg_canvas, height=10, width=30, font=("Arial", 14))
        self.guess_history_text.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.master = master
        self.secret_code = self.generate_secret_code()
        self.num_guesses = 0
        self.guess_history = []

        self.bg_image = tk.PhotoImage(file="bg.png")
        self.bg_canvas = tk.Canvas(master, width=1250, height=800)
        self.bg_canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)
        self.bg_canvas.pack()

        self.label = tk.Label(self.bg_canvas, text="Enter your guess (4-letter word):", font=("Arial", 16), bg="white")
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
        nltk.download('words')
        from nltk.corpus import words
        word_list = words.words()
        four_letter_words = [word for word in word_list if len(word) == 4]
        random_word = random.choice(four_letter_words)
        return random_word

    def check_guess(self):
        guess = self.guess_entry.get()
        if len(guess) != 4 or not guess.isalpha():
            messagebox.showerror("Error", "Please enter a valid 4-digit word.")
            return

        self.num_guesses += 1
        bulls, cows = self.calculate_bulls_and_cows(guess)
        self.guess_history.append((guess, bulls, cows))

        if bulls == 4:
            messagebox.showinfo("Congratulations", f"You guessed the secret code {self.secret_code} in {self.num_guesses} tries!")
            self.master.destroy()
        else:
            self.result_label.config(text=f"Bulls: {bulls}, Cows: {cows}")
            self.update_guess_history()

    def calculate_bulls_and_cows(self, guess):
        bulls = sum(1 for i in range(4) if guess[i] == self.secret_code[i])
        cows = sum(1 for digit in guess if digit in self.secret_code) - bulls
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