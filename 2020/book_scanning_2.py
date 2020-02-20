import sys
from collections import namedtuple

# Handling input

class Library:
    def __init__(self, id, number_of_books, signup_duration, books_per_day, books, score=0):
        self.id = id
        self.number_of_books = number_of_books
        self.signup_duration = signup_duration
        self.books_per_day = books_per_day
        self.books = books
        self.score = score

file_name = sys.argv[1]
libraries = []
with open(f'{file_name}.in') as f:
    number_of_books, number_of_libraries, max_days = (int(value) for value in f.readline().strip().split(' '))
    books = [int(score) for score in f.readline().strip().split(' ')]

    remaining_time = max_days

    for i in range(number_of_libraries):
        number_of_books_in_library, days_to_finish_signup, books_shipped_per_day = (int(value) for value in f.readline().strip().split(' '))
        books_in_library = [int(book) for book in f.readline().strip().split(' ')]

        books_in_library.sort(key=lambda x: books[x], reverse=True)

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
books_seen = set()
while remaining_time > 0:
    print(remaining_time)

    library_with_max_score = ''
    max_score = 0
    for library in libraries:
        if library.signup_duration < remaining_time:
            library.books = [book for book in library.books if book not in books_seen]
            library.number_of_books = len(library.books)
            books_library_can_process = min(
                (remaining_time - library.signup_duration) * library.books_per_day, library.number_of_books
            )

            book_scores = (books[index] for index in library.books[0:books_library_can_process])
            score = sum(book_scores)

            if score >= max_score:
                library_with_max_score = library
                score = max_score
    if library_with_max_score == '':
        break
    remaining_time -= library_with_max_score.signup_duration
    libraries.remove(library_with_max_score)
    selected_libraries.append(library_with_max_score)
    for book in library_with_max_score.books:
        books_seen.add(book)

# Handling output
with open(f'{file_name}.out', 'w') as f:
    f.write(f'{len(selected_libraries)}\n')
    for library in selected_libraries:
        f.write(f'{library.id} {library.number_of_books}\n')
        f.write(' '.join((str(score) for score in library.books)) + '\n')
