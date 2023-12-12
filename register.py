#!/usr/bin/env python3
import sys, os
import json
import commons as cm
import datetime

#__________________________________________________________
def get_dirs(input, force):
    #create list of folders to process
    outdirs=[]
    for root, dirs, files in os.walk(input):
        for d in dirs:
            testdir=os.path.join(root,d)
            for key in cm.data_types:
                for type in cm.data_types[key]:
                    if key in testdir and type in testdir and "raw_files" in testdir:
                        if os.path.isfile(testdir.replace("/raw_files","/metadata.json")) and not force:
                            print('--> metadata already exist for: ',testdir.replace("/raw_files",""))
                        else:
                            outdirs.append(testdir.replace("/raw_files",""))
                            print('--> adding raw file directory: ',testdir.replace("/raw_files",""))

    return outdirs

#__________________________________________________________
def add_data(input):
    #creating directories if not already done
    datadict={}

    for d in cm.data_dirs:
        datalist=[]
        cdir=os.path.join(input,d)
        if not os.path.isdir(cdir):
            os.makedirs(cdir)
        else:
            print('--> Already exists:   ',cdir)
        print('--> Listing files')

        fname = []
        for root,d_names,f_names in os.walk(cdir):
	        for f in f_names:
		        fname.append(os.path.join(root, f))


        files=os.listdir(cdir)
        files=fname
        for f in files:
            filedic={}
            if f[0]=='.':continue
            filedic["name"]=f
            filedic["size"]=str(os.path.getsize(os.path.join(cdir,f)))
            datalist.append(filedic)
        newlist = sorted(datalist, key=lambda d: d['name']) 
        datadict[d]=newlist
    return datadict


#__________________________________________________________
def create_metadata(dir):
    outdict={}
    outdict["data"]=add_data(dir)
    outdict["date"]=datetime.datetime.now().strftime('%Y-%m-%d')

    with open(os.path.join(dir,"metadata.json"), "w") as outfile:
        json_object = json.dumps(outdict)
        outfile.write(json_object)
        outfile.close()

#__________________________________________________________
if __name__=="__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="input directory to register the data in the metadata.", type=str, required=True)
    parser.add_argument("--force", help="force recreation of the metadata.", action='store_true')
    args = parser.parse_args()

    #creating directories in not already done
    dirs=get_dirs(args.input, args.force)
    for d in dirs:
        create_metadata(d)
