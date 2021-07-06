import pyautogui, time, os, json, platform
from termcolor import colored

if platform.system() == "Windows":
    clear = "cls"
else:
    clear = "clear"

settings_json_data = json.load(open("settings.json", "r"))
waittime = int(settings_json_data["waittime_in_seconds"])
waittime_after_using_entry = float(settings_json_data["waiting_time_after_filling_entry"])
zoom_file_path = str(settings_json_data["zoom_installation_path"])


def JOIN_ZOOM_MEETING(meetingid, password):
    try:
        os.system(zoom_file_path)
    except:
        exit()

    while True:
        join1 = pyautogui.locateOnScreen("1.png")
        if join1 != None:
            pyautogui.click(join1)
            print(colored("Cliked on the first button", "green"))
            break
        else:
            print(colored(f"Unable to find the first button on screen, Waiting {waittime} seconds and trying again", "red"))
            time.sleep(waittime)
    
    while True:
        join2 = pyautogui.locateOnScreen("2.png")
        if join2 != None:
            pyautogui.click(join2)
            print(colored("Made the input feild active", "green"))

            pyautogui.typewrite(meetingid)
            time.sleep(waittime_after_using_entry)
            print(colored(f"Waiting {waittime_after_using_entry} seconds before clicking the next button", "green"))
            time.sleep(1)

            pyautogui.click(pyautogui.locateOnScreen("3.png"))
            print(colored("Clicked on the second button", "green"))
            break
        else:
            print(colored(f"Unable to find the second window, Waiting {waittime} seconds and trying again", "red"))
            time.sleep(waittime)
    
    while True:
        join2 = pyautogui.locateOnScreen("4.png")
        if join2 != None:
            pyautogui.click(join2)
            print(colored("Made the input feild active", "green"))

            pyautogui.typewrite(password)
            time.sleep(waittime_after_using_entry)
            print(colored(f"Waiting {waittime_after_using_entry} seconds before clicking the next button", "green"))
            time.sleep(1)

            pyautogui.click(pyautogui.locateOnScreen("5.png"))
            print(colored("Clicked on the third button", "green"))
            break
        else:
            print(colored(f"Unable to find the third window, Waiting {waittime} seconds and trying again", "red"))
            time.sleep(waittime)
    

def MAIN_PROGRAM():
    os.system(clear)

    id = input(colored("[+] Enter the Meeting ID: ", "blue"))
    passcode = input(colored("[+] Enter the Meeting Passcode: ", "blue"))
    time.sleep(1)
    print("\n\nStarting the process...")
    
    JOIN_ZOOM_MEETING(id, passcode)


MAIN_PROGRAM()
