import time
import src.constants as cs

# Function to print a line with color transition
def print_colored_line(text, color1, color2):
    print(f"\033[{color1}m{text}\033[{color2}m")

# Function to print a line with padding from top and left
def print_padded_line(text, padding_top, padding_left):
    for _ in range(padding_top):
        print()

    print(f"{' ' * padding_left}{text}")

# VisionX ASCII art with color transition and padding
def intro():
    # Clear the screen
    print("\033c", end="")

    print_padded_line("", 2, 4)

    print_colored_line("@@           @@    @@@@@@@@    @@@@      @@    @@          @@    ", "34", "36")
    print_colored_line(" @@         @@     @@          @@ @@     @@      @@      @@    ", "32", "35")
    print_colored_line("  @@       @@      @@          @@  @@    @@        @@  @@     ", "33", "34")
    print_colored_line("   @@     @@       @@@@@@@@    @@   @@   @@          @@     ", "36", "31")
    print_colored_line("    @@   @@        @@          @@    @@  @@        @@  @@     ", "35", "33")
    print_colored_line("     @@ @@         @@          @@     @@ @@      @@      @@    ", "34", "36")
    print_colored_line("      @@@          @@@@@@@@    @@      @@@@    @@          @@    ", "34", "36")
    print("\033[0m")
    print()
    print()

    # Author, Version, and GitHub reference
    print("\033[1;36m")
    print(f"Version: {cs.version}")
    print("\033[0m")
    print("\033[1;33m")
    print("Author: martian58")
    print("GitHub: https://github.com/martian58")
    print("\033[0m")

    print("\033[1;33m")
    print("Welcome to VisionX, a powerful tool crafted for your visionary needs!")
    time.sleep(0.3)
    print("VisionX empowers you with cutting-edge capabilities, but remember:")
    print("Use it responsibly and never for malicious purposes!")
    print("\033[0m")
    time.sleep(0.3)
    print()
    print()

# Assuming cs.version is defined in your constants module
# Call the intro function
intro()
