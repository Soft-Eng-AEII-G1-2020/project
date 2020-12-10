

class BinConverter:
    def __init__(self):
        self.text_output = ""
        self.byte_count = 0

    # Splits the supplied string into byte-long chunks
    def __prepare_input_data(self, data):
        self.text_output = ""
        self.byte_count = round(len(data) / 9)

    # Converts input binary data to output text (byte-by-byte)
    def __process_to_ascii(self, data):
        for byte in range(self.byte_count):
            self.text_output = self.text_output + chr(int(data[(byte*9):(byte*9+8)], base=2))

    # Converts input binary data to hexadecimal form (byte-by-byte)
    def __process_to_hex(self, data):
        for byte in range(self.byte_count):
            self.text_output = self.text_output + ("%0.2X" % int(data[(byte*9):(byte*9+8)], base=2)) + " "
    
    # Converts input binary data to decimal form (byte-by-byte)
    def __process_to_decimal(self, data):
        for byte in range(self.byte_count):
            self.text_output = self.text_output + ("%0.3d" % int(data[(byte*9):(byte*9+8)], base=2)) + " "
    
    # Converts input binary data to octal form (byte-by-byte)
    def __process_to_octal(self, data):
        for byte in range(self.byte_count):
            self.text_output = self.text_output + ("%0.3o" % int(data[(byte*9):(byte*9+8)], base=2)) + " "

    # Takes binary data (as string of hexes) and converts it to an ascii string
    def convert(self, data, toFormat):
        self.__prepare_input_data(data)
        if(toFormat == 0):
            self.__process_to_ascii(data)
        if(toFormat == 1):
            self.__process_to_hex(data)
        if(toFormat == 2):
            self.__process_to_decimal(data)
        if(toFormat == 3):
            self.__process_to_octal(data)
        return self.text_output
