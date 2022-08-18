from bill import Bill
from flatmate import Flatmates
from pdfreport import PdfReport, FileSharer

amount = float(input("Enter the Bill Amount: "))
bill_period = input("Enter the Bill period (December 2020): ")
name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during {bill_period}: "))
name2 = input(f"Enter {name1}'s flatmate name: ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during {bill_period}: "))
the_bill = Bill(amount, bill_period)
user1 = Flatmates(name1, days_in_house1)
user2 = Flatmates(name2, days_in_house2)
print(user1.pays(the_bill, user2), user2.pays(the_bill, user1),
      user1.pays(the_bill, user2) + user2.pays(the_bill, user1))
pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(user1, user2, the_bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())
