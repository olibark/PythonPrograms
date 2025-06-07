import time
import os



def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_clock_with_alarm(alarm_time):
    """Displays the clock and checks for alarm time."""
    try:
        while True:
            clear_screen()
            current_time = time.strftime("%H:%M:%S")  # Format: HH:MM:SS
            print(f"Current Time: {current_time}")

            # Check if the current time matches the alarm time
            if current_time == alarm_time:
                print("\n⏰ Alarm! Wake up!")
                for i in range (100):
                    print ("WAKE UP!! ")

                break  # Exit the loop when the alarm goes off
            
            time.sleep(1)  # Wait for 1 second before updating
    except KeyboardInterrupt:
        print("\nClock stopped.")

if __name__ == "__main__":
    alarm_time = input("When would you like to be awoken? (HH:MM:SS): ").strip()
    display_clock_with_alarm(alarm_time)