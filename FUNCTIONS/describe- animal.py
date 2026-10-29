def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('hamster', 'harry')
describe_pet('Dog', 'Skubidoo')
describe_pet(animal_type='Dog', pet_name='Skubidoo')
describe_pet(pet_name='Skubidoo', animal_type= 'Dog')
