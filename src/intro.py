import time,string,random
import src.constants as cs
class intro:
    def __init__(self):
        self
    def print_colored_line(self,text, color1, color2):
        print(f"\033[{color1}m{text}\033[{color2}m")

    def print_padded_line(self,text, padding_top, padding_left):
        for _ in range(padding_top):
            print()

        print(f"{' ' * padding_left}{text}")

    def print_colored_lines(self):
        self.print_colored_line("__        __   ______    ___     _   __   __ ", "31", "36")
        time.sleep(0.2)
        self.print_colored_line("\▄\      /▄/  |▄ ▄_▄_|  |▄ ▄\   |▄|  \▄\ /▄/ ", "32", "35")
        time.sleep(0.2)
        self.print_colored_line(" \▄\    /▄/   |▄|____   |▄|\▄\  |▄|   \▄/▄/ ", "33", "34")
        time.sleep(0.2)
        self.print_colored_line("  \▄\  /▄/    |▄ ▄_▄_|  |▄| \▄\ |▄|    /▄/\ ", "34", "31")
        time.sleep(0.2)
        self.print_colored_line("   \▄\/▄/     |▄|____   |▄|  \▄\|▄|   /▄/\▄\ ", "35", "33")
        time.sleep(0.2)
        self.print_colored_line("    \▄▄/      |▄_▄_▄_|  |▄|   \▄_▄|  /▄/  \▄\ ", "36", "31")
        print("\033[0m")
        print()
        print()

    def intro(self):
        self.print_padded_line("", 2, 4)

        self.print_colored_lines()

        print("\033[1;35m")
        print(f"VisionX - Version {cs.version}")
        print("\033[0m")
        print("\033[1;33m")
        print("Author: martian58")
        print("GitHub: https://github.com/martian58")
        print("\033[0m")
        print("\033[1;33m")
        print("Welcome to VisionX, your creative companion!")
        time.sleep(0.3)
        print("Unleash your imagination responsibly and innovate fearlessly!")
        print("\033[0m")
        print()

class intro2:
    def __init__(self):
        self
        
    def print_colored_line(self,text, color1, color2):
        print(f"\033[{color1}m{text}\033[{color2}m")

    # Function to print a line with padding from top and left
    def print_padded_line(self,text, padding_top, padding_left):
        for _ in range(padding_top):
            print()

        print(f"{' ' * padding_left}{text}")

    # VisionX ASCII art with color transition and padding
    def intro(self):
        # Clear the screen
        print("\033c", end="")

        self.print_padded_line("", 2, 4)

        self.print_colored_line("__        __   ______    ___     _   __   __ ", "34", "36")
        time.sleep(0.2)
        self.print_colored_line("\ \      / /  |  ____|  |   \   | |  \ \ / / ", "32", "35")
        time.sleep(0.2)
        self.print_colored_line(" \ \    / /   | |____   | |\ \  | |   \ / / ", "33", "34")
        time.sleep(0.2)
        self.print_colored_line("  \ \  / /    |  ____|  | | \ \ | |    / /\ ", "36", "31")
        time.sleep(0.2)
        self.print_colored_line("   \ \/ /     | |____   | |  \ \| |   / /\ \ ", "35", "33")
        time.sleep(0.2)
        self.print_colored_line("    \__/      |______|  |_|   \___|  /_/  \_\ ", "34", "36")
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

