pi = 3.14159

def is_number(input_string):
    if input_string == "":
        return False
    dot_count = 0
    for i in range(len(input_string)):
        character = input_string[i]
        if character == '.':
            dot_count += 1
            if dot_count > 1:
                return False
        elif character == '-' and i == 0:
            continue
        elif character < '0' or character > '9':
            return False
    return True

def super_ai_circle_helper():
    print(">>> Circle Helper <<<\n")
    print("I can calculate the following for a circle:")
    print("1. Distance from middle to edge (radius)")
    print("2. Edge length around the circle (circumference)")
    print("3. Area of the circle\n")
    
    print("Instructions:")
    print("- Choose what you know: distance, edge, or area.")
    print("- Then type the number for what you know.")
    print("- If you don't have a real circle, just pick a number to explore:")
    print("    Example: 5 → small circle")
    print("    Example: 20 → medium circle")
    print("    Example: 100 → huge circle")
    print("- Type 'quit' anytime to exit.\n")

    while True:
        print("Reminder: type 'distance', 'edge', or 'area' (or 'quit').")
        print("Pick a number to explore if you don't have a real circle.")

        user_choice = input("What do you know? (distance / edge / area or 'quit'): ").lower()
        
        if user_choice == "quit":
            print(">>> Goodbye! <<<")
            break

        distance_from_center = 0
        edge_length_of_circle = 0
        area_of_circle = 0
        input_is_valid = False

        if user_choice == "distance":
            user_input = input("Enter the distance from middle to edge: ")
            if is_number(user_input):
                distance_from_center = float(user_input)
                edge_length_of_circle = 2 * pi * distance_from_center
                area_of_circle = pi * distance_from_center * distance_from_center
                input_is_valid = True
            else:
                print("Please type a valid number!\n")
        else:
            if user_choice == "edge":
                user_input = input("Enter the edge length: ")
                if is_number(user_input):
                    edge_length_of_circle = float(user_input)
                    distance_from_center = edge_length_of_circle / (2 * pi)
                    area_of_circle = pi * distance_from_center * distance_from_center
                    input_is_valid = True
                else:
                    print("Please type a valid number!\n")
            else:
                if user_choice == "area":
                    user_input = input("Enter the area: ")
                    if is_number(user_input):
                        area_of_circle = float(user_input)
                        distance_from_center = (area_of_circle / pi) ** 0.5
                        edge_length_of_circle = 2 * pi * distance_from_center
                        input_is_valid = True
                    else:
                        print("Please type a valid number!\n")
                else:
                    print("Sorry, I didn't understand. Type distance, edge, area, or quit.\n")

        if input_is_valid:
            # Determine size description
            if distance_from_center < 1:
                circle_size_description = "This circle is very tiny."
            elif distance_from_center < 10:
                circle_size_description = "This is a small circle."
            elif distance_from_center < 50:
                circle_size_description = "This is a medium circle."
            else:
                circle_size_description = "This is a huge circle."

            if area_of_circle > edge_length_of_circle:
                circle_size_description += " The area is bigger than the edge length."
            else:
                circle_size_description += " The edge length is bigger than the area, as normal."

            # Round values for display
            if distance_from_center < 1:
                distance_rounded = round(distance_from_center, 6)
                edge_rounded = round(edge_length_of_circle, 6)
                area_rounded = round(area_of_circle, 6)
            elif distance_from_center < 100:
                distance_rounded = round(distance_from_center, 4)
                edge_rounded = round(edge_length_of_circle, 4)
                area_rounded = round(area_of_circle, 4)
            else:
                distance_rounded = round(distance_from_center, 2)
                edge_rounded = round(edge_length_of_circle, 2)
                area_rounded = round(area_of_circle, 2)

            # Show results
            print("\n[RESULTS]")
            print("Distance from middle ->", distance_rounded)
            print("Edge length ->", edge_rounded)
            print("Area ->", area_rounded)
            print("\n[NOTES]")
            print(circle_size_description)
            print("\n>>> Done! Type 'quit' to exit or try another value.\n")

super_ai_circle_helper()