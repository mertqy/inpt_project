import random

MAX_LINE = 3
MAX_BET = 1000
MIN_BET = 5

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
    return winnings, winnings_lines


# ------------------------------------------------------------------

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


# ------------------------------------------------------------------

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="| ")
            else:
                print(column[row])


# ------------------------------------------------------------------

def deposit():
    while True:
        amount = input("siteye kaç para yatırcan? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("sıfırdan büyük sayı gircen (FAKIIR)")
        else:
            print("sayı gırcen")

    return amount


# -----------------------------------------------------------------
def get_bet():
    while True:
        amount = input("oyuna kaç para yatırcan? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"tutar ${MIN_BET} - ${MAX_BET} arasında olmalıdır.")
                # bir diğer yöntem print("tutar {}-{} arasında olmalıdır.".format(MİN_BET,MAX_BET))
        else:
            print("sayı gırcen")
    return amount


# ------------------------------------------------------------------

def spin(balance):
    lines = 3
    while True:
        bet = get_bet()
        if bet > balance:
            print("yeterli miktarda paran yok şuanda ${} paran var".format(balance))
        else:
            break
    print(f"${bet} yatırıyorsunuz")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winning, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print("{} kazandın".format(winning))
    return winning - bet


# ------------------------------------------------------------------

def main():
    balance = deposit()
    while True:
        print(f"mevcut paranız ${balance}")
        answer = input("oynamak için enter'a bas (çıkmak için q ya bas)")
        if answer == "q":
            break
        balance += spin(balance)


main()

# %%
