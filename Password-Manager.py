import tkinter as tk 
from tkinter import messagebox 
import sqlite3 
import random 
import string 
 
# Connect to SQLite database 
con = sqlite3.connect('MasterPasswords.db') 
cursor = con.cursor() 

# Create tables if not exists 
MasterPasswords = '''CREATE TABLE IF NOT EXISTS MasterPasswords( 
    masterPassword TEXT NOT NULL, 
    usernames TEXT NOT NULL, 
    pins INTEGER NOT NULL, 
    email TEXT NOT NULL, 
    hint TEXT NOT NULL)''' 

cursor.execute(MasterPasswords) 
 

Passwords = '''CREATE TABLE IF NOT EXISTS Passwords( 
    pins INTEGER NOT NULL, 
    Passwords TEXT  NOT NULL, 
    usernames TEXT NOT NULL, 
    emails TEXT NOT NULL, 
    website_names TEXT NOT NULL, 
    url TEXT NOT NULL, 
    FOREIGN KEY (pins) REFERENCES MasterPasswords(pins))''' 

cursor.execute(Passwords) 
 
RDeleted = '''CREATE TABLE IF NOT EXISTS RDeleted( 
    pins INTEGER NOT NULL, 
    Passwords TEXT  NOT NULL, 
    usernames TEXT NOT NULL, 
    emails TEXT NOT NULL, 
    website_names TEXT NOT NULL, 
    url TEXT NOT NULL, 
    FOREIGN KEY (pins) REFERENCES MasterPasswords(pins))''' 
 
cursor.execute(RDeleted)  

Settings = '''CREATE TABLE IF NOT EXISTS Settings( 
    pins INTEGER NOT NULL, 
    stopPinCheck INTEGER NOT NULL, 
    autoAnother INTEGER NOT NULL, 
    autoAddFrom INTEGER NOT NULL, 
    autoPermenanent INTEGER NOT NULL, 
    FOREIGN KEY (pins) REFERENCES MasterPasswords(pins))''' 

cursor.execute(Settings) 

# Function to switch to login frame 

def gologin(): 
    LorR_frame.grid_forget() 
    global count 
    count = 3 
    login_frame.grid() 

#function to go back to the login or register option from the login window
def gobacklogin():
    login_frame.grid_forget()
    LorR_frame.grid()

#function to go back to the login or register option from the login window
def gobackregister():
    register_frame.grid_forget()
    LorR_frame.grid()

# Function to switch to register frame 
def goregister(): 
    LorR_frame.grid_forget() 
    register_frame.grid() 

# Function to switch to add frame 
def goadd(): 
    main_frame.grid_forget() 
    #count is a variable that stores the amount of time 
    global count 
    count = 3
    #current made to store the current window 
    global current
    current = add_frame 
    add_frame.grid() 

# Function to switch to delete frame 
def godelete(): 
    main_frame.grid_forget() 
    global count 
    count = 3
    global current
    current = delete_frame
    delete_frame.grid() 

# Function to switch to change frame 
def gochange(): 
    main_frame.grid_forget() 
    global count 
    count = 3
    global current
    current = change_frame
    change_frame.grid() 

# Function to switch to generate frame 
def gogenerate(): 
    main_frame.grid_forget() 
    global count 
    count = 3
    global current
    current = generate_frame
    generate_frame.grid() 

# Function to switch to strength frame 
def gostrength(): 
    main_frame.grid_forget() 
    global count 
    count = 3
    global current
    current = strength_frame
    strength_frame.grid() 

# Function to switch to settings frame 
def gosettings(): 
    global count 
    count = 3
    global current
    current.grid_forget()
    current = settings_frame
    settings_frame.grid()

# Function to switch to view profile frame 
def goviewP(): 
    settings_frame.grid_forget() 
    global current
    current = viewP_frame
    viewP_frame.grid() 

# Function to switch to edit profile frame 
def goeditP(): 
    settings_frame.grid_forget() 
    global current
    current = editP_frame 
    editP_frame.grid() 

# Function to switch to delete profile frame 
def godeleteP(): 
     settings_frame.grid_forget() 
     global current
     current = deleteP_frame
     deleteP_frame.grid() 

# Function to switch to menu frame 
def gomenu(): 
    global current
    #the current window is closed then the main menu opens
    current.grid_forget()
    current = main_frame 
    main_frame.grid() 

# Function to close the program 
def quit(): 
    root.destroy() 

#adds the user's information to the database 
def add(): 
    global count 
    try: 
