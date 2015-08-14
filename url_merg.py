#/usr/bin/python

__author__ = "luantao"
__date__ = "$2015-8-4 10:41:11$"

import getopt
import os
import re
import sys
config = {
    "file":"", 
    "config":""
}  
configList = {}
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:c:", ["help", "file=", "config="])
    except getopt.GetoptError:
        print "-f read-file \n -c config-file"
    for option, value in opts:
        if option in ["-h", "--help"]:
            print "-f read-file\n-c config-file"
            os._exit(1)
        if  option in ["-f", "--file"]:
            config['file'] = value
        if  option in ["-c", "--config"]:
            config['config'] = value
    
    if(config['file'] == ""):
        print "please input file use -f"
        os._exit(1)
    if(config['config'] == ""):
        print "please input config use -c"
        os._exit(1)
    readconfig()    
    
def readconfig():
    f = open(config['config'])
    for line in f.readlines():
        line = line.strip('\n').strip('\r')
        lineF = line.strip()
        if not len(lineF) or lineF.startswith('#'):
            continue
        lineConf = line.split('\t')
        kk = lineConf[0].strip('\"')
        if(configList.has_key(kk)):
            configList[kk].append(lineConf[1].strip('\"'));
        else:
            configList[kk] = [lineConf[1].strip('\"')];
    data_f = open(config['file'])
    single=0
    for data_line in data_f.readlines():
        for (k, v) in configList.items():
            for l in v:
                if re.search(r'%s' % l.lower(), data_line.lower()):
                    on_re(k, data_line)
                    single=1
        if(single==0):
            un_re(data_line)
        single=0

def un_re(txt):
    fileHandle = open ('./un_re/un_re.txt', 'a')
    fileHandle.write(txt);
    fileHandle.close()
def on_re(file_name, txt):
    fileHandle = open ('./on_re/%s.txt' % file_name, 'a')
    fileHandle.write(txt);
    fileHandle.close()
if __name__ == "__main__":
    main()
