class Bill:
    """
    Object that contains data about a Bill, such as
    total amount and period of Bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmates:
    """
    Creates a flatmate person who lives in the flat and
    pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        return bill.amount * self.days_in_house / (self.days_in_house + flatmate2.days_in_house)


class PdfReport:
    """
    Creates a report in pdf format detailing how much each
    flatmate has to pay
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


bill = Bill(120, "July 2022")
kushi = Flatmates("kushi", 25)
praveen = Flatmates("praveen", 27)
print(kushi.pays(bill, praveen), praveen.pays(bill, kushi),
      kushi.pays(bill, praveen)+praveen.pays(bill, kushi))