#pin check to check if they're pin is correct 
        pin = Apin_entry.get() 
        pincheck = cursor.execute(f"SELECT pins FROM MasterPasswords WHERE pins={pin}") 
        pin2 = pincheck.fetchone() 
        if pin2 is None: 
            messagebox.showerror("pin is incorrect") 
            count=count-1 
            Atries_label.config(text="You have " + str(count) + " chances left") 
            
            if count==0: 

                messagebox.showerror("you have no more chances left") 
            pin2 = pin2[0] 
            pin2 = int(pin2) 
            print(pin2) 
            if int(pin) == pin2: 
                messagebox.showinfo("pin is correct") 
                #gets the information typed into each entry and inserts ot into the Passwords table
                website_name = AwebsiteName_entry.get() 
                url = AwebsiteURL_entry.get() 
                username = Ausername_entry.get() 
                password = Apassword_entry.get() 
                email = Aemail_entry.get() 
                cursor.execute("INSERT INTO Passwords VALUES (?,?,?,?,?,?)", (int(pin),password,username,email,website_name,url)) 
                con.commit() 
                messagebox.showinfo("Add passwords", "Information added successfully") 
                add_frame.grid_forget() 
                main_frame.grid() 
    #when their is an error it outputs the message below
    except: 
            messagebox.showerror("Error", "An error has occured") 

#adds passwords from the strength test and generator 
def addfrom(pwd,pin): 
    addfrom_frame.grid() 
    try: 
        username= AFusername_entry.get() 

        email= AFemail_entry.get() 

        website_name= AFwebsiteName_entry.get() 

        website_url= AFwebsiteURL_entry.get() 

        cursor.execute("INSERT INTO Passwords VALUES(?,?,?,?,?,?)",(pin,pwd,username,email,website_name,website_url)) 

        cursor.execute("SELECT*FROM Passwords") 

        results= cursor.fetchall() 

        print(results) 

        ask= messagebox.askyesno("Confirm", "Are you sure you want to add this information?") 

        if ask== "yes": 

            confirm = True 

        else: 

            pass 

    except: 
        messagebox.showerror("Error", "An error has occured") 

 

     

# deletes any  

def delete(): 
    global count  
    try: 
        pin = Dpin_entry.get() 
        pincheck = cursor.execute(f"SELECT pins FROM MasterPasswords WHERE pins={pin}") 
        pin2 = pincheck.fetchone() 
            
        if pin2 is None: 
            messagebox.showerror("pin is incorrect") 
            count=count-1 
            Dtries_label.config(text="You have " + str(count) + " chances left") 
                
            if count==0: 
                 messagebox.showerror("you have no more chances left") 
            pin2 = pin2[0] 
            pin2 = int(pin2) 
            print(pin2) 
            
            if int(pin) == pin2: 
                messagebox.showinfo("pin is correct") 
            
            #searches through each catorgry the user can delete 
                while True: 
                    search = Dsearch_entry.get() 
                    value = Dvalue_entry.get() 
                    
                    if search == "username" or search == "password" or search == "email" or search == "website name" or search == "website url": 
                        cursor.execute(f"SELECT * FROM Passwords WHERE {search}='{value}' AND pins={pin}") 
                        results= cursor.fetchall() 
                        print(results) 
                        delete = messagebox.askyesno("is this the imformation you want to delete?") 
                        
                        if delete: 
                            cursor.execute(f"DELETE FROM Passwords WHERE {search}='{value}' AND pins={pin}") 

                        else: 

                             messagebox.showinfo("you will go back to main page") 

                             delete_frame.grid_forget()  

                             main_frame.grid() 

                    else: 

                        messagebox.showerror("you can only delete username, password, email, website name, website url") 

                        continue 

    except: 
            messagebox.showerror("pin is incorrect") 
            count=count-1 
            tries_label.config(text="You have "+ str(count)+ " tries left") 
            
            if count==0: 
                delete_frame.grid_forget() 

#changes any information in the database based on search and value inputs 
def change(): 
    global count 
    try: 
            pin = Cpin_entry.get() 
            pincheck = cursor.execute(f"SELECT pins FROM MasterPasswords WHERE pins={pin}") 
            pin2 = pincheck.fetchone() 
            
            if pin2 is None: 
                messagebox.showerror("pin is incorrect") 
                count=count-1 
                Ctries_label.config(text="You have " + str(count) + " chances left") 
                if count==0: 
                    messagebox.showerror("you have no more chances left") 
            pin2 = pin2[0] 
            pin2 = int(pin2) 
            print(pin2) 
            if int(pin) == pin2: 
                messagebox.showinfo("pin is correct") 
                while True: 
                    search = Csearch_entry.get() 
                    value = Cvalue_entry.get() 
                    value1 = CNvalue_entry.get() 
                    if search == "username" or search == "Passwords" or search == "email" or search == "website_name" or search == "url": 
                        cursor.execute(f"SELECT * FROM Passwords WHERE {search}='{value}' AND pins={pin}") 
                        results= cursor.fetchall() 
                        print(results) 
                        change = messagebox.askyesno("is this the imformation you want to change?") 
                        if change == "yes": 
                            cursor.execute(f"UPDATE Passwords SET {search}='{value1}' WHERE {search}='{value}' AND pins={pin}") 
                            messagebox.showinfo("information changed") 
                            change_frame.grid_forget() 
                            main_frame.grid() 

                    else: 
                        messagebox.showerror("you can only change username, password, email, website name, website url") 
                        continue 

    except: 
        messagebox.showerror("pin is incorrect") 
        count=count-1 
        tries_label.config(text="You have "+ str(count)+ " tries left") 

        if count==0: 
            change_frame.grid_forget() 

