import os,re

def split_file(path,filename):
    count = {}
    f = open('{}/{}'.format(path,filename),'r')
    lines = f.readlines()
    for line in lines:
        if parse_line(line) in count.keys():
            g = open('{}/{}.{}.csv'.format(path,filename,parse_line(line)), 'a')
            g.write(format_line(line))
            count[parse_line(line)] = count[parse_line(line)] + 1
            g.close()
        else:
            count[parse_line(line)] = 1
    print(count)
def parse_line(line):
    # Use a breakpoint in the code line below to debug your script.
    splited_list = line.split(' ')
    final_list = splited_list[:-1] + splited_list[-1].split(',')
    return len(final_list)

def format_line(line):
    splited_list = line.split(' ')
    final_list = splited_list[:-1] + splited_list[-1].split(',')
    return ','.join(final_list)
def purge(path):
    for f in os.listdir(path):
        if '.csv' in f:
            os.remove(os.path.join(path, f))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    purge('/Users/tudorsorin/filterpfsense/')
    split_file('/Users/tudorsorin/filterpfsense/','filter.log.concat')


