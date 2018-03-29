__author__ = 'olga.ostapenko'


class Invoice:
    def __init__(self, Customer, Buyer, Document_Number, Total_Value):
        self.Customer = Customer
        self.Buyer = Buyer
        self.Document_Number = Document_Number
        self.Total_Value = Total_Value

