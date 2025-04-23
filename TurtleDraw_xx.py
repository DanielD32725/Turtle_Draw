import turtle
import math

# Ask the user for the name of the input file
filename = input("Enter the name of the input file: ")

# Try to open and read the input file
try:
    with open(filename, 'r') as file:
        # Create a screen object with the specified dimensions
        screen = turtle.Screen()
        screen.setup(width=450, height=450)

        # Create a turtle object
        my_turtle = turtle.Turtle()

        # Set the turtle to maximum speed
        my_turtle.speed(0)  # 0 is the fastest speed

        # Lift the pen initially to move without drawing
        my_turtle.penup()

        first_point = True  # Flag to track the first movement
        last_position = (0, 0)  # Initial position (origin)
        total_distance = 0  # Variable to track the total distance

        # Read the file line by line
        for line in file:
            line = line.strip()  # Remove any leading or trailing whitespace
            components = line.split()  # Split the line into components

            # Process each line
            if len(components) == 0:
                continue  # Skip empty lines

            command = components[0]

            if command == "stop":
                my_turtle.penup()  # Lift the pen
                continue  # Skip to the next line
            elif command == "color" and len(components) == 2:
                color = components[1]
                my_turtle.pendown()  # Start drawing
                my_turtle.color(color)  # Set the drawing color
            elif command == "move" and len(components) == 3:
                x = int(components[1])
                y = int(components[2])

                # If it's the first point, just move without drawing
                if first_point:
                    my_turtle.goto(x, y)
                    first_point = False
                else:
                    # Calculate the distance between the last position and the new position
                    distance = math.sqrt((x - last_position[0]) ** 2 + (y - last_position[1]) ** 2)
                    total_distance += distance

                    my_turtle.pendown()  # Start drawing from this point
                    my_turtle.goto(x, y)  # Move to the new location

                last_position = (x, y)  # Update the last position

        # Display the total distance at the bottom right
        my_turtle.penup()
        my_turtle.goto(150, -200)  # Move to the bottom right area
        my_turtle.write(f"Total Distance: {total_distance:.2f}", align="center", font=("Arial", 16, "normal"))

        # Close the file properly and wait for the user to press Enter
        input("Press Enter to close the window...")

        # This line prevents the window from closing immediately
        turtle.done()

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
