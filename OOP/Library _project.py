from dbm.ndbm import library


class Library:

    def __init__(self, listofbooks):
        self.availablebooks = listofbooks

    def displayAvailablebooks(self):
        print("The books we have in our library are as follows:")
        print("================================================")
        for book in self.availablebooks:
            print(book)
    
    def lendBook(self, requestedbook):
        if requestedbook in self.availablebooks:
            print("The book you requested has now been borrowed")
            self.availablebooks.remove(requestedbook)
        else:
            print("Sorry the book you have requested is currently not in the library")
    
    def addBook(self, returnedbook):
        self.availablebooks.append(returnedbook)
        print("Thanks for returning your borrowed book")

class Student:

    def requestBook(self):
        print("Enter the name of the book you'd like to borrow>>")
        self.book =input()
        return self.book
    
    def returnBook(self):
        print("Enter the name of the book you'd like to return>>")
        self.book = input()
        return self.book

library = Library(["The Last Battle","The Screwtape letters","The Great Divorce"])
student = Student()
done = False
while done == False:
    print("""=====Library Menu=====
    1. Display all available books
    2. Request a book
    3. return a book
    4. Exit
===============================
    """)
    try:
        choice = int(input("Enter Choice:"))
    except:
        print("please choice an option:1, 2, 3, 4")
    if choice == 1:
        library.displayAvailablebooks()
    elif choice == 2:
        library.lendBook(student.requestBook())
    elif choice == 3:
        library.addBook(student.returnBook())
    elif choice == 4:
        print("Thanks for visiting our Library")
        exit()