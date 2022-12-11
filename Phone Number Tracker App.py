from tkinter import Tk, Label, Button, Entry, CENTER
from phone_iso3166.country import phone_country
import phonenumbers
from phonenumbers import geocoder, carrier
import pycountry


class LocationTracker:
    def __init__(self, app):
        self.window = app
        self.window.title("Phone number Tracker")
        self.window.geometry("500x400")
        self.window.configure(bg="black")
        self.window.resizable(False, False)

        # ___________Application menu_____________
        Label(
            app,
            text="Enter a phone number",
            fg="cyan",
            font=("Times", 20, "bold", "italic"),
            bg="black",
        ).place(x=150, y=30)
        self.phone_number = Entry(
            app,
            bg="black",
            width=16,
            fg="#a6fb3f",
            font=("Times", 18, "bold", "italic"),
            relief="flat",
        )
        self.track_button = Button(
            app, fg="red", text="Track Country", bg="cyan", relief="sunk"
        )
        self.country_label = Label(
            app, fg="black", font=("Times", 20), bg="cyan", relief="flat"
        )
        self.test_label = Label(app, fg="black", font=("Times", 20), bg="cyan")

        # ___________Place widgets on the window______
        self.phone_number.place(x=165, y=120)
        self.track_button.place(x=185, y=200)
        self.country_label.place(x=150, y=280)
        self.test_label.place(x=200, y=320)

        # __________Linking button with countries ________
        self.track_button.bind("<Button-1>", self.phone_numbers)
        # 255757294146

    def phone_numbers(self, event):
        phone_number = self.phone_number.get()
        test = ""
        test_1 = ""
        number = phonenumbers.parse(phone_number)
        operator = carrier.name_for_number(number, "en")
        country = geocoder.description_for_number(number, "en")
        py_country = pycountry.countries.get(alpha_2=phone_country(phone_number))
        tracker = (operator, country, py_country, number)
        print(tracker)
        if py_country:
            test = py_country.official_name
            if operator:
                test_1 = operator
        self.test_label.configure(text=test_1)
        self.country_label.configure(text=test)


PhoneTracker = Tk()
MyApp = LocationTracker(PhoneTracker)
PhoneTracker.mainloop()
