import psutil
import subprocess
import argparse


def run(**kwargs):
    while(True):
        for key,value in kwargs.items():
            if key not in (p.name() for p in psutil.process_iter()):
                try:
                    subprocess.call(value)
                except:
                    print("Something wrong with process {}, pls check it out".format(key))
                
def createDict(processes, locations):
    thisDict = {}
    for i in range(0, len(processes)):
        thisDict[processes[i]] = locations[i] + '/' + processes[i]
    return thisDict
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--processes_name',dest='processes',required=True,nargs="+",type=str,help='A tuple of process names')
    parser.add_argument('--processes_location',dest='locations',required=True,nargs="+",type=str,help='A tuple of the location of the .exes')
    args = parser.parse_args()
    if(len(args.processes) == len(args.locations)):
        kwargs = createDict(args.processes, args.locations)
        run(**kwargs)
    else:
        print("Something done went wrong, pls check your inputs")
        
