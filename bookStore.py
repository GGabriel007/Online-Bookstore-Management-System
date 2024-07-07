import tkinter as tk
from tkinter import messagebox
from tkinter import font
from books_data import books 
from admin import admin_credentials
from user import user_credentials

def menu():

    def admin_login():
        login_window.destroy()
        login_as_admin()
        

    def user_login():
        login_window.destroy()
        login_as_user()
        

    login_window = tk.Tk()
    login_window.title("Login")

    bold_font = font.Font(weight='bold', size =11)

    login_window['padx'] = 30
    login_window['pady'] = 15

    space_label = tk.Label(login_window, text=f'')
    space_label.grid(row=0, column=0)

    login_label = tk.Label(login_window, text="Login" , font = bold_font)
    login_label.grid(row =0, column = 1)

    space_label = tk.Label(login_window, text=f'')
    space_label.grid(row=0, column=2)

    space_label = tk.Label(login_window, text=f'')
    space_label.grid(row=1, column=0)

    space_label = tk.Label(login_window, text=f'Welcome to my Bookstore\n Please Log in as user \nor administrator\n')
    space_label.grid(row=1, column=1)

    space_label = tk.Label(login_window, text=f'')
    space_label.grid(row=1, column=3)

    
    # Create buttons for selecting the role
    admin_button = tk.Button(login_window, text = "Login as Admin", command = admin_login)
    admin_button.grid( row= 2, column = 0 )

    

    space_label = tk.Label(login_window, text=f'')
    space_label.grid(row=2, column=1)


    user_button = tk.Button(login_window, text = "Login as User", command = user_login)
    user_button.grid( row = 2, column = 2)

    login_window.mainloop()

def login_as_user():

    

    user_window = tk.Tk()
    user_window.title("User Login")

    user_window['padx'] = 22
    user_window['pady'] = 10

    bold_font = font.Font(weight='bold', size =11)

    header = tk.Label(user_window, text='User Login\n', font = bold_font)
    header.grid(row = 0, columnspan =2)

    # Create entry widgets for user ID and passowrd
    user_id_label = tk.Label(user_window, text = "User ID (UID):")
    user_id_label.grid(row = 1, column = 0, sticky= 'w')
    user_entry = tk.Entry(user_window)
    user_entry.grid(row = 1, column = 1)

    password_label = tk.Label(user_window, text = "Password:")
    password_label.grid(row = 2, column = 0, sticky= 'w')
    password_entry = tk.Entry(user_window, show = "*")
    password_entry.grid(row = 2, column =1)

    # Function to handle admin login authentication
    def authenticated_user():


        userName = user_entry.get()
        password = password_entry.get()

        # Checking if the admin exists in the credentials dictionary
        # and if the password matches
        if not userName or not userName.isdigit():
            messagebox.showerror("Login Failed", "Invalid User ID (UID) or password")
            return 


        for user in user_credentials:
            if user["UID"] == int(userName) and user["password"] == password: 
                messagebox.showinfo("Login Successful", f"Welcome, User {userName}!")

                user_window.destroy() # Closing the login window
                # Calling admin menu function after successful login
                user_menu(userName)
                
                
                return 
            
        # If no matching credentials are found, show error message
        messagebox.showerror("Login Failed", "Invalid User ID (UID) or password")

    def main_menu():
        user_window.destroy()
        menu()
        

    space_label = tk.Label(user_window, text=f'')
    space_label.grid(row=3, column=0)

    # Button to submit admin login
    admin_login_button = tk.Button(user_window, text = " Login ", command = authenticated_user)
    admin_login_button.grid (row = 4, columnspan= 1)

    sign_up_button = tk.Button(user_window, text = "Sign Up", command = create_account)
    sign_up_button.grid(row = 4, columnspan = 3)

    cancel_button = tk.Button(user_window, text=" Cancel ", command= main_menu)
    cancel_button.grid(row=4, columnspan=2, sticky = 'e')

    

    user_window.mainloop()