# Function to handle generating passwords 
def generate(): 
    global count 
    try: 
            pin = Gpin_entry.get() 
            pincheck = cursor.execute(f"SELECT pins FROM MasterPasswords WHERE pins={pin}") 
            pin2 = pincheck.fetchone() 
            
            if pin2 is None: 
                messagebox.showerror("pin is incorrect") 
                count=count-1 
                Gtries_label.config(text="You have " + str(count) + " chances left") 
                
                if count==0: 
                    messagebox.showerror("you have no more chances left") 
            
            pin2 = pin2[0] 
            pin2 = int(pin2) 
            print(pin2) 

            if int(pin) == pin2:
                messagebox.showinfo("Success", "Pin is correct") 
                length = int(length_entry.get()) 
                letters = string.ascii_letters 
                digits = string.digits 
                special = string.punctuation 
                characters = letters 
                numbers = messagebox.askyesno("Number", "Would you like to include numbers?") 
                special_character = messagebox.askyesno("Special Character", "Would you like to include special characters?") 

                if numbers: 
                    characters += digits 
                if special_character: 
                    characters += special 
                pwd = "" 
                meets_criteria = False 
                has_number = False 
                has_special = False

                if length < 8:
                    messagebox.showerror("Error", "Length has to be greater than 8")
                    return

                # Generate password meeting specified criteria 
                while not meets_criteria or len(pwd) < length: 
                    new_char = random.choice(characters) 
                    pwd += new_char 

                    if new_char in digits: 
                        has_number = True 

                    elif new_char in special: 
                        has_special = True 
 
                    meets_criteria = True 

                    if numbers: 
                        meets_criteria = has_number 

                    if special_character: 
                        meets_criteria = meets_criteria and has_special 
                 
                generated.config(text=pwd) 
                # Ask user if they want to add the generated password to their account 
                add = messagebox.askyesno("Add Password", "Do you want to add this password to your account?") 
                if add: 
                    addfrom(pwd, pin) 
                    addfrom_frame.grid_forget() 
                    generate_frame.grid_forget() 
                    main_frame.grid() 

            else: 
                messagebox.showerror("Error", "Something went wrong. Please try again.") 

    except Exception as e: 
        messagebox.showerror("Error", str(e)) 
        count -= 1 
        tries_label.config(text="You have " + str(count) + " tries left") 
        if count == 0: 
            generate_frame.grid_forget() 

 

# Function to test password strength    
def strength_test(): 
    global count 
    try: 
        pin = Spin_entry.get() 
        pincheck = cursor.execute(f"SELECT pins FROM MasterPasswords WHERE pins={pin}") 
        pin2 = pincheck.fetchone() 

        if pin2 is None: 
            messagebox.showerror("pin is incorrect") 
            count=count-1 
            Stries_label.config(text="You have " + str(count) + " chances left") 

            if count==0: 
                messagebox.showerror("you have no more chances left") 
           
            pin2 = pin2[0] 
            pin2 = int(pin2) 
            print(pin2) 

            if int(pin) == pin2: 
                messagebox.showinfo("pin is correct") 

                
                pwd=pwd_entry.get() 
                #checks if the password is more than or equal to 8 characters 
                if len(pwd) >= 8: 
                    #checks if the password has at least one uppercase letter and lowercase 
                    if any(chr.islower() for chr in pwd)==True and any(chr.isupper() for chr in pwd)==True: 
                        #checks if the password has at least one digit 
                        if any(chr.isdigit() for chr in pwd)==True: 
                            #checks if the password has at least one special character 
                            if pwd.isalnum()==False: 
                                messagebox.showinfo("Password strength: Strong") 
                                add = messagebox.askyesno("do you want to add this password to your account yes or no") 
                                if add == "yes": 
                                    addfrom(pwd,pin) 
                                    addfrom_frame.grid_forget() 
                                    strength_frame.grid_forget() 
                                    main_frame.grid() 
                                else: 
                                    strength_frame.grid_forget() 
                                    main_frame.grid() 
                            else: 
                                messagebox.showinfo("Password strength: Medium") 
                                changepwd = messagebox.askyesno("would you like to change the password y/anything else") 
                                    
                                if changepwd=="yes": 
                                    return 

                                else: 
                                    messagebox.showinfo("Password strength: Strong") 
                                    add = messagebox.askyesno("do you want to add this password to your account yes or no") 

                                    if add == "yes": 
                                        addfrom(pwd,pin) 
                                        addfrom_frame.grid_forget() 
                                        strength_frame.grid_forget() 
                                        main_frame.grid() 

                                    else: 
                                        strength_frame.grid_forget() 
                                        main_frame.grid() 

                        else: 
                            messagebox.showerror("Password strength: Weak. You need to make it stronger") 

                    else: 
                        messagebox.showerror("Password strength: very weak. You need to make it stronger")
            
                else: 
                    messagebox.showerror("password too weak. Make a new one") 

    except: 
        messagebox.showerror("pin is incorrect") 
        count=count-1 
        tries_label.config(text="You have "+ str(count)+ " tries left") 
        if count==0: 
            strength_frame.grid_forget() 

