# ------------------------------
# -- Advanced Age Calculator ---
# ------------------------------

print("#" * 80)
print(" You can write the first letter or full name of the time unit ".center(80, '#'))
print("#" * 80)

# Collect age data
age = int(input("please enter your age").strip())

# Collect time units data
unit = input("Please choose time unit: months, weeks, days").strip().lower()

# Get time units
months = int(age) * 12
weeks = months * 4
days = age * 365

if unit == 'months' or unit == 'm':
    print(f"you lived for {months:,} months.")
elif unit == 'weeks' or unit == 'w':
    print(f"you lived for {weeks:,} weeks.")
elif unit == 'days' or unit == 'd':
    print(f"you lived for {days:,} days.")       
