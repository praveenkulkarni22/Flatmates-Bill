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