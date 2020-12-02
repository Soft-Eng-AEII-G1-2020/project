

class BinConverter:
    def __init__(self):
        self.text_output = ""
        self.byte_count = 0

    # Splits the supplied string into byte-long chunks
    def __prepare_input_data(self, data):
        self.byte_count = round(len(data)/3)
    
    # Converts input binary data to output text
    def __process_data(self, data):
        self.text_output = ""
        for i in range(self.byte_count):
            self.text_output = self.text_output + chr(int(data[(i*3):(i*3)+2], base=16))

    # Takes binary data (as string of hexes) and converts it to an ascii string
    def convert(self, data):
        self.__prepare_input_data(data)
        self.__process_data(data)
        return self.text_output