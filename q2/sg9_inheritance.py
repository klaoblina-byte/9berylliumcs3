# Parent Class
class Publication:
    def __init__(self, title: str, author: str):
        self.__title = title # Private attribute for title of the publication
        self.__author = author # Private attribute for author of the publication

    def set_title(self, title: str): # Sets the title of the publication in string format
        self.__title = title

    def set_author(self, author: str): # Sets the author of the publication in string format
        self.__author = author

    def get_title(self): # Gets the title of the publication and returns it as a string
        return self.__title

    def get_author(self): # Gets the author of the publication and returns it as a string
        return self.__author

    def display_info(self): # Functions as the method that displays all the details regarding the publication, namely, its title and the author
        print(f"Title: {self.__title}") # Print the title of the publication 
        print(f"Author: {self.__author}") # Print the author of the publication 

# Child Class 1
class Book(Publication):
    def __init__(self, title: str, author: str, number_pages: int):
        super().__init__(title, author) # Initializes the parent class attributes which are title and author
        self.__number_pages = number_pages # Special private attribute for Book child class

    def set_number_pages(self, number_pages: int): # Sets the number of pages of a book in integer format
        if number_pages <= 0: # Checks if inputted number of pages is valid (greater than 0), if not the function will print a warning and will retain the original number of pages, disregarding the inputted negative value
            print("Warning: Number of pages must be a positive integer.") # Warning for invalid inputs
        else:
            self.__number_pages = number_pages # If inputted number of pages is valid, the function will replace and set the number of pages into the inputted value

    def get_number_pages(self): # Getter method for number of pages
        return self.__number_pages

# Child Class 2
class Magazine(Publication): 
    def __init__(self, title: str, author: str, issue_number: int):
        super().__init__(title, author) # Initializes the parent class attributes are title and author
        self.__issue_number = issue_number # Special private attribute for Magazine child class

    def set_issue_number(self, issue_number: int): # Sets the issue number of a magazine in interger format
        if issue_number <= 0: # Serves as a checkpoint if the inputted issue number is valid (greater than 0), if not the function will print a warning and will retain the original issue number, disregarding the inputted negative value
            print("Warning: Issue number must be a positive integer.") # Printed warning for invalid inputs
        else:
            self.__issue_number = issue_number # If inputted number is valid, the function will replace and set the inputted value as the new issue number

    def get_issue_number(self): # Gets the issue number of a magazine
        return self.__issue_number # Returns the number

# Creating 2 Objects For Each Class
pub1 = Publication("Journal of AI Research", "John Doe")
pub2 = Publication("Science Daily", "Jane Smith")

book1 = Book("Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", 280)
book2 = Book("Hunger Games The Mockingjay", "Suzanne Collins", 400)

mag1 = Magazine("National Geographic", "Various Authors", 209)
mag2 = Magazine("Time", "Various Authors", 99)

# PUBLICATION OUTPUT FOR PUB1
print("Publication Information:")
pub1.display_info()

# Setting new title and author for pub2
pub2.set_title("Science Weekly")
pub2.set_author("Dr. Emily Johnson")
pub2.display_info() # Display updated details of pub2

# BOOK OUTPUT FOR BOOK1
print("\nBook Information:")
book1.set_number_pages(-455) # Update number of pages

print()
book1.display_info()
print(f"Number of pages: {book1.get_number_pages()}")
print()

# Update to a positive value
book1.set_number_pages(455)

book1.display_info() # Display updated details of book1
print(f"Number of pages: {book1.get_number_pages()}")

print()

# BOOK OUTPUT FOR BOOK2
book2.display_info()
print(f"Number of pages: {book2.get_number_pages()}")

# MAGAZINE OUTPUT FOR MAG1
print("\nMagazine Information:")
mag1.display_info()
print(f"Issue number: {mag1.get_issue_number()}")

# MAGAZINE OUTPUT FOR MAG2
mag2.set_issue_number(-208) # Update issue number
print()

mag2.display_info()
print(f"Issue number: {mag2.get_issue_number()}")
print()

# Update issue number of mag2 to a positive value
mag2.set_issue_number(208)

# Display updated details of mag2
mag2.display_info()
print(f"Issue number: {mag2.get_issue_number()}")
print()