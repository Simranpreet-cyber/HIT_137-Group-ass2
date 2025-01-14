import turtle


##Calling the turtle module

def draw_branch(t, starting_branch_length, left_angle, right_angle, recursion_depth, reduction_factor):
    if recursion_depth == 0:
        return

    t.pensize(5)
    t.speed(0)

    t.forward(starting_branch_length)

    t.left(left_angle)
    draw_branch(t, starting_branch_length * reduction_factor, left_angle, right_angle, recursion_depth - 1,
                reduction_factor)
    t.right(left_angle)

    t.right(right_angle)
    draw_branch(t, starting_branch_length * reduction_factor, left_angle, right_angle, recursion_depth - 1,
                reduction_factor)
    t.left(right_angle)

    t.backward(starting_branch_length)


def main():  # Setting up the main function with the parameters and turtle environment
    t = turtle.Turtle()
    screen = turtle.Screen()

    left_angle = float(input("Enter the angle for the left branch: "))
    right_angle = float(input("Enter the angle for the right branch: "))
    starting_branch_length = float(input("Enter the starting branch length: "))
    recursion_depth = float(input("Enter the recursion depth: "))
    reduction_factor = float(input("Enter the reduction factor (e.g. 0.6): "))

    # Setting up the turtle environment
    t.color("green")
    t.penup()
    t.goto(0, -200)
    t.left(90)
    t.pendown()

    # Drawing the branches
    draw_branch(t, starting_branch_length, left_angle, right_angle, recursion_depth, reduction_factor)

    screen.mainloop()


if __name__ == "__main__":
    main()