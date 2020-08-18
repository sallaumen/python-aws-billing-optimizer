import pandas as pd
import pandas.plotting
import matplotlib.pyplot as plt
import numpy


class CurProcessor:

    def __init__(self, df):
        self.df = df

    def graph_cost_by_product(self, product_code):
        # Custo por produto(Bom filtrar para ProductCode = EC2 *) X = UsageStartDate Y = Unblended Cost, Comparador =
        # PricingTerm(Variações de EC2)
        df = self._filtered_by_ProductCode(product_code)

        date_field = 'lineItem/UsageStartDate'
        df['lineItem/UnblendedCost'] = df['lineItem/UnblendedCost']  # .astype(float)
        df = self._simplify_date(date_field, df)

        df.plot.bar(x=date_field, y=['lineItem/UnblendedCost', 'lineItem/ProductCode'], stacked=True)

        # df.plot.bar(x=date_field, y=['lineItem/ProductCode'], values=['TotalCost'], aggfunc=numpy.sum,
        #                        margins=True)
        plt.show()

    def _simplify_date(self, date_field, df):
        df[date_field] = df[date_field].str.replace('T00:00:00Z', '')
        # df[date_field] = pd.to_datetime(df[date_field])
        return df

    def create_graph(self):
        # Comparar gasto por tipo de instância(gráfico de barras) Y = InstaceType, X = (Sum) UsageAmount Comparador =
        # PricingTerm
        pass

    def _filtered_by_ProductCode(self, filter):
        df_copy = self.df
        # prevous_df_shape = df_copy.shape()
        drop_indexes = [index for index in df_copy.index if (filter in df_copy['lineItem/ProductCode'])]
        df_copy.drop(drop_indexes)
        # assert prevous_df_shape != df_copy.shape()
        # remove_rule = df_copy.loc[(filer not in df_copy['lineItem/ProductCode'])]
        # df_copy = df_copy.drop(remove_rule.index)
        return df_copy
