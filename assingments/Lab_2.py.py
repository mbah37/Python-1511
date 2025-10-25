# Lab 2: Tip Calculator
# Moustapha Bah - 9/12/2025
total = int(input())
print(f'Your total is: ${total}. Would you like to add a tip?')
# Loop until valid tip is given
while True:
    tip_choice = input('1 for yes, 0 for no: ')
    if tip_choice in ['1', '0']:
        tip = bool(int(tip_choice))
        break
    else:
        print("Invalid input. Please enter 1 for yes or 0 for no.")

if tip:
    print('Would you like to add a 15% or 20% tip?')
# Loop until valid tip is is given
    while True:
        tip_amount_input = input('15 or 20: ')
        if tip_amount_input in ['15', '20']:
            tip_amount = int(tip_amount_input)
            break
        else:
            print("Invalid input. Please enter 15 or 20.")

    if tip_amount == 15:
        total = total * 1.15
        print(f'Your new total is: ${total:.2f}')
    elif tip_amount == 20:
        total = total * 1.20
        print(f'Your new total is: ${total:.2f}')
else:
    print(f'Your total remains: ${total}. Have a nice day!')