class intro3:
    def __init__(self):
        self
        # Function to print a line with color transition
    def print_colored_line(self,text, color1, color2):
        print(f"\033[{color1}m{text}\033[{color2}m")

    # Function to print a line with padding from top and left
    def print_padded_line(self,text, padding_top, padding_left):
        for _ in range(padding_top):
            print()

        print(f"{' ' * padding_left}{text}")

    # VisionX ASCII art with color transition and padding
    def intro(self):
        # Clear the screen
        print("\033c", end="")

        self.print_padded_line("", 2, 4)

        self.print_colored_line(" __             _______   ___     _    __    __ ", "34", "36")
        time.sleep(0.2)
        self.print_colored_line("\██         ██ |███████  |████    ██  \██   /██ ", "32", "35")
        time.sleep(0.2)
        self.print_colored_line(" \██       ██  |██       |██\██   ██   \██ /██ ", "33", "34")
        time.sleep(0.2)
        self.print_colored_line("  \██     ██   |███████  |██ \██  ██     /██ ", "36", "31")
        time.sleep(0.2)
        self.print_colored_line("   \██   ██    |██       |██  \██ ██   /██ \██  ", "35", "33")
        time.sleep(0.2)
        self.print_colored_line("    \██▄██     |███████  |██   \████  /██   \██ ", "34", "36")
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

class intro4:
    def __init__(self):
        self

    # Function to print a line with color transition
    def print_colored_line(self,text, color1, color2):
        print(f"\033[{color1}m{text}\033[{color2}m")

    # Function to print a line with padding from top and left
    def print_padded_line(self,text, padding_top, padding_left):
        for _ in range(padding_top):
            print()

        print(f"{' ' * padding_left}{text}")

    # VisionX ASCII art with color transition and padding
    def intro(self):
        # Clear the screen
        print("\033c", end="")

        self.print_padded_line("", 2, 4)

        self.print_colored_line("&&           &&    &&&&&&&&    &&&&      &&    &&          &&    ", "34", "36")
        time.sleep(0.2)
        self.print_colored_line(" &&         &&     &&          && &&     &&      &&      &&    ", "32", "35")
        time.sleep(0.2)
        self.print_colored_line("  &&       &&      &&          &&  &&    &&        &&  &&     ", "33", "34")
        time.sleep(0.2)
        self.print_colored_line("   &&     &&       &&&&&&&&    &&   &&   &&          &&     ", "36", "31")
        time.sleep(0.2)
        self.print_colored_line("    &&   &&        &&          &&    &&  &&        &&  &&     ", "35", "33")
        time.sleep(0.2)
        self.print_colored_line("     && &&         &&          &&     && &&      &&      &&    ", "34", "36")
        time.sleep(0.2)
        self.print_colored_line("      &&&          &&&&&&&&&   &&      &&&&    &&          &&    ", "34", "36")
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

class intro5:
    def __init__(self):
        self
    # Function to print a line with color transition
    def print_colored_line(self,text, color1, color2):
        print(f"\033[{color1}m{text}\033[{color2}m")

    # Function to print a line with padding from top and left
    def print_padded_line(self,text, padding_top, padding_left):
        for _ in range(padding_top):
            print()

        print(f"{' ' * padding_left}{text}")

    # VisionX ASCII art with color transition and padding
    def intro(self):
        # Clear the screen
        print("\033c", end="")

        self.print_padded_line("", 2, 4)

        self.print_colored_line("@@           @@    @@@@@@@@    @@@@      @@    @@          @@    ", "34", "36")
        time.sleep(0.2)
        self.print_colored_line(" @@         @@     @@          @@ @@     @@      @@      @@    ", "32", "35")
        time.sleep(0.2)
        self.print_colored_line("  @@       @@      @@          @@  @@    @@        @@  @@     ", "33", "34")
        time.sleep(0.2)
        self.print_colored_line("   @@     @@       @@@@@@@@    @@   @@   @@          @@     ", "36", "31")
        time.sleep(0.2)
        self.print_colored_line("    @@   @@        @@          @@    @@  @@        @@  @@     ", "35", "33")
        time.sleep(0.2)
        self.print_colored_line("     @@ @@         @@          @@     @@ @@      @@      @@    ", "34", "36")
        time.sleep(0.2)
        self.print_colored_line("      @@@          @@@@@@@@    @@      @@@@    @@          @@    ", "34", "36")
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