#shows the user's profile details 
def viewP(): 
    try: 
                while True: 
                    search = Esearch_entry.get() 
                    value = Evalue_entry.get() 
                    value1 = ENvalue_entry.get() 

                    if search == "username" or search == "Passwords" or search == "email" or search == "website_name" or search == "url": 
                        cursor.execute(f"SELECT * FROM Passwords WHERE {search}='{value}'") 
                        results= cursor.fetchall() 
                        messagebox.showinfo(results) 
                        viewP_frame.grid_forget() 
                        main_frame.grid()                         

                    else: 
                        messagebox.showerror("you can only change username, password, email, website name, website url") 
                        continue 

    except: 
        messagebox.showerror("something went wrong, please try again") 
 
#changes the profile details 
def editP(): 
    while True: 
        try: 
                    search = Esearch_entry.get() 
                    value = Evalue_entry.get() 
                    value1 = ENvalue_entry.get() 

                    if search == "username" or search == "Passwords" or search == "email" or search == "website_name" or search == "url": 
                        cursor.execute(f"SELECT * FROM Passwords WHERE {search}='{value}'") 
                        results= cursor.fetchall() 
                        print(results) 
                        
                        change = messagebox.askyesno("is this the imformation you want to change?") 
                        if change == "yes": 
                            cursor.execute(f"UPDATE Passwords SET {search}='{value1}' WHERE {search}='{value}'") 
                            messagebox.showinfo("information changed") 
                            change_frame.grid_forget() 
                            main_frame.grid() 

                    else: 
                        messagebox.showerror("you can only change username, password, email, website name, website url") 
                        continue 

        except: 
            messagebox.showerror("something went wrong, please try again") 
             
 
def deleteP(): 
    try: 
            pin = DPpin_entry.get() 
            pincheck = cursor.execute(f"SELECT pins FROM MasterPasswords WHERE pins={pin}") 
            pin2 = pincheck.fetchone() 

            if pin2 is None: 
                messagebox.showerror("pin is incorrect") 
                count = count-1
                Dtries_label.config(text="You have " + str(count) + " chances left") 
                if count==0: 
                    messagebox.showerror("you have no more chances left") 

            pin2 = pin2[0] 
            pin2 = int(pin2) 
            print(pin2) 
            if int(pin) == pin2: 
                messagebox.showinfo("pin is correct") 
                # Delete record from passwords table and closes teh tkinter window 
                cursor.execute(f"DELETE FROM MasterPasswords WHERE pins={pin}") 
                messagebox.showinfo("profile deleted successfully") 
                root.destroy() 

    except: 
            messagebox.showerror("something went wrong, please try again") 

# Function to handle user registration 
def register(): 
    # Get user input from registration form 
    username = Rusername_entry.get() 
    MPassword = RMpassword_entry.get() 
    ConfirmMPassword = Rconfirm_password_entry.get() 
    pin = Rpin_entry.get() 
    email = Remail_entry.get() 
    hint = Rhint_entry.get() 
 
   # Check if pin already exists 
    pincheck = cursor.execute(f"SELECT pins FROM MasterPasswords WHERE pins = ?", (pin,)) 
    pin2 = pincheck.fetchone() 
    if pin2 is not None: 
        messagebox.showerror("Error", "Pin already exists") 
        return 

    # Check validity of input data 
    if MPassword.isalnum() == True: 
        messagebox.showerror("Error", "Password must have special characters") 
        return 
    
    if not(len(MPassword) > 7): 
        messagebox.showerror("Error", "Password must have 7 or more characters")
        return
    if ConfirmMPassword != MPassword: 
        messagebox.showerror("Error", "Passwords do not match") 
        return 

    if len(pin) != 4 or not pin.isdigit(): 
        messagebox.showerror("Error", "Pin must have 4 digits") 
        return 

    if '@' not in email: 
        messagebox.showerror("Error", "Invalid Email") 
        return 

    # Insert user details into MasterPasswords table 
    cursor.execute("INSERT INTO MasterPasswords VALUES (?,?,?,?,?)", (MPassword,username,int(pin),email,hint)) 
    con.commit() 
    messagebox.showinfo("Registration Successful", "You have successfully registered") 
    register_frame.grid_forget() 
    login_frame.grid() 
 
