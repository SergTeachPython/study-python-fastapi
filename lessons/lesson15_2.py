from unittest import case

class MyConverter:
    __money_sum = 0
    __uah_rate = 45
    __converter_direction = 1


    def __init__(self,input_money, convert_dir):
        self.__money_sum = input_money
        self.__converter_direction = convert_dir

    @property
    def converter_direction(self):
        return self.__converter_direction

    @converter_direction.setter
    def converter_direction(self, converter_dir):
        if converter_dir == 1 or converter_dir == 2:
            self.__converter_direction = converter_dir
        else:
            raise Exception("Provide corret direction direction")

    def uah_rate(self):
        return self.__uah_rate

    def show_uah_rate(self):
        print(f"Current UAH rate: {self.__uah_rate}")

    def show_result(self):
        print(self.__get_money_result())

    def __get_money_result(self):
        match self.__converter_direction:
            case 1:
                return f"{self.__money_sum} UAH = {self.__get_usd_sum()} USD"
            case 2:
                return f"{self.__money_sum} USD = {self.__get_uah_sum()} UAH"
            case _:
                raise Exception("Incorrect converter direction")

    def __get_usd_sum(self):
        return self.__money_sum / self.__uah_rate

    def __get_uah_sum(self):
        return self.__money_sum * self.__uah_rate


try:
    converter = MyConverter(5000, convert_dir=1)
    converter.show_result()

except Exception as error:
    print(error)






