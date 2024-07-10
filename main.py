# https://mycourses.csp.edu/content/enforced/9016-35437.202430/csfiles/home_dir/courses/CSC422_OL_TER_PRIMARY/READ_ONLY/question/_6328078_1/embedded/CSC%20422%20Assignment%202%20Part%202.pdf

class Pet:
    # pet class with name and age as the attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PetDatabase:
    # list of pets
    def __init__(self):
        self.pets = []
        self.load_pets() # calling load pets to load initial values from the txt file

    def load_pets(self):
        # load pets from the file
        try:
            with open('pets.txt', 'r') as file:
                for line in file:
                    name, age = line.strip().split(',')
                    self.pets.append(Pet(name, int(age)))
                print('Pets loaded from pets.txt')
        except FileNotFoundError:
            print("pets.txt not found, starting with an empty database.")
        except Exception as e:
            print(f"An error occurred while loading pets: {e}")

    def save_pets(self):
        # save pets to the pets.txt file
        try:
            with open('pets.txt', 'w') as file: # we are re-writing the file every time, though the data is preserved
                for pet in self.pets:
                    file.write(f"{pet.name},{pet.age}\n")
        except Exception as e:
            print(f"An error occurred while saving pets: {e}")

    def add_pets(self):
        # to add pets to the list
        while True:
            pet_info = input("Add pet (name, age): ")
            if pet_info.lower() == "done":
                break
            try:
                # splitting the input into name and age
                name, age = pet_info.split()
                age = int(age)
                self.pets.append(Pet(name, age)) #creating pet and adding to the list from user input
            except ValueError:
                # non integer age or invalid format error
                print("Invalid input. Please enter a name and an integer age.")

    def search_by_name(self):
        # search by name : takes name cleans it (strip and to lower case) and search in existing pets
        search_name = input("Enter a name to search: ").strip().lower()
        found_pets = [pet for pet in self.pets if pet.name.lower() == search_name] # is a list of 0 to len(pets)
        if found_pets:
            self.display_search_results(found_pets)
        else:
            print("No pets named '{}' in the list. Try adding new.".format(search_name))

    def search_by_age(self):
        # searching bets by age
        try:
            search_age = int(input("Enter pet's age to search: ").strip()) # strip space and convert to int
            found_pets = [pet for pet in self.pets if pet.age == search_age]
            if found_pets:
                self.display_search_results(found_pets)
            else:
                print("No pets with the age '{}'.".format(search_age))
        except ValueError:
            print("Age should be an integer")

    def display_search_results(self, found_pets=None):
        # takes list and displays, removes the need for view_pets by taking default parameter for found pets
        if found_pets is None:
            found_pets = self.pets
        print("+----------------------+")
        print("| ID | NAME      | AGE |")
        print("+----------------------+")
        for i, pet in enumerate(found_pets):
            print("| {:<2} | {:<10} | {:<3} |".format(i, pet.name, pet.age))
        print("+----------------------+")
        print("{} rows in set.".format(len(found_pets)))

    def edit_pet(self):
        # to edit a pet's details
        try:
            pet_id = int(input("Enter the ID of the pet to edit: "))
            if 0 <= pet_id < len(self.pets):
                new_name = input("Enter new name: ").strip()
                new_age = int(input("Enter new age: "))
                self.pets[pet_id].name = new_name
                self.pets[pet_id].age = new_age
                print("Pet details updated successfully.")
            else:
                print("Invalid ID.")
        except ValueError:
            print("Please enter a valid ID and age.")
            
    def remove_pet(self):
        # to remove a pet from the list
        try:
            pet_id = int(input("Enter the ID of the pet to remove: "))
            if 0 <= pet_id < len(self.pets):
                self.pets.pop(pet_id)
                print("Pet removed successfully.")
            else:
                print("Invalid ID. Should be in the range 0 - {}".format(len(self.pets)))
        except ValueError:
            print("Please enter a valid ID")

def main():
    database = PetDatabase() #initialising the database
    while True:
        print("What would you like to do?")
        print("1) View all pets")
        print("2) Add more pets")
        print("3) Update an existing pet")
        print("4) Remove an existing pet")
        print("5) Search pets by name")
        print("6) Search pets by age")
        print("7) Save and exit program")
        choice = input("Your choice: ")

        if choice == '1':
            database.display_search_results()
        elif choice == '2':
            database.add_pets()
        elif choice == '3':
            database.edit_pet()
        elif choice == '4':
            database.remove_pet()
        elif choice == '5':
            database.search_by_name()
        elif choice == '6':
            database.search_by_age()
        elif choice == '7':
            database.save_pets() # added call to save_pets
            print("Goodbye!")
            break
        else:
            # handling invalid menu choices
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

# references
# https://www.geeksforgeeks.org/enumerate-in-python/