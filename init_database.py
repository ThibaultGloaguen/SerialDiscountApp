import csv
import pickledb

if __name__ == '__main__':
    with open('serial_numbers.csv', 'rt') as csvfile:

        spamreader = csv.reader(csvfile)
        next(spamreader)
        db = pickledb.load('serial_discount.db', True)
        for row in spamreader:
            db.set(row[0], None)

    with open('discount_codes.csv', 'rt') as csvfile:

        spamreader = csv.reader(csvfile)
        next(spamreader)
        db = pickledb.load('discount_codes.db', True)
        coupons = []
        for row in spamreader:
            coupons.append(row[0])
        db.set('discounts', coupons)
