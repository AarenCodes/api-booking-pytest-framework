Auth
- create auth token
- invalid username
- invalid password
- missing username
- missing password

Booking create
- create booking with valid payload
- create booking with missing firstname negative test

Booking read
- create booking, capture bookingid, get booking by ID
- validate retrieved booking matches payload

Booking delete
- create booking
- create token
- delete booking
- verify deleted booking returns 404

Booking update
- create booking
- create token
- update booking with PUT
- validate updated response matches updated payload

Framework structure
- config/settings.py
- data payload files
- helper functions
- organized tests by module
- pytest + requests
- logging with -s
