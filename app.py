def welcome_message():
    print("Welcome to the Ocean Conservation Interactive App!")
    print("Developed by Bassel")

def quiz():
    print("\nWelcome to the Ocean Conservation Quiz!")
    questions = [
        {
            "question": "What percentage of Earth's surface is covered by oceans?",
            "choices": ["1. 50%", "2. 70%", "3. 90%"],
            "answer": 2,
            "info": "Oceans cover about 70% of Earth's surface."
        },
        {
            "question": "Which is the largest ocean on Earth?",
            "choices": ["1. Atlantic Ocean", "2. Indian Ocean", "3. Pacific Ocean"],
            "answer": 3,
            "info": "The Pacific Ocean is the largest ocean, covering more area than all the land masses combined."
        },
        {
            "question": "How much of the ocean is unexplored?",
            "choices": ["1. 20%", "2. 50%", "3. 80%"],
            "answer": 3,
            "info": "About 80% of the ocean remains unexplored and unmapped."
        }
    ]

    score = 0
    for q in questions:
        print(q["question"])
        for choice in q["choices"]:
            print(choice)
        while True:
            try:
                answer = int(input("Enter the number of your answer: "))
                if answer in [1, 2, 3]:
                    break
                else:
                    print("Please enter a valid number (1, 2, or 3).")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        if answer == q["answer"]:
            score += 1
        print(f"Correct Answer: {q['info']}\n")

    print(f"\nYou scored {score} out of {len(questions)}.")

def marine_life():
    print("\nMarine Life Explorer")
    marine_life_data = [
        {
            "name": "Dolphin",
            "description": "Dolphins are highly intelligent marine mammals known for their agility and playful behavior. They live in groups called pods and communicate using a variety of clicks, whistles, and other vocalizations."
        },
        {
            "name": "Sea Turtle",
            "description": "Sea turtles are ancient marine reptiles that have existed for millions of years. They migrate long distances between feeding grounds and nesting sites and play a crucial role in marine ecosystems by maintaining healthy seagrass beds and coral reefs."
        },
        {
            "name": "Coral Reef",
            "description": "Coral reefs are diverse underwater ecosystems held together by calcium carbonate structures secreted by corals. They support a vast array of marine life and protect coastlines from the effects of wave action and tropical storms."
        },
        {
            "name": "Blue Whale",
            "description": "Blue whales are the largest animals ever known to have lived on Earth. They are baleen whales, using their baleen plates to filter food from the water. Despite their size, they primarily feed on tiny shrimp-like animals called krill."
        },
        {
            "name": "Octopus",
            "description": "Octopuses are highly intelligent invertebrates known for their ability to solve complex problems and escape from enclosures. They have three hearts and blue blood, and their ability to change color and texture helps them camouflage and avoid predators."
        }
    ]

    for species in marine_life_data:
        print(f"\nName: {species['name']}\nDescription: {species['description']}")

def sustainable_practices():
    print("\nSustainable Practices")
    practices = [
        "Reduce single-use plastics by using reusable bags, bottles, and containers.",
        "Support marine conservation organizations through donations or volunteering.",
        "Be mindful of seafood consumption by choosing sustainably sourced options.",
        "Participate in beach cleanups to help remove debris from coastal areas."
    ]

    for practice in practices:
        print(f"- {practice}")

def impact_calculator():
    print("\nImpact Calculator")
    while True:
        try:
            plastic_bags = int(input("Enter the number of plastic bags avoided per week: "))
            plastic_bottles = int(input("Enter the number of plastic bottles avoided per week: "))
            reusable_containers = int(input("Enter the number of reusable containers used per week: "))
            break
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    total_plastic_saved = (plastic_bags + plastic_bottles + reusable_containers) * 52
    print(f"\nBy avoiding single-use plastics, you are saving approximately {total_plastic_saved} plastic items per year from entering the ocean.")

def main():
    welcome_message()
    while True:
        print("\nOcean Conservation Interactive App")
        print("1. Interactive Quiz")
        print("2. Marine Life Explorer")
        print("3. Sustainable Practices")
        print("4. Impact Calculator")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            quiz()
        elif choice == '2':
            marine_life()
        elif choice == '3':
            sustainable_practices()
        elif choice == '4':
            impact_calculator()
        elif choice == '5':
            print("Thank you for using the Ocean Conservation Interactive App!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