def create_account():
    # Finding the next available User ID
    next_user_id = max(user_credentials, key=lambda x: x["UID"])["UID"] + 1 if user_credentials else 1


    # Function to handle creatinga a new user account 
    def save_user():
        # Get the password entered by the user
        password1 = password_entry1.get()
        password2 = password_entry2.get()

        if password1 == password2:

            # Checking for the password for not be an empty string 
            if password1.strip() != "":


                # Save the user information
                new_user = {"UID": next_user_id, "password": password1}
                user_credentials.append(new_user)

                # Write the updated user data back to the user.py file
                with open("user.py", "w") as file:
                    file.write(f"user_credentials = {user_credentials}")

                # Provide feedback to the user
                messagebox.showinfo("Account Created", f"Your User ID: {next_user_id} \n Your account has been created successfully!")

                # Close the create account window
                create_account_window.destroy()
            else: 
                # Password is empty, showing error message
                messagebox.showerror("Empty Password", "Invalid Password.")
        else:
            # Passwords don't match, show error message
            messagebox.showerror("Password Mismatch", "Passwords do not match. Please enter them again.")


    # Create a new window for creating a user account
    create_account_window = tk.Toplevel()
    create_account_window.title("New Account")
    
    bold_font = font.Font(weight='bold', size =11)
    regular_font = font.Font(size = 10)

    create_account_window['padx'] = 10
    create_account_window['pady'] = 10

    header = tk.Label(create_account_window, text='New User Account\n', font = bold_font)
    header.grid(row = 0, sticky= "w",columnspan = 2 )

    description = tk.Label(create_account_window, text= f'The User ID is given automatically', font = regular_font)
    description.grid(row = 1, sticky= "w", columnspan = 2)

    description = tk.Label(create_account_window, text= f'Your User ID: {next_user_id}', font = regular_font)
    description.grid(row = 2, sticky= "w",columnspan = 2)

    space_label = tk.Label(create_account_window, text=f'')
    space_label.grid(row=3, column=0)


    # Create a label and entry widget for password
    password_label1 = tk.Label(create_account_window, text = "Enter Password:")
    password_label1.grid(row= 4, column = 0, sticky= 'w')
    password_entry1 = tk.Entry(create_account_window, show ="*")
    password_entry1.grid(row = 4, column =1 )

    password_label2 = tk.Label(create_account_window, text = "Confirm Password:")
    password_label2.grid(row= 5, column = 0, sticky= 'w')
    password_entry2 = tk.Entry(create_account_window, show ="*")
    password_entry2.grid(row =5, column =1 )

    space_label = tk.Label(create_account_window, text=f'')
    space_label.grid(row=6, column=0)

    # Create a button to save the user information
    save_button = tk.Button(create_account_window, text = " Save ", command = save_user)
    save_button.grid(row = 7, columnspan = 2)

    cancel_button = tk.Button(create_account_window, text=" Cancel ", command=create_account_window.destroy)
    cancel_button.grid(row=7, columnspan=3, sticky= 'e')

def login_as_admin():

    admin_user_window = tk.Tk()
    admin_user_window.title("Admin Login")

    

    admin_user_window['padx'] = 22
    admin_user_window['pady'] = 10

    bold_font = font.Font(weight='bold', size =11)

    header = tk.Label(admin_user_window, text='Administrator Login\n', font = bold_font)
    header.grid(row = 0, columnspan =2)

    # Create entry widgets for admin ID and passowrd
    admin_id_label = tk.Label(admin_user_window, text = "Admin ID (AID):")
    admin_id_label.grid(row = 1, column = 0, sticky= 'w')
    admin_entry = tk.Entry(admin_user_window)
    admin_entry.grid(row = 1, column = 1)

    password_label = tk.Label(admin_user_window, text = "Password:")
    password_label.grid(row = 2, column = 0, sticky= 'w')
    password_entry = tk.Entry(admin_user_window, show = "*")
    password_entry.grid(row = 2, column =1)

    # Function to handle admin login authentication
    def authenticated_admin():


        adminName = admin_entry.get()
        password = password_entry.get()

        # Checking if the admin exists in the credentials dictionary
        # and if the password matches
        if not adminName or not adminName.isdigit():
            messagebox.showerror("Login Failed", "Invalid Admin ID (AID) or password")
            return 
    
        for admin in admin_credentials:
            if admin["AID"] == int(adminName) and admin["password"] == password: 
                messagebox.showinfo("Login Successful", f"Welcome, Admin {adminName}!")

                admin_user_window.destroy() # Closing the login window

                # Calling admin menu function after successful login
                admin_menu(adminName)
                
                return 
            
        # If no matching credentials are found, show error message
        messagebox.showerror("Login Failed", "Invalid Admin ID (AID) or password")

    def main_menu():
        admin_user_window.destroy()
        menu()

    space_label = tk.Label(admin_user_window, text=f'')
    space_label.grid(row=3, column=0)

    # Button to submit admin login
    admin_login_button = tk.Button(admin_user_window, text = "  Login  ", command = authenticated_admin)
    admin_login_button.grid (row = 4, columnspan= 2, sticky= 'w')

    cancel_button = tk.Button(admin_user_window, text=" Cancel ", command= main_menu)
    cancel_button.grid(row=4, columnspan=2, sticky = 'e')


    admin_user_window.mainloop()

