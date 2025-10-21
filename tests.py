# tests.py
from operations import *

# Reset data
books.clear()
members.clear()

assert add_book("101", "Python", "John", "Non-Fiction", 3) == True
assert add_book("101", "Duplicate", "John", "Non-Fiction", 3) == False
assert add_member("M001", "Alice", "a@example.com") == True
assert add_member("M001", "Duplicate", "a@example.com") == False
assert borrow_book("101", "M001") == True
assert borrow_book("101", "M001") == True
assert borrow_book("101", "M001") == True
assert borrow_book("101", "M001") == False  # exceeds limit
assert return_book("101", "M001") == True
assert delete_member("M001") == False  # still has borrowed books

print("✅ All tests passed successfully!")
