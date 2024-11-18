import pandas as pd


class DataProvider(object):

    def __init__(self, datasource):
        self._datasource = datasource
        self.apply_map()

    def apply_map(self):
        self.cast_columns()
        columns_map = {column._origin: column._target for column in self._datasource.mapper}
        self.df = self.df.rename(
            columns=columns_map,
            inplace=False
        )
        
    def cast_columns(self):
        for column in  self._datasource.mapper:
            if hasattr(column, 'preprocess'):
                self.df = column.preprocess(self.df)

class CSVProvider(DataProvider):

    def __init__(self, file_path, datasource):
        self.df = pd.read_csv(file_path, dtype=str)
        super().__init__(datasource)
