def start_bulls_and_cows(self):
        root.destroy() 
        self.bulls_and_cows_game = tk.Tk()
        self.bulls_and_cows_game.title("Bulls and Cows Game")
        game = BullsAndCowsGameChoice(self.bulls_and_cows_game)
        self.bulls_and_cows_game.mainloop()