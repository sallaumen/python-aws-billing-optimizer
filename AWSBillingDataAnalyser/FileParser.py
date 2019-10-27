import pandas as pd


class FileParser:
    @staticmethod
    def parse_csv():
        df = pd.read_csv('./dataset/aws-cur-report-sample.csv', sep=',')
        df = FileParser.create_index(df)
        for row in df:
            df[row].fillna('???', inplace=True)
        #raw['UsageType'].fillna('???', inplace=True)
        #raw[tag_name].fillna('???', inplace=True)
        return df

    @staticmethod
    def create_index(df):
        # df = df.set_index('lineItem/ResourceId')  # ResourceId nao presente no doc exemplo
        df = df.set_index('identity/LineItemId')  # ResourceId nao presente no doc exemplo
        df = df.sort_index()
        return df

