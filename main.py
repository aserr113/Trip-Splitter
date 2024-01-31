
#Selecting the mode to the application
def mode_selector():
    #Lets users select what actions they want to go foward with. 
    options = [
        "Start an Event",
        "Start a Trip",
        "Split the Check",
        "Who Pays?"
    ]

    print ("What would you like to do:")

    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    modes = int(input("Enter the number corresponding to your choice: "))
    return modes

#Event Details/Configuration Function
def get_event_info():
    event_name = input("What is the name of the event :")
    event_location = input("Where is this event taking place :")
    event_date = input("Select the date for this event: ")

    #Configuration settings 
    print("Set your event configurations!")

    event_cost = input("Are you splitting cost(s) of this event [Y/N] :")
    event_guest = input("Do you want to show attendees of this event [Y/N] :")
    event_guest_items = input("Are your guess bringing items for the event [Y/N] :")

#Event Guest List Function
def get_event_attendees():
    event_num_people = int(input("How many peoplep will be comming to this event: "))
    event_people_names = []

    if event_num_people > 0: 
        ask_event_names = input("Do you want to to make a list of people coming. [Y/N] :")
        if ask_event_names.upper() == 'Y':
            for i in range (event_num_people):
                add_event_names  = input("Enter the name of person {}:".format (i+1))
                event_people_names.append(add_event_names)

    return event_people_names

#Event Item List/ Guest Item List Function
def event_item_list():
    print("What do you have already for the event")

    host_items [] = input("Enter items :")

#Event Questionary and Response Function
def event_questionaire():
    print("What Questions do you want to ask your Guest :")
    
#Print Event Summary 
def event_summary():
    print("Event Summary :")

#Trip Details/Configuration Functions
def get_trip_info():
    trip_location = input("Where is this trip going to be :")
    trip_date = input("Select the date for this event: ")
    
    trip_attendees = int(input("How many people are going on this trip: "))

    #Configuration settings 
    print("Set your trip configurations!")

    trip_cost = input("Are you splitting cost(s) of this trip. [Y/N] :")
    trip_guest = input("Do you want to show attendees of this trip. [Y/N] :")
    trip_guest_items = input("Are your guest bringing items for the trip. [Y/N] :")

#Trip Trip Transportation Function
def get_trip_trans():
    print("How will you be travel to this destination : ")

#Trip Attendees List Function
def get_trip_attendees():
    trip_num_people = int(input("How many people will be comming to this trip: "))
    trip_people_names = []

    if trip_num_people > 0: 
        ask_trip_names = input("Do you want to to make a list of people coming. [Y/N] :")
        if ask_trip_names.upper() == 'Y':
            for i in range (trip_num_people):
                add_trip_names  = input("Enter the name of person {}:".format (i+1))
                trip_people_names.append(add_trip_names)

    return trip_people_names

#Trip Expense Functions 
def get_trip_expenses():
     print("Lets calculate the trip expenses :")

#Itinerary Log and Selection Functions
def get_trip_itinerary():
    print("Lets create the best trip itenirary :")

#Trip Savings Function 
def get_savings_trip():
    print("Lets create a savings plan for this trip. ")

#Trip Items List/Guest Items List Function
def trip_item_list():
    trip_items = []
    total_trip_itemcost = 0

    while True: 
        trip_item_input = input("What is being brought: ")
        try:
            trip_item_cost = float(input("How much will it be $"))
            if trip_item_cost >= 0:
                        trip_items.append((trip_item_input, trip_item_cost))
            else:
                print("Please enter a non-negative amount.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

            add_to_list = input("Add another item [Y/N]: ")
            if add_to_list.upper() != 'Y':
                break

            print("These are the items being brought: ")
            for trip_item, trip_item_cost in trip_items:
                print("{}: ${:.2f}".format(trip_item, trip_item_cost))

    print("What will people bring? ")
    trip_item_list()

#Calculates the split total each person has to pay.
def calc_total(total_amount, num_people):
    split_amount = total_amount / num_people
    return split_amount

#Split the bill mode 
def split_bill():
    while True: 
        try:
            total_amount = float(input("Enter the total amount of the bill: $"))
            if total_amount >=0:
                num_people = int(input("How many people are going to split the bill :"))

                split_tip = ("Will you be splitting the tip as well. [Y/N] :").upper()
                if split_tip == 'Y':
                    tip_amt = float(input("How much will you be leaving in tip: $"))
                    total_amount += tip_amt
                    print("The new shared amount will be ${:.2f}".format(total_amount))    
                
                if num_people > 0:
                    split_amount = calc_total(total_amount, num_people)
                    return split_amount
                else:
                    print("Please enter a positive number of people.")
            else:
                print("Please enter a non-negative amount.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

#Who Pays Randomizer 
def who_pays_rand():
    print("Let see who will pay next")
    while True:
        price_rand = input("Enter the total amount of the price : $")
        try:
            price_rand = float(price_rand)
            if price_rand >= 0:
                return price_rand
            else: 
                print("Please enter a non-negative amount.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
num_people_rand = int(input("How many people are there total :"))
names_rand = []

for i in range(num_people_rand):
    name_rand = input("Enter the name of person {}:".format(i+1))
    names_rand.append(name_rand)
    
    return num_people_rand, names_rand

num_spins_rand = int(input("Enter the number of people paying the bill : "))

        #Enter each name in a spinning wheel that will then spin the number of num_spin_rand
        #Then it will get to randomly choose a name that will have to split the cost of the total amount. 








#Main Function 
def main():
    print("Welcome to Trip Splitter :") 
    print("An application that takes the worst parts about plannning a trip and streamlines the process in an organized fashion.")

    mode_selector()
    
    if modes == 1:
    #run Start event functions
        get_event_info()
        get_event_attendees()
        event_item_list()
        event_questionaire()
        event_summary()

    elif modes == 2:
    #run Start trip functions

    elif modes == 3:
    #run Split Bill function
        split_bill()
        print("Each person will have to pay ${:.2f}".format(split_amount))

        returnOp = input("Do you want to return to the main menu [Y/N] :")
    
        if returnOp.upper() == 'Y':
            mode_selector()
        else: 
            print("Invalid option. Please choose a valid mode.")
            mode_selector
        

    elif modes == 4:
    #run Who Pays function

    else: 
        print("Invalid option. Please choose a valid mode.")
        mode_selector()

print("Thank you and enjoy your trip!")




    