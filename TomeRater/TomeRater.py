class User(object):
  
  def __init__(self, name, email):
    self.name = name
    if ("@") in email:
      self.email = email
    else:
      print("Please enter a valid email address!")
      self.email = "--No Valid Email Listed--"
    self.books = {}
    
  def get_email(self):
    return self.email
  
  def change_email(self, address):
    if ("@") in address:
      self.email = address
      print("This user's email has been updated.")
    else:
      print("Please enter a valid email address!")
    
  def __repr__(self):
    return ("The user: {}, with email: {}, has {} books read".format(self.name, self.email, len(self.books)))
   

  def __eq__(self, other):
    if (self.name == other.name) and (self.email == other.email):
      return True
    else:
      return False
    
  def read_book(self, book, rating = None):
    self.books[book] = rating
  
  def get_average_rating(self):
    book_count = 0
    rating_sum = 0
    for i in self.books.values():
      if i:
        book_count += 1
        rating_sum += i
        avg_rating = rating_sum/book_count
    return avg_rating

class Book(object):
  
  def __init__(self, title, isbn):
    self.title = title
    self.isbn = isbn
    self.ratings = []
  def __repr__(self):
    return self.title
    
  def get_title(self):
    return self.title
  
  def get_isbn(self):
    return self.isbn
  
  def set_isbn(self, new_isbn):
    self.isbn = new_isbn
    print("This book's ISBN has been updated.")
  
  def add_rating(self, rating):
    if rating > 0 and rating < 4:
      self.ratings.append(rating)
    else:
      print("Invalid Rating")

      
  def __eq__(self, other):
    if (self.title == other.title) and (self.get_isbn == other.get_isbn):
      return True
    else:
      return False
    
  def get_average_rating(self):
    rating_sum = 0
    for i in self.ratings:
      rating_sum += i
    if len(self.ratings) != 0:
      avg_rating = rating_sum/len(self.ratings)
    else:
      avg_rating = 0
    return avg_rating
    
  def __hash__(self):
    return hash((self.title, self.isbn))
  
  
class Fiction(Book):
  
  def __init__(self, title, author, isbn):
    super().__init__(title, isbn)
    self.author = author
    
  def get_author(self):
    return self.author
  
  def __repr__(self):
    return ("{} by {}.".format(self.title, self.author))
  
  
class NonFiction(Book):
  
  def __init__(self, title, subject, level, isbn):
    super().__init__(title, isbn)
    self.subject = subject
    self.level = level
    
  def get_subject(self):
    return self.subject
  
  def get_level(self):
    return self.level
  
  def __repr__(self):
    return ("{}, a {} manual on {}".format(self.title, self.level, self.subject))
  
  
class TomeRater(object):
  
  def __init__(self):
    self.users = {}
    self.books = {}
    
  def __repr__(self):
    return "TomeRater {} and {}".format(self.users, self.books)
  
  def __str__(self):
    return "in TomeRater users are {} and books are {}".format(self.users, self.books)
  
  def __eq__(self, other):
    if (self.users == other.users) and (self.books == other.books):
      return True
    else:
      return False
     
  def create_book(self, title, isbn):
    nbook = Book(title, isbn)
    return nbook
  
  def create_novel(self, title, author, isbn):
    nnovel = Fiction(title, author, isbn)
    return nnovel
  
  def create_non_fiction(self, title, subject, level, isbn):
    n_non_fic = NonFiction(title, subject, level, isbn)
    return n_non_fic
  
  

  def add_book_to_user(self, book, email, rating = None):
    user = self.users.get(email, None)
    if user:
      user.read_book(book, rating)
      if book not in self.books:
        self.books[book] = 0
      self.books[book] += 1
      if rating != None:
        book.add_rating(rating)
    else:
      print("No user with email {}".format(email))

  def add_user(self, name, email, user_books = None):
    nuser = User(name, email)
    self.users[email] = nuser
    if user_books:
      for i in user_books:
        self.add_book_to_user(i, email)

  def print_catalog(self):
    for i in self.books:
      print(i)
      
  def print_users(self):
    for i in self.users.values():
      print(i)
      
  def most_read_book(self):
    v = 0
    nb = None
    for i in self.books:
      nOr = self.books[i]
      if nOr > v:
        v = nOr
        nb = i
    return nb
  
  def highest_rated_book(self):
    HRating = 0
    b = None
    for i in self.books:
      CRating = i.get_average_rating()
      if CRating > HRating:
        HRating = CRating
        b = i
    return b
  
  def most_positive_user(self):
    HRating = 0
    u = None
    for i in self.users.values():
      CRating = i.get_average_rating()
      if CRating > HRating:
        HRating = CRating
        u = i
    return u
  

  


Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())