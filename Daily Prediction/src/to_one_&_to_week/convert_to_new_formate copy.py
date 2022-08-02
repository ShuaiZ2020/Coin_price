from fileinput import filename
import os
import pandas as pd
import datetime
def get_filename():
    filename_list = []
    path = "D:\\Dropbox (ASU)\\Cryptocurrency\\CoinMarketCap_CoinPrice_data\\old data archieve"
    for i in os.listdir(path):
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
    for j in range(len(data['December_mean'].tolist())):
        for index in index_list:
            if data[data_columns[index]].tolist()[j] != 'There are not enough estimates to calculate the stats':
                values_list.append(data[data_columns[index]].tolist()[j])
            else:
                values_list.append(None)

def convert_formate():
    filename_list = get_filename()
    for i in range(1):
        data = getdata_from_filename(filename_list[i])
        data_columns = data.columns
        print(data.columns)
        #### date
        current_date = data['current_date'].tolist()[0]
        date = datetime.datetime.strptime(str(current_date), '%Y-%m-%d %H:%M:%S')
        date = [date.strftime("%d-%b-%y")]*len(data['current_date'].tolist())*6
        #### crypto_symbol
        url = data['crypto'].tolist()
        crypto_symbol = []
        for j in url:
            url_list = j.split('/')
            coin_name = [url_list[4]]*6
            for j in coin_name:
                crypto_symbol.append(j)
        #### median
        values_median = []
        for j in range(len(data['December_mean'].tolist())):
            if data[data_columns[0]].tolist()[j] != 'There are not enough estimates to calculate the stats':
                values_median.append(data[data_columns[0]].tolist()[j])
            else:
                values_median.append(None)
            if data[data_columns[3]].tolist()[j] != 'There are not enough estimates to calculate the stats':
                values_median.append(data[data_columns[3]].tolist()[j])
            else:
                values_median.append(None)
            if data[data_columns[6]].tolist()[j] != 'There are not enough estimates to calculate the stats':
                values_median.append(data[data_columns[6]].tolist()[j])
            else:
                values_median.append(None)
            if data[data_columns[9]].tolist()[j] != 'There are not enough estimates to calculate the stats':
                values_median.append(data[data_columns[9]].tolist()[j])
            else:
                values_median.append(None)
            if data[data_columns[12]].tolist()[j] != 'There are not enough estimates to calculate the stats':
                values_median.append(data[data_columns[12]].tolist()[j])
            else:
                values_median.append(None)
            if data[data_columns[15]].tolist()[j] != 'There are not enough estimates to calculate the stats':
                values_median.append(data[data_columns[15]].tolist()[j])
            else:
                values_median.append(None)
        print(values_median)


def main():
    convert_formate()
    
if __name__ == "__main__":
    main()