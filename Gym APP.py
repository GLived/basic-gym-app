# (BIT502), Glen Liventaal, ID 5126701, assessment 1

# break and continue will be important

import os
import sys

# Clear the terminal screen and display the menu fresh
#os.system("cls")

while(True): #makes all the break and continue statements run
    os.system("cls")
    print("Welcome to City Gym! We have a brand new app and we're very excited for you to give it a try.") #print main menu and choice input
    print("1. Membership plans \n2. Optional extras \n3. Gym Challange \n4. Exit the program \n")
    main_menu_choice = (input("Enter your option: ")) 


    if (main_menu_choice == "1"): #print membership plans and display choices per input
        while(True):
            os.system("cls")
            print("Membership Plans!")
            print("1. Basic \n2. Regular \n3. Premium \n4. Return to main menu \n5. Exit \n")
            membership_plans_choice = (input("Enter your option: "))

            if membership_plans_choice == "1":
                print("Basic membership costs 10$ a week.")
                input("Press Enter to continue")
                continue
            elif membership_plans_choice == "2":
                print("Regular membership costs 15$ a week.")
                input("Press Enter to continue")
                continue
            elif membership_plans_choice == "3":
                print("Premium membership costs 20$ a week.")
                input("Press Enter to continue")
                continue
            elif membership_plans_choice == "4":
                print("Returning to main menu")
                input("Press Enter to continue")
                break
            elif membership_plans_choice == "5":
                print("Thank you for visiting")
                input("Press Enter to leave application")
                sys.exit() #exits the application
            else:
                print("Incorrect choice, please try again.")
                input("Press Enter to try again")
                continue




    elif (main_menu_choice == "2"):
        while(True):
            os.system("cls")
            print("The optional extras are: ")
            print("1. 24/7 gym access - 1$ a week \nGrants you full access to the facilities 24 hours a day, 7 days a week")
            print("2. Personal training - 20$ a week \nProvides you a weekly meeting with a personal trainer")
            print("3. Diet consultation - 20$ a week \nProvides you a weekly consultation with a professional nutritionist")
            print("4. Online video access - 2$ a week \nProvides you full access to online resouces made by personal trainers")
            optional_extra_choice = input("Would you like to add any of these to your membership? 'y' for yes and 'n' for no: ").lower()

            if (optional_extra_choice == "n"):
                print("Taking you back to the main menu")
                input("Press Enter to continue")
                break

            if (optional_extra_choice == "y"):
                total_price = 0  #needs to be here, otherwise while loops over it, deleting total_price input
                go_to_main_menu = False #takes you back to main menu when True
                while(True):
                    os.system("cls")
                    gym_access = input("Would you like 24/7 gym access for 1$ a week? 'y' for yes and 'n' for no: ").lower()
                    if (gym_access == "y"):
                        total_price += 1
                        
                    personal_trainer = input("Would you like a personal trainer for $20 dollars a week? 'y' for yes and 'n' for no: ").lower()
                    if (personal_trainer == "y"):
                        total_price += 20
                        
                    diet_consultation = input("Would you like a diet consultation for $20 dollars a week? 'y' for yes and 'n' for no: ").lower()
                    if (diet_consultation == "y"):
                        total_price += 20
                                                
                    online_video_access = input("Would you like access to online videos for $2 a week? 'y' for yes and 'n' for no: ").lower()
                    if (online_video_access == "y"):
                        total_price += 2
                        
                    print(f"The total price for your services will be {total_price}$ a week.")
                    input("Press Enter to go back to the main menu.")
                    go_to_main_menu = True
                    break
                if go_to_main_menu:
                    break
                                    
            else:
                print("Incorrect choice, please try again.")
                input("Press Enter to try again")
                continue
        
    elif (main_menu_choice == "3"):
        #go_to_main_menu = False
        while(True):
            os.system("cls")
            print("Welcome to the Gym Challenge! Please record your time for all 4 challenges.")
            print("The 4 challenges are: \n50 skips with a skipping rope \n20 push-ups \n10 squats \n100 m run \n")
            input("Press Enter to start")

            os.system("cls")
            skipping_time = int(input("Insert your time (in seconds) for 50 skips with a skipping rope: "))
            #print(skipping_time)
            push_ups_time = int(input("Insert your time (in seconds) for 20 push-ups: "))
            squats_time = int(input("Insert your time (in seconds) for 20 squats: "))
            run_time = int(input("Insert your time (in seconds) for 100 m run: "))
            total_time = skipping_time + 15 + push_ups_time + 15 + squats_time + 15 + run_time
            total_time_in_minutes = round(total_time / 60)  #minutes for comparison operators
            if (total_time_in_minutes > 8):
                print(f"Final time: {total_time} seconds (including 15-second break between each activity).")
                print("Congratulations, you are ranked Steel")
                print(f"To achieve Bronze, you need to complete the activities in less than {total_time - 480} seconds from your current time. Good luck.")
            elif (total_time_in_minutes > 6):
                print(f"Final time: {total_time} seconds (including 15-second break between each activity).")
                print("Congratulations, you are ranked Bronze")
                print(f"To achieve Silver, you need to complete the activities in less than {total_time - 360} seconds from your current time. Good luck.")
            elif (total_time_in_minutes > 5):
                print(f"Final time: {total_time} seconds (including 15-second break between each activity).")
                print("Congratulations, you are ranked Silver")
                print(f"To achieve Gold, you need to complete the activities in less than {total_time - 300} seconds from your current time. Good luck.")
            elif (total_time_in_minutes <= 5 and total_time >= 264):
                print(f"Final time: {total_time} seconds (including 15-second break between each activity).")
                print("Congratulations, you are ranked Gold")
                print(f"To achieve the gym record, you need to complete the activities in less than {total_time - 263} seconds from your current time. Good luck.") #current best time is 264 seconds, so needs to be better not equal
            else:
                print(f"Final time: {total_time} seconds (including 15-second break between each activity).")
                print("Congratulations, you are ranked Gold")
                print("Congratulations, You have also achieved the current gym record. Way to go!")

            
            input("Press Enter to go to main menu")
            break


    elif (main_menu_choice == "4"):
        print("Thank you for visiting")
        input("Press Enter to exit the application")
        sys.exit()
    else:
        print("This choice does not exist")
        input("Press Enter to try again")
        continue



    


