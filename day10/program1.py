def format_name(f_name, l_name):
    """
    formats the name to title case.
    input:  first_name and last_name
    output: first_name and last_name in title case.
    """
    if f_name == "" or l_name == "":
        # return
        return "You didn't provide a valid input."
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))