import sys
from collections import namedtuple

# Handling input

Library = namedtuple('Library', ['id', 'number_of_books', 'signup_duration', 'books_per_day', 'books'])

file_name = sys.argv[1]
libraries = []
with open(f'{file_name}.in') as f:
    number_of_books, number_of_libraries, max_days = (int(value) for value in f.readline().strip().split(' '))
    books = [int(score) for score in f.readline().strip().split(' ')]

    remaining_time = max_days

    for i in range(number_of_libraries):
        number_of_books_in_library, days_to_finish_signup, books_shipped_per_day = (int(value) for value in f.readline().strip().split(' '))
        books_in_library = [int(score) for score in f.readline().strip().split(' ')]
        books_in_library.sort(reverse=True)

        library = Library(
            i,
            number_of_books_in_library,
            days_to_finish_signup,
            books_shipped_per_day,
            books_in_library
        )
        libraries.append(library)

# Compute
selected_libraries = []
while remaining_time > 0:
    print(remaining_time)
    library_with_max_score = ''
    max_score = 0
    for library in libraries:
        books_library_can_process = min(
            (remaining_time - library.signup_duration) * library.books_per_day, library.number_of_books
        )
        score = sum(library.books[0:books_library_can_process])
        if score >= max_score:
            library_with_max_score = library
            score = max_score
    if library_with_max_score == '':
        break
    remaining_time -= library_with_max_score.signup_duration
    libraries.remove(library_with_max_score)
    selected_libraries.append(library_with_max_score)

# Handling output
with open(f'{file_name}.out', 'w') as f:
    f.write(f'{len(selected_libraries)}\n')
    for library in selected_libraries:
        f.write(f'{library.id} {library.number_of_books}\n')
        f.write(' '.join((str(score) for score in library.books)) + '\n')
