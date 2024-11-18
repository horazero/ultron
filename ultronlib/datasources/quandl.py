import pandas as pd


class Column(object):
    def __init__(self, origin, target):
        self._origin = origin
        self._target = target


class CDate(Column):

    def __init__(self, origin, target, fmt):
        super().__init__(origin, target)
        self._format = fmt

    def preprocess(self, df):
        df[self._origin] = pd.to_datetime(
            df[self._origin],
            format=self._format
        )
        return df


class CFloat(Column):
    def __init__(self, origin, target, precision=3):
        super().__init__(origin, target)
        self._precision = precision

    def preprocess(self, df):
        df[self._origin] = pd.to_numeric(
            df[self._origin]
        ).round(self._precision)
        return df


class CInteger(Column):
    pass


class CString(Column):
    pass


class CUnmapped(Column):
    def __init__(self, origin):
        super().__init__(origin, origin)
    
    def preprocess(self, df):

        df = df.drop(columns=self._origin)
        return df


class Quandl(object):
    mapper = [
        CString('ticker', 'ticker'),
        CDate('date', 'date', '%Y-%m-%d'),
        CFloat('open', 'open'),
        CFloat('high', 'high'),
        CFloat('low', 'low'),
        CFloat('close', 'close'),
        CFloat('volume', 'volume', 1),
        CUnmapped('closeadj'),
        CUnmapped('closeunadj'),
        CDate('lastupdated', 'updated', '%Y-%m-%d'),
    ]
