
class Commentary:
    def __init__(self, text, commentator):
        self.__text = text
        self.__created_at = datetime.date.today()
        self.__created_by = commentator

