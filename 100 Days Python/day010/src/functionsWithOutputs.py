# Function with Outputs
def format_name(f_name, l_name):
    f_name = input("Enter Your Fist Name: ")
    l_name = input("Enter Your Last Name: ")

    print(f_name.title() + " " + l_name.title())

format_name("f_name", "l_name")

# -------------------------- / ------------------------------ # 

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("bAnAnA", "SYrUP"))

# -------------------------- / ------------------------------ # 

# Bypass an empty input
def input_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did'nt provided valid input "
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return (f"result: {formated_f_name} {formated_l_name}")

print(input_name(input("What is your first name? "), input("What is your last name? ")))
