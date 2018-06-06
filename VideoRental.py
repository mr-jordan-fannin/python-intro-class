''' Video Rental by Jordan Fannin. 5-15-2018'''

class Rental:
    new_fee = 3.00
    old_fee = 2.00

    def __init__(self):
        self.new_qty = 0
        self.new_nights = 0
        self.old_qty = 0
        self.old_nights = 0
        self.values = [
            self.new_qty,
            self.new_nights,
            self.old_qty,
            self.old_nights
        ]
        self.prompts = [
            self.prompt_new_qty(),
            self.prompt_new_nights(),
            self.prompt_old_qty(),
            self.prompt_old_nights()
        ]

    def prompt_new_qty(self):
        self.new_qty = int(input("Number of New Rentals: "))

    def prompt_new_nights(self):
        self.new_nights = int(input("Nights to rent New Rentals: "))

    def prompt_old_qty(self):
        self.old_qty = int(input("Number of Old Rentals: "))

    def prompt_old_nights(self):
        self.old_nights = int(input("Nights to rent Old Rentals: "))

    def input_check(self):
        for i in self.values:
            if i < 0:
                self.values.i = 0

    def call(self, query):
        for i in vars(self):
            if i == query:
                exec(query)

    def get_total(self):
        return ((self.new_nights * self.new_qty * self.new_fee) + (self.old_nights * self.old_qty * self.old_fee))


def main():
    print("***** Five Star Retro Video *****")
    customer = Rental()
    for i in customer.prompts:
        customer.call(i)
    print(f"The total comes to ${format(customer.get_total(), '.2f')}")


if __name__ == "__main__":
    main()