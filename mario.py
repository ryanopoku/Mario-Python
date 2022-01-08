from cs50 import get_int


def main(): #subroutine for main program that is called later
    height = getheight("Height: ")
    drawpyramid(height)



def getheight(prompt): # subroutine that prompts the user for their input
    while True:
        h = get_int(prompt)
        # input needs to be between 1 and 8 to be true
        if h > 0 and h < 9:
            break
    return h


def drawpyramid(rows): # Subroutine draws a pyramid of hashes
    for row in range(1, rows + 1): # Print left pyramid with spaces & hashes
        print(" " * (rows - row) + "#" * row, end="")
        print("  ", end="") # Prints out a  gap of two spaces
        print("#" * row)  # Prints out a  right pyramid consisting of only hashes

if __name__ == "__main__":
    main()