class intro6:
    def __init__(self):
        self
    # Function to print a line with color transition
    def print_colored_line(self,text, color1, color2):
        print(f"\033[{color1}m{text}\033[{color2}m")

    # Function to print a line with padding from top and left
    def print_padded_line(self,text, padding_top, padding_left):
        for _ in range(padding_top):
            print()

        print(f"{' ' * padding_left}{text}")

    # VisionX ASCII art with color transition and padding
    def intro(self):
        # Clear the screen
        print("\033c", end="")

        self.print_padded_line("", 2, 4)

        self.print_colored_line("77           77    77777777    7777      77    77          77    ", "34", "36")
        time.sleep(0.2)
        self.print_colored_line(" 77         77     77          77 77     77      77      77    ", "32", "35")
        time.sleep(0.2)
        self.print_colored_line("  77       77      77          77  77    77        77  77     ", "33", "34")
        time.sleep(0.2)
        self.print_colored_line("   77     77       77777777    77   77   77          77     ", "36", "31")
        time.sleep(0.2)
        self.print_colored_line("    77   77        77          77    77  77        77  77     ", "35", "33")
        time.sleep(0.2)
        self.print_colored_line("     77 77         77          77     77 77      77      77    ", "34", "36")
        time.sleep(0.2)
        self.print_colored_line("      777          77777777    77      7777    77          77    ", "34", "36")
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

class intro7:
    def __init__(self):
        self
    # Function to print a line with color transition
    def print_colored_line(self,text, color1, color2):
        print(f"\033[{color1}m{text}\033[{color2}m")

    # Function to print a line with padding from top and left
    def print_padded_line(self,text, padding_top, padding_left):
        for _ in range(padding_top):
            print()

        print(f"{' ' * padding_left}{text}")

    # VisionX ASCII art with color transition and padding
    def intro(self):
        # Clear the screen
        print("\033c", end="")

        self.print_padded_line("", 2, 4)

        self.print_colored_line("OO           OO    OOOOOOOO    OOOO      OO    OO          OO    ", "34", "36")
        time.sleep(0.2)
        self.print_colored_line(" OO         OO     OO          OO OO     OO      OO      OO    ", "32", "35")
        time.sleep(0.2)
        self.print_colored_line("  OO       OO      OO          OO  OO    OO        OO  OO     ", "33", "34")
        time.sleep(0.2)
        self.print_colored_line("   OO     OO       OOOOOOOO    OO   OO   OO          OO     ", "36", "31")
        time.sleep(0.2)
        self.print_colored_line("    OO   OO        OO          OO    OO  OO        OO  OO     ", "35", "33")
        time.sleep(0.2)
        self.print_colored_line("     OO OO         OO          OO     OO OO      OO      OO    ", "34", "36")
        time.sleep(0.2)
        self.print_colored_line("      OOO          OOOOOOOOO   OO      OOOO    OO          OO    ", "34", "36")
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


class intro8:
    def __init__(self):
        self
    # Function to print a line with color transition
    def print_colored_line(self,text, color1, color2):
        print(f"\033[{color1}m{text}\033[{color2}m")

    # Function to print a line with padding from top and left
    def print_padded_line(self,text, padding_top, padding_left):
        for _ in range(padding_top):
            print()

        print(f"{' ' * padding_left}{text}")

    # VisionX ASCII art with color transition and padding
    def intro(self):
        # Clear the screen
        print("\033c", end="")

        self.print_padded_line("", 2, 4)

        self.print_colored_line("WW           WW    WWWWWWWW    WWWW      WW    WW          WW    ", "34", "36")
        time.sleep(0.2)
        self.print_colored_line(" WW         WW     WW          WW WW     WW      WW      WW    ", "32", "35")
        time.sleep(0.2)
        self.print_colored_line("  WW       WW      WW          WW  WW    WW        WW  WW     ", "33", "34")
        time.sleep(0.2)
        self.print_colored_line("   WW     WW       WWWWWWWW    WW   WW   WW          WW     ", "36", "31")
        time.sleep(0.2)
        self.print_colored_line("    WW   WW        WW          WW    WW  WW        WW  WW     ", "35", "33")
        time.sleep(0.2)
        self.print_colored_line("     WW WW         WW          WW     WW WW      WW      WW    ", "34", "36")
        time.sleep(0.2)
        self.print_colored_line("      WWW          WWWWWWWWW   WW      WWWW    WW          WW    ", "34", "36")
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

