import json
import re
from auxilary import printProgressBar
import sys
# Open file

jsonfn = sys.argv[1]
outfn = sys.argv[2]


#jsonfn='../externals/fans-instagram.json' # temp file (extracted from zip file)
#outfn='../output/fans-instagram.csv' # final file, parsed CSV

# Calculate file size in lines
print("Loading " + jsonfn + "...")
buffer = 10000

try:
    f = open(jsonfn, 'r')
    num_lines = sum(1 for line in f)
    print('num lines: '+str(num_lines))
except:
    print('Cant load file length; assuming 1E6')
    num_lines=1E6
    
# Read file line-by-line
f = open(jsonfn, 'r')
tmp_lines = f.readlines(buffer)



# Parse
g=open(outfn, 'w', encoding='utf-8')
fields = ['value','timestp','flags']

# Write header
g.write('cm_artistid\tlink\t'+'\t'.join(fields)+'\n')
cnt=0

print('Starting to parse')

while tmp_lines:
   #if (cnt>100): break
   for chunk in tmp_lines:
        parsingobj = json.loads(chunk.replace('\n',''))
        printProgressBar(cnt, total=num_lines)
        cnt+=1
                   
        artist_id = 'NA'
        m = re.search('artist/(.+?)/', parsingobj.get('url'))
        if m:
            artist_id = m.group(1)
        
        for retr in parsingobj.get('retrievals'):
            if retr.get('status_code')!=200: continue
            resp = retr.get('response')
            try:
                if resp.get('obj') is None: continue
            except:
                continue
            link = str(resp.get('obj').get('link'))
            handle = 'fans'
            if ('deezer' in jsonfn): handle = 'fans'
            if ('instagram' in jsonfn): handle = 'followers'
            for item in resp.get('obj').get(handle):
                res = []
                g.write(artist_id+'\t')
                g.write(link+'\t')
                for it in fields:
                    try:
                        tmp=item.get(it)
                        tmp = str(tmp).replace('\t', '').replace('\n',' ').replace('T00:00:00.000Z','')
                    except:
                        tmp = 'NA'
                    res.append(tmp)
                g.write('\t'.join(res)+'\n')
   tmp_lines = f.readlines(buffer)
   
g.close()
print('Done.')