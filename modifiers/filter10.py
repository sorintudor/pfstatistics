import os
import pandas as pd

class Filter10:

    def __init__(self, path, filename):
        self.path = path
        self.name = filename
        self.outpath = path + "/filter10/"
        try:
            os.mkdir(self.outpath)
        except OSError as error:
            print("Directory already exists")

    def split_line_ends(self):
        f = open('{}/{}'.format(self.path,self.name),'r')
        lines = f.readlines()
        line_types = {}
        counter = 1
        for line in lines:
            ending = line.split(',')[-1]
            if ending not in line_types.keys():
                line_types[ending] = counter
                g = open('{}/filter10/.{}.csv'.format(self.path, line_types[ending]), 'a')
                g.write(line)
                g.close()
                counter = counter + 1
            else:
                g = open('{}/filter10/.{}.csv'.format(self.path, line_types[ending]), 'a')
                g.write(line)
                g.close()
    def create_dataframe(self, outpath):
        list_of_df = []
        for f in os.listdir(outpath):
            df = pd.read_csv(f)
            list_of_df.append(df)
