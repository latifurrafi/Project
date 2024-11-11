import random

def roll_dice(number_of_dice):
    results = []
    for _ in range(number_of_dice):
        result = random.randint(1, 6)  # Generate a random number between 1 and 6
        results.append(result)
    return results

def main():
    print("Welcome to the Dice Simulation!")
    number_of_dice = int(input("Enter the number of dice you want to roll: "))
    
    results = roll_dice(number_of_dice)
    print(f"You rolled: {results}")
    print(f"Total: {sum(results)}")

if __name__ == "__main__":
    main()
