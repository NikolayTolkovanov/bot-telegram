#Хранение и обработка значений с сайта

class Data():
    def __init__(self, values):
        self.names = values[0::3]#Список имен
        self.sell_price = values[1::3]#Список цен продажи
        self.buy_price = values[2::3]#Список цен покупки

        self.best_sell_price = max(self.sell_price)#Самая выгодная цена продажи
        self.best_buy_price = min(self.buy_price)#Самая выгодная цена покупки

    def get_all_list(self):#Весь список с банком, ценой покупки и продажи
        message = ''
        i = 0
        while i<len(self.names):
            message += f'{self.names[i]}: \nПродажа: {self.sell_price[i]}\nПокупка: {self.buy_price[i]}\n\n'
            i+=1

        message = message.strip()
        
        return message

    def __get_best_values(self, values, best_value):
        i=0
        message = ''
        while i<len(values):
            i+=1
            if values[i] == best_value:
                message += f'{self.names[i]} - {best_value}\n'
            
                message = message.strip()
                return message

    def get_best_buy_price(self):
        return self.__get_best_values(self.buy_price, self.best_buy_price)
            
    def get_best_sell_price(self):
        return self.__get_best_values(self.sell_price, self.best_sell_price)