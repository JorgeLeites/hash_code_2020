import sys
from collections import namedtuple

# Handling input

Library = namedtuple('Library', ['id', 'number_of_books', 'signup_duration', 'books_per_day', 'books', 'score'])

file_name = sys.argv[1]
libraries = []
with open(f'{file_name}.in') as f:
    number_of_books, number_of_libraries, max_days = (int(value) for value in f.readline().strip().split(' '))
    books = [int(score) for score in f.readline().strip().split(' ')]
    for i in range(number_of_libraries):
        number_of_books_in_library, days_to_finish_signup, books_shipped_per_day = (int(value) for value in f.readline().strip().split(' '))
        books_in_library = [int(score) for score in f.readline().strip().split(' ')]
        
        score = min((max_days - days_to_finish_signup) * books_shipped_per_day, number_of_books_in_library)

        library = Library(
            i,
            number_of_books_in_library,
            days_to_finish_signup,
            books_shipped_per_day,
            books_in_library,
            score
        )
        libraries.append(library)
        libraries.sort(key=lambda x: x.score, reverse=True)

# Compute
total_sum = 0
selected_libraries = []
for library in libraries:
    days_sum = total_sum + library.signup_duration
    if days_sum <= max_days:
        total_sum = days_sum
        selected_libraries.append(library)
    else:
        break

# Handling output
with open(f'{file_name}.out', 'w') as f:
    f.write(f'{len(selected_libraries)}\n')
    for library in selected_libraries:
        f.write(f'{library.id} {library.number_of_books}\n')
        f.write(' '.join((str(score) for score in library.books)) + '\n')
