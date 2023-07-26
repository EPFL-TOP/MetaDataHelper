import os, sys
import glob
import json
import datetime
import commons as cm

path = "/Volumes/upoates-raw/raw_data/"

try:
    os.listdir(path)
except FileNotFoundError:
    print("probably volume is not mounted, or vpn is out, exit")
    sys.exit(3)
data_type=cm.data_types

outdict={}
outdictlist=[]

#list data types
for key in data_type:
    #list sub data types
    for type in data_type[key]:
        #list projects
        for proj in os.listdir(os.path.join(path,key,type)):
            if proj[0]=='.':continue
            #list experiments
            for exp in os.listdir(os.path.join(path,key,type,proj)):
                if exp[0]=='.':continue

                basedir=os.path.join(path, key, type, proj, exp)
                basefile=os.path.join(basedir,'metadata.json')
                if not os.path.isfile(basefile):
                    print('metadata missing in ',basedir)
                else:
                    f = open(basefile)
                    data = json.load(f)
                    outdicttmp={}
                    outdicttmp[basedir]=data
                    outdictlist.append(outdicttmp)

summaryname="metadatasummary"
latest=glob.glob(os.path.join(path,"metadata",summaryname+"*_latest.json"))
if len(latest)>1:
    print("more than 1 latest, please check, exit")
    sys.exit(3)

if len(latest)==1:
    f = open(latest[0])
    data = json.load(f)
    if outdict==data:
        print("identical latest file, return")
        sys.exit(3)

now=datetime.datetime.now()
outdict["date"]=str(now.date())
outdict["time"]=str(now.time())
outdict["data"]=outdictlist

with open(os.path.join(path,"metadata",'{}_{}_{}_latest.json'.format(summaryname,now.date(), now.time())), "w") as outfile:
    json_object = json.dumps(outdict)
    outfile.write(json_object)
    outfile.close()

if len(latest)==1:
    os.system("mv {} {}".format(latest[0], latest[0].replace("_latest","")))