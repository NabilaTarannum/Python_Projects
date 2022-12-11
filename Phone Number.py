import phonenumbers
from phonenumbers import geocoder, carrier
import pycountry
from phone_iso3166.country import phone_country


def phone_numbers():
    enter = input("Enter a phone number with country code :")
    code = phone_country(enter)
    number = phonenumbers.parse(enter)
    operator = carrier.name_for_number(number, "en")
    country = geocoder.description_for_number(number, "en")
    py_country = pycountry.countries.get(alpha_2=code)
    tracker = (operator, country, py_country, number)
    print(tracker)


phone_numbers()
