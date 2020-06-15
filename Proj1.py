import os,sys
class library:
    def __init__(self,list_of_books,library_name):
        self.name=library_name
        self.books=list_of_books
        self.lending_dictionary={}
    def display_books(self):
        print(f"List of Books : {self.books}")
    def lend_book(self):
        self.lended_book=input("Enter Book Name  : ")
        if self.lended_book in self.books:
            self.lender_name=input("Enter Your Name : ")
            self.lending_records(self.lended_book,self.lender_name)
        else:
            print("Book Not Available in Stock !!")
    def donate_book(self):
        self.donated_book=input("Enter Book Name : ")
        self.books.append(self.donated_book)
        print("Book Successfully Donated !!")
    def return_book(self):
        self.returner_name=input("Enter Name on whose name book was issued : ")
        if self.returner_name in self.lending_dictionary.values():
            returner_book=input("Enter Issued Book Name : ")
            self.lending_dictionary.pop(returner_book)
            self.books.append(returner_book)
            print("Book Successfully Returned !! ")
        else:
            print("Book Not Returned !!")
    def lending_records(self,temp_book,temp_lender):
        self.lending_dictionary[temp_book]=temp_lender
        self.books.remove(temp_book)
def __main__():
    book_list=["C","C++","Python","Java","Kotlin","Go Lang","Erlang","Javascript","HTML","CSS","MySQL"]
    Sarwar=library(book_list,"Sarwar's Library Management System")
    while(1):
        os.system("cls")
        print("1.Display List Of Books")
        print("2.Lend a Book")
        print("3.Donate a Book")
        print("4.Return a Book")
        print("5.Lending Records")
        print("6.Exit")
        choice=int(input("Enter Your Choice : "))
        if choice==1:
            Sarwar.display_books()
        elif choice==2:
            Sarwar.lend_book()
        elif choice==3:
            Sarwar.donate_book()
        elif choice==4:
            Sarwar.return_book()
        elif choice==5:
            print(f"Lended Book Records : {Sarwar.lending_dictionary}")
        elif choice==6:
            sys.exit("Bye Bye !!")
        else:
            print("Invalid Choice !!")
__main__()
