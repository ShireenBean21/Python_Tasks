import getpass

chances = 0
correct_pin = '1234'

while chances < 3:
    supplied_pin = getpass.getpass(prompt="Enter your pin: ")
    if supplied_pin == correct_pin:
        print('Pin successful.')
        break
    else:
        print('Pin incorrect.')
        chances += 1

if chances == 3:
    print('Maximum number of attempts exceeded.')


