import random

def game():
    # Step 1: Assign random numbers to the doors
    door1 = random.randint(1, 100)  # Goat
    door2 = random.randint(1, 100)  # Goat
    door3 = random.randint(101, 200)  # Car
    
    # Randomly shuffle the "goats" and the "car" to random doors
    doors = [door1, door2, door3]
    random.shuffle(doors)
    
    # Display the game setup
    print("Welcome to the Monty Hall Game Show!")
    print("There are three doors. Behind one door is a car, behind the other two are goats.")
    print("You will choose a door, Monty will reveal a goat behind one of the other doors, and then you'll decide whether to stick with your choice or switch.")

    # Step 2: Player makes an initial choice
    print("Choose a door (1, 2, or 3): ")
    player_choice = input()
    
    # Convert the player's choice to a door number (1-based)
    if player_choice == "1":
        player_door = doors[0]
        chosen_door = 1
    elif player_choice == "2":
        player_door = doors[1]
        chosen_door = 2
    elif player_choice == "3":
        player_door = doors[2]
        chosen_door = 3
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        return

    # Step 3: Monty opens a door to reveal a goat (not the player's choice)
    remaining_doors = [1, 2, 3]
    remaining_doors.remove(chosen_door)  # Remove the player's choice
    
    # Find a door with a goat
    monty_opens = None
    for door in remaining_doors:
        if (door == 1 and doors[0] <= 100) or (door == 2 and doors[1] <= 100) or (door == 3 and doors[2] <= 100):
            monty_opens = door
            break
    
    print(f"Monty opens door {monty_opens} and reveals a goat!")

    # Step 4: Offer the player a chance to switch
    switch_choice = input("Do you want to switch doors? (yes/no): ")

    # Determine the new door choice after switching, if applicable
    if switch_choice == "yes":
        remaining_doors.remove(monty_opens)  # Remove Monty's revealed door
        new_choice = remaining_doors[0]  # Only one door left
        print(f"You switched to door {new_choice}.")
        player_door = doors[new_choice - 1]  # Assign the new choice's door value
    else:
        print(f"You decided to stay with door {chosen_door}.")
    
    # Step 5: Reveal if the player won or lost
    if player_door >= 101:
        print("Congratulations! You won the car!")
    else:
        print(f"Sorry, you got a goat. The car was behind door {doors.index(door3) + 1}.")

    input("Press Enter to exit")
