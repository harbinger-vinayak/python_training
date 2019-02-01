import re
import time
import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ECONOMY = 'Economy'
BUSINESS = 'Business'
WINDOW = 'Window'
MIDDLE = 'Middle'
AISLE = 'Aisle'


class Seat:
    def __init__(self, row_number, letter):
        self.row_number = row_number
        self.letter = letter

    def __str__(self):
        return '{}{}'.format(self.row_number, self.letter)


class SeatingArea:
    def __init__(self, booking_class, start_row, row_count, seats_per_row):
        self.booking_class = booking_class
        self.window_seat_count = row_count * 2
        self.aisle_seat_count = row_count * 2
        self.seat_count = row_count * seats_per_row
        self.middle_seat_count = self.seat_count - (self.window_seat_count + self.aisle_seat_count)
        self.seats_remaining = []
        self.window_remaining = []
        self.aisle_remaining = []
        self.middle_remaining = []

        for wrn in range(self.window_seat_count):
            w_new_seat = Seat(wrn, letters[wrn])
            self.window_remaining.append(w_new_seat)

        for arn in range(self.aisle_seat_count):
            a_new_seat = Seat(arn, letters[arn])
            self.aisle_remaining.append(a_new_seat)

        for mrn in range(self.middle_seat_count):
            m_new_seat = Seat(mrn, letters[mrn])
            self.middle_remaining.append(m_new_seat)


class Flight:
    def __init__(self, economy_seats, business_seats):
        self.seating_areas = {
            ECONOMY: economy_seats,
            BUSINESS: business_seats}

    def remaining_seat_count(self, booking_class):
        # return len(self.seating_areas[booking_class].seats_remaining)
        window_seat = len(self.seating_areas[booking_class].window_remaining)
        aisle_seat = len(self.seating_areas[booking_class].aisle_remaining)
        middle_seat = len(self.seating_areas[booking_class].middle_remaining)
        total_seat = window_seat + aisle_seat + middle_seat
        return total_seat

    def remaining_seat_count_window(self, booking_class):
        window_seat = len(self.seating_areas[booking_class].window_remaining)
        return window_seat

    def remaining_seat_count_aisle(self, booking_class):
        aisle_seat = len(self.seating_areas[booking_class].aisle_remaining)
        return aisle_seat

    def remaining_seat_count_middle(self, booking_class):
        middle_seat = len(self.seating_areas[booking_class].middle_remaining)
        return middle_seat

    def get_seat(self, booking_class, seating_class):
        if seating_class == WINDOW:
            return self.seating_areas[booking_class].window_remaining.pop()
        elif seating_class == AISLE:
            return self.seating_areas[booking_class].aisle_remaining.pop()
        elif seating_class == MIDDLE:
            return self.seating_areas[booking_class].middle_remaining.pop()
        else:
            return self.seating_areas[booking_class].seats_remaining.pop()


class Passenger:
    def __init__(self, name):
        self.name = name
        self.booking_id = None
        self.seat = None
        self.seat_class = None
        self.message = None

    def book(self, flight, booking_class, seating_class):
        if flight.remaining_seat_count(booking_class) != 0:
            if flight.remaining_seat_count_window(booking_class) != 0 and seating_class == WINDOW:
                self.seat = flight.get_seat(booking_class, seating_class)
                self.booking_id = random.Random().randrange(1000, 10000)
                self.seat_class = WINDOW
                self.message = ""
                return True
            elif flight.remaining_seat_count_middle(booking_class) != 0:
                self.seat = flight.get_seat(booking_class, MIDDLE)
                self.booking_id = random.Random().randrange(1000, 10000)
                self.seat_class = MIDDLE
                self.message = "Sorry! Window seat is not available."
                return True

            if flight.remaining_seat_count_aisle(booking_class) != 0 and seating_class == AISLE:
                self.seat = flight.get_seat(booking_class, seating_class)
                self.booking_id = random.Random().randrange(1000, 10000)
                self.seat_class = AISLE
                self.message = ""
                return True
            elif flight.remaining_seat_count_middle(booking_class) != 0:
                self.seat = flight.get_seat(booking_class, MIDDLE)
                self.booking_id = random.Random().randrange(1000, 10000)
                self.seat_class = MIDDLE
                self.message = "Sorry! Aisle seat is not available."
                return True

            return True

        return False


business = SeatingArea(BUSINESS, start_row=1, row_count=1, seats_per_row=9)
economy = SeatingArea(ECONOMY, start_row=2, row_count=1, seats_per_row=6)
flight = Flight(economy, business)


class main():
    print '** Welcome to flight booking system **'
    while True:
        response = raw_input('\nDo you want to book a ticket now? ')
        match = re.search('yes|y', response, re.I)
        if not match:
            print 'Thanks for using flight booking system'
            break

        b_len = flight.remaining_seat_count(BUSINESS)
        e_len = flight.remaining_seat_count(ECONOMY)
        print '\nTotal number of seats available in Business class is {} and Economy class is {}: '.format(b_len, e_len)

        name = raw_input('\nWhat is passenger name: ')
        name_obj = Passenger(name)

        class_response = raw_input('which class you prefer (business/economy)? ')
        match = re.search('business|economy', class_response, re.I)

        if not match:
            print 'Thanks for using flight booking system, I am not able to understand your input'
            break

        # seat_response = raw_input('Do you have window or Aisle or Middle preferance? ')
        seat_response = raw_input('which seat you prefer (window/middle/aisle)? ')
        match = re.search('window|aisle|middle', seat_response, re.I)

        if class_response == 'economy':
            if seat_response == 'window':
                name_obj.book(flight, ECONOMY, WINDOW)
            elif seat_response == 'aisle':
                name_obj.book(flight, ECONOMY, AISLE)
            elif seat_response == 'middle':
                name_obj.book(flight, ECONOMY, MIDDLE)

        elif class_response == 'business':
            if seat_response == 'window':
                name_obj.book(flight, BUSINESS, WINDOW)
            elif seat_response == 'aisle':
                name_obj.book(flight, BUSINESS, AISLE)
            elif seat_response == 'middle':
                name_obj.book(flight, BUSINESS, MIDDLE)

        if not match:
            print 'Thanks for using flight booking system, I am not able to understand your input'
            break

        print '\nThanks, I am booking class {}, {} seat, waiting for 2 sec'.format(class_response, seat_response)
        time.sleep(2)
        print name_obj.message
        print 'Passenger Details - '
        print 'Name:', name
        print 'Seat Number:', name_obj.seat
        print 'Seat Class:', class_response
        print 'Seat Preference:', name_obj.seat_class
        print 'Booking ID:', name_obj.booking_id

main()
