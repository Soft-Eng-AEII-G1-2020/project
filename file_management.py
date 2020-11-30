import os

# Stores a file or several files in a list of tuples: (filename : String,
# handle : File)


class BinFile:

    def __init__(self):
        self.readList = []
        self.writeList = []
        self.iterator = 0

    # Clears the list and reverts the iterator back to 0
    def reset(self):
        for f in self.readList:
            f[1].close()
        for f in self.writeList:
            f.close()
        self.readList.clear()
        self.writeList.clear()
        self.iterator = 0

    # Extracts file's name and returns it alongside the file handle in a tuple
    def __create_tuple(self, file_handle):
        filename = os.path.basename(file_handle.name)
        filename_no_ext = os.path.splitext(filename)[0]  # remove extension
        return (filename_no_ext, file_handle, filename)

    # Loads a single file and saves its filename and handle into a list.
    def load_file(self, path):
        handle = open(path, "rb")
        self.reset()
        self.readList.append(self.__create_tuple(handle))

    # Loads all files within a folder
    def load_folder(self, path):
        filenames = []
        for _p, _d, f in os.walk(path):
            filenames.append(f)
        filenames = filenames[0]
        self.reset()
        filedirs = []
        for fn in filenames:
            filedirs.append(path + "/" + fn)
        for fd in filedirs:
            handle = open(fd, "rb")
            self.readList.append(self.__create_tuple(handle))

    # Each call returns a file handle from the list in order. When there's no more to return, returns -1
    # After each next_read() call, there should be a next_write() call to save
    # changes appropriately
    def next_read(self):
        if self.iterator == len(self.writeList):
            if self.iterator != len(self.readList):
                self.iterator += 1
                return self.readList[self.iterator - 1][1]
            else:
                return -1
        else:
            raise Exception(
                "Every next_read() should be followed by a next_write() before calling next_read() again.")

    def next_write(self, path, override_filename=False):
        directory, filename = os.path.split(path)
        # make a list [0] - filename, [1] - file extension
        filename = os.path.splitext(filename)
        if self.iterator - 1 == len(self.writeList):
            if(override_filename == False):
                file = open(
                    directory + "/" + self.readList[self.iterator - 1][0] + filename[1], "w+")
            else:
                if(len(self.readList) == 1):
                    file = open(directory + ("/%s%s" %
                                             (filename[0], filename[1])), "w+")
                else:
                    file = open(directory + ("/%s_%04i%s" %
                                             (filename[0], self.iterator - 1, filename[1])), "w+")
            self.writeList.append(file)
            return file
        else:
            raise Exception(
                "Called next_write() without calling next_read() first")

    # Saves file to supplied path, based on the name of the read file (or if
    # requested, a custom filename) with given content.
    def save_file_by_index(self, path, index, content, filename_override=""):
        if filename_override == "":
            actualPath = os.path.split(
                path)[0] + "/" + self.readList[index][0] + "_output.txt"
        else:
            actualPath = os.path.split(
                path)[0] + "/" + filename_override + ".txt"
        file = open(actualPath, "w")
        file.write(content)
        file.close()

    # Get a file name in string format. It contains the extension (ie ".txt",
    # ".bin")
    def get_read_file_name_by_index(self, index):
        if (index < len(self.readList)):
            return self.readList[index][2]
        else:
            raise Exception(
                "get_read_file_name_by_index(" +
                str(index) +
                "): Index out of bounds")

    # Get contents of a file selected by index. I think it's in string format,
    # might be wrong about that though
    def get_read_file_content_by_index(self, index):
        if (index < len(self.readList)):
            file = self.readList[index][1]
            return file.read()
        else:
            raise Exception(
                "get_read_file_content_by_index(" +
                str(index) +
                "): Index out of bounds")

    # Get number of files selected by the user
    def get_file_count(self):
        return len(self.readList)

    def is_single_file(self):
        if len(self.readList) == 1:
            return True
        else:
            return False
