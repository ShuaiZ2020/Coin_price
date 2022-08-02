import os
import pandas as pd
import datetime

first = True
file_name = 'D:\\Shuai-Jingbo-Pei-yu\\CoinMarketCap_CoinPrice_data\\Daily Prediction\src\\to_one_&_to_week\\total-after-Jun.csv'
open(file_name,'w')
def get_filename():
    filename_list = []
    path = "D:\\Shuai-Jingbo-Pei-yu\\CoinMarketCap_CoinPrice_data\\Daily Prediction"
    month_list = ['Jun-2022'] ### update month in here
    for i in month_list:
        monthly_path = path+"\\"+i
        for j in os.listdir(monthly_path):
            filename_list.append(monthly_path+'\\'+j)
    return filename_list

def getdata_from_filename(filename):
    data = pd.read_csv(filename)
    return data

def to_onefile():
    global first
    filename_list = get_filename()
    length_filename_list = len(filename_list)
    for i in range(length_filename_list):
        data = getdata_from_filename(filename_list[i])
        data.rename(columns = {'Predication_month':'Predication_month_year'},inplace= True)
        data['Predication_month_year'] = pd.to_datetime(data['Predication_month_year'],format='%B-%y').dt.strftime('%b-%y')
        if first:
            data.to_csv(file_name, mode='a',index = False,encoding='utf-8')
            first = False
        else:
            data.to_csv(file_name, mode='a',header=False, index = False,encoding='utf-8')
            

def main():
    to_onefile()
    
if __name__ == "__main__":
    main()