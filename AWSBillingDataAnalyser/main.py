from datetime import time
from FileParser import FileParser
from CurProcessor import CurProcessor

if __name__ == '__main__':
    df = FileParser.parse_csv()
    data_processor = CurProcessor(df)
    data_processor.graph_cost_by_product('EC2')