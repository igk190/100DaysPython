year = int(input("What's your year of birth?"))

if year > 1980 and year <= 1994: # AND equal to, otherwise it skips over 1994
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
else:
    print("Damn you are sth different.")
