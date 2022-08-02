import random

def add_series():
    inpt = input('\n\
Please enter the name of the series you would like to add.\n\
      or type "exit" to return to the main menu.\n')
    if inpt.lower() == 'exit':
        welcome()
    else:
        with open('series.txt', 'a') as f:
            f.write(inpt + '\n')
            print(f'\n{inpt} added to the list!\n')
        add_series()

def random_series():
    pass

def welcome():
    message = input('\
         Welcome to the Series Selector.\n\
 Would you like to ADD a new series to the list or\n\
would you like to recieve a RANDOM series from the list?\n\
                    (add/random)\n')
    while True:
        if message == 'add':
            add_series()
        elif message == 'random':
            random_series()
        else:
            message = input('Please enter either "add" or "random"\n')
            continue

def main():
    welcome()


if __name__ == '__main__':
    main()