def user_menu(userName):
    """
    Display a menu of options for users using Tkinter GUI.
    
    Args:
        None
    
    Returns:
        None
    """
    # Create main window
    root = tk.Tk()
    root.title("Bookstore")

    bold_font = font.Font(weight='bold', size =12)
    regular_font = font.Font(size = 11)

    root['padx'] = 20
    root['pady'] = 13

    # Header label
    header = tk.Label(root, text='Bookstore Menu', font= bold_font)
    header.grid(row = 0, column= 0, sticky= 'w')

    user_name = tk.Label(root, text = f"Hello, User {userName}\n", font = regular_font)
    user_name.grid(row = 1, column = 0, sticky= 'w')

    retrieve_button = tk.Button(root, text="Look for Book Information by ID", command=retrieve_book)
    retrieve_button.grid(row = 2, column= 0, sticky= 'w')

    header = tk.Label(root, text='                        ')
    header.grid(row= 3)

    buy_button = tk.Button(root, text="Buy a book", command= buy_book)
    buy_button.grid(row = 4, column= 0, sticky= 'w')

    header = tk.Label(root, text='                        ')
    header.grid(row = 5)

    cancel_button = tk.Button(root, text=" Logout ", command=lambda: (root.destroy(), menu()))
    cancel_button.grid(row=6, column=1, sticky = 'e')


    # Run the main event loop
    root.mainloop()

def admin_menu(adminName):
    """
    Display a menu of options for administrators using Tkinter GUI.
    
    Args:
        None
    
    Returns:
        None
    """
    

    # Create main window
    root = tk.Tk()
    root.title("Bookstore Management System")

    bold_font = font.Font(weight='bold', size =12)

    regular_font = font.Font(size = 11)

    root['padx'] = 20
    root['pady'] = 13


    # Header label
    header = tk.Label(root, text='Bookstore Management System Menu', font = bold_font)
    header.grid(row = 0, column =0)

    admin_name = tk.Label(root, text = f"Hello, Admin {adminName}\n", font = regular_font)
    admin_name.grid(row = 1, column = 0, sticky= 'w')

    # Create buttons for each option
    add_button = tk.Button(root, text="Add a new book", command = add_new_book) 
    add_button.grid(row = 2, column = 0, sticky= 'w')

    header = tk.Label(root, text='                        ')
    header.grid( row = 3, column =0)

    retrieve_button = tk.Button(root, text="Retrieve information for a book", command=retrieve_book)
    retrieve_button.grid(row = 4, column = 0, sticky= 'w')

    header = tk.Label(root, text='                        ')
    header.grid(row = 5, column =0)

    update_button = tk.Button(root, text="Update a book", command=update_existing_book)
    update_button.grid(row = 6, column = 0, sticky= 'w')

    header = tk.Label(root, text='                        ')
    header.grid(row = 7, column =0)

    cancel_button = tk.Button(root, text=" Logout ", command=lambda: (root.destroy(), menu()))
    cancel_button.grid(row=8, column=1, sticky = 'e')


    # Run the main event loop
    root.mainloop()

def add_book(new_book):
    """
    Add a new book to the inventory and update the books_data.py file.

    Args: 
        new_book (dict): The dictionary containing information about the new book.
        It should have keets "id", "title", "author", "genre", "price", "quantity".

    Returns:
        None
    """
    # Adds the new book to the list of books
    books.append(new_book)

    # Write the updated list of books to the books_data file 
    with open("books_data.py", "w") as file:
        file.write("books = " + str(books))

