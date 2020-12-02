

class BinConverter:
    def __init__(self):
        self.binary_input = ""
        self.text_output = ""

    # Splits the supplied string into byte-long chunks
    def __prepare_input_data(self, data):
        self.binary_input = data.split(" ")

    # Converts from hexadecimal char to number
    def __letter_to_number(self, letter):
        if letter in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            return int(letter)
        if letter == "A":
            return 10
        if letter == "B":
            return 11
        if letter == "C":
            return 12
        if letter == "D":
            return 13
        if letter == "E":
            return 14
        if letter == "F":
            return 15
        raise Exception("__letter_to_number(): Supplied wrong input data (outside of 0 - F range)")
    
    # Converts input binary data to output text
    def __process_data(self):
        self.text_output = ""
        for byte in self.binary_input:
            msb = self.__letter_to_number(byte[0])*16
            lsb = self.__letter_to_number(byte[1])
            self.text_output = self.text_output + [chr(msb+lsb)]

    # Takes binary data (as string of hexes) and converts it to an ascii string
    def convert(self, data):
        self.__prepare_input_data(data)
        self.__process_data()
        return self.text_output