# Function to handle user login 
def login(): 
        global count 
        username = username_entry.get() 
        Mpassword = Mpassword_entry.get() 
        pin = pin_entry.get() 
 
        try: 
                # Using parameterized query to prevent SQL injection 
            cursor.execute("SELECT * FROM MasterPasswords WHERE usernames = ? AND masterPassword = ? AND pins = ?", (username, Mpassword, pin)) 
            if cursor.fetchone(): 
                messagebox.showinfo("Login Successful", "Welcome, " + username + "!") 
                main(username) 
                return  # Exit function after successful login 
            
            else: 
                #if the login check fails then the count 
                messagebox.showerror("Login Failed", "Invalid username, password, or pin") 
                count -= 1 
                tries_label.config(text="You have " + str(count) + " tries left") 
 
            if count == 2: 
                hint = messagebox.askyesno("Hint", "Would you like to see your hint?") 
                
                if hint: 
                    try: 
                        cursor.execute("SELECT hint FROM MasterPasswords WHERE usernames = ?", (username,)) 
                        results = cursor.fetchone() 
                        
                        if results: 
                            messagebox.showinfo("Hint", "Hint: " + results[0]) 

                        else: 
                            messagebox.showerror("Error", "No hint found for this user") 

                    except sqlite3.Error as e: 
                        messagebox.showerror("Error", "Failed to retrieve hint: " + str(e)) 

        except sqlite3.Error as e: 
            messagebox.showerror("Database Error", "An error occurred while accessing the database: " + str(e)) 
            return 

        if count==0: 
            messagebox.showerror("Error", "No more tries left")
            login_frame.grid_forget()
 
# Function to switch to main frame after successful login 
def main(username): 
    login_frame.grid_forget() 
    global current
    current = main_frame
    main_frame.grid() 
    welcome_label.config(text="Welcome, " + username + "!")  

root = tk.Tk() 
root.title("Farrell's Password manager") 
 
# Create initial window 
LorR_frame = tk.Frame(root) 
LorR_frame.grid(padx=10, pady=10) 
 
# Add buttons for login and register 
LButton = tk.Button(LorR_frame, text="Login", command=gologin) 
LButton.grid(row=0, column=0, columnspan=2, padx=5, pady=5) 
 
Rbutton = tk.Button(LorR_frame, text="Register", command=goregister) 
Rbutton.grid(row=0, column=2, columnspan=2, padx=5, pady=5)  

# Create register window 
register_frame = tk.Frame(root) 
register_frame.grid(padx=10, pady=10) 
register_frame.grid_forget() 
 
# Add labels and entry fields for registration 
Rusername_label = tk.Label(register_frame, text="Username:") 
Rusername_label.grid(row=0, column=0, padx=5, pady=5)
Rusername_entry = tk.Entry(register_frame) 
Rusername_entry.grid(row=0, column=1, padx=5, pady=5) 
 
RMpassword_label = tk.Label(register_frame, text="Master Password:") 
RMpassword_label.grid(row=1, column=0, padx=5, pady=5) 
RMpassword_entry = tk.Entry(register_frame, show="*")
RMpassword_entry.grid(row=1, column=1, padx=5, pady=5) 
 
Rconfirm_passord_label = tk.Label(register_frame, text="Confirm Master Password:") 
Rconfirm_passord_label.grid(row=2, column=0, padx=5, pady=5) 
Rconfirm_password_entry = tk.Entry(register_frame, show="*")
Rconfirm_password_entry.grid(row=2, column=1, padx=5, pady=5) 
 
Rpin_label = tk.Label(register_frame, text="Pin (4 digits):") 
Rpin_label.grid(row=3, column=0, padx=5, pady=5) 
Rpin_entry = tk.Entry(register_frame, show="*")
Rpin_entry.grid(row=3, column=1, padx=5, pady=5)  

Remail_label = tk.Label(register_frame, text="Email:") 
Remail_label.grid(row=4, column=0, padx=5, pady=5) 
Remail_entry = tk.Entry(register_frame) 
Remail_entry.grid(row=4, column=1, padx=5, pady=5) 
 
Rhint_label = tk.Label(register_frame, text="Hint (Reminder of Password):") 
Rhint_label.grid(row=5, column=0, padx=5, pady=5) 
Rhint_entry = tk.Entry(register_frame) 
Rhint_entry.grid(row=5, column=1, padx=5, pady=5) 

# Add register button 
register_button = tk.Button(register_frame, text="Register", command=register) 
register_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

back_button = tk.Button(register_frame, text="Back", command=gobackregister)
back_button.grid(row=6, column=1, columnspan=1, padx=3,)
 
# Create login window 
login_frame = tk.Frame(root) 
login_frame.grid(padx=10, pady=10) 
login_frame.grid_forget() 

# Add labels, entry fields, and login button 
username_label = tk.Label(login_frame,text="Username:") 
username_label.grid(row=0, column=0, padx=5, pady=5) 
username_entry = tk.Entry(login_frame) 
username_entry.grid(row=0, column=1, padx=5, pady=5) 

Mpassword_label = tk.Label(login_frame, text="Password:") 
Mpassword_label.grid(row=1, column=0, padx=5, pady=5) 
Mpassword_entry = tk.Entry(login_frame, show="*") 
Mpassword_entry.grid(row=1, column=1, padx=5, pady=5) 

pin_label = tk.Label(login_frame, text="Pin:") 
pin_label.grid(row=2, column=0, padx=5, pady=5) 
pin_entry = tk.Entry(login_frame, show="*") 
pin_entry.grid(row=2, column=1, padx=5, pady=5) 
 
login_button = tk.Button(login_frame, text="Login", command=login) 
login_button.grid(row=3,column =0, columnspan=2, padx=5, pady=5)

