#!/usr/bin/env python3

import datetime


class Photo:
    def __init__(self, id, path, member):
        self.__photo_id = id
        self.__photo_path = path
        self.__creation_date = datetime.datetime.now()
        self.__creating_member = member

    def delete(self):
        pass
