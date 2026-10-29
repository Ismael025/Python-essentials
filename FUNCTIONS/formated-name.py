def get_formated_name(f_Name, l_Name):
    
    full_Name = f_Name +' '+ l_Name
    return full_Name

while True:
    print("\n enter your names:")
    f_Name = input("Your first name:")
    if f_Name == 'q':
        break
    l_Name = input('Your last name:')
    if l_Name == 'q':
        break
    formated_Name = get_formated_name(f_Name, l_Name)
    print(f"Hello, {formated_Name} !")