import pandas as pd
import datetime
first = True
to_file = 'D:\\Shuai-Jingbo-Pei-yu\\CoinMarketCap_CoinPrice_data\\Daily Prediction\\src\\to_one_&_to_week\\weekly_net.csv'
open(to_file,'w')  
def getdata_from_filename(filename):
    data = pd.read_csv(filename)
    return data
def extract_date_list(start_date,data):
    date_list = data['Date'].tolist()
    previous = ''
    unique_datelist = []
    for i in range(len(date_list)):
        if date_list[i] != previous:
            previous = date_list[i]
            unique_datelist.append(date_list[i])
    unique_datelist = unique_datelist[unique_datelist.index(start_date):]
    return unique_datelist
def net(net_list,current_row,week_ago_row,value):
    week_ago_value= str(week_ago_row[value].tolist()[0]).replace(',','')
    current_value = str(current_row[value]).replace(',','')
    if week_ago_value =='' or str(week_ago_value) =='nan':
        week_ago_value = None
    if current_value != None and week_ago_value != None:
        if value == 'Votes':
            net_value = float(current_value)-float(week_ago_value)
        else:
            current_votes = str(current_row['Votes']).replace(',','')
            week_ago_votes = str(week_ago_row['Votes'].tolist()[0]).replace(',','')

            net_votes = float(current_votes)-float(week_ago_votes)
            
            net_value = (float(current_value)*float(current_votes)-float(week_ago_value)*float(week_ago_votes))/(net_votes)
            # print(net_value)
    net_list.append(net_value)
    # print(net_value)
    # print('len: '+str(len(net_list)))
    return net_list

def get_netvote(df,date_list):
    global to_file
    global first
    for i in range(28,len(date_list)):

        df_current = df.loc[df['Date']==date_list[i]]
        df_week_ago = df.loc[df['Date'] == date_list[i-28]]
        
        net_vote_list = []
        net_median_list = []
        net_average_list = []
        for j in range(len(df_current)):
            current_row = df_current.iloc[j,:]
            # try:
            #     week_ago_row = df_week_ago[(df_week_ago['Crypto_symbol'] == current_row['Crypto_symbol']) & (df_week_ago['Predication_month'] == current_row['Predication_month'])]
            # except:
            # print(df_week_ago['Predication_month'].str.split('-', expand=True))



            try:
                week_ago_row = df_week_ago[(df_week_ago['Crypto_symbol'] == current_row['Crypto_symbol']) & (df_week_ago['Predication_month_year'] == current_row['Predication_month_year'] )]
                # print(week_ago_row)
                # print(current_row)
                # print('---')
                net_vote_list = net(net_vote_list,current_row,week_ago_row,'Votes')
            except:
                net_vote_list.append(None)

            try:
                net_median_list = net(net_median_list,current_row,week_ago_row,'Values_median')
            except:
                net_median_list.append(None)
                
            try:
                net_average_list = net(net_average_list,current_row,week_ago_row,'Values_average')
            except:
                net_average_list.append(None)
        df_current['net_votes'] = net_vote_list
        df_current['net_median'] = net_median_list
        df_current['net_average'] = net_average_list
        print(df_current)
        if first:
            df_current.to_csv(to_file, mode='a',index = False,encoding='utf-8')
            first = False
        else:
            df_current.to_csv(to_file, mode='a',header=False, index = False,encoding='utf-8')
            # print('----')

def main():
    filename = r'D:\Shuai-Jingbo-Pei-yu\CoinMarketCap_CoinPrice_data\Daily Prediction\src\to_one_&_to_week\total-before-jun.csv'
    data_before_jun = getdata_from_filename(filename)
    data_after_jun = getdata_from_filename(r'D:\Shuai-Jingbo-Pei-yu\CoinMarketCap_CoinPrice_data\Daily Prediction\src\to_one_&_to_week\total-after-Jun.csv')
    data = pd.concat([data_before_jun,data_after_jun])
    # pm = []
    # for i in data['Predication_month']:
    #     date = i.split('-')[0]
    #     pm.append(date)
    # print(data.loc[data['Date']=='21-May-22'])
    # data['Predication_month'] = pm
    start_date = '19-Nov-21'
    date_list = extract_date_list(start_date,data)
    # print(date_list)
    get_netvote(data,date_list)

# def remove_negative_net():
#     filename = 'new_weekly_net.csv'
#     data = getdata_from_filename(filename)
#     date_list = extract_date_list(data)
#     for i in 

if __name__ == "__main__":
    main()