class Book: 
        # def __init__ initalise the attributes of an objects
        def __init__(self, title, author, pages, current_page):
            self.title = title
            self.author = author
            self.pages = pages
            self.current = current_page
            self.bookmark = 1
            # bookmark is not in the above but it can be defined here
#             self.boolean = True
#             # change true to move forward or false to move backwards 
#             # self.boolean = boolean
        
        # current book page 
        def bookmark_page(self):
            self.bookmark = self.current
            
        # turning to the next page from the current page , hence + 1    
        def turn_page(self):
            self.current += 1
        
        # turning back one page from the current page, -1
        def back_page(self):
            self.current -= 1
            
        # defining this class object as a string 
        def __str__(self):
            return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
        
        # defining this class object as length
        def __len__(self):
            return self.pages
        
# create a variable and print the class 
my_book = Book("Mar & Venus", "John Gray", 198, 3)
print(my_book)

# print my current page 
my_book.bookmark_page()
print (f"Current Page: {my_book.bookmark}")

# print the next page from the current page 
my_book.turn_page()
my_book.bookmark_page()
print(f"Turn the next page: {my_book.bookmark}")

# print the page previously from the current page 
my_book.back_page()
my_book.bookmark_page()
print(f"Flip back a page: {my_book.bookmark}")

# if my_book.boolean:
#     my_book.turn_page()
#     my_book.bookmark_page()
#     print(my_book.bookmark)
# else:
#     my_book.back_page()
#     my_book.bookmark_page()
#     print(my_book.bookmark)

# class Employee:
#     # Initialising the object with the following attributes 
#     def __init__(self, name, salary, phone_number, start_date):
#         self.name = name
#         self.salary = salary
#         self.start_date = start_date
#         self.phone_number = phone_number

#     # creating a function within the object to get employment details 
#     def get_employment_details(self):
#         return (self.name, self.salary, self.start_date)
    
#     # creating a function with the object to get contact details 
#     def get_contact_details(self):
#         return (self.name, self.phone_number)
        
# #creating the variable to call the class with the arguments for the above attributes         
# employee_1 = Employee("Fran", 78000, "12345678", "1st June 2020")

# # Different ways to print 
# print (f"Employee Name: {employee_1.name} Salary: ${employee_1.salary} Start Date: {employee_1.start_date} ")
# print (employee_1.get_employment_details())
# print(employee_1.get_contact_details())
        