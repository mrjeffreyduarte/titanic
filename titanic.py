#! /usr/bin/env python
import pandas as pd

file_path = 'train.csv'


def csv_to_df(file_path):
    df = pd.DataFrame(pd.read_csv(file_path))

    return df


def get_survivors(dataframe):
    survivors_df = 'Hello'

    return survivors_df


if __name__ == '__main__':
    original_df = csv_to_df(file_path)
    survivors = get_survivors(original_df)
    print survivors
