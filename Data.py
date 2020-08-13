from datetime import datetime

class Data :

    def __init__(self, date, address, description) :
        self.date = datetime.strptime(date, "%m/%d/%Y")
        self.address = address
        self.description = description

    def __repr__(self) :
        return f"Date is {self.date} / Address is {self.address} / Description is {self.description}"