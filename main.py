

#Event Details Function
def get_event_info():
    event_name = input("What is the name of the event :")
    event_location = input("Where is this event taking place :")
    event_date = input("Select the date for this event: ")

    print("Set your event configurations!")

    event_cost = input("Are you splitting cost(s) of this event [Y/N] :")
    event_guest = input("Do you want to show attendees of this event [Y/N] :")
    event_guest_items = input("Are your guess bringing items for the event [Y/N] :")


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
    print("Each person will have to pay ${:.2f}".format(split_amount))

    returnOp = input("Do you want to return to the main menu [Y/N] :")
    
    if returnOp.upper() == 'Y':
         main()
    else: 
        print("Invalid option. Please choose a valid mode.")
        main()















def main():
    print("Welcome to Trip Splitter :") 
    print("An application that takes the worst parts about plannning a trip and streamlines the process in an organized fashion.")

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
    