class path_generator():
    def __init__(self, file):
        self.file = file
        self.key = 0
        self.dict = {}
        self.keyWords = ["break", "class", "continue", "else:", "finally", "import"]
        
    def read_file(self):
        self.input_file = open(self.file, "r")
        self.file_lines = self.input_file.readlines() #get eachline
        return self.file_lines

    def generate_path(self):
        python_file = self.read_file()
        for line in python_file:
            line = line.strip()
            words = line.split()
            if (line == ""):
                continue
            if words[0] in self.keyWords:
                continue
            if(words[0] == "if"):
                self.key += 1
                self.dict[self.key] = line
            else:
                self.key += 1
                self.dict[self.key] = line
        return self.dict
    
    def print_path(self):
        path = self.generate_path()
        key = path.keys
        for i in range (len(path)):
            print (i+1, "-->", path[i+1])
                
                
                