# Function to add a new book
def add_new_book():
    """
    Display a form for adding a new book using Tkinter GUI.
    
    Args:
        None
    
    Returns:
        None
    """
    # Create a new window for adding a book
    add_book_window = tk.Toplevel()
    add_book_window.title("Add New Book")

    bold_font = font.Font(weight='bold', size =11)
    regular_font = font.Font(size = 10)

    add_book_window['padx'] = 8
    add_book_window['pady'] = 8

    # Find the maximum ID currently in the books list
    max_id = max(book["id"] for book in books) if books else 0

    # Auto-assign the next ID for the new book
    next_id = max_id + 1

    # Function to handle adding a new book
    def add_book_to_inventory():

        new_book = {}

        # Validate that the price and quantity are numbers
        price = price_entry.get()
        quantity = quantity_entry.get()
        
                    
        if title_entry.get() and author_entry.get() and genre_entry.get() and price_entry.get() and quantity_entry.get():
            # Validate that the price and quantity are numbers
            try:
                # Attempt to convert price and quantity to float values
                price = float(price)
                quantity = float(quantity)
            except ValueError:
                messagebox.showerror("Error", "Price and quantity must be numeric.")
                return  

            # Assign the provided information to the new book dictionary
            new_book["id"] = next_id 
            new_book["title"] = title_entry.get()
            new_book["author"] = author_entry.get()
            new_book["genre"] = genre_entry.get()
            new_book["price"] = price_entry.get()
            new_book["quantity"] = quantity_entry.get()

            # Add the new book to the inventory
            add_book(new_book)

            # Showing the add book to the inventory)
            messagebox.showinfo("New Book Added", f"Book ID: {next_id}\nTitle: {new_book['title']}\nAuthor: {new_book["author"]}\nGenre: {new_book["genre"]}\nPrice: {new_book["price"]}\nQuantity: {new_book["quantity"]}")

            # Close the add book window
            add_book_window.destroy()

        else:
            # Display an error message if any required field is missing
            messagebox.showerror("Error", "Please provide all information to add a new book to the inventory.")

    # Create labels and entry widgets for each input field

    header_label = tk.Label(add_book_window, text=f'Add Information', font = bold_font)
    header_label.grid(row=0, column=0, sticky= 'w')

    header_label = tk.Label(add_book_window, text=f'of new Book\n', font = bold_font)
    header_label.grid(row=1, column=0, sticky= 'w')

    title_label = tk.Label(add_book_window, text="Title: ", font= regular_font)
    title_label.grid(row=2, column=0, sticky= 'w')
    title_entry = tk.Entry(add_book_window)
    title_entry.grid(row=2, column=1)

    space_label = tk.Label(add_book_window, text=f'')
    space_label.grid(row=3, column=0)

    author_label = tk.Label(add_book_window, text="Author: ", font= regular_font)
    author_label.grid(row=4, column=0, sticky= 'w')
    author_entry = tk.Entry(add_book_window)
    author_entry.grid(row=4, column=1)

    space_label = tk.Label(add_book_window, text=f'')
    space_label.grid(row=5, column=0)

    genre_label = tk.Label(add_book_window, text="Genre: ", font= regular_font)
    genre_label.grid(row=6, column=0, sticky= 'w')
    genre_entry = tk.Entry(add_book_window)
    genre_entry.grid(row=6, column=1)

    space_label = tk.Label(add_book_window, text=f'')
    space_label.grid(row=7, column=0)

    price_label = tk.Label(add_book_window, text="Price: ", font= regular_font)
    price_label.grid(row=8, column=0, sticky= 'w')
    price_entry = tk.Entry(add_book_window)
    price_entry.grid(row=8, column=1)

    space_label = tk.Label(add_book_window, text=f'')
    space_label.grid(row=9, column=0)

    quantity_label = tk.Label(add_book_window, text="Quantity: ", font= regular_font)
    quantity_label.grid(row=10, column=0, sticky= 'w')
    quantity_entry = tk.Entry(add_book_window)
    quantity_entry.grid(row=10, column=1)

    space_label = tk.Label(add_book_window, text=f'')
    space_label.grid(row=11, column=0)

    # Create a button to add the book
    add_button = tk.Button(add_book_window, text=" Add Book ", command=add_book_to_inventory)
    add_button.grid(row=12, column=0, sticky= 'e')

    cancel_button = tk.Button(add_book_window, text=" Cancel ", command=add_book_window.destroy)
    cancel_button.grid(row=12, column=1, sticky = 'w')

    # Run the main event loop for the add book window
    add_book_window.mainloop()

