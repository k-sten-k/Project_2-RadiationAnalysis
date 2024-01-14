# xxxxxxxxxxxxxxx
import statistics

# Function displays radiation data from dictionary in column format:
def display_dict ():
    '''
    Displays radiation data from dictionary in a column format
    '''
    print("{:<25} {:<10}".format('LOCATION', 'RADIATION'))
    for location in locations_levels_dict:
        print("{:<25} {:<10}".format(location, str(locations_levels_dict[location]['radiation_levels'])))

# Function calculates statistics data (average and standard deviation) for each location and stores values in the dictinary.
def statistics_calc():
    '''
    Calculates statistic data for each location
    '''
    for location in locations_levels_dict:
        average = statistics.mean(locations_levels_dict[location]['radiation_levels'])
        locations_levels_dict[location]['avg'] = average            # this will add average into dictionary
        std_dev = statistics.stdev(locations_levels_dict[location]['radiation_levels'])
        locations_levels_dict[location]['std'] = round(std_dev,2)   # this will add standard dev into dictionary

# Function displays calculated data in columns: 
def display_calc_data_columns ():
    '''
    Displays calculated data in a column format
    '''
    print("{:<25} {:<10} {:<10}".format('LOCATION', 'AVERAGE', 'STD-DEV'))
    for location in locations_levels_dict:
        print("{:<25} {:<10} {:<10}".format(location, locations_levels_dict[location]['avg'], locations_levels_dict[location]['std']))

# Function try-except to handle incorrect inputs, checks if input= whole number:
def check_menu_input (menu_opition_input):
    '''
    Checks is input is an integer
    '''
    try:
        menu_opition_input = int(menu_opition_input)
        input_check = True
    except ValueError:
        input_check = False
    return input_check

# Dictionary storing locations and their radiation levels:
locations_levels_dict = {
    'City centre' : {'radiation_levels':[22, 19, 20, 31, 28]},
    'Industrial zone' : {'radiation_levels':[35, 32, 30, 37, 40]},
    'Residential district' : {'radiation_levels':[15, 12, 18, 20, 14]},
    'Rural outskirts' : {'radiation_levels':[9, 13, 16, 14, 7]},
    'Downtown' : {'radiation_levels':[25, 18, 22, 21,26]}
    }
print("\nWelcome to Radiation Data Analysis program!")
# Main loop displaying available options to user:
while True:
    print("""\n Select one of the following options:
      1- Show data
      2- Calculate average and standard deviation
      3- Add data
      4- Exit""")   
    main_menu_selection = input("\nPlease enter option number (1 - 4): ")
    input_check_main_menu = check_menu_input(main_menu_selection)                  # Calling function to chcek if input is numeric 
    if input_check_main_menu == True and int(main_menu_selection) == 1:            # Option 1 selected form main manu: displaying radiation data
        print("\nHere is the current data:")
        display_dict()
    elif input_check_main_menu == True and int(main_menu_selection) == 2:           # Option 2 selected from main menu: average and std dev calculations, displaying calculated data                       
        print("\nHere is calculated data:")
        statistics_calc()
        display_calc_data_columns()
    elif input_check_main_menu == True and int(main_menu_selection) == 3:           # Option 3 selected from main menu: adding new data to dictionary. Displaying new selection menu
    
        while True:                                                                 # Nested loop for user to enter additional data into dictionary
            print("""\nPlease select one of the following options:
                    1- Add values to existing location
                    2- Add new location
                    3- Go back to main menu""")                                                         
            add_data_menu = input("\nPlease enter option number (1-3): ")
            input_check_add_menu = check_menu_input(add_data_menu)                 # Calling function to chcek if input is numeric 
            if input_check_add_menu == True and int(add_data_menu) == 1:           # Option for adding new radiation measurements to existing location
                print("\nHere are available locations:")                            
                for i, location in enumerate(locations_levels_dict):               # Listing out available locations
                    print(f"{i+1} - {location}")
                add_to_location = input("\nPlease select location by typing corresponding number: ")  
                input_check_add_loc_menu = check_menu_input(add_to_location)       # Calling function to check if input is valid (integer)
                if input_check_add_loc_menu == True:                               
                    add_to_location_index = int(add_to_location) - 1               
                    selected_location = list(locations_levels_dict.keys())[add_to_location_index] 

                    while True:                                                     # Loop to keep appending numbers until user chooses to stop
                        new_value = input(f"\nEnter new radiation value for {selected_location} (or type 'q' to quit): ")
                        if new_value.lower() == 'q':
                            print("\nLets take you back to 'Add data' menu.")
                            break
                        else:
                            try:                                                                               # checking if an integer was entered by user
                                new_value = int(new_value)
                                locations_levels_dict[selected_location]['radiation_levels'].append(new_value) # Appends value entered by user to exsisting location in dictionary
                                print(f"\nNew value {new_value} added to {selected_location}.")
                            except ValueError:
                                print("\nInvalid input. Please enter an integer or 'q' to quit.")

                elif input_check_add_loc_menu == False:
                    print("\nIncorrect Input. Please enter a number.")
                    continue
                else:
                    print("\nWrong number. Please make sure the number is between 1 and 3.")
            elif input_check_add_menu == True and int(add_data_menu) == 2:           # Adding new location to dictionary and and creating new list for radiation data
                new_location = input("\nEnter the name of the new location: ")
                if new_location in locations_levels_dict:                            # Checking if location already exsists in the dictionary
                    print("\nLocation already exists. Please choose a different name or add to exsisting location.")
                else:
                    locations_levels_dict[new_location] = {'radiation_levels': []}   # Creating new entry with empty list to add radiation levels
                    print(f"\nNew location '{new_location}' added successfully.")

                    while True:                                                     # Loop to keep appending radiation values until user chooses to stop
                        new_value = input(f"\nEnter new radiation value for {new_location} (or type 'q' to quit): ")
                        if new_value.lower() == 'q':
                            print("\nLets take you back to 'Add data' menu.")
                            break
                        else:
                            try:
                                new_value = int(new_value)
                                locations_levels_dict[new_location]['radiation_levels'].append(new_value)
                                print(f"\nNew value {new_value} added to {new_location}.")
                            except ValueError:
                                print("\nInvalid input. Please enter an integer or 'q' to quit.")

            elif input_check_add_menu == True and int(add_data_menu) == 3:           # Exiting back to main menu
                print("\nOK. Lets go back to main menu.")
                break
            elif input_check_main_menu == False:
                print("\nIncorrect Input. Please enter a number.")
                continue
            else:
                print("\nWrong number. Please make sure the number is between 1 and 3.")

    elif input_check_main_menu == True and int(main_menu_selection) == 4:             # Option 4 selected from main menu: Exit
        print("\nThank you! See you later!\n")
        break
    elif input_check_main_menu == False:
        print("\nIncorrect Input. Please enter a number.")
        continue
    else:
        print("\nWrong number. Please make sure the number is between 1 and 4.")
