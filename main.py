import tkinter as tk
from tkinter import messagebox

class FlashcardApp:
    def __init__(self, root, flashcards):
        self.root = root
        self.root.title("Flashcard App")
        
        self.flashcards = flashcards
        self.current_index = 0

        # Label to show question/answer
        self.card_label = tk.Label(root, text="", font=('Helvetica', 24), width=40, height=10, relief="solid")
        self.card_label.pack(pady=20)

        # Show Question
        self.show_card("question")
        
        # Button to show answer
        self.answer_button = tk.Button(root, text="Show Answer", font=('Helvetica', 14), command=self.show_answer)
        self.answer_button.pack(pady=10)

        # Button to go to the next flashcard
        self.next_button = tk.Button(root, text="Next", font=('Helvetica', 14), command=self.next_card)
        self.next_button.pack(side=tk.LEFT, padx=20, pady=20)

        # Button to go to the previous flashcard
        self.prev_button = tk.Button(root, text="Previous", font=('Helvetica', 14), command=self.prev_card)
        self.prev_button.pack(side=tk.LEFT, padx=20, pady=20)

    def show_card(self, card_type):
        """Display question or answer based on card_type ('question' or 'answer')"""
        if card_type == "question":
            self.card_label.config(text=self.flashcards[self.current_index]["question"])
        elif card_type == "answer":
            self.card_label.config(text=self.flashcards[self.current_index]["answer"])

    def show_answer(self):
        """Display the answer of the current flashcard"""
        self.show_card("answer")

    def next_card(self):
        """Go to the next flashcard"""
        self.current_index += 1
        if self.current_index >= len(self.flashcards):
            self.current_index = 0  # Loop back to the first card
        self.show_card("question")  # Show the question for the new card

    def prev_card(self):
        """Go to the previous flashcard"""
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.flashcards) - 1  # Loop back to the last card
        self.show_card("question")  # Show the question for the new card


if __name__ == "__main__":
    # Sample flashcards (question, answer)
    flashcards = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 2 + 2?", "answer": "4"},
        {"question": "What is the largest ocean?", "answer": "Pacific Ocean"},
    ]
    
    # Initialize the Tkinter window
    root = tk.Tk()
    
    # Create the Flashcard app with the sample flashcards
    app = FlashcardApp(root, flashcards)
    
    # Run the Tkinter event loop
    root.mainloop()
