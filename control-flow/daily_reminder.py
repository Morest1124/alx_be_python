task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


match priority:
    case "high":
        priority_message = "high priority task"
        if time_bound == "yes":
            reminder = f"'{task}' is a {priority_message} that requires immediate attention today!"
        else:
            reminder = f"Note: '{task}' is a {priority_message}. It's recommended to complete it as soon as possible."
    case "medium":
        priority_message = "medium priority task"
        if time_bound == "yes":
            reminder = f"'{task}' is a {priority_message} that requires attention today!"
        else:
            reminder = f"Note: '{task}' is a {priority_message}. Consider completing it within a reasonable timeframe."
    case "low":
        priority_message = "low priority task"
        if time_bound == "yes":
            reminder = f"'{task}' is a {priority_message} that requires attention today!"
        else:
            reminder = f"Note: '{task}' is a {priority_message}. Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level. Please try again."


print("Reminder:", reminder)
