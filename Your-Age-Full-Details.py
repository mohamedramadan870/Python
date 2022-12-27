# -------------------------------------
# -- Practical Your Age Full Details --
# -------------------------------------

# Input Age
age = int(input("What\'s your age? "))

# Get Age in All Time Units
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print("You lived for:")
print(f"{months} months.")
print(f"{weeks:,} weeks.")
print(f"{days:,} days.")
print(f"{hours:,} hours.")
print(f"{minutes:,} minutes.")
print(f"{seconds:,} seconds.")