# Function to retrieve information for a book
def retrieve_book():
    """
    Display a form for retrieving information for a book by its ID using Tkinter GUI.

    Args:
        None
    Returns:
        None
    """
    # Creating a new window for retrieving a book
    retrieve_book_window = tk.Toplevel()
    retrieve_book_window.title("Retrieve Book Information")

    retrieve_book_window['padx'] = 3

     # Create label and entry widget for the book ID
    id_label = tk.Label(retrieve_book_window, text = "Book ID: ")
    id_label.grid(row = 0, column = 0, sticky= 'e')
    id_entry = tk.Entry(retrieve_book_window)
    id_entry.grid(row = 0, column = 1)

    # Function to handle retrieving information for a book
    def retrieve_book_info():
        # Get the book ID from the entry widget
        book_id_str = id_entry.get()
        

        if not book_id_str:
            # Display an error message if any required field is missing
            messagebox.showerror("Error", "Please provide an ID (e.g., '1', '2'...)")

        else:
            if book_id_str.isdigit():

                book_id = int(book_id_str)
                found_book = None

                # Search for the book by its ID in the books list
                for book in books:
                    if book["id"] == book_id:
                        found_book = book
                        break 
                # Displaying the book information if found, otherwise show a message
                if found_book:
                    messagebox.showinfo("Book Information", f"Book ID: {found_book['id']}\n Title: {found_book['title']}\n Author: {found_book['author']}\n Genre: {found_book['genre']}\n Price: {found_book['price']}\n Quantity: {found_book['quantity']}")
                else:
                    messagebox.showinfo("Book Not Found", f"No book found with ID {book_id}")
            else:
                # Display an error message if the input is not a valid integer
                messagebox.showerror("Error", "Please provide a valid integer ID.")

    # Create a button to retrieve the book information
    retrieve_button = tk.Button(retrieve_book_window, text = "Retrieve Book", command = retrieve_book_info)
    retrieve_button.grid( row = 1, columnspan = 1, sticky= 'w')

    cancel_button = tk.Button(retrieve_book_window, text="Cancel", command=retrieve_book_window.destroy)
    cancel_button.grid(row=1, columnspan=1, sticky = 'e')

    # Creatinga label to display the inventory list
    inventory_label = tk.Label(retrieve_book_window, text = "Inventory List:\n")
    inventory_label.grid(row = 2, column = 0, columnspan = 2, sticky= 'w')

    # Create a text widget to display the inventory list
    inventory_text = tk.Text(retrieve_book_window, height= 10, width = 50)
    inventory_text.grid(row =3, column = 0, columnspan = 2)


    # Populated the inventory list 
    for book in books:
        inventory_text.insert(tk.END, f"Book ID: {book['id']}\n Title: {book['title']}\n Author: {book['author']}\n Genre: {book['genre']}\n Price: {book['price']}\n Quantity: {book['quantity']}\n\n")

    scrollbar = tk.Scrollbar(retrieve_book_window, command = inventory_text.yview)
    scrollbar.grid(row =3, column = 2, sticky = 'ns')
    inventory_text.config(yscrollcommand = scrollbar.set)

    # Disable the Text widget
    inventory_text.config(state= tk.DISABLED)

    # Run the main event loop for the retrieve book window
    retrieve_book_window.mainloop()

# Function to update information for a book
def update_book(books, book_id, updated_info):
    """
    Update information about a book in the invertory.

    Args: 
        books (list): The list of books in the inventory.
        book_id (int): The ID of the book to update.
        update_info (dict): A dictionary containing updated information about the book.
            It can contain any combination of keys: "title", "author", "genre", "price", "quantity".

    Returns: 
        None   
    """
    for book in books: 
        if book ["id"] == book_id:
            book.update(updated_info)
            return

