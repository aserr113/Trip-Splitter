def main():
    print("Welcome to Trip Splitter :") 
    print("An application that takes the worst parts about plannning a trip and streamlines the process in an organized fashion.")

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