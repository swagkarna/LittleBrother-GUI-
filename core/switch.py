from tkinter import *
from tkinter import messagebox

# setting switch function:
def switch(self, navself, topFrame, btnState):
    # dictionary of colors:
    color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

    if btnState is True:
            # create animated Navbar closing:
            for x in range(301):
                navself.place(x=-x, y=0)
                topFrame.update()

            # resetting widget colors:
            topFrame.config(bg="#252726")

            # turning button OFF:
            btnState = False
    else:
        # make self dim:
        topFrame.config(bg="#252726")

        # created animated Navbar opening:
        for x in range(-300, 0):
            navself.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True

# to show profile if exist
def seeProfle(navself):
    return messagebox.showinfo("info ","seeprofile")

# to show all existing profile in database
def allprofile(navself):
    return messagebox.showinfo("info","allprofile")


# to create a profile
def createprofile(navself):
    navself = Toplevel(navself)
    navself.title("Create Profile")
    navself.minsize(713, 398)
    navself.maxsize(713, 398)
    navself.config(bg="grey17")
    ltxt = ["Profile Name:"]
    for i in ltxt:
        Label(navself, text=i, bg="grey17", fg="red", font=("comicsansms", 15, "bold"), relief=FLAT).place(x=5, y=20)
    p1 = Entry(navself)
    p1.place(x=150, y=20)
    Label(navself, text="(Format: First name Last name)", bg="grey17", fg="red", font=("comicsansms", 10, "bold"), relief=FLAT).place(x=100, y=50)
    Button(navself, text="submit", command=lambda:).place(x=50, y=100)
    navself.mainloop()

# to decrypte hash
def hashdecrypter(navself):
    return messagebox.showinfo("info","hash")

def Person_lookup(navself):
    return messagebox.showinfo("info","Person_lookup")

def Mail_tracer(navself):
    return messagebox.showinfo("info", "Mail_tracer")


def Username_lookup(navself):
    return messagebox.showinfo("info", "Username_lookup")


def Employees_search(navself):
    return messagebox.showinfo("info", "Employees_search")


def Lookup_address(navself):
    return messagebox.showinfo("info", "Lookup_address")


def Google_search(navself):
    return messagebox.showinfo("info", "Google_search")


def Phone_lookup(navself):
    return messagebox.showinfo("info", "Phone_lookup")


def Facebook_GraphSearch(navself):
    return messagebox.showinfo("info", "Facebook_GraphSearch")


def IP_lookup(navself):
    return messagebox.showinfo("info", "IP_lookup")


def twitter_info(navself):
    return messagebox.showinfo("info", "twitter_info")


def SSID_locator(navself):
    return messagebox.showinfo("info", "SSID_locator")


def instagram_info(navself):
    return messagebox.showinfo("info","instagram_info")

def Email_lookup(navself):
    return messagebox.showinfo("info","Email_lookup")

def FR(navself):
    return messagebox.showinfo("info","FR")

def LU(navself):
    return messagebox.showinfo("info","LU")

def BE(navself):
    return messagebox.showinfo("info","BE")

def All(navself):
    return messagebox.showinfo("info","ALL")

def CH(navself):
    return messagebox.showinfo("info","CH")
