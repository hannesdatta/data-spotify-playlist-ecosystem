import json
import os
import zipfile
import re
from auxilary import printProgressBar
import sys
import glob
# Open file
jsonpath = sys.argv[1]

outfn = sys.argv[2]  

# Parse
g=open(outfn, 'w', encoding='utf-8')
fields = ['value','timestp','interpolated']

# Write header
g.write('playlist_id\t'+'\t'.join(fields)+'\n')

# Load data in chunks of 'buffersize' lines
buffer = int(10000E5)

logfile = 'followers.log'

fns = glob.glob(jsonpath)

for jsonfn in fns:
    print(jsonfn)
    
    # Calculate file size in lines
    print("Loading " + jsonfn + " to count lines...")
    f = open(jsonfn, 'r')
    num_lines = sum(1 for line in f)
    print('number of lines: '+str(num_lines))
    
    # Read 'buffersize' lines at the time
    f = open(jsonfn, 'r')
    tmp_lines = f.readlines(buffer) # first x lines
    
    cnt=0
    
    print('Starting to parse')
    
    errlog=open(logfile, 'w', encoding = 'utf-8')
    errlog.close()
    linenumber=0
    
    while tmp_lines:
       #if (cnt>100): break
       for chunk in tmp_lines:
            parsingobj = json.loads(chunk.replace('\n',''))
            printProgressBar(cnt, total=num_lines)
            cnt+=1
                       
            #for parsingobj in chunkobj:
            playlist_id = 'NA'
            m = re.search('spotify/(.+?)/', parsingobj.get('url'))
            if m:
                playlist_id = m.group(1)
            
            for retr in parsingobj.get('retrievals'):
                if retr.get('status_code')!=200: continue
                resp = retr.get('response')
                try:
                    if resp.get('obj') is None: continue
                except:
                    continue
                  
                for item in resp.get('obj'):
                    res = []
                    g.write(playlist_id+'\t')
                    for it in fields:
                        try:
                            tmp=item.get(it)
                            tmp = str(tmp).replace('\t', '').replace('\n',' ').replace('T00:00:00.000Z','')
                        except:
                            tmp = 'NA'
                        res.append(tmp)
                    g.write('\t'.join(res)+'\n')
       tmp_lines = f.readlines(buffer)
    print('Done with file. Proceed.')
     
g.close()
print('Done.')