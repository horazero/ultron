import pandas as pd


class DataProvider(object):

    def __init__(self, datasource):
        self._datasource = datasource
        self.apply_map()

    def apply_map(self):
        columns_map = {column._origin: column._target for column in self._datasource.mapper}
        self.df = self.df.rename(
            columns=columns_map,
            inplace=False
        )
        self.cast_columns()
        
    def cast_columns(self):
        for column in  self._datasource.mapper:
            if hasattr(column, 'preprocess'):
                self._datasource = column.preprocess(self._datasource)

class CSVProvider(DataProvider):

    def __init__(self, file_path, datasource):
        self.df = pd.read_csv(file_path)
        super(DataProvider).__init__(datasource)

    def GetDF(self):
        return self.df
