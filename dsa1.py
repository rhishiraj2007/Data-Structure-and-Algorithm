from pyautogui import countdown

def countdown_timer(count):
    if count < 0:
        print("Launching rocket...")
    else:
        print(count)
        countdown_timer(count - 1)

n = int(input("Enter the countdown time in seconds: "))
countdown_timer(n)

        