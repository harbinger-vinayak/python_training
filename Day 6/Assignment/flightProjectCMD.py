import re, time

print '** Welcome to flight booking system **'
while True:
    response = raw_input('Do you want to book a ticket now? ')
    match = re.search('yes|y', response, re.I)
    if not match:
        print 'Thanks for using flight booking system'
        break

    print 'Total number of seats available in Business and economy class is: '

    name = raw_input('What is passenger name: ')

    class_response = raw_input('which class you prefer? ')
    match = re.search('business|economy', class_response, re.I)
    if not match:
        print 'Thanks for using flight booking system, I am not able to understand your input'
        break

    seat_response = raw_input('Do you have window or Aisle preferance? ')
    match = re.search('window|aisle', seat_response, re.I)
    if not match:
        print 'Thanks for using flight booking system, I am not able to understand your input'
        break

    print 'Thanks, I am booking class {}, {} seat, waiting for 2 sec'.format(class_response, seat_response)
    time.sleep(2)

    print 'Passenger {} has seat number {} and bookingId {}'.format(name, 1, 1)
