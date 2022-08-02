from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import ast
directory = 'D:\\Shuai-Jingbo-Pei-yu\\CoinMarketCap_CoinPrice_data\\Daily Prediction\\src\\to_one_&_to_week\\'
open(directory+'temp.csv','w')
first = True
def get_short_symbol(full_symbol):
    url = 'https://coinmarketcap.com/currencies/'+full_symbol
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'lxml')
    short_symbol = soup.find('small',{'class':'nameSymbol'}).text
    return short_symbol
def remove_comma(number):
    if number is None or number == '':
        return None
    else:
        try:
            number_return = float(str(number).replace(',',''))
            return number_return
        except:
            return None

def formate():
    global first
    global directory 
    df = pd.read_csv(r'D:\Shuai-Jingbo-Pei-yu\CoinMarketCap_CoinPrice_data\Daily Prediction\Jun-2022\02-Jun-22_Crypto_price.csv')
    # print(df)
    Date = df['Date'].tolist()
    
    Crypto_symbol = df['Crypto_symbol'].tolist()
    
    Predication_month = df['Predication_month'].tolist()
    Votes = df['Votes'].tolist()
    Values_median = df['Values_median'].tolist()
    Values_average = df['Values_average'].tolist()
    month_2021 = ['November','December']
    symbol_dict = {}
    with open(directory+'dict.txt','r') as file:
        dict = file.read()
    symbol_dict = ast.literal_eval(dict)
    

    for i in range(0,len(Crypto_symbol),6):
        
        print(Crypto_symbol[i])
        try:
            short_symbol = symbol_dict[Crypto_symbol[i]]
            print('try')
        except:
            short_symbol = get_short_symbol(Crypto_symbol[i])
            symbol_dict = symbol_dict|{Crypto_symbol[i]:short_symbol}
            with open(directory+'dict.txt','w') as file:
                file.write(str(symbol_dict))
            print('get')
       
        print(short_symbol)
        for j in range(6):  
            index = i+j
            if Predication_month[index] in month_2021:
                Predication_month_year = Predication_month[index]
            else:
                Predication_month_year = Predication_month[index] 
            data = {
                'Date' : [Date[index]] ,
                'Crypto_symbol': [short_symbol],
                'Predication_month_year':[Predication_month_year],
                'Votes' : [remove_comma(Votes[index])],
                'Values_median': [remove_comma(Values_median[index])],
                'Values_average' : [remove_comma(Values_average[index])]

            }
            df = pd.DataFrame(data)
            if first:
                df.to_csv(directory+'temp.csv', mode='a',index = False,encoding='utf-8')
                first = False
            else:
                df.to_csv(directory+'temp.csv', mode='a',header=False, index = False,encoding='utf-8')
                
# def combine():
#     df = pd.read_csv('temp copy.csv')
#     df2 = pd.read_csv('weekly_net.csv')
#     Date = df2['Date'].tolist()
#     net_votes = df2['net_votes'].tolist()
#     net_median = df2['net_median'].tolist()
#     net_average = df2['net_average'].tolist()
#     df.insert(0,'Date',Date)
#     df.insert(6,'net_votes',net_votes)
#     df.insert(7,'net_median',net_median)
#     df.insert(8,'net_average',net_average)
#     print(df)
#     df.to_csv('new_weekly_net.csv',index = False)
    


def main():
    formate()

if __name__ == "__main__":
    main()