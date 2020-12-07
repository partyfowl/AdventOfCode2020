'''Advent of Code Day 5'''

class Seat:
    def __init__(self, code):
        '''
        Calculates the seat row, column, and ID based on the seat code, which is a binary object
        where:
        The first 7 digits represent the column, in which the 'F' character represents a 0, and
        the 'B' character represents a 1.
        The final 3 digits represent the row, in which the 'L' character represents a 0, and the
        'R' character represents a 1.
        '''
        self.code = code
        self.row = int(self.code[:7].replace('F', '0').replace('B', '1'), 2)
        self.column = int(self.code[7:].replace('L', '0').replace('R', '1'), 2)
        self.id = self.row * 8 + self.column

def main():
    '''
    Prints our seat ID as the only seat not seen in the list in 
    the provided text file, as well as the highest seat ID seen
    '''
    with open('day5.txt') as f:
        seating_chart = [Seat(_) for _ in f.read().split('\n')]
    seating_chart.sort(key=lambda _: _.id) # Sorting the chart by seat ID so that we can find our seat ID
    # Initialising loop variables
    previous_seat = None
    my_seat = None
    for seat in seating_chart:
        if previous_seat and (previous_seat.id == seat.id - 2):
            my_seat = seat.id - 1
            break
        previous_seat = seat
    print('Highest Seat ID:', seating_chart[-1].id)
    print('My seat:        ', my_seat)


if __name__ == "__main__":
    main()
