"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """

    letters = ["A", "B", "C", "D"]
    for num in range(number):
        yield letters[num % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """

    seats_per_row = ("A", "B", "C", "D")
    count = 0
    row = 1

    while count < number:
        if row == 13:
            row += 1

        for letter in seats_per_row:
            yield f"{row}{letter}"
            count += 1
            if count == number:
                break

        row += 1


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seat_no_generator = generate_seats(len(passengers))
    passenger_seat_assignment = {passenger: seat_no_generator.__next__() for passenger in passengers}
    return passenger_seat_assignment
    


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        seat_flight_combined = seat+flight_id
        no_of_zeros_to_fill = 12-len(seat_flight_combined)
        yield seat_flight_combined+"0"*no_of_zeros_to_fill
