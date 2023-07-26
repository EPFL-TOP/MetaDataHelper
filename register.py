#!/usr/bin/env python3
import sys, os
import json
import commons as cm


#__________________________________________________________
def get_dirs(input):
    #create list of folders to process
    outdirs=[]
    for root, dirs, files in os.walk(input):
        for d in dirs:
            testdir=os.path.join(root,d)
            for key in cm.data_types:
                for type in cm.data_types[key]:
                    if key in testdir and type in testdir and "raw_files" in testdir:
                        if os.path.isfile(testdir.replace("/raw_files","/metadata.json")):
                            print('--> metadata already exist for: ',testdir.replace("/raw_files",""))
                        else:
                            outdirs.append(testdir.replace("/raw_files",""))
                            print('--> adding raw file directory: ',testdir.replace("/raw_files",""))

    return outdirs

#__________________________________________________________
def add_data(input):
    #creating directories in not already done
    datadict={}

    for d in cm.data_dirs:
        datalist=[]
        cdir=os.path.join(input,d)
        if not os.path.isdir(cdir):
            os.makedirs(cdir)
        else:
            print('--> Already exists:   ',cdir)
            print('--> Listing files')
            files=os.listdir(cdir)
            for f in files:
                filedic={}
                if f[0]=='.':continue
                filedic["name"]=f
                filedic["size"]=str(os.path.getsize(os.path.join(cdir,f)))
                datalist.append(filedic)
            datadict[d]=datalist
    return datadict


#__________________________________________________________
def create_metadata(dir):
    outdict={}
    outdict["data"]=add_data(dir)
    outdict["common"]=cm.metadata_common

    #select specific case
    if 'microscopy' in args.input:
        if 'in_vitro' in args.input:
            outdict["specific"]=cm.metadata_invitro
        elif 'in_vivo' in args.input:
            outdict["specific"]=cm.metadata_invivo
    elif 'sequencing' in args.input:      
        if 'CUTandTAG' in args.input:
            outdict["specific"]=cm.metadata_cutandtag
        elif 'scRNA-seq' in args.input:
            outdict["specific"]=cm.metadata_scrna        
        elif 'scMultiome-seq' in args.input:
            outdict["specific"]=cm.metadata_scmultiome
        

    with open(os.path.join(dir,"metadata.json"), "w") as outfile:
        json_object = json.dumps(outdict)
        outfile.write(json_object)
        outfile.close()

#__________________________________________________________
if __name__=="__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="input directory to register the data in the metadata.", type=str, required=True)
    args = parser.parse_args()

    #creating directories in not already done
    dirs=get_dirs(args.input)
    for d in dirs:
        create_metadata(d)
