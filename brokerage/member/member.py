#!/usr/bin/env python3

import datetime
from brokerage.data_types.enums import ReturnStatus, OrderStatus
from brokerage.member.account import Account
from brokerage.order.order import LimitOrder
from brokerage.stock_exchange.stock_exchange import StockExchange


class Member(Account):
    def __init__(self):
        self.__available_funds_for_trading = 0.0
        self.__date_of_membership = datetime.date.today()
        self.__stock_positions = {}
        self.__active_orders = {}

    def place_sell_limit_order(self, stock_id, quantity, limit_price, enforcement_type):
        # check if member has this stock position
        if stock_id not in self.__stock_positions:
            return ReturnStatus.NO_STOCK_POSITION
        stock_position = self.__stock_positions[stock_id]
        # check if the member has enough quantity available to sell
        if stock_position.get_quantity() < quantity:
            return ReturnStatus.INSUFFICIENT_QUANTITY
        order = LimitOrder(stock_id, quantity, limit_price, enforcement_type)
        order.is_buy_order = False
        order.save_in_DB()
        success = StockExchange.place_order(order)
        if success:
            order.set_status(OrderStatus.FILLED)
            order.save_in_DB()
        else:
            self.__active_orders[order.get_order_id()] = order
        return success

    def place_buy_limit_order(self, stock_id, quantity, limit_price, enforcement_type):
        # check if the member has enough funds to buy this stock
        if self.__available_funds_for_trading < quantity * limit_price:
            return ReturnStatus.INSUFFICIENT_FUNDS
        order = LimitOrder(stock_id, quantity, limit_price, enforcement_type)
        order.is_buy_order = True
        order.save_in_DB()
        success = StockExchange.place_order(order)
        if not success:
            order.set_status(OrderStatus.FILLED)
            order.save_in_DB()
        else:
            self.__active_orders[order.get_order_id()] = order
        return success

    # this function will be invoked whenever there is an update from
    # stock exchange against an order
    def callback_stock_exchange(self, order_id, order_parts, status):
        order = self.__active_orders[order_id]
        order.add_order_parts(order_parts)
        order.set_status(status)
        order.update_in_DB()
        if status == OrderStatus.FILLED or status == OrderStatus.CANCELLED:
            del self.__active_orders[order_id]
