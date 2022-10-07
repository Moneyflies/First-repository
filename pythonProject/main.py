# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Use a breakpoint in the code line below to debug your script.
# Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
email = (input("Enter your email: ").lower()).strip().replace(" ", "")
username = email[:email.index('@')]
domain = email[(email.index('@') + 1):]
print(email.index('@'))
print(domain)
print(username)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
