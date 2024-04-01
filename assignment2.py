from datetime import date
from datetime import datetime


# artwork.py
class Artwork:
    """A class to represent an artwork"""

    def __init__(self, art_id=" ", title=" ", artist=" ", creation_date=date, historical_significance=" ",
                 exhibition_location=" "):
        self.art_id = art_id
        self.title = title
        self.artist = artist
        self.creation_date = creation_date
        self.historical_significance = historical_significance
        self.exhibition_location = exhibition_location

    def displayInformation(self):
        pass

    # Getters and setters
    def get_art_id(self):
        return self.art_id

    def set_art_id(self, art_id):
        self.art_id = art_id

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_artist(self):
        return self._artist

    def set_artist(self, artist):
        self._artist = artist

    def get_date_of_creation(self):
        return self._date_of_creation

    def set_date_of_creation(self, date_of_creation):
        self._date_of_creation = date_of_creation

    def get_historical_significance(self):
        return self._historical_significance

    def set_historical_significance(self, historical_significance):
        self._historical_significance = historical_significance

    def get_exhibition_location(self):
        return self._exhibition_location

    def set_exhibition_location(self, exhibition_location):
        self._exhibition_location = exhibition_location


class Visitor:
    """A class to represnet a visitor"""

    def __init__(self, name=" ", age=0):
        self._name = name
        self._age = age

    # Getters and setters
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age


class Visitor_category:
    """A class to represent the visitor category"""

    def __init__(self, age_range=None):
        self.age_range = age_range


class Ticket:
    """a class to reprenet a ticket"""

    def __init__(self, ticket_type=" ", price=0.0, date=None, visitor_info=None, details=" "):
        self.ticket_type = ticket_type
        self.price = price
        self.date = date
        self.visitor_info = visitor_info
        self.details = details

    # method to claculate the final price of the ticket
    def final_price(self):
        pass

    # method to display the details of the ticket
    def displayTicketDetails(self):
        pass

    # Getters and setters
    def get_ticket_type(self):
        return self._ticket_type

    def set_ticket_type(self, ticket_type):
        self._ticket_type = ticket_type

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    def get_visitor_info(self):
        return self._visitor_info

    def set_visitor_info(self, visitor_info):
        self._visitor_info = visitor_info

    def get_details(self):
        return self._details

    def set_details(self, details):
        self._details = details


class Pricing:
    """A class to represent the pricing"""

    def __init__(self, adult_price=0.0, child_price=0.0, group_discount=0.0, vat=0.0):
        self.adult_price = adult_price
        self.child_price = child_price
        self.group_discount = group_discount
        self.vat = vat

        # method to update the pricing information
        def updatePrices(self):
            pass

        # method to calculate the discounted price
        def calculateDiscountedPrice(self):
            pass

        # Getters and setters
        def get_adult_price(self):
            return self.adult_price

        def set_adult_price(self, adult_price):
            self.adult_price = adult_price

        def get_child_price(self):
            return self.child_price

        def set_child_price(self, child_price):
            self.child_price = child_price

        def get_group_discount(self):
            return self.group_discount

        def set_group_discount(self, group_discount):
            self.group_discount = group_discount

        def get_vat(self):
            return self.vat

        def set_vat(self, vat):
            self.vat = vat


class Exhibition:
    """A class to represent an exhibition"""

    def __init__(self, title=" ", location=" ", duration=" "):
        self.title = title
        self.location = location
        self.duration = duration

        # method to update the location of the exhibition
        def update_location(self):
            pass

        # Getters and setters
        def get_title(self):
            return self.title

        def set_title(self, title):
            self.title = title

        def get_location(self):
            return self.location

        def set_location(self, location):
            self.location = location

        def get_duration(self):
            return self.duration

        def set_duration(self, duration):
            self.duration = duration


class Location:
    """A class to represent a location"""

    def __init__(self, name, location_type):
        self.location_name = location_name

    def getCapacity(self):
        pass

        # Getters and setters
        def get_location_name(self):
            return self.location_name

        def set_location_name(self, location_name):
            self.location_name = location_name


class Event:
    """A class to represent a location"""

    def __init__(self, title=" ", location=" ", duration=" "):
        self.title = title
        self.location = location
        self.duration = duration

        # Getters and setters
        def get_title(self):
            return self.title

        def set_title(self, title):
            self.title = title

        def get_location(self):
            return self.location

        def set_location(self, location):
            self.location = location

        def get_duration(self):
            return self.duration

        def set_duration(self, duration):
            self.duration = duration

# Test Case 1: Adding a piece of Artwork to the museum catalog

artwork1 = Artwork("001", "Girl with a Pearl Earring", "Johannes Vermeer", "A manifestation of beauty in simplicity ", date(1665, 1, 1), "Permanent Gallery")
artwork2 = Artwork("002", "The Starry Night", "Vincent van Gogh", "Symbolizes Van Gogh's deteriorating mental state", date(1889, 6, 1), "Special Exhibition Hall")
museum_catalog= [artwork1, artwork2]

print("Museum Catalog:")
for artwork in museum_catalog:
    print("Artwork ID:", artwork.art_id)
    print("  Title:", artwork.title)
    print("  Artist:", artwork.artist)
    print("  Historical Significance:", artwork.historical_significance)
    print("  Date of Creation:", artwork.creation_date)
    print("  Location:", artwork.exhibition_location)

# Test Case 2: Opening a new exhibition or event
exhibition1 = Exhibition("Fundraising", "Exhibition Hall 011", "3 Days")
event1 = Event("Light Shows", "Outdoor Space", "5 Days")
# Adds exhibition and event to museum schedule
museum_schedule = [exhibition1, event1]

print("Museum Events:")
for event in museum_schedule:
    print("Title:", event.title)
    print("  Location:", event.location)
    print("  Duration:", event.duration)


# Test case 3: Purchasing of tickets
visitor1 = Visitor("Aisha", 19)
visitor_category1 = Visitor_category((18, 60))
visitor_category1 = Visitor_category((18, 60))
ticket1 = Ticket("Regular", 100.0, datetime.now(), visitor1, "General Admission")
ticket2 = Ticket("Child", 0.0, datetime.now(), visitor1, "Children under 18")
ticket3 = Ticket("Senior", 0.0, datetime.now(), visitor1, "Seniors above 60")
ticket4 = Ticket("Group", 70, datetime.now(), visitor1, "Group Discount")

total_bill = ticket1.price + ticket2.price + ticket3.price + ticket4.price
total_bill_with_vat = total_bill * 1.05

print("Ticket Details:")
print("   Regular Ticket:", ticket1.price, "AED")
print("   Child Ticket:", ticket2.price, "AED")
print("   Senior Ticket:", ticket3.price, "AED")
print("   Group Ticket:", ticket4.price, "AED")
print("Total Bill (including VAT):", total_bill_with_vat, "AED")

# Test Case 4: The purchase of tickets for a special event

special_event_ticket = Ticket("Special Event", 100.0, datetime.now(), visitor1, "VIP Pass")
print("Special Event Ticket Details:")
print("   Ticket Type:", special_event_ticket.ticket_type)
print("   Price:", special_event_ticket.price, "AED")
print("   Purchase Date:", special_event_ticket.date)
print("   Visitor Information:", special_event_ticket.visitor_info.get_name())
print("   Details:", special_event_ticket.details)