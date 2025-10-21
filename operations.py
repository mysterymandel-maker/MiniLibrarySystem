# operations.py
"""
Mini Library Management System Core Functions
Uses only lists, dictionaries, and tuples (no OOP)
"""

# ----- Global Data -----
GENRES = ("Fiction", "Non-Fiction", "Sci-Fi", "History", "Fantasy", "Mystery")
books = {}    # ISBN: {title, author, genre, total_copies}
members = []  # List of member dicts


# ----- Book Functions -----
def add_book(isbn, title, author, genre, total_copies):
    if isbn in books or genre not in GENRES:
        return False
    books[isbn] = {"title": title, "author": author, "genre": genre, "total_copies": total_copies}
    return True


def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    if isbn not in books or (genre and genre not in GENRES):
        return False
    if title: books[isbn]["title"] = title
    if author: books[isbn]["author"] = author
    if genre: books[isbn]["genre"] = genre
    if total_copies is not None: books[isbn]["total_copies"] = total_copies
    return True


def delete_book(isbn):
    if isbn not in books: return False
    for m in members:
        if isbn in m["borrowed_books"]:
            return False
    del books[isbn]
    return True


def search_books(query, by="title"):
    query = query.lower()
    return [b for b in books.values() if query in b[by].lower()]


# ----- Member Functions -----
def add_member(member_id, name, email):
    for m in members:
        if m["member_id"] == member_id:
            return False
    members.append({"member_id": member_id, "name": name, "email": email, "borrowed_books": []})
    return True


def update_member(member_id, name=None, email=None):
    for m in members:
        if m["member_id"] == member_id:
            if name: m["name"] = name
            if email: m["email"] = email
            return True
    return False


def delete_member(member_id):
    for m in members:
        if m["member_id"] == member_id:
            if m["borrowed_books"]:
                return False
            members.remove(m)
            return True
    return False


# ----- Borrow/Return Functions -----
def borrow_book(isbn, member_id):
    if isbn not in books: return False
    if books[isbn]["total_copies"] <= 0: return False
    for m in members:
        if m["member_id"] == member_id:
            if len(m["borrowed_books"]) >= 3: return False
            m["borrowed_books"].append(isbn)
            books[isbn]["total_copies"] -= 1
            return True
    return False


def return_book(isbn, member_id):
    for m in members:
        if m["member_id"] == member_id and isbn in m["borrowed_books"]:
            m["borrowed_books"].remove(isbn)
            books[isbn]["total_copies"] += 1
            return True
    return False
