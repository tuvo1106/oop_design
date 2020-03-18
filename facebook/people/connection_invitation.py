#!/usr/bin/env python3

import datetime
from facebook.data_types.enums import ConnectionInvitationStatus


class ConnectionInvitation:
    def __init__(self, member_invited, name,
                 status=ConnectionInvitationStatus.PENDING):
        self.__member_invited = member_invited
        self.__status = status
        self.__date_created = datetime.date.today()
        self.__date_updated = datetime.date.today()

    def accept_connection(self):
        pass

    def reject_connection(self):
        pass
