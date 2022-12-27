# -------------------------------
# -- Slice Email --
# -------------------------------

theName = input('what\'s your name?').strip().capitalize()
theEmail = input('what\'s your email?').strip()

theUsername = theEmail[0:theEmail.index("@")]
theDomain = theEmail[theEmail.index("@") + 1:]


print(f"Hello {theName} your Email is {theEmail}")
print(f"your username is {theUsername} \n and your website is {theDomain}")
