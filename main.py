def adventure_game():
   
    print("--- Welcome to Adventure Island! ---")
    print("Your mission is to find the treasure. Good luck!")

    while True:
        print("You are standing in front of a cave.")
        print("You can go left or right.")
        
        # First choice
        choice = input("Which way do you want to go? (left/right): ").lower()
        if choice == "left":
            print("You found a river.")
            print("You can swim across or walk around.")
            
            # Second choice
            choice = input("What do you want to do? (swim/walk): ").lower()
            if choice == "swim":
                print("You tried to swim but were eaten by a crocodile. Game over.")
            elif choice == "walk":
                print("After a long walk, you found 3 doors.")
                print("A red door, a yellow door, and a blue door.")
                
                # Third choice
                choice = input("Which door do you want to open? (red/yellow/blue): ").lower()
                if choice == "red":
                    print("The room was filled with fire. Game over.")
                elif choice == "yellow":
                    print("You fell into a pit of quicksand. Game over.")
                elif choice == "blue":
                    print("Congratulations! You opened the blue door and found the treasure!")
                    print("You win!")
                    break
                else:
                    print("Invalid choice. Game over.")
            else:
                print("Invalid choice. Game over.")
        elif choice == "right":
            print("You took a step to the right and fell into a hidden pit. Game over.")
        else:
            print("Invalid choice. Game over.")
        
        # Retry option
        retry = input("\nDo you want to try again? (yes/no): ").lower()
        if retry != "yes":
            print("Thanks for playing! Goodbye!")
            break

adventure_game()
