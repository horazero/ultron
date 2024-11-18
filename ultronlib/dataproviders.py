import pandas as pd
class DataProvider(object):
    pass

class CSVProvider(DataProvider):
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
    def GetDF(self):
        return self.df