class intro9:
    def __init__(self):
        self
    # Function to print a line with color transition
    def print_colored_line(self,text, color1, color2):
        print(f"\033[{color1}m{text}\033[{color2}m")

    # Function to print a line with padding from top and left
    def print_padded_line(self,text, padding_top, padding_left):
        for _ in range(padding_top):
            print()

        print(f"{' ' * padding_left}{text}")

    # VisionX ASCII art with color transition and padding
    def intro(self):
        # Clear the screen
        print("\033c", end="")

        self.print_padded_line("", 2, 4)

        self.print_colored_line("%%           %%    %%%%%%%%    %%%%      %%    %%          %%    ", "34", "36")
        time.sleep(0.2)
        self.print_colored_line(" %%         %%     %%          %% %%     %%      %%      %%    ", "32", "35")
        time.sleep(0.2)
        self.print_colored_line("  %%       %%      %%          %%  %%    %%        %%  %%     ", "33", "34")
        time.sleep(0.2)
        self.print_colored_line("   %%     %%       %%%%%%%%    %%   %%   %%          %%     ", "36", "31")
        time.sleep(0.2)
        self.print_colored_line("    %%   %%        %%          %%    %%  %%        %%  %%     ", "35", "33")
        time.sleep(0.2)
        self.print_colored_line("     %% %%         %%          %%     %% %%      %%      %%    ", "34", "36")
        time.sleep(0.2)
        self.print_colored_line("      %%%          %%%%%%%%%   %%      %%%%    %%          %%    ", "34", "36")
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

class intro10:
    def __init__(self):
        self
        self.chars = []
        # Add uppercase characters
        self.chars.extend(list(string.ascii_uppercase))

        # Add special characters
        self.chars.extend(list(string.punctuation))
        self.rnd_char=random.choice(self.chars)
    # Function to print a line with color transition
    def print_colored_line(self,line, foreground_color, background_color):

        modified_line = line.replace('@', self.rnd_char)
        print(f"\033[{foreground_color};{background_color}m{modified_line}\033[0m")

    # Function to print a line with padding from top and left
    def print_padded_line(self,text, padding_top, padding_left):
        for _ in range(padding_top):
            print()

        print(f"{' ' * padding_left}{text}")

    # VisionX ASCII art with color transition and padding
    def intro(self):
        # Clear the screen
        print("\033c", end="")

        self.print_padded_line("", 2, 4)

        self.print_colored_line("@@           @@    @@@@@@@@    @@@@      @@    @@          @@    ", "34", "36")
        time.sleep(0.2)
        self.print_colored_line(" @@         @@     @@          @@ @@     @@      @@      @@    ", "32", "35")
        time.sleep(0.2)
        self.print_colored_line("  @@       @@      @@          @@  @@    @@        @@  @@     ", "33", "34")
        time.sleep(0.2)
        self.print_colored_line("   @@     @@       @@@@@@@@    @@   @@   @@          @@     ", "36", "31")
        time.sleep(0.2)
        self.print_colored_line("    @@   @@        @@          @@    @@  @@        @@  @@     ", "35", "33")
        time.sleep(0.2)
        self.print_colored_line("     @@ @@         @@          @@     @@ @@      @@      @@    ", "34", "36")
        time.sleep(0.2)
        self.print_colored_line("      @@@          @@@@@@@@    @@      @@@@    @@          @@    ", "34", "36")
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