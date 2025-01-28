import argparse
import os
from time import time
import pandas as pd
from sqlalchemy import create_engine

parser = argparse.ArgumentParser(description='Ingest csv data to postgres')

#user
#password
#host
#port
#database name
#table name
#url of csv


def main(params):

    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    csv_name ='output.csv'

    os.system(f" wget {url} -O {csv_name}")
    

    #Download the csv
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    #CHUNK THE DATA SIZE INTO SMALLER DATA BITS BY USING ITERATORS

    df_iter = df = pd.read_csv(csv_name, compression='gzip', iterator=True, chunksize=100000)

    df = next(df_iter)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists="replace")

    df.to_sql(name=table_name, con=engine, if_exists="append")


    while True:
        t_start = time()

        df = next(df_iter)

        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        df.to_sql(name=table_name, con=engine, if_exists="append")
        t_end = time()

        print("inserted another chunk... took %.3f second" %(t_end - t_start))

if __name__ == "__main__":

    parser.add_argument('--user')        
    parser.add_argument('--password')     
    parser.add_argument('--host') 
    parser.add_argument('--port')
    parser.add_argument('--db')
    parser.add_argument('--table_name')
    parser.add_argument('--url')

    args = parser.parse_args()

    main(args)
       # print(args.filename, args.count, args.verbose)
