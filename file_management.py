import os

# Stores a file or several files in a list of tuples: (filename : String, handle : File)
class BinFile:
    
    def __init__(self):
        self.readList = []
        self.writeList = []
        self.iterator = 0
    
    # Clears the list and reverts the iterator back to 0
    def __reset(self):
        for f in self.readList:
            f.close()
        for f in self.writeList:
            f.close()
        self.readList.clear()
        self.writeList.clear()
        self.iterator = 0

    # Extracts file's name and returns it alongside the file handle in a tuple
    def __create_tuple(self, file_handle):
        return (os.path.basename(file_handle.name),file_handle)

    # Loads a single file and saves its filename and handle into a list. Returns the handle for convenience.
    def load_file(self, path):
        handle = open(path, "rb")
        __reset()
        self.readList.append(__create_tuple(handle))
        return handle
    
    # Loads all files within a folder 
    def load_folder(self, path):
        (_, _, filenames) = next(os.walk(path))
        __reset()
        filedirs = []
        for fn in filenames:
            filedirs.append(os.path.join(path, fn))
        for fd in filedirs:
            handle = open(fd, "rb")
            self.readList.append(__create_tuple(handle))
    
    # Each call returns a file handle from the list in order. When there's no more to return, returns -1
    # After each next_read() call, there should be a next_write() call to save changes appropriately
    def next_read(self):
        if self.iterator == len(self.writeList):
            if self.iterator != len(self.readList):
                self.iterator += 1
                return self.readList[self.iterator-1]
            else:
                return -1
        else:
            raise Exception("Every next_read() should be followed by a next_write() before calling next_read() again.")
    
    def next_write(self, path, override_filename=""):
        if self.iterator-1 == len(self.writeList):
            if(override_filename==""):
                file = open(path + "/" + self.readList[self.iterator-1][0], "w+")
            else:
                file = open(path + ("/%s_%04i.txt" % (override_filename, self.iterator-1)))
            self.writeList.append(file)
            return file
        else:
            raise Exception("Called next_write() without calling next_read() first")