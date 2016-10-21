import datetime
import csv


class Bench:
    def __init__(self):
        pass

    def lookup(self, search_key):
        pass

    def create(self, data):
        pass


class BasicMember:
    def get_discount(self):
        pass


class SilverMember:
    def get_discount(self):
        pass


class GoldMember:
    def get_discount(self):
        pass


class Customer(Bench):
    def __init__(self, customer_data, purchases):
        Bench.__init__(self)
        self.type = 'cust'
        self.customer_id = customer_data['cid']
        self.name = customer_data['name']
        self.address = customer_data['address']
        self.city = customer_data['city']
        self.state = customer_data['state']
        self.zip_code = customer_data['zip']
        self.purchases = purchases
        self.favorite_store = self.get_favorite_store()
        self.monthly_spend = self.get_monthly_spend()
        self.memberlevel = ''
        self.check_level()

    def get_favorite_store(self):
        stores = {}
        fav_store = ('', 0)
        for i in self.purchases:
            try:
                stores[i['store_id']] += 1
            except KeyError:
                stores[i['store_id']] = 1

        for store, tally in stores.items():
            if tally > fav_store[1]:
                fav_store = (store, tally)

        return fav_store

    def get_monthly_spend(self):
        total_spent = 0
        for i in self.purchases:
            total_spent += int(i['amount'])

        return total_spent

    def check_level(self):
        if self.monthly_spend < 800:
            self.memberlevel = 'basic'
        elif self.monthly_spend < 1200:
            self.memberlevel = 'silver'
        else:
            self.memberlevel = 'gold'


class Store(Bench):
    def __init__(self, number, manager, address, city, state, zip_code):
        Bench.__init__(self)
        self.type = 'store'
        self.store_number = number
        self.manager = manager
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.ytd = self.ytd_sales()
        self.mtd = self.mtd_sales()

    def ytd_sales(self):
        pass

    def mtd_sales(self):
        pass


class Transaction(Bench):
    def __init__(self, trans_id, cid, store_num, amount, date=datetime.date.today()):
        Bench.__init__(self)
        self.type = 'trans'
        self.id = trans_id
        self.date = date
        self.cid = cid
        self.store_number = store_num
        self.amount = amount
        self.customer = ''

    def get_customer_info(self, cid):
        pass


def main():
    gold_and_silver_customers = []
    transactions = []
    customers = []
    customer_headers = ['cid', 'name', 'address', 'city', 'state', 'zip']
    with open('customers.dat', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            customers.append(dict(zip(customer_headers, row)))

    with open('transactions.dat', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            transactions.append(row)
    for i in customers:
        purchases = [x for x in transactions if x[3] == i['cid']]
        customer = Customer(i, purchases)


if __name__ == '__main__':
    main()
