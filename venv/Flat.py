class Bill:
    """Object that contains data about a bill, such as
    total amount of bill and period of the bill."""
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person who lives in a flat and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, other_flatmates, the_bill):
        # I made it *other to extend the number of flatmates to be more than two if needed
        sum_of_days = 0
        for flatmate in range(len(other_flatmates)):
            sum_of_days += other_flatmates[flatmate].days_in_house
        weight = self.days_in_house/(self.days_in_house + sum_of_days)
        return round(weight * the_bill.amount, 2)