# Function to update an existing book
def update_existing_book():
    """
    Display a form for updating information for an existing book by its ID using Tkinter GUI.

    Args:
        None
    Returns:
        None
    """

    # Create a new window for updating a book
    update_by_id_window = tk.Toplevel()
    update_by_id_window.title("Update Book by ID")

    bold_font = font.Font(weight='bold', size =11)

    update_by_id_window['padx'] = 3

    # Function to handle updating information for an existing book
    def update_by_id():
        # Getting the book ID from the entry widget
        book_id_str = id_entry.get()

        if not book_id_str:
            # Displaying an error message if any required field is missing
            messagebox.showerror("Error", "Please provide an ID (e.g., '1', '2'...)")

        else: 
            if book_id_str.isdigit():
                book_id = int(book_id_str)
                # Search for the book by its ID in the books list
                found_book = None
                for book in books:
                    if book["id"] == int(book_id):
                        found_book = book
                        break

                # If the book is found, proceed with updating
                if found_book:

                    # Close the update by ID window
                    update_by_id_window.destroy()

                    # Create a new window for selecting which information to update
                    update_book_window = tk.Toplevel()
                    update_book_window.title("Select Information")

                    update_book_window['padx'] = 8
                    update_book_window['pady'] = 4

                    # Function to handle updating selected information for the book
                    def update_selected_info():
                        # Get the updated information from the entry widgets
                        updated_info = {}
                            
                        if title_entry.get():
                            updated_info["title"] = title_entry.get()
                        if author_entry.get():
                            updated_info["author"] = author_entry.get()
                        if genre_entry.get():
                            updated_info["genre"] = genre_entry.get()
                        if price_entry.get():
                            try: 
                                # Checking if the price is a float
                                updated_info["price"] = float(price_entry.get())
                            except ValueError:
                                messagebox.showerror("Error", "Price must be a number.")
                                return

                        if quantity_entry.get():

                            try:
                                # Checking if the quantity is an integer
                                updated_info["quantity"] = int(quantity_entry.get())
                            except ValueError:
                                messagebox.showerror("Error", "Quantity must be a valud integer.")
                                return
                        
                        # Update the book information
                        update_book(books, int(book_id), updated_info)

                        try: 

                            #Write the updated book data back to the books_data file
                            with open("books_data.py", "w") as file:
                                file.write("books =" + str(books))
                            # Display a message box indicating the book information has been updated
                            messagebox.showinfo("Book Information Updated", f"Book ID: {found_book['id']}\n Title: {found_book['title']}\n Author: {found_book['author']}\n Genre: {found_book['genre']}\n Price: {found_book['price']}\n Quantity: {found_book['quantity']}")

                        except Exception as e:
                            print ("Error writing to file:", e)

                        # Close the update book window
                        update_book_window.destroy()

                    # Header
                    header_label = tk.Label(update_book_window, text=f'Add Information', font = bold_font)
                    header_label.grid(row=0, column=0, sticky= 'w')

                    header_label = tk.Label(update_book_window, text=f'to update\n', font = bold_font)
                    header_label.grid(row=1, column=0, sticky= 'w')

                    # Create labels and entry widgets for updating book information
                    title_label = tk.Label(update_book_window, text= f"Update Title:")
                    title_label.grid(row=2, column=0, sticky= 'w')
                    title_entry = tk.Entry(update_book_window)
                    title_entry.grid(row=2, column=1)
                    title_entry.insert(0, found_book['title'])

                    space_label = tk.Label(update_book_window, text=f'')
                    space_label.grid(row=3, column=0)

                    author_label = tk.Label(update_book_window, text=f"Update Author:")
                    author_label.grid(row=4, column=0, sticky= 'w')
                    author_entry = tk.Entry(update_book_window)
                    author_entry.grid(row=4, column=1)
                    author_entry.insert(0, found_book['author'])

                    space_label = tk.Label(update_book_window, text=f'')
                    space_label.grid(row=5, column=0)

                    genre_label = tk.Label(update_book_window, text=f"Update Genre:")
                    genre_label.grid(row=6, column=0, sticky= 'w')
                    genre_entry = tk.Entry(update_book_window)
                    genre_entry.grid(row=6, column=1)
                    genre_entry.insert(0, found_book['genre'])

                    space_label = tk.Label(update_book_window, text=f'')
                    space_label.grid(row=7, column=0)

                    price_label = tk.Label(update_book_window, text=f"Update Price:")
                    price_label.grid(row=8, column=0, sticky= 'w')
                    price_entry = tk.Entry(update_book_window)
                    price_entry.grid(row=8, column=1)
                    price_entry.insert(0, found_book['price'])

                    space_label = tk.Label(update_book_window, text=f'')
                    space_label.grid(row=9, column=0)

                    quantity_label = tk.Label(update_book_window, text=f"Update Quantity:")
                    quantity_label.grid(row=10, column=0, sticky= 'w')
                    quantity_entry = tk.Entry(update_book_window)
                    quantity_entry.grid(row=10, column=1)
                    quantity_entry.insert(0, found_book['quantity'])

                    space_label = tk.Label(update_book_window, text=f'')
                    space_label.grid(row=11, column=0)

                    # Create a button to update the book information
                    update_button = tk.Button(update_book_window, text="Update Book", command=update_selected_info)
                    update_button.grid(row=12, column=0, sticky= 'e')

                    cancel_button = tk.Button(update_book_window, text="Cancel", command=update_book_window.destroy)
                    cancel_button.grid(row=12, column=1, sticky= 'w')

                    update_book_window.mainloop()



                else:
                    # Display a message box indicating that the book ID was not found
                    messagebox.showerror("Error", f"No book found with ID {book_id}")
            else:
                # Display an error message if the input is not a valid integer
                messagebox.showerror("Error", "Please provide a valid integer ID.")

    # Create labels and entry widgets for the book ID
    id_label = tk.Label(update_by_id_window, text="Book ID:")
    id_label.grid(row=0, column=0, sticky= 'e')
    id_entry = tk.Entry(update_by_id_window)
    id_entry.grid(row=0, column=1)

    # Create a button to proceed with updating
    update_id_button = tk.Button(update_by_id_window, text="Proceed", command=update_by_id)
    update_id_button.grid(row=1, columnspan=1, sticky= 'w')

    cancel_button = tk.Button(update_by_id_window, text="Cancel", command=update_by_id_window.destroy)
    cancel_button.grid(row=1, columnspan=1, sticky = 'e')

    # Creatinga label to display the inventory list
    inventory_label = tk.Label(update_by_id_window, text = "Inventory List:\n")
    inventory_label.grid(row = 2, column = 0, columnspan = 2, sticky= 'w')

    # Create a text widget to display the inventory list
    inventory_text = tk.Text(update_by_id_window, height= 10, width = 50)
    inventory_text.grid(row =3, column = 0, columnspan = 2)

    # Populated the inventory list 
    for book in books:
        inventory_text.insert(tk.END, f"Book ID: {book['id']}\n Title: {book['title']}\n Author: {book['author']}\n Genre: {book['genre']}\n Price: {book['price']}\n Quantity: {book['quantity']}\n\n")

    # Disable the Text widget
    inventory_text.config(state= tk.DISABLED)

    scrollbar = tk.Scrollbar(update_by_id_window, command = inventory_text.yview)
    scrollbar.grid(row =3, column = 2, sticky = 'ns')
    inventory_text.config(yscrollcommand = scrollbar.set)

    update_by_id_window.mainloop()

