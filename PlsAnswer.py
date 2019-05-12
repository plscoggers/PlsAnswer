import psutil
import subprocess
import argparse


def run(**kwargs):
    while(True):
        for key,value in kwargs.items():
            if key not in (p.name() for p in psutil.process_iter()):
                subprocess.call(value)
                
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
        
