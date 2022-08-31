def input_name(f_name, l_name):
    """Take the first and last name and format it to return the title case 
    version of the name """
    if f_name == "" or l_name == "":
        return "You did'nt provided valid input "
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return (f"result: {formated_f_name} {formated_l_name}")
    


