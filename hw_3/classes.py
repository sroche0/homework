

class Customer:
    def __init__(self, cid, name, address, city, state, zip):
        self.customer_id = cid
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip


class Store:
    def __init__(self, number, manager, address, city, state, zip):
        self.store_number = number
        self.manager = manager
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip


class Transaction:
    def __init__(self, trans_id, date, cid, store_num, amount):
        self.id = trans_id
        self.date = date
        self.cid = cid
        self.store_number = store_num
        self.amount = amount
        self.customer = ''

    def get_customer_info(self, cid):
        pass
