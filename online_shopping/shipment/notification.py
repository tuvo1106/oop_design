#!/usr/bin/env python3

from abc import ABC, abstractmethod
import datetime


class Notification(ABC):
    def __init__(self, id, content):
        self.__notification_id = id
        self.__created_on = datetime.date.today()
        self.__content = content

    def send_notification(self, account):
        pass
