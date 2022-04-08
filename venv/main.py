from Flat import Bill, Flatmate
from Report import PdfReport, FileSharer

bill_amount = float(input('Hey user, enter the bill amount: '))
bill_period = input('For which month/year is this bill? E.g. December 2020: ')
bill = Bill(amount=bill_amount, period=bill_period)
# print("Now, you have to instantiate objects for yourself and Flatmates.")
# print("Enter the name and days_in_house for each one.")

# Instantiating the flatmates using a while loop
flatmates = []
flag = True
number_of_flatmates = 0
while flag:
    FM = Flatmate(input('What is your name? '),
                  int(input(f'How many days did you spent during the bill period? ')))
    flatmates.append(FM)
    status = input("Do you have any other flatmates? Y/N only: ")
    number_of_flatmates += 1
    if status in ['Yes', 'yes', 'YES', 'Y', 'y']:
        pass
    elif status in ['No', 'NO', 'no', 'N', 'n']:
        flag = False
    else:
        raise NameError('Error! Only Y/N answers are allowed. Please try again using Y/N answers only')
print()

# To get how much each flatmate should pay
flatmates_usd = []
for index, FM in enumerate(flatmates):
    # Lists are mutable, so I must have a copy with a different pointer in order to smooth the process of pays() method
    flatmates_copy = flatmates[:]
    # I will remove the item 'index' each time from the flatmates_copy list
    # and send it as a parameter to the pays() method
    flatmates_copy.pop(index)
    fm_usd = flatmates[index].pays(flatmates_copy, the_bill=bill)
    flatmates_usd.append(fm_usd)

# Print how much each flatmate should pay
for index in range(len(flatmates_usd)):
    print(f'{flatmates[index].name} should pay {flatmates_usd[index]}$')

# Write how much each flatmate should pay to a PDF file
pdf_report = PdfReport(f'{bill.period}.pdf')
pdf_report.generate(flatmates, flatmates_usd, the_bill=bill)
sharer = FileSharer(filename=f'{bill.period}.pdf')
print(sharer.share())