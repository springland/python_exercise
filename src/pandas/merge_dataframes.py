
import pandas as pd


def   merge_dataframes(df1 , df2):

    df = pd.concat([df1 , df2] , axis = 0)

    return df



def  group_by_and_agg():
    d = {'col1' : [1 , 2  , 2] , 'col2' : [3 , 4 , 4] , 'col3' : [ 1 , 1  , 1] , 'col4': [1 , 2 , 1] }
    df1 = pd.DataFrame(data=d)

    df2 = pd.DataFrame(data=d)

    print(df1 )

    print(df2)

    df3 = merge_dataframes(df1 , df2)
    print(df3)

    agg_func = {
        'col3' : ['sum'] , 'col4': ['mean']
    }
    df4 = df3.groupby(['col1' , 'col2']).agg(agg_func)
    print(df4)


if __name__ == '__main__':



    df1 = pd.read_csv('data/data1.csv')
    df2 = pd.read_csv('data/data2.csv')
    df3 = pd.concat([df1  , df2] , axis=0)

    group_by_col_names = ['gene site' , 'genome site' , 	'wt nt' , 	'mutant nt' , 	'aa site' , 	'wt aa', 'mutant aa']
    agg_func = {
        'total seq.':['sum'] , 'count':['sum']
    }

    df4 = df3.groupby(group_by_col_names).agg(agg_func)
    print(df4)