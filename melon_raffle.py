#WHY CAN'T I JUST IMPORT CUSTOMER_INFO?
from customer_info import organize_customer_data
from random import choice


def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(customers)

    print
    print "Contact {name} at {email} to notify them they've won!".format(
        name=chosen_customer.name,
        email=chosen_customer.email
        )
    print

customers = organize_customer_data("customers.txt")

pick_winner(customers)
