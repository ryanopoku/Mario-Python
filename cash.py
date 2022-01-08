from cs50 import get_float

def main():
    change = change_owed("Changed owed is: ")
    cents = dollarsto_cents(change)

    # Print the amount of cents as number of coins to return
    print(centsto_coins(cents))


# Prompt user for an amount of change
def change_owed(prompt):
    while True:
        n = get_float(prompt)
        if n > 0:
            break
    return n


# Convert dollars into cents
def dollarsto_cents(amount):
    c = round(amount * 100)
    return c



def centsto_coins(cents):
    # How many quarters are in cents
    quarters = cents // 25
    dimes = (cents % 25) // 10
    nickels = ((cents % 25) % 10) // 5
    pennies = ((cents % 25) % 10) % 5

    # Return the total amount of coins
    return quarters + dimes + nickels + pennies


if __name__ == "__main__":
    main()
