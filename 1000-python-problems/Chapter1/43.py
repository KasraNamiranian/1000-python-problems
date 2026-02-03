pages = int(input("Please enter your book's page number: "))
flash_size = int(input("Please enter your flash size in GB: "))
lines = pages * 30
lines_size = lines * 80
flash_size_b = flash_size * (1024**3)
number_of_books = flash_size_b / lines_size
print("Number of books this flash can store is: ",number_of_books)
