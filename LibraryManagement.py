library = {
    'DELD': 3,
    'OOP': 4,
    'CG': 4,
    'DM': 5,
    'UHV': 2
}  

print(library)  # Printing the dictionary



def avg(library):
    total_borrowed = sum(library.values())  # sum() calculates the total number of books borrowed.
    total_books = len(library)  # lfor book_key in frequent_books:en() finds the total number of unique books in the library.
    average = (total_borrowed / total_books)  # The average is calculated by dividing the total borrowed by the total number of books.
    return average

a = avg(library)  
print("The average of books borrowed:", a)

                                                                                                                         

def highest_lowest(library): 

    highest = max(library, key=library.get)  
    lowest = min(library, key=library.get)  # min() finds the key (book) with the minimum value.
    
    return highest, lowest


highest, lowest = highest_lowest(library)
print("The highest borrowed book",highest)
print("The lowest borrowed book", lowest)



def most_frequent_book(library):

    max_count = max(library.values())  
    
    most_frequent = [book for book, count in library.items() if count == max_count]  
    
    return most_frequent

frequent_books = most_frequent_book(library)
print("Most frequently borrowed books ", frequent_books)  
print("Most frequently borrowed book(s) and their count:")
for book_key in frequent_books: 

    print(f"{book_key}: {library[book_key]}")