from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Store work schedule information
work_schedules = []

# Function to input work schedule
def input_schedule():
    name = input("Employee Name: ")
    date = input("Date (YYYY-MM-DD): ")
    start_time = input("Start Time (HH:MM): ")
    end_time = input("End Time (HH:MM): ")
    
    schedule = {
        "name": name,
        "date": date,
        "start_time": start_time,
        "end_time": end_time
    }
    
    work_schedules.append(schedule)
    print("Schedule added.")

# Function to check for conflicts
def check_conflict():
    date = input("Enter the date to check (YYYY-MM-DD): ")
    time_conflicts = []
    
    for schedule in work_schedules:
        if schedule['date'] == date:
            start = datetime.strptime(f"{schedule['date']} {schedule['start_time']}", "%Y-%m-%d %H:%M")
            end = datetime.strptime(f"{schedule['date']} {schedule['end_time']}", "%Y-%m-%d %H:%M")
            
            # Check for conflicts
            for other in work_schedules:
                if other['date'] == date and other != schedule:
                    other_start = datetime.strptime(f"{other['date']} {other['start_time']}", "%Y-%m-%d %H:%M")
                    other_end = datetime.strptime(f"{other['date']} {other['end_time']}", "%Y-%m-%d %H:%M")
                    
                    if (start < other_end and end > other_start):
                        time_conflicts.append((schedule, other))
    
    if time_conflicts:
        print("Conflicts found:")
        for conflict in time_conflicts:
            print(f"{conflict[0]} <-> {conflict[1]}")
    else:
        print("No conflicts found.")

# Function to draw work schedule chart
def draw_schedule_chart():
    names = {}
    
    for schedule in work_schedules:
        name = schedule['name']
        if name not in names:
            names[name] = []
        names[name].append((schedule['date'], schedule['start_time'], schedule['end_time']))
    
    for name, shifts in names.items():
        dates = [s[0] for s in shifts]
        start_times = [s[1] for s in shifts]
        end_times = [s[2] for s in shifts]
        
        plt.figure()
        plt.title(f"Work Schedule for {name}")
        plt.bar(dates, [1]*len(dates), bottom=[int(s[1][:2]) for s in shifts], color='blue', alpha=0.5)
        plt.xlabel('Date')
        plt.ylabel('Shift')
        plt.show()

# Function to count employees by shift
def employee_statistics():
    date = input("Enter the date for statistics (YYYY-MM-DD): ")
    time_slot = input("Enter time slot (8am-12pm, 12pm-4pm, 4pm-8pm, 8pm-11pm): ")
    count = 0
    
    for schedule in work_schedules:
        if schedule['date'] == date:
            start = int(schedule['start_time'][:2])
            end = int(schedule['end_time'][:2])
            if time_slot == "8am-12pm" and 8 <= start < 12:
                count += 1
            elif time_slot == "12pm-4pm" and 12 <= start < 16:
                count += 1
            elif time_slot == "4pm-8pm" and 16 <= start < 20:
                count += 1
            elif time_slot == "8pm-11pm" and 20 <= start < 23:
                count += 1
    
    print(f"Number of employees working the {time_slot} shift on {date}: {count}")

# Main menu
def main_menu():
    while True:
        print("\n--- Work Schedule Management ---")
        print("1. Input Schedule")
        print("2. Check for Conflicts")
        print("3. Draw Employee Work Schedule Chart")
        print("4. Employee Statistics by Shift")
        print("5. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            input_schedule()
        elif choice == '2':
            check_conflict()
        elif choice == '3':
            draw_schedule_chart()
        elif choice == '4':
            employee_statistics()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main_menu()