back_button = tk.Button(login_frame, text="Back", command=gobacklogin)
back_button.grid(row=3, column=1, columnspan=1, padx=3,)
 
tries_label = tk.Label(login_frame, text="") 
tries_label.grid(row=4, columnspan=2) 
 
# Create main window 
main_frame = tk.Frame(root) 
welcome_label = tk.Label(main_frame, text="") 
welcome_label.grid(padx=10, pady=10) 
main_frame.grid_forget() 
 
# Buttons to go to features 
PasswordGenerator_button = tk.Button(main_frame, text="Password Generator", command=gogenerate) 
PasswordGenerator_button.grid(row= 1, column=0, columnspan=1,padx=5, pady=5) 

PasswordStrength_button = tk.Button(main_frame, text="Password Strength", command=gostrength) 
PasswordStrength_button.grid(row= 2, column=0, columnspan=1,padx=5, pady=5) 

Add_button = tk.Button(main_frame, text="Add Password", command=goadd) 
Add_button.grid(row= 3,column=0, columnspan=1,padx=5, pady=5) 

Delete_button = tk.Button(main_frame, text="Delete Password", command=godelete) 
Delete_button.grid(row= 4, column=0, columnspan=1,padx=5, pady=5) 

Change_button = tk.Button(main_frame, text="Change Password", command=gochange) 
Change_button.grid(row= 5, column=0, columnspan=1,padx=5, pady=5) 

Settings_button = tk.Button(main_frame, text="Settings", command=gosettings) 
Settings_button.grid(row= 6, column=0, columnspan=1,padx=5, pady=5) 

Quit_button = tk.Button(main_frame, text="Quit", command=root.quit) 
Quit_button.grid(row= 7, column=0, columnspan=1,padx=5, pady=5) 

# Create add window 
add_frame = tk.Frame(root) 
add_frame.grid(padx=10, pady=10) 
add_frame.grid_forget()

Apin_label = tk.Label(add_frame, text="Pin:") 
Apin_label.grid(row=0, column=0, padx=5, pady=5) 
Apin_entry = tk.Entry(add_frame) 
Apin_entry.grid(row=0, column=1, padx=5, pady=5)

Ausername_label = tk.Label(add_frame, text="Username:") 
Ausername_label.grid(row=1, column=0, padx=5, pady=5) 
Ausername_entry = tk.Entry(add_frame) 
Ausername_entry.grid(row=1, column=1, padx=5, pady=5)  

Apassword_label = tk.Label(add_frame, text="Master Password:") 
Apassword_label.grid(row=2, column=0, padx=5, pady=5) 
Apassword_entry = tk.Entry(add_frame) 
Apassword_entry.grid(row=2, column=1, padx=5, pady=5) 

Aemail_label = tk.Label(add_frame, text="Email:") 
Aemail_label.grid(row=3, column=0, padx=5, pady=5) 
Aemail_entry = tk.Entry(add_frame) 
Aemail_entry.grid(row=3, column=1, padx=5, pady=5) 

AwebsiteURL_label = tk.Label(add_frame, text="website URl:") 
AwebsiteURL_label.grid(row=4, column=0, padx=5, pady=5) 
AwebsiteURL_entry = tk.Entry(add_frame) 
AwebsiteURL_entry.grid(row=4, column=1, padx=5, pady=5) 

AwebsiteName_label = tk.Label(add_frame, text="Website Name:") 
AwebsiteName_label.grid(row=5, column=0, padx=5, pady=5) 
AwebsiteName_entry = tk.Entry(add_frame) 
AwebsiteName_entry.grid(row=5, column=1, padx=5, pady=5) 
 
Atries_label = tk.Label(add_frame, text="") 
Atries_label.grid(row=6, columnspan=2) 

add_button = tk.Button(add_frame, text="Add", command=add) 
add_button.grid(row=7, column=0, columnspan=1,padx=5, pady=5)
 
Amenu = tk.Button(add_frame, text="Main Menu", command=gomenu) 
Amenu.grid(row=8, column=0, columnspan=1,padx=5, pady=5) 

#create delete window 
delete_frame = tk.Frame(root) 
delete_frame.grid(padx=10, pady=10) 
delete_frame.grid_forget() 

Dpin_label = tk.Label(delete_frame, text="Pin:") 
Dpin_label.grid(row=0, column=0, padx=5, pady=5) 
Dpin_entry = tk.Entry(delete_frame) 
Dpin_entry.grid(row=0, column=1, padx=5, pady=5) 

Dsearch_label = tk.Label(delete_frame, text="Search:") 
Dsearch_label.grid(row=1, column=0, padx=5, pady=5) 
Dsearch_entry = tk.Entry(delete_frame) 
Dsearch_entry.grid(row=1, column=1, padx=5, pady=5)

Dvalue_label = tk.Label(delete_frame, text= "value you want to delete:") 
Dvalue_label.grid(row=2, column=0, padx=5, pady=5) 
Dvalue_entry = tk.Entry(delete_frame) 
Dvalue_entry.grid(row=2, column=1, padx=5, pady=5) 

