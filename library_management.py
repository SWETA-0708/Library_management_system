class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def print_all_books(self):
        if self.no_of_books == 0:
            print("No books in the library.")
        else:
            print("All books in the library:")
            for book in self.books:
                print(book)

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books += 1
        print(f"Book '{book}' added successfully.")

    def get_no_of_books(self):
        return self.no_of_books


# Program to demonstrate the Library class
def main():
    library = Library()

    while True:
        print("\nMenu:")
        print("1. Print all books")
        print("2. Add a book")
        print("3. Get the number of books")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            library.print_all_books()
        elif choice == '2':
            book_name = input("Enter the name of the book to add: ")
            library.add_book(book_name)
        elif choice == '3':
            num_books = library.get_no_of_books()
            print(f"Number of books in the library: {num_books}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
