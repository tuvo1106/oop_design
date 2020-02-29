#!/usr/bin/env python3

import datetime


class Notification:
    def __init__(self, id, content):
        self.__notification_id = id
        self.__created_on = datetime.datetime.now()
        self.__content = content

    def send_notification(self):
        pass
