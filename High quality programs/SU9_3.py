##Tebatso_Seshayi

email_ad = input("Enter your email address: ")
name = " "
domain = " "
f = False
for char in email_ad:
    f = True
    if char == "@":
        f = True
    elif f:
        domain += char
    else:
        name += char
print("The name is ",name)
print("The domain of the email is", domain)
