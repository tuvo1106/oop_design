from restaurant.data_types.enums import AccountStatus


class Account:
    def __init__(self, id, password, address, status=AccountStatus.ACTIVE):
        self.__id = id
        self.__password = password
        self.__address = address
        self.__status = status

    def reset_password(self):
        pass