DNvalue_label = tk.Label(delete_frame, text= "New value:") 
DNvalue_label.grid(row=3, column=0, padx=5, pady=5) 
DNvalue_entry = tk.Entry(delete_frame) 
DNvalue_entry.grid(row=3, column=1, padx=5, pady=5) 

Dtries_label = tk.Label(delete_frame, text="") 
Dtries_label.grid(row=3, columnspan=2) 

delete_button = tk.Button(delete_frame, text="Delete", command=delete) 
delete_button.grid(row=4, column=0, columnspan=1,padx=5, pady=5) 

Dmenu = tk.Button(delete_frame, text="Main Menu", command=gomenu) 
Dmenu.grid(row=5, column=0, columnspan=1,padx=5, pady=5) 

#create change window 
change_frame = tk.Frame(root) 
change_frame.grid(padx=10, pady=10) 
change_frame.grid_forget() 

Cpin_label = tk.Label(change_frame, text="Pin:") 
Cpin_label.grid(row=0, column=0, padx=5, pady=5) 
Cpin_entry = tk.Entry(change_frame) 
Cpin_entry.grid(row=0, column=1, padx=5, pady=5) 

Csearch_label = tk.Label(change_frame, text="Search:") 
Csearch_label.grid(row=1, column=0, padx=5, pady=5) 
Csearch_entry = tk.Entry(change_frame) 
Csearch_entry.grid(row=1, column=1, padx=5, pady=5)

Cvalue_label = tk.Label(change_frame, text= "value you want to change:") 
Cvalue_label.grid(row=2, column=0, padx=5, pady=5) 
Cvalue_entry = tk.Entry(change_frame) 
Cvalue_entry.grid(row=2, column=1, padx=5, pady=5)
 
CNvalue_label = tk.Label(change_frame, text= "New value:") 
CNvalue_label.grid(row=3, column=0, padx=5, pady=5) 
CNvalue_entry = tk.Entry(change_frame) 
CNvalue_entry.grid(row=3, column=1, padx=5, pady=5) 

Ctries_label = tk.Label(change_frame, text="") 
Ctries_label.grid(row=4, columnspan=2) 

change_button = tk.Button(change_frame, text="Change", command=change) 
change_button.grid(row=5, column=0, columnspan=1,padx=5, pady=5) 

Cmenu = tk.Button(change_frame, text="Main Menu", command=gomenu) 
Cmenu.grid(row=6, column=0, columnspan=1,padx=5, pady=5) 

#create generate window 
generate_frame = tk.Frame(root) 
generate_frame.grid(padx=10, pady=10) 
generate_frame.grid_forget() 

Gpin_label = tk.Label(generate_frame, text="Pin:") 
Gpin_label.grid(row=0, column=0, padx=5, pady=5) 
Gpin_entry = tk.Entry(generate_frame) 
Gpin_entry.grid(row=0, column=1, padx=5, pady=5) 
 
length_label = tk.Label(generate_frame, text="Length of password(has to be greater than 8):") 
length_label.grid(row=1, column=0, padx=5, pady=5) 
length_entry = tk.Entry(generate_frame) 
length_entry.grid(row=1, column=1, padx=5, pady=5) 

Gtries_label = tk.Label(generate_frame, text="") 
Gtries_label.grid(row=2, columnspan=2) 

generated = tk.Label(generate_frame, text="") 
generated.grid(row=4,column=0, columnspan=2) 

generate_button = tk.Button(generate_frame, text="Generate", command=generate) 
generate_button.grid(row=3, column=0, columnspan=1,padx=5, pady=5) 

Gmenu = tk.Button(generate_frame, text="Main Menu", command=gomenu) 
Gmenu.grid(row=5, column=0, columnspan=1,padx=5, pady=5) 

#create strength test window 
strength_frame = tk.Frame(root) 
strength_frame.grid(padx=10, pady=10) 
strength_frame.grid_forget() 

Spin_label = tk.Label(strength_frame, text="Pin:") 
Spin_label.grid(row=0, column=0, padx=5, pady=5) 
Spin_entry = tk.Entry(strength_frame) 
Spin_entry.grid(row=0, column=1, padx=5, pady=5) 

pwd_label = tk.Label(strength_frame, text="Password:") 
pwd_label.grid(row=1, column=0, padx=5, pady=5) 
pwd_entry = tk.Entry(strength_frame) 
pwd_entry.grid(row=1, column=1, padx=5) 

Stries_label = tk.Label(strength_frame, text="") 
Stries_label.grid(row=2, columnspan=2) 
 
strength_button = tk.Button(strength_frame, text="Check Strength", command=strength_test) 
strength_button.grid(row=3, column=0, columnspan=1,padx=5, pady=5) 

Smenu = tk.Button(strength_frame, text="Main Menu", command=gomenu) 
Smenu.grid(row=4, column=0, columnspan=1,padx=5, pady=5) 
 
# create addfrom window 
addfrom_frame = tk.Frame(root) 
addfrom_frame.grid(padx=10, pady=10) 
addfrom_frame.grid_forget() 