def buying_book(book_id, book_info_window):

    # Find the book in the inventory
    for book in books:
        if book["id"] == book_id:
            found_book = book
            break
    else:
        messagebox.showinfo("Book Not Found", f"No book found with ID {book_id}")

        return

    # Check if the book is in stock 
    if int(found_book['quantity']) > 0:
        
        # Prompt the user to confirm the purchase
        confirm_purchase = messagebox.askyesno("Confirm Purchase", f"Do you want to buy {found_book['title']}?")

        if confirm_purchase:

            # Decrement the quantity of the book by 1 
            found_book['quantity'] = str(int(found_book['quantity']) - 1)

            # Optionally, display a message confirming the purchase
            messagebox.showinfo("Purchase Successful", f"You have successfully purchased {found_book['title']}!")

            # Optionally, update the book's quantity in the inventory file
            with open("books_data.py", "w") as file:
                file.write("books= " + str(books))

            book_info_window.destroy()
            

        else: 
            messagebox.showinfo("Purchase Canceled", "Purchase canceled by user.")
            
    else:
        messagebox.showinfo("Out of Stock", f"{found_book['title']} is currently out of stock.")
        
def buy_book():
    """
    Display a form for buying a book by its ID using Tkinter GUI.

    Args:
        None
    Returns:
        None
    """
    bold_font = font.Font(weight='bold', size =12)

    regular_font = font.Font(size = 10)

    # Creating a new window for buying a book
    buy_book_window = tk.Toplevel()
    buy_book_window.title("Buy a Book")

    buy_book_window['padx'] = 3

    # Function to handle information for a book
    def book_info():
        # Get the book ID from the entry widget
        book_id_str = id_entry.get()

        if not book_id_str:
            # Display an error message if any required field is missing
            messagebox.showerror("Error", "Please provide an ID (e.g., '1', '2'...)")

        else:
            if book_id_str.isdigit():
                 
                book_id = int(book_id_str)
                found_book = None
                # Search for the book by its ID in the books list
                for book in books:
                    if book["id"] == book_id:
                        found_book = book
                        break 
                
                # Displaying the book information if found, otherwise show a message
                if found_book:

                    # Close the retrieve window
                    buy_book_window.destroy()

                    book_info_window = tk.Toplevel()
                    book_info_window.title("Book Information")

                    book_info_window['padx'] = 10
                    book_info_window['pady'] = 5

                    header_label = tk.Label(book_info_window, text=f'\nBook Information\n', font= bold_font )
                    header_label.grid(row=0, column=0, sticky= 'w')

                    title_label = tk.Label(book_info_window, text=f'Title:', font = regular_font)
                    title_label.grid(row=1, column=0, sticky = 'w')

                    title_label_text = tk.Label(book_info_window, text=f'{found_book['title']}')
                    title_label_text.grid(row=1, column=1, sticky = 'e')

                    space_label = tk.Label(book_info_window, text=f'  ')
                    space_label.grid(row=2, column=0)

                    author_label = tk.Label(book_info_window, text=f'Author:', font = regular_font)
                    author_label.grid(row=3, column=0, sticky = 'w')

                    author_label_text = tk.Label(book_info_window, text=f'{found_book['author']}')
                    author_label_text.grid(row=3, column=1, sticky = 'e')

                    space_label = tk.Label(book_info_window, text=f'  ')
                    space_label.grid(row=4, column=0)

                    genre_label = tk.Label(book_info_window, text=f'Genre:', font = regular_font)
                    genre_label.grid(row=5, column=0, sticky = 'w')

                    genre_label_text = tk.Label(book_info_window, text=f'{found_book['genre']}')
                    genre_label_text.grid(row=5, column=1, sticky = 'e')

                    space_label = tk.Label(book_info_window, text=f'  ')
                    space_label.grid(row=6, column=0)

                    price_label = tk.Label(book_info_window, text=f'Price:', font = regular_font)
                    price_label.grid(row=7, column=0, sticky = 'w')

                    price_label_text = tk.Label(book_info_window, text=f'{found_book['price']}')
                    price_label_text.grid(row=7, column=1, sticky = 'e')

                    space_label = tk.Label(book_info_window, text=f'  ')
                    space_label.grid(row=8, column=0)

                    quantity_label = tk.Label(book_info_window, text=f'Quantity:', font = regular_font)
                    quantity_label.grid(row=9, column=0, sticky = 'w')

                    quantity_label_text = tk.Label(book_info_window, text=f'{found_book['quantity']}')
                    quantity_label_text.grid(row=9, column=1, sticky = 'e')

                    space_label = tk.Label(book_info_window, text=f'  ')
                    space_label.grid(row=10, column=0)

                    # Button to buy the book
                    buy_button = tk.Button(book_info_window, text = " Buy ", command = lambda: buying_book(book_id, book_info_window))
                    buy_button.grid(row=11, column=0, sticky = 'e')

                    # Create a cancel button to close the window
                    cancel_button = tk.Button(book_info_window, text=" Cancel ", command=book_info_window.destroy)
                    cancel_button.grid(row=11, column=1, sticky = 'w')

                    
                else:
                    messagebox.showinfo("Book Not Found", f"No book found with ID {book_id}")
            else:
                # Display an error message if the input is not a valid integer
                messagebox.showerror("Error", "Please provide a valid integer ID.")



    # Create label and entry widget for the book ID
    id_label = tk.Label(buy_book_window, text = "Book ID: ")
    id_label.grid(row = 0, column = 0, sticky= 'e')
    id_entry = tk.Entry(buy_book_window)
    id_entry.grid(row = 0, column = 1)

    # Create a button to retrieve the book information
    retrieve_button = tk.Button(buy_book_window, text = "Retrieve Book", command = book_info)
    retrieve_button.grid( row = 1, columnspan= 1, sticky='w')

    # Create a cancel button to close the window
    cancel_button = tk.Button(buy_book_window, text="Cancel", command=buy_book_window.destroy)
    cancel_button.grid(row=1, columnspan=1, sticky= 'e')

        # Creatinga label to display the inventory list
    inventory_label = tk.Label(buy_book_window, text = "Inventory List:")
    inventory_label.grid(row = 2, column = 0, columnspan = 2, sticky= 'w')

    # Create a text widget to display the inventory list
    inventory_text = tk.Text(buy_book_window, height= 10, width = 50)
    inventory_text.grid(row =3, column = 0, columnspan = 2)

    # Populated the inventory list 
    for book in books:
        inventory_text.insert(tk.END, f"Book ID: {book['id']}\n Title: {book['title']}\n Author: {book['author']}\n Genre: {book['genre']}\n Price: {book['price']}\n Quantity: {book['quantity']}\n\n")

    # Disable the Text widget
    inventory_text.config(state= tk.DISABLED)

    scrollbar = tk.Scrollbar(buy_book_window, command = inventory_text.yview)
    scrollbar.grid(row =3, column = 2, sticky = 'ns')
    inventory_text.config(yscrollcommand = scrollbar.set)


    # Run the main event loop for the retrieve book window
    buy_book_window.mainloop()  

# Call the menu function to display the GUI
if __name__ == "__main__":
    menu()
