import pandas as pd


class FileParser:
    @staticmethod
    def parse_csv():
        df = pd.read_csv('./dataset/aws-cur-report-sample.csv', sep=',')
        df = FileParser.create_index(df)
        FileParser._fill_null_fields(df)

        return df

    @staticmethod
    def _fill_null_fields(df):
        for column in df:
            df[column].fillna('???', inplace=True)

    @staticmethod
    def create_index(df):
        # df = df.set_index('lineItem/ResourceId')  # ResourceId nao presente no doc exemplo
        df = df.set_index('identity/LineItemId')  # ResourceId nao presente no doc exemplo
        df = df.sort_index()
        return df

