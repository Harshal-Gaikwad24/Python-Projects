# 🎰 Slot Machine Project

This is a simple console-based **Slot Machine Game** built using Python. The project demonstrates core programming concepts such as functions, loops, conditionals, random number generation, and user input handling.

## 🧾 Features

- Allows users to deposit money.
- Bet on 1 to 4 lines simultaneously.
- Customize bet amount per line.
- Symbols are randomly spun across a 5x5 slot grid.
- Winnings are calculated based on symbol matches across lines.
- Loop to continuously play until the user quits.

## 📌 Game Rules

- The slot machine has 5 rows and 5 columns.
- Each symbol (A, B, C, D) has a predefined frequency and value:
  - A: appears 2 times, value = 5
  - B: appears 4 times, value = 3
  - C: appears 5 times, value = 2
  - D: appears 6 times, value = 4
- You win if all symbols match in a horizontal line you’ve bet on.

## 💻 How to Run

Make sure you have Python installed (version 3.6 or higher recommended).

1. Clone this repository:
   ```bash
   git clone https://github.com/Harshal-Gaikwad24/Python Projects.git
   cd slot-machine

Here's a sample runup of the slot machine designed for a small scale game:
What would you like to deposit ?: $ 100
Enter no. of lines to bet on (1-4)? 3
How much would you like to bet on each line? 10
You are betting $10 on 3 lines. Total bet is equal to:30
A | D | C | B | A
C | B | A | A | C
D | C | C | D | D
You won 30.
You won on lines: 2


