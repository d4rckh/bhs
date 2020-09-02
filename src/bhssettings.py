import src.util.bcolors as bc

prompt = f"{bc.LightCyan}T: {bc.NC} {bc.Green}(target){bc.NC} {bc.LightPurple}% {bc.NC} "


dirbustCommand = ["python3", "/home/d4rckh/Desktop/dirsearch/dirsearch.py", "-u", "http://(target)", "-w", 
                    "/home/d4rckh/Desktop/bhs/wordlist",
                    "-e", "php,txt,zip"]