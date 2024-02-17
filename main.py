import tkinter
import customtkinter

#system
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

def home_page():
    app = customtkinter.CTk()
    app.geometry("1000x700")
    app.title("Library Management System")


    my_font = customtkinter.CTkFont(family="Helvetica", size=50, weight="bold")
    main_header = customtkinter.CTkLabel(app, text="Menu", font=my_font, text_color="green")
    main_header.pack(padx=15, pady=15)

    #menu elements
    list_btn = customtkinter.CTkButton(app, text="List Books", command=lib.list_book)
    list_btn.pack(padx=15, pady=15)

    add_btn = customtkinter.CTkButton(app, text="Add Book", command=lib.add_book)
    add_btn.pack(padx=15, pady=15)

    remove_btn = customtkinter.CTkButton(app, text="Remove Book", command=lib.remove_book)
    remove_btn.pack(padx=15, pady=15)

    app.mainloop()



class Library:
    def __init__(self, file_name='books.txt'):
        self.file_name = file_name
        self.file = open(self.file_name, 'a+')

    def __del__(self):
        self.file.close()

    def list_book(self):
        list_app = customtkinter.CTk()
        list_app.geometry("500x350")
        list_app.title("List Book")

        my_font = customtkinter.CTkFont(family="Helvetica", size=20, weight="bold")
        list_book_label = customtkinter.CTkLabel(list_app, text="Book List", font=my_font, text_color="red")
        list_book_label.pack(padx=15, pady=15)

        self.file.seek(0)
        lines = self.file.read().splitlines()
        for line in lines:
            book = line.split(",")
            book_line = customtkinter.CTkLabel(list_app, text=f"Title: {book[0]}, Author: {book[1]}")
            book_line.pack()

        list_app.mainloop()

    def add_book(self):
        add_app = customtkinter.CTk()
        add_app.geometry("500x500")
        add_app.title("Add Book")

        title_label = customtkinter.CTkLabel(add_app, text="Please Enter Book Title")
        title_label.pack()
        title_entry = customtkinter.CTkEntry(add_app, width=400, height=40)
        title_entry.pack(padx=15, pady=15)

        author_label = customtkinter.CTkLabel(add_app, text="Please Enter Book Author")
        author_label.pack()
        author_entry = customtkinter.CTkEntry(add_app, width=400, height=40)
        author_entry.pack(padx=15, pady=15)

        year_label = customtkinter.CTkLabel(add_app, text="Please Enter Book Release Year")
        year_label.pack()
        year_entry = customtkinter.CTkEntry(add_app, width=400, height=40)
        year_entry.pack(padx=15, pady=15)

        page_label = customtkinter.CTkLabel(add_app, text="Please Enter Number Of Page")
        page_label.pack()
        page_entry = customtkinter.CTkEntry(add_app, width=400, height=40)
        page_entry.pack(padx=15, pady=15)

        add_comp_label = customtkinter.CTkLabel(add_app, text="", text_color="red")
        add_comp_label.pack()

        def add_submit():
            title = title_entry.get()
            author = author_entry.get()
            year = year_entry.get()
            page = page_entry.get()

            book = f"{title}, {author}, {year}, {page}\n"
            self.file.write(book)
            add_comp_label.configure(text=f"Book '{title}' added successfully.")

        add_submit_btn = customtkinter.CTkButton(add_app, text="Submit", command=add_submit)
        add_submit_btn.pack(padx=15, pady=15)

        add_app.mainloop()

    def remove_book(self):
        remove_app = customtkinter.CTk()
        remove_app.geometry("500x350")
        remove_app.title("Remove Book")

        remove_label = customtkinter.CTkLabel(remove_app, text="Please Enter Book Title that You Want to Remove")
        remove_label.pack()

        remove_entry = customtkinter.CTkEntry(remove_app,  width=400, height=40)
        remove_entry.pack(padx=15, pady=15)

        rmv_completed = customtkinter.CTkLabel(remove_app, text="")
        rmv_completed.pack()

        def inner_remove():
            remove_entry_var = remove_entry.get()
            self.file.seek(0)
            lines = self.file.read().splitlines()

            remove_index = -1
            for i, line in enumerate(lines):
                if remove_entry_var in line:
                    remove_index = i
                    break

            if remove_index != -1:
                del lines[remove_index]
                self.file.seek(0)
                self.file.truncate()
                for line in lines:
                    self.file.write(line + '\n')
                rmv_completed.configure(text=f"Book '{remove_entry_var}' removed successfully.", text_color="red")
            else:
                rmv_completed.configure(text=f"Book '{remove_entry_var}' not found.", text_color="red")

        remove_submit_btn = customtkinter.CTkButton(remove_app, text="Submit", command=inner_remove)
        remove_submit_btn.pack(padx=10, pady=10)

        remove_app.mainloop()

lib = Library()
home_page()