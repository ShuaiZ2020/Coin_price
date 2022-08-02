import datetime
import os
from re import T
import pandas as pd

def main():
    directory = 'D:\\Shuai-Jingbo-Pei-yu\\CoinMarketCap_CoinPrice_data\\Daily Prediction\\May-2022'
    file_list = os.listdir(directory)[:16]
    print(file_list)
    for i in range(len(file_list)):
        filename = directory+"\\"+str(file_list[i])
        df = pd.read_csv(filename)
        # df['Predication_month'] = df['Predication_month'].str.split('-').str[1]
        date_list = df.loc[:,'Predication_month']
        predication_month = []
        for i in range(len(date_list)):
            # date = str(datetime.datetime.strptime(date_list[i],'%b').strftime('%B'))+'-22'
            date = str(date_list[i])+'-22'
            predication_month.append(date)
        df['Predication_month'] = predication_month
        print(df)
        df.to_csv(filename,header = True,index=False)


if __name__ =="__main__":
    main()