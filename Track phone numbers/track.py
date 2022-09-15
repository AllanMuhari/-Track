import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier



phonenumber = phonenumbers.parse("+254713982805", "GB")

x= input("Enter the phone number: ")

print(geocoder.description_for_number(phonenumber , 'en')) 