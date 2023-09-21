#importing libraries
import numpy as np
import pandas as pd
import os
#import tensorflow as tf
#testing will this work

def to_read(file_name, header_name):
    '''
    Takes the wanted filenames without the .csv and formats it properly

        Parameter:
                file_name (csv): a sample file with data
                header_name (csv): file with all the headers
    '''
    # file_name = "CAS_2018-C01_G1_102018"
    # file has 186,525 rows of data, excluding the first row (which is the header)

    headerDf = pd.read_csv(r"./Data/" + header_name + ".csv", encoding='unicode_escape')
    header = headerDf.columns.tolist()
    df = pd.read_csv(r"./Data/" + file_name + ".csv", sep = '|', names = header)
    df.to_csv(r"./Data/" + file_name + "_Header.csv", index = False)

    return df

def data_visualization(file_name):
    '''
    Testing to better visualize data

    '''
    df = pd.read_csv(r"./Data/" + file_name + ".csv")
    # data.head(20)
    # date_cols = [col for col in data.columns if 'Date' in col]
    # print(date_cols)
    # data.describe(include='all')
    # data.loc['Original UPB'] > 1000000
    
    
    #columns_with_nulls = df.columns[df.isnull().any()].tolist()
    # print(np.sum(df.isnull().any(), axis = 0)) --> 68 columns that have null values
    # print(columns_with_nulls)
    # print(np.sum(df[columns_with_nulls].isnull(), axis = 0)) --> 10,000 to all the rows

    print(np.sum(df['Zero Balance Code'].isnull())) # --> 176,525
    print(df['Current Loan Delinquency Status'])

def make_new(file_name):
    '''
    Testing to better visualize data
    
    '''
    df = pd.read_csv(r"./Data/" + file_name + ".csv")
    # df = df[['Current Actual UPB', 'Remaining Months to Legal Maturity', 'Zero Balance Code']]
    # df = df[['Original UPB', 'Loan Age', 'Loan Payment History', 'Foreclosure Date', 'Zero Balance Code']]
    df = df[['Channel','Seller Name', 'Servicer Name', 'Original UPB', 'Current Actual UPB', 'Remaining Months to Legal Maturity','Zero Balance Code']]
    #df.dropna(subset=['Zero Balance Code'], inplace=True)
    df.to_csv(r"./Data/unpaid_testing.csv", index = False)

if __name__ == "__main__":
    #data = to_read("CAS_2018-C01_G1_102018", "CRT_Header_File")
    #data_visualization("CAS_2018-C01_G1_102018_Header")
    make_new("CAS_2018-C01_G1_102018_Header")
    