





class Library:
    def __init__(self, acc_number, publisher, title, author):
        self.acc_number = acc_number
        self.publisher = publisher
        self.title = title
        self.author = author
        self.days_late = 0

    def read(self):
        print("Account Number:", self.acc_number)
        print("Title:", self.title)
        print("Author:", self.author)

    def compute(self, days_late):
        self.days_late = days_late
        fine = self.days_late * 1.50
        print("Fine charged: $", fine)

    def display(self):
        print("Account Number:", self.acc_number)
        print("Publisher:", self.publisher)
        print("Title:", self.title)
        print("Author:", self.author)



book1 = Library("1786", "The Mecha", "The Python", "Siddhesh Dalvi")
book1.read()  
book1.compute(5) 
book1.display() 