AFusername_label = tk.Label(addfrom_frame, text="Username:") 
AFusername_label.grid(row=1, column=0, padx=5, pady=5) 
AFusername_entry = tk.Entry(addfrom_frame) 
AFusername_entry.grid(row=1, column=1, padx=5, pady=5) 

AFemail_label = tk.Label(addfrom_frame, text="Email:") 
AFemail_label.grid(row=2, column=0, padx=5, pady=5) 
AFemail_entry = tk.Entry(addfrom_frame) 
AFemail_entry.grid(row=2, column=1, padx=5, pady=5) 

AFwebsiteURL_label = tk.Label(addfrom_frame, text="Confirm Master Password:") 
AFwebsiteURL_label.grid(row=3, column=0, padx=5, pady=5) 
AFwebsiteURL_entry = tk.Entry(addfrom_frame) 
AFwebsiteURL_entry.grid(row=3, column=1, padx=5, pady=5) 

AFwebsiteName_label = tk.Label(addfrom_frame, text="Pin (4 digits):") 
AFwebsiteName_label.grid(row=4, column=0, padx=5, pady=5) 
AFwebsiteName_entry = tk.Entry(addfrom_frame) 
AFwebsiteName_entry.grid(row=4, column=1, padx=5, pady=5) 

#create settings window 
settings_frame = tk.Frame(root) 
settings_frame.grid(padx=10, pady=10) 
settings_frame.grid_forget() 

viewProfile_button = tk.Button(settings_frame, text="View Profiles", command=goviewP) 
viewProfile_button.grid(row=0, column=0, columnspan=1,padx=5, pady=5) 

editProfile_button = tk.Button(settings_frame, text="Edit Profile", command=goeditP) 
editProfile_button.grid(row=1, column=0, columnspan=1,padx=5, pady=5) 

deleteProfile_button = tk.Button(settings_frame, text="Delete Profile", command=godeleteP) 
deleteProfile_button.grid(row=2, column=0, columnspan=1,padx=5, pady=5) 

Semenu = tk.Button(settings_frame, text="Main Menu", command=gomenu) 
Semenu.grid(row=3, column=0, columnspan=1,padx=5, pady=5) 

#create view profiles window 
viewP_frame = tk.Frame(root) 
viewP_frame.grid(padx=10, pady=10) 
viewP_frame.grid_forget() 

Vsearch_label = tk.Label(viewP_frame, text="Search:") 
Vsearch_label.grid(row=1, column=0, padx=5, pady=5) 
Vsearch_entry = tk.Entry(viewP_frame) 
Vsearch_entry.grid(row=1, column=1, padx=5, pady=5) 

viewP_button = tk.Button(viewP_frame, text="View", command=viewP) 
viewP_button.grid(row=2, column=0, columnspan=1,padx=5, pady=5) 

Vsettings = tk.Button(viewP_frame, text="Settings", command=gosettings) 
Vsettings.grid(row=3, column=0, columnspan=1,padx=5, pady=5) 

#create edit profiles window 
editP_frame = tk.Frame(root) 
editP_frame.grid(padx=10, pady=10) 
editP_frame.grid_forget() 

Esearch_label = tk.Label(editP_frame, text="Search:") 
Esearch_label.grid(row=1, column=0, padx=5, pady=5) 
Esearch_entry = tk.Entry(editP_frame) 
Esearch_entry.grid(row=1, column=1, padx=5, pady=5) 

Evalue_label = tk.Label(editP_frame, text= "value you want to change:") 
Evalue_label.grid(row=2, column=0, padx=5, pady=5) 
Evalue_entry = tk.Entry(editP_frame) 
Evalue_entry.grid(row=2, column=1, padx=5, pady=5)

ENvalue_label = tk.Label(editP_frame, text= "New value:") 
ENvalue_label.grid(row=3, column=0, padx=5, pady=5) 
ENvalue_entry = tk.Entry(editP_frame) 
ENvalue_entry.grid(row=3, column=1, padx=5, pady=5) 

editP_button = tk.Button(editP_frame, text="Edit", command=editP) 
editP_button.grid(row=4, column=0, columnspan=1,padx=5, pady=5) 

Esettings = tk.Button(editP_frame, text="Settings", command=gosettings) 
Esettings.grid(row=5, column=0, columnspan=1,padx=5, pady=5)

#delete profile window 
deleteP_frame = tk.Frame(root) 
deleteP_frame.grid(padx=10, pady=10) 
deleteP_frame.grid_forget() 

DPpin_label = tk.Label(deleteP_frame, text="Pin:") 
DPpin_label.grid(row=1, column=0, padx=5, pady=5) 
DPpin_entry = tk.Entry(deleteP_frame) 
DPpin_entry.grid(row=1, column=1, padx=5, pady=5)

deleteP_button = tk.Button(deleteP_frame, text="Delete", command=deleteP) 
deleteP_button.grid(row=2, column=0, columnspan=1,padx=5, pady=5) 

Dsettings = tk.Button(deleteP_frame, text="Settings", command=gosettings) 
Dsettings.grid(row=3, column=0, columnspan=1,padx=5, pady=5)

root.mainloop()
