from TwitterPost import TwitterPost
from datetime import datetime

class StockPricePost(TwitterPost):
    def __init__(self, stock: str, price: float, time: datetime):
        self.__stock = stock
        self.__price = price
        self.__time = time

    def get_post_text(self):
        return (
            f"${self.__stock} is now at {self.__price}.\n"
            f"Time: {self.__time.strftime('%H:%M')}"
        )
