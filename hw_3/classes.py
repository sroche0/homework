import csv


class Bench:
    """
    Base class for the store, customer and transaction classes. Does nothing at the moment but allows for easy editing
    should we need to add more functionality such as lookup or entry creation.
    """
    def __init__(self):
        pass

    def lookup(self, search_key):
        pass

    def create(self, data):
        pass


class BasicMember:
    """
    Basic membership level class
    """
    discount = 0

    @staticmethod
    def get_discount():
        return BasicMember.discount

    @staticmethod
    def set_discount(amount):
        setattr(BasicMember, 'discount', amount)


class SilverMember:
    discount = 10

    @staticmethod
    def get_discount():
        return SilverMember.discount

    @staticmethod
    def set_discount(amount):
        setattr(SilverMember, 'discount', amount)


class GoldMember:
    discount = 15

    @staticmethod
    def get_discount():
        return GoldMember.discount

    @staticmethod
    def set_discount(amount):
        setattr(GoldMember, 'discount', amount)


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
        self.member_level = ''
        self.discount = 0
        self.check_level()

    def get_favorite_store(self):
        """
        Adds up the customers purchases sorted by store and returns a Store object for the store they spent the most at
        :return: Store object of store with highest monthly spend
        """
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

        fav_store = Store(fav_store[0])
        return fav_store

    def get_monthly_spend(self):
        """
        Add up the total amount the customer spent this month across all store
        :return:
        """
        total_spent = 0.0
        for i in self.purchases:
            total_spent += float(i['amount'])

        return total_spent

    def check_level(self):
        """
        Checks what member level the customer is  based on their spending and sets their discount level appropriately
        """
        if self.monthly_spend < 800:
            self.member_level = 'basic'
            self.discount = BasicMember.get_discount()
        elif self.monthly_spend < 1200:
            self.member_level = 'silver'
            self.discount = SilverMember.get_discount()
        else:
            self.member_level = 'gold'
            self.discount = GoldMember.get_discount()


class Store(Bench):
    def __init__(self, store_id):
        Bench.__init__(self)
        with open('stores.dat', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if str(row[0]) == str(store_id):
                    self.store_id = store_id
                    self.manager = row[1]
                    self.address = row[2]
                    self.city = row[3]
                    self.state = row[4]
                    self.zip = row[5]

    def ytd_sales(self):
        pass

    def mtd_sales(self):
        pass


def main():
    """
    Main Function that contains most of the logic.
    """
    # create empty lists to be populated by later methods
    gold_and_silver_customers = []
    transactions = []
    customers = []

    # Open the customers.dat file and create a dict out of it so items can be accessed without knowing the position
    customer_headers = ['cid', 'name', 'address', 'city', 'state', 'zip']
    with open('customers.dat', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            customers.append(dict(zip(customer_headers, row)))

    # Open the transactions.dat file and create a dict out of it so items can be accessed without knowing the position
    transaction_headers = ['trans_id', 'date', 'cid', 'store_id', 'amount']
    with open('transactions.dat', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            transactions.append(dict(zip(transaction_headers, row)))

    # Loop through the customers and create a customer object for each. For gold and silver customers append them to
    # gold_and_silver_customers list to be given to marketing for the mailers.
    for i in customers:
        # create a list of just this customers transactions using list comprehension
        purchases = [x for x in transactions if x['cid'] == i['cid']]
        customer = Customer(i, purchases)
        if customer.member_level != 'basic':
            # if the customer is higher than a basic member add the additional data marketing requested on the discount
            # level and store manager
            i.update({'discount': customer.discount, 'favorite_manager': customer.favorite_store.manager})
            gold_and_silver_customers.append(i)

    if gold_and_silver_customers:
        # If there are customers who spent enough to meet our membership levels for discounts, write them to a file to
        # be sent to marketing

        print("Found {} gold and silver level customers. Writing their details to a file for use in mailers.".format(
            len(gold_and_silver_customers)))
        with open('targeted_customers.csv', 'wb') as f:
            writer = csv.DictWriter(f, gold_and_silver_customers[0].keys())
            writer.writeheader()
            writer.writerows(gold_and_silver_customers)

if __name__ == '__main__':
    main()
