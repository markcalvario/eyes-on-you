import datetime
from Data import Data

class Database :

    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI",
    "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS",
    "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR",
    "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    def __init__(self) :
        # constructor: initializing a dictionary with keys from the
        # list 'states' and setting the initial values as None
        self.database = {key: [] for key in self.states}
        # self.database_archive =  {key: [] for key in self.states} # archive?

    def addData(self, state_input, data_input) :
        # parameters: String state_input, Data data_input
        # this function adds a Data input to the dictionary Database
        self.database[state_input].append(data_input)

    def printData(self, state_input) :
        # parameters: String state_input
        # this function prints out a list of Data instances for inputed state
        self.updateData(state_input)
        print(self.database.get(state_input))

    def updateData(self, state_input) :
        # this function updates the database to remove Data instances
        # that are more than a week old
        today_date = datetime.datetime.now()

        for data in self.database[state_input] :
            if ((today_date - data.date).days > 7) :
                self.database[state_input].remove(data)

    def clear(self) :
        # this function cleans the Database entirely
        self.database.clear();


def main() :
    db = Database()
    data = Data("02/08/2020", "4997 Atlschul", "We are testing code!")
    db.addData("NY", data)
    db.printData("NY")

if __name__ == "__main__" :
    main()