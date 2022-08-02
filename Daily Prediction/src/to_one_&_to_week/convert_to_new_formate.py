from fileinput import filename
from operator import index
import os
import pandas as pd
import datetime

from pkg_resources import to_filename
def get_filename():
    filename_list = []
    path = "D:\\Dropbox (ASU)\\Cryptocurrency\\CoinMarketCap_CoinPrice_data\\old data archieve"
    month_list = ['april_data','may_data']
    for i in month_list:
        monthly_path = path+"\\"+i
        for j in os.listdir(monthly_path):
            filename_list.append(monthly_path+'\\'+j)
    return filename_list

def getdata_from_filename(filename):
    data = pd.read_excel(filename,index_col=0)
    needed_data = data.iloc[:,0:20]
    return needed_data

def formate_to_list(data,values_list,index_list):
    data_columns = data.columns
    for j in range(len(data['current_date'].tolist())):
        for index in index_list:
            if data[data_columns[index]].tolist()[j] != 'There are not enough estimates to calculate the stats':
                values_list.append(data[data_columns[index]].tolist()[j])
            else:
                values_list.append(None)

def convert_formate():
    filename_list = get_filename()
    print(len(filename_list))
    
    for i in range(19,35):
        print(i)
        print(filename_list[i])
        data = getdata_from_filename(filename_list[i])
        data_columns = data.columns
        # print(data.columns)
        ##### data cleaning
        #### date
        current_date = data['current_date'].tolist()[0]
        date = str(current_date).split(' ')[0]
        try:
            date = [datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%d-%b-%y')]*len(data['current_date'].tolist())*6
        except:
            try:
                date = [datetime.datetime.strptime(date, '%d-%b-%y').strftime('%d-%b-%y')]*len(data['current_date'].tolist())*6
            except:
                date = [datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%d-%b-%y')]*len(data['current_date'].tolist())*6
        # if type(current_date) is pd.Timestamp:
        #     date = datetime.datetime.strptime(str(current_date), '%Y-%m-%d %H:%M:%S')
        #     date = [date.strftime("%d-%b-%y")]*len(data['current_date'].tolist())*6
        # else:
        #     date = [datetime.datetime.strptime(str(current_date), '%Y-%m-%d').date().strftime('%d-%b-%y')]*len(data['current_date'].tolist())*6
        #### crypto_symbol
        url = data['crypto'].tolist()
        crypto_symbol = []
        for j in url:
            url_list = j.split('/')
            coin_name = [url_list[4]]*6
            for j in coin_name:
                crypto_symbol.append(j)
        #### average
        values_average = []
        average_index = [0,3,6,9,12,15]
        formate_to_list(data,values_average,average_index)
        #### median
        values_median = []
        median_index = [1,4,7,10,13,16]
        formate_to_list(data,values_median,median_index)
        #### votes
        votes = []
        votes_index = [2,5,8,11,14,17]
        formate_to_list(data,votes,votes_index)
        #### predication_month
        formated_date = []
        for j in data_columns[average_index].tolist():
            formated_date.append(j.split('_')[0])
        formated_date = formated_date*len(data['current_date'])


        source_data = {
                'Date':date,
                "Crypto_symbol":crypto_symbol,
                'Predication_month':formated_date,
                'Votes' : votes,
                'Values_median': values_median,
                'Values_average': values_average
                
            }
        
        df = pd.DataFrame(source_data)
        filename_date = filename_list[i].split('\\')[-1].split('_')[0]
        
        # new_filename = datetime.datetime.strptime(filename_date, '%m-%b-%y').strftime("%Y_%m_%d")+'_Crypto_price.csv'
        new_filename = filename_date+'_Crypto_price.csv'
        print(new_filename)
        df.to_csv('.\\formated_folder\\'+new_filename,index = False)
        

def main():
    convert_formate()
    
if __name__ == "__main__":
    main()