# This is a sample Python script.
import psycopg

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import DataFetcher
import DatabaseConnection
import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


    dreef = DataFetcher.DataFetcher()
    dreef.fetchCircuits()

  #  df = pd.read_csv('./f1db_csv/results.csv', "/f1db_csv/races.csv")

  #  print(df.to_string())
