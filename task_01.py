#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""SQL applications in Python"""


import data


def sum_orders(customers, orders):
    """Dictionary applications.

    Args:
        customers (dict): dictionary of customers keyed by customer_id
        orders (dict): dictionary of orders keyed by order_id

    Returns:
        A combined dictionary

    Examples:
        >>> ORDERS = {1: {'customer_id': 2, 'total': 10},
                      3: {'customer_id': 2, 'total': 10},
                      4: {'customer_id': 3, 'total': 15}}
        >>> CUSTOMERS = {2: {'name': 'Person One', 'email': 'email@one.com'},
                         3: {'name': 'Person Two', 'email': 'email@two.com'}}
        >>> sum_orders(customers=CUSTOMERS, orders=ORDERS)
        {2: {'name': 'Person One',
             'email': 'email@one.com',
             'orders': 2,
             'total': 20}
         3: {'name': 'Person Two',
             'email': 'email@two.com',
             'orders': 1,
             'total': 15}}
    """
    CUSTOMERS = {customer_id: {'name': 'Name', 'email': 'email address'}}
    ORDERS = {'customer_id': customer_id, 'total': order_total}
    return CUSTOMERS.items(customer_id, ORDERS)
