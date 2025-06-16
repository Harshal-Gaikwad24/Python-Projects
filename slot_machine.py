#SLOT MACHINE PROJECT Project:

import random

MAX_LINES=4
MAX_BET=9999
MIN_BET=1

ROWS=5
COLS=5

symbol_count={
    "A": 2,
    "B": 4,
    "C": 5,
    "D": 6
}


symbol_value={
    "A": 5,
    "B": 3,
    "C": 2,
    "D": 4
}

def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winning+=values[symbol]*bet
            winning_lines.append(line+1)

    return winnings,winning_lines

def get_slot_spin(rows, cols, symbols):     #spin the slot machine
    all_symbols=[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns

def print_slot(columns):        #slot column printer
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="  ")

        print()

def deposit():      #deposit funciton
    while True:
        amount=input("What would you like to deposit ?: $ ")
        if amount.isdigit():    #check input for valid amount
            amount=int(amount)  #convert to integer 
            if amount>0:
                break
            else:
                print('Amount should be greater than 0.')
        else:
            print('Please enter a valid amount.')
    return amount

def get_number_off_lines():     #function for betting on lines
    while True:
        lines=input("Enter no. of lines to bet on (1-" + str(MAX_LINES)+ ")?")
        if lines.isdigit():    #line check
            lines=int(lines)   
            if 0<lines<=MAX_LINES:
                break
            else:
                print('Enter valid number of lines.')
        else:
            print('Please enter a line number.')
    return lines
    

#bet function
def bet_check():
    while True:
        bet_amount=input("How much would you like to bet on each line ?")
        if bet_amount.isdigit():
            bet_amount=int(bet_amount)
            if MIN_BET<=bet_amount<=MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}:")
        else:
            print("Please enter a valid amount to bet!")
    return bet_amount


def spin(balance):
    
    lines=get_number_off_lines()
    while True:
        bet=bet_check()
        total_bet=bet*lines

        if total_bet>balance: # type: ignore
            print(f"You don't have enough to bet that amount. Your current balance is {balance}.")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to:{total_bet}")

    slots=get_slot_spin(ROWS,COLS,symbol_count)
    print_slot(slots)
    winnings,winning_lines=check_winnings(slots,lines,bet,symbol_value)
    print(f"You won {winnings}.")
    print(f"You won on lines:",*winning_lines)
    return winnings-total_bet

def main():     #re-run the program thoughout
    balance=deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer=input("Press enter to play (q to quit).")
        if answer=='q':
            break
        balance+=spin(balance)
    
main()
