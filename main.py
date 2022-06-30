import csv

print("Welcome to the Esports Tournament Participant Interface (ETPI)")
print("==============================================================")

num_of_participants_chosen = False
while not num_of_participants_chosen:
    num_of_participants = input("Please enter the number of participants: ")

    if num_of_participants.isdecimal():
        num_of_participants = int(num_of_participants)

        if num_of_participants > 1 and num_of_participants < 1000000:
            print("There are " + str(num_of_participants) + " participant slots ready for sign-ups.")
            num_of_participants_chosen = True

        else: print("Please choose a valid number of participants.")

    else: print("Please choose a valid number of participants.")

slots_participants = dict([(i, None) for i in range(num_of_participants)])

user_exited = False
while not user_exited:
    print("Actions Menu")
    print("============")
    print("1. Sign Up")
    print("2. Cancel Sign Up")
    print("3. View Participants")
    print("4. Save Changes")
    print("5. Exit")
    menu_choice = input("")
    print("============")

    if menu_choice == "1":
        print("Sign Up")
        print("=======") 

        name_valid = False
        while not name_valid:
            participant_name = input("Participant name: ")

            if participant_name.isalpha() and len(participant_name) > 1:
                name_valid = True

            else: print("Please enter a valid name.")

        starting_slot_valid = False
        while not starting_slot_valid:
            starting_slot = input("Desired starting slot #[1-" + num_of_participants + "]: ")

            if starting_slot.isdecimal():
                starting_slot = int(starting_slot)

                if starting_slot >= 1 and starting_slot <= num_of_participants:

                    if slots_participants[starting_slot] == None:
                        print(participant_name + " is signed up in starting slot #" + starting_slot)
                        starting_slot_valid = True

                    else: print("Slot #" + starting_slot + " is filled. Please try again.")

                else: print("Please enter a valid starting spot.")

            else: print("Please enter a valid starting spot.")

    elif menu_choice == "2":
        print("Cancellation")
        print("============")

        cancellation_valid = False
        while not cancellation_valid:
            starting_slot = input("Starting slot #[1-" + num_of_participants + "]: ")

            if starting_slot.isdecimal():
                starting_slot = int(starting_slot)

                if starting_slot >= 1 and starting_slot <= num_of_participants:

                    if slots_participants[starting_slot] != None:
                        participant_name = input("Participant name: ")

                        if participant_name == slots_participants[starting_slot]:
                            print(participant_name + " has been cancelled from starting slot #" + starting_slot + ".")

                        else: print(participant_name + " is not in that starting slot.")

                    else: print("Slot #" + starting_slot + " is empty. Please try again.")

                else: print("Please enter a valid starting spot.")

            else: print("Please enter a valid starting spot.")

    elif menu_choice == "3":
        print("View Participants")
        print("=================")

        starting_slot_valid = False
        while not starting_slot_valid:
            starting_slot = input("Starting slot #[1-" + num_of_participants + "]: ")

            if starting_slot.isdecimal():
                starting_slot = int(starting_slot)

                if starting_slot >= 1 and starting_slot <= num_of_participants:
                    start_index = starting_slot - 5
                    end_index = starting_slot + 5

                    if start_index < 0:
                        start_index = 0

                    if end_index > num_of_participants:
                        end_index = num_of_participants

                    for i in range(start_index, end_index):
                        print(i + ": " + slots_participants[i])
    
                else: print("Please enter a valid starting spot.")

            else: print("Please enter a valid starting spot.")

    elif menu_choice == "4":
        print("Save Changes")
        print("============")

        save_choice_valid = False
        while not save_choice_valid:
            save_choice = input("Save your changes to CSV? [y/n]: ")

            if save_choice == "y":
                with open("tournament-participants.csv", "w") as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(["Slot", "Participant"])
                    
                    for x in slots_participants:
                        csv_writer.writerow([x, slots_participants[x]])

                print("File 'tournament-participants.csv' successfully saved.")
                save_choice_valid = True
            
            elif save_choice == "n":
                save_choice_valid = True

            else: print("Please enter a valid choice.")

    elif menu_choice == "5":
        print("Exit")
        print("====")

        exit_choice_valid = False
        while not exit_choice_valid:
            print("Any unsaved changes will be lost.")
            exit_choice = input("Are you sure you want to exit? [y/n]: ")

            if exit_choice == "y":
                print("Goodbye.")
                user_exited = True
            
            elif exit_choice == "n":
                exit_choice_valid = True

            else: print("Please enter a valid choice.")