# ==========================================
#  Title:  Question 4
#  Author: elifyener
#  Date:   20 Feb 2021
# ==========================================

# Question 4
# Hangman Game
# Write a classic Hangman game using Object Oriented programming.

import random

class HangmanGame:
    def __init__(self):
        
        self.flag = True
        
        print("Let's play hangman")
        
        word_list = ["adversary","brackish","bluff","barricade","commotion","cunning","debris","destination","exhilarate","furtive","grueling","gypsy","headway","habitation","ignite","imperious","jabber","jargon","jut","jostle","knoll","luminous","misgiving","momentum","monotonous","narrate","obscure","outlandish","persistent","plenteous","potential","precipice","quell","recuperate","repugnant","restitution","sabotage","scarcity","serenity","tactic","translucent","uncanny","vulnerable","waver","yesterday","yarn","zeal","zebra","Zombie"]
       
       # Set everything to uppercase
       # i -> I
       # j -> J
        for item in word_list:
            index = word_list.index(item)
            item = item.replace("i","I")
            item = item.replace("j", "J")
            item = item.upper()
            word_list[index] = item
        
        self.word_list = word_list
        self.lives = 6
        
        return None
    
    # Choice random word
    def random_word(self):
        
        word = random.choice(self.word_list)
        self.word = word
            
    
    # Prints a string of '*' with the same lenght of the secret word
    def secret_word(self):
        secret_list=['*' for i in range(len(self.word))]
        print(f"Your word contains {format(len(self.word))} letters")
        print(''.join(secret_list))
        self.secret_list = secret_list
        return None
    
    # Prints the current life status
    def life_status(self):
    
        if (self.lives)!=1:
            print(f"You have {self.lives} lives.")
        else:
            print(f"You have {self.lives} live.")

        return self.lives
    
    # Gets a letter from the user.
    def press_letter(self):
        letter = input("Write a letter: ")
        # Make it uppercase for anything
        # i -> I
        # j -> J
        letter = letter.upper()
        letter = letter.replace("i","I")
        letter = letter.replace("j", "J")
        self.letter = letter
    
    # Evaluates whether the character being introduced is in the correct format.
    def play(self):
        if  len(self.letter)>1 or len(self.letter)==0:
            print("\t\nYou entered more than one character or none. \nYou must write one character at a time. (-1 life)\n")
            
            self.lives=self.lives - 1
            
        elif (self.letter).isalpha()==False:
            print("\t\nYou entered a character that does not belong to the alphabet. (-1 life)\n")
            
            self.lives=self.lives - 1
            
        elif self.letter not in self.word:
            print("That letter is not in the word. (-1 life)\n")
            
            self.lives=self.lives - 1
            
        else:
            # If correct, print it
            print("Great!")
            # Replace the "*" with the already found characters that are in the word
            for index in range(len(self.word)):
                if self.letter==self.word[index]:
                    self.secret_list[index]=self.letter
        
        # Prints secret_list            
        print(''.join(self.secret_list))
    
    def man(self):
        li = self.lives
        if (li == 6):
            print('''
               +---+
                   |
                   |
                   |
                  ===''')
        elif (li == 5):
            print('''
               +---+
               O   |
                   |
                   |
                  ===''')
        elif (li == 4):
            print('''
               +---+
               O   |
               |   |
                   |
                  ===''')
            
        elif (li == 3):
            print('''
               +---+
               O   |
              /|   |
                   |
                  ===''')
            
        elif (li == 2):
            print('''
               +---+
               O   |
              /|\  |
                   |
                  ===''')
            
        elif (li == 1):
            print('''
               +---+
               O   |
              /|\  |
              /    |
                  ===''')
            
        elif (li == 0):
            print('''
               +---+
               O   |
              /|\  |
              / \  |
                  ===''')
                      
    # Signs a boolean value of True if the user guess the secret word
    def win(self):
        # If you guess before you spend your chances, you win
        if '*' not in self.secret_list: 
            print(f"\nYou have won, the word is: {self.word} \nCongratulations!")
            return True
   
    #Prints a message if in "list" remains '*'
    def loss(self):
        if '*' in self.secret_list:
            print("\n\nYou lost :(")
    
    # Ask the user whether to continue
    def goodbye(self):
        try:
            status=int(input("Play again?\nYES: press 0\nNO: press 1\n"))
            if status==0:
                self.lives = 6
                return True
            elif status==1:
                print("\nSee you soon...")
                return False
            else:
                print("You keyed it wrong try again. ")
                return HangmanGame.goodbye(self)
        except:
            print("Try again.")
            return HangmanGame.goodbye(self)
        
    def status(self):
        
        self.flag= HangmanGame.goodbye(self)
        
        return self.flag
    
def main():
    hangman = HangmanGame()

    while hangman.flag==True:
        
        hangman.random_word()
        hangman.secret_word()
        hangman.life_status()
        
        while (hangman.lives) > 0:
            
            hangman.press_letter()
            hangman.play()
            hangman.life_status()
            hangman.man()
            
            if hangman.win()==True:
                break
            
        hangman.loss()
        hangman.status()
        
if __name__ == "__main__":
    main()
