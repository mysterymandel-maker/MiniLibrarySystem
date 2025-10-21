# demo.py
from operations import *

print("📚 MINI LIBRARY SYSTEM DEMO\n")

# --- Add Books ---
add_book("111", "Python Basics", "John Doe", "Non-Fiction", 5)
add_book("222", "Space Odyssey", "Arthur C. Clarke", "Sci-Fi", 3)
add_book("333", "Mystery Night", "Agatha Christie", "Mystery", 2)
add_book("444", "World History", "Jane Smith", "History", 4)
add_book("555", "Fantasy Realm", "Rick Jordan", "Fantasy", 6)

# --- Add Members ---
add_member("M001", "Alice Smith", "alice@example.com")
add_member("M002", "Bob Johnson", "bob@example.com")
add_member("M003", "Carol Lee", "carol@example.com")

# --- Borrow & Return ---
borrow_book("111", "M001")
borrow_book("222", "M002")
return_book("222", "M002")

# --- Search & Update ---
print("Search by author 'John':", search_books("John", by="author"))
update_book("111", title="Advanced Python", total_copies=10)

# --- Delete Member ---
delete_member("M003")

# --- Final State ---
print("\nBooks:", books)
print("Members:", members)
