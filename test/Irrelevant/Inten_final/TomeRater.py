class User(object):
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.books = {}
	
	def get_email(self):
		return self.email

	def change_email(self, address):
		self.email = address
		print("{user}'s email has been updated to {email}".format(user = self.name, email = self.email))

	def __repr__(self):
		return 'User {user}, email: {email}, books read: {books}'.format(user = self.name, email = self.email, books = self.books)

	def __eq__(self, other_user):
		return (self.name == other_user.name and self.email == other_user.email)
		
	def get_average_rating(self):
		ratings = 0
		numbers = 0
		for val in self.books.values():
			ratings += val
			numbers += 1
			return ratings / numbers
		
	def read_book(self, book, rating = 0):
		self.books[book] = rating

class Book(object):
	def __init__(self, title, isbn):
		self.title = title
		self.isbn = isbn
		self.ratings = []
		
	def get_title(self):
		return self.title
	
	def get_isbn(self):
		return self.isbn
	
	def set_isbn(self, new_isbn):
		self.isbn = new_isbn
		print("the isbn has been changed to {isbn}".format(isbn = self.isbn))
		
	def add_rating(self, rating):
		if rating >= 0 and rating <= 4:
			self.ratings.append(rating)
	
	def __eq__(self, other_book):
		return (self.title == other_book.title and self.isbn == other_book.isbn)
		
	def get_average_rating(self):
		ratings = 0
		nums= 0
		for val in self.ratings:
			ratings += val
			nums =+ 1
		return ratings / nums
		
	def __repr__(self):
		return '{book}'.format(book = self.title)
		
	def __hash__(self):
		return hash((self.title, self.isbn))
		
class Fiction(Book):
	def __init__(self, title, author, isbn):
		super().__init__(title, isbn)
		self.author = author
	
	def get_author(self):
		return self.author
		
	def __repr__(self):
		return "{title} by {author}".format(title = self.title, author = self.author)
	
class Non_Fiction(Book):
	def __init__(self, title, subject, level, isbn):
		super().__init__(title, isbn)
		self.subject = subject
		self.level = level
		
	def get_subject(self):
		return self.subject
	
	def get_level(self):
		return self.level
	
	def __repr__(self):
		return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)
		
class TomeRater:
	def __init__(self):
		self.users = {}
		self.books = {}
		self.isbns = {}
	
	def create_book(self, title, isbn):
		if len(self.isbns) == 0:
			self.isbns[title] = isbn
			return Book(title, isbn)
		else:
			for isbns in self.isbns.values():
				if isbns != isbn:
					self.isbns[title] = isbn
					return Book(title, isbn)
				else:
					print('That ISBN is already used')
	
	def create_novel(self, title, author, isbn):
		if len(self.isbns) == 0:
			self.isbns[title] = isbn
			return Fiction(title, author, isbn)
		else:
			for isbns in self.isbns.values():
				if isbns != isbn:
					self.isbns[title] = isbn
					return Fiction(title, author, isbn)
				else:
					print('That ISBN is already used')
	
	def create_non_fiction(self, title, subject, level, isbn):
		if len(self.isbns) == 0:
			self.isbns[title] = isbn
			return Non_Fiction(title, subject, level, isbn)
		else:
			for isbns in self.isbns.values():
				if isbns != isbn:
					self.isbns[title] = isbn
					return Non_Fiction(title, subject, level, isbn)
				else:
					print('That ISBN is already used')
	
	def add_book_to_user(self, book, email, rating = 0):
		mail_there = False
		if self.users.get(email):
			mail_there = True
			user = self.users.get(email)
			book = Book(book, isbn = 0)
			user.read_book(book, rating)
			book.add_rating(rating)
			if not self.books.get(book):
				self.books[book] = 1
			else:
				self.books[book] += 1
		else:
			mail_there = False
		if mail_there == False:
			print("No user with email {email}!".format(email = email))
				
	def add_user(self, name, email, user_books = []):
		isAtThere = False
		ending = False
		endings = ['.com', '.org', '.edu']
		for letter in email:
			if letter == '@':
				isAtThere = True

		for end in endings:
			if email[-4:] == end:
				ending = True
				break
				
		if self.users.get(email):
			print('That email is already in use.')
		else: 
			if isAtThere == True and ending == True:
				user = User(name, email)
				self.users[email] = user
				if len(user_books) > 0:
					for book in user_books:
						self.add_book_to_user(book, email)
			else:
				print('That is not a valid email')
	def print_catalog(self):
		print('***Our catalog***')
		for book in self.books:
			print(book)
	
	def print_users(self):
		print('***Our users***')
		for user in self.users.values():
			print(user)
	
	def most_read_book(self):
		top = 0
		top_book = ''
		for book,val in self.books.items():
			if val > top:
				top = val
				top_book = book
		return top_book
	def highest_rated_book(self):
		top = ''
		top_val = 0
		for book in self.books.keys():
			temp = book.get_average_rating()
			if temp > top_val:
				top_val = temp
				top = book
		return top
			
	def most_positive_user(self):
		highest = 0
		h_user = ''
		for user in self.users.values():
			if user.get_average_rating() > highest:
				highest = user.get_average_rating()
				h_user = user
		return h_user