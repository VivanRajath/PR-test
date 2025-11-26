# Simple Library Management System

books = ["Python Basics", "Machine Learning", "Data Science", "AI Intro"]

print("===== Library System =====")

while True:
    print("\n1. View Books")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Search Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nAvailable Books:")
        for b in books:
            print("-", b)

    elif choice == 2:
        new_book = input("Enter book name to add: ")
        books.append(new_book)
        print("Book added successfully.")

    elif choice == 3:
        remove_book = input("Enter book name to remove: ")
        if remove_book in books:
            books.remove(remove_book)
            print("Book removed.")
        else:
            print("Book not found.")

    elif choice == 4:
        search = input("Enter book name to search: ")
        if search in books:
            print("Book is available.")
        else:
            print("Book not available.")

    elif choice == 5:
        print("Exiting Library System.")
        break

    else:
        print("Invalid choice. Try again.")
