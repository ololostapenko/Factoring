__author__ = 'olga.ostapenko'

from model.invoice import Invoice

def test_create_invoice(app):
    app.session.login(username="devteam", password="password")
    app.invoice.create(Invoice(Customer="SUSHIVESLA", Buyer="BESK Co.", Document_Number="11111g", Total_Value="10000"))
    app.session.logout()