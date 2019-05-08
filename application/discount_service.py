from utils.custom_exceptions import NoMoreDiscountException


class DiscountService:
    def __init__(self, discount_db, serial_db):
        self.discount_db = discount_db
        self.serial_db = serial_db

    def exists(self, serial_number):
        return self.serial_db.exists(serial_number)

    def get_discount(self, serial_number):
        return self.serial_db.get(serial_number)

    def set_discount(self, serial_number):
        discounts = self.discount_db.get('discounts')
        if len(discounts) == 0:
            raise NoMoreDiscountException('No more discount available')
        discount = discounts.pop()
        self.discount_db.set('discounts', discounts)
        self.serial_db.set(serial_number, discount)
        return discount
