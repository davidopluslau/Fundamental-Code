from decimal import ROUND_UP, Decimal

from getkey import getkey, keys


class ItemShare:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __str__(self):
        return f"Item: {self.name}, Cost: ${self.cost}"

    def __repr__(self):
        return str(self)


class Item:
    def __init__(self, name, cost, shares):
        self.name = name
        self.cost = cost
        share_denominator = Decimal(sum(shares.values()))
        self.shares = {person: shares[person] / share_denominator for person in shares}

    def __str__(self):
        breakdown = [f" {person}: {self.cost * self.shares[person]}" for person in self.shares]
        breakdown_formatted = "\n".join(breakdown)
        return f"Item: {self.name}\nCost: ${self.cost}\nBreakdown:\n{breakdown_formatted}"

    def __repr__(self):
        return str(self)


class Bill:
    items: list[Item]
    people: list[str]
    tip: Decimal
    tax: Decimal
    subtotal: Decimal
    grand_total: Decimal
    valid_fast_inputs: set[str]

    def __init__(self):
        self.items = []
        self.people = []

    def calculate(self):
        self.assign_totals()
        self.assign_people()
        self.assign_items()
        self.print_assignments()

    def assign_items(self):
        running_cost = Decimal(0)
        while True:
            item_name = input("Enter an item. If you're finished entering items, press \"Enter\"\n")
            if not item_name:
                return
            cost = Decimal(input("What did it cost? If you ordered multiple, put in the total cost "
                                 "of the items\n"))
            running_cost += cost
            # TODO add editing functionality
            if running_cost > self.subtotal:
                raise Exception(f"Your running total {running_cost} is greater than the "
                                f"listed subtotal {self.subtotal}")

            print("If the whole party split this equally, press \"a\"")
            print("If one single person had this item, press \"s\"")
            print("If a subset of people split this item equally, press \"b\"")
            print("Otherwise, press \"o\"")
            payment_mode = getkey()
            if payment_mode == "a":
                shares = {person: Decimal(1) for person in self.people}
            elif payment_mode == "s":
                print("Whose was this?\n")
                self.enumerate_people()
                person = self.choose_person()
                while not person:
                    print("Please choose a valid person based on their number")
                    person = self.choose_person()
                shares = {person: Decimal(1)}
            elif payment_mode == "o":
                shares = self.handle_share_split_item()
            elif payment_mode == "b":
                shares = self.handle_subset_split_item()
            else:
                print(f"{payment_mode} is unrecognized. Please try again\n")
                continue
            self.items.append(Item(item_name, cost, shares))
            print("\nRunning bill:")
            Bill.print_list(self.items)
            print()
        if running_cost != self.subtotal:
            Bill.print_list(self.items)
            raise Exception(f"Uh oh, running cost ${running_cost} doesn't match the subtotal "
                            f"${self.subtotal}")

    def choose_person(self):
        while True:
            person_index = getkey()
            # TODO support for more than 9 attendees
            if person_index == keys.ENTER:
                return None
            elif person_index in self.valid_fast_inputs:  # 1 through 9 inclusive
                return self.people[int(person_index) - 1]
            else:
                print(f"{person_index} was not a valid input. Please enter the item again")

    def enumerate_people(self):
        for index, value in enumerate(self.people):
            print(str(index + 1) + " " + value)

    # TODO Handle cases where a non-complete set of attendees split an item
    def handle_subset_split_item(self):
        shares = {}
        while True:
            print("Whose shared this item? If you're finished entering people, press \"Enter\"\n")
            self.enumerate_people()
            person = self.choose_person()
            if not person:
                return shares
            shares[person] = 1
            print("\nCurrent payers")
            Bill.print_list(shares.keys())
            print()

    def handle_share_split_item(self):
        shares = {}
        while True:
            print("Whose shared this item? If you're finished entering people, press \"Enter\"\n")
            self.enumerate_people()
            person = self.choose_person()
            if not person:
                return shares
            share = Decimal(input(f"What was {person}'s share? e.g. If one person ate an ice cream "
                                  "and three people split a second ice cream, put in \"1\" for the "
                                  "first person and \"0.33\" for the other three\n"))
            shares[person] = share
            print("\nCurrent payers")
            Bill.print_list(shares.keys())
            print()

    def assign_totals(self):
        self.subtotal = Decimal(input("What was the subtotal?\n"))
        self.tax = Decimal(input("What was the tax?\n"))
        self.tip = Decimal(input("What was the tip?\n"))
        self.grand_total = Decimal(input("What was the grand total?\n"))
        print("Subtotal: " + str(self.subtotal))
        print("Tax: " + str(self.tax))
        print("Tip: " + str(self.tip))
        print("Grand total: " + str(self.grand_total))
        calculated_total = (self.subtotal + self.tax + self.tip)
        if self.grand_total != calculated_total:
            raise Exception(
                f"The grand total doesn't match the calculated total {calculated_total}")

    def assign_people(self):
        while True:
            # TODO add editing functionality
            person = input("Enter the name of a person. "
                           "If you're done adding people, press \"Enter\"\n")
            if not person:
                print("These are the people: " + "\n".join(self.people))
                print()
                self.valid_fast_inputs = {str(index) for index in range(1, len(self.people) + 1)}
                return
            if person in self.people:
                print(
                    person + " is already listed. Please add this person with a unique name (like "
                             "adding a last initial)")
            else:
                self.people.append(person)
            print("\nPeople so far:")
            Bill.print_list(self.people)
            print()

    def print_assignments(self):
        item_shares_by_person = {person: [] for person in self.people}
        for item in self.items:
            for person in item.shares:
                share = item.shares[person]
                item_shares_by_person[person].append(ItemShare(item.name, share * item.cost))
        print(item_shares_by_person)

        tax_tip_surcharge = Bill.round_up(self.grand_total / self.subtotal)
        print(f"Tax + Tip Surcharge: {tax_tip_surcharge}")
        for person in item_shares_by_person:
            item_shares = item_shares_by_person[person]
            final_share = Bill.round_up(
                sum(item_share.cost for item_share in item_shares) * tax_tip_surcharge)
            print(f"{person}: ${final_share}")
            for item_share in item_shares_by_person[person]:
                print(f"  {item_share.name}: ${Bill.round_up(item_share.cost)}")
            print()

    @staticmethod
    def round_up(number):
        return number.quantize(Decimal("0.00"), rounding=ROUND_UP)

    @staticmethod
    def print_list(things):
        for thing in things:
            print(thing)


Bill().calculate()
