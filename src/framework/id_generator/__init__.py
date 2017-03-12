from time import time


class IdGenerateLimitException(Exception):
    pass


class IdGenerator:
    ID_GENERATE_LIMIT = 100000

    def __init__(self):
        self.__counter = 0
        self.__last_timestamp = None

    def generate(self):
        now = int(time())
        return self.generate_by_time(now)

    def generate_by_time(self, timestamp: int):
        if timestamp != self.__last_timestamp:
            self.__counter = 0
            self.__last_timestamp = timestamp
        elif self.__counter >= self.ID_GENERATE_LIMIT:
            raise IdGenerateLimitException()

        uuid = (timestamp << 32) + self.__counter
        self.__counter += 1
        return uuid

    @staticmethod
    def get_time(uuid):
        return uuid >> 32


id_generator = IdGenerator()
