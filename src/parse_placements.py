import json
import re
from auxilary import printProgressBar
import sys
import glob
import os

try:
	os.mkdir('../output')
except:
	print('output dir exists.')

try:
	os.mkdir('../temp')
except:
	print('temp dir exists.')

jsonpath = sys.argv[1]
fn_parsed_placements = sys.argv[2]  
fn_parsed_positions = sys.argv[3] 

#jsonpath='../externals/playlist-placements.json'
#fn_parsed_placements='../output/test-parse-placements.csv'
#fn_parsed_positions = '../output/test-parse_positions'

logfile = '../temp/errlog.log'

# Load data in chunks of 'buffersize' lines
buffer = int(10000E5)

# Define variables that will be parsed
fields = ['track_id',
              #'isrc',
              #'position',
              'added_at','removed_at',
              #'period',
              #'id',
              'name',
              'spotify_album_id',
              'spotify_popularity',
              #'cm_track',
              'track_genre',
              'cm_artist',
              'artist_names',
              #'code2s',
              'spotify_duration_ms',
              'album_names', 'album_label', 'release_dates']
 
fields_audio = ['key', 'mode', 'danceability','energy','speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence','tempo', 'loudness']
    
# Open output CSV files for writing
g=open(fn_parsed_placements, 'w', encoding='utf-8')
h=open(fn_parsed_positions, 'w', encoding='utf-8')
     
# Write headers
g.write('playlist_id\t'+'\t'.join(fields)+'\t'+'\t'.join(fields_audio)+'\n')
h.write('playlist_id\ttrack_id\tdate\tposition\n')
    
# Search for files to parse
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
       linenumber+=1
       #if (cnt>100): break
       for chunk in tmp_lines:
            try:
               parsingobj = json.loads(chunk.replace('\n',''))
            except:
               errlog=open(logfile, 'a', encoding = 'utf-8')
               errlog.write('line number: ' + str(linenumber) + '; item number: ' + str(cnt)+'\n')
               errlog.write(chunk+'\n\n')
               errlog.close()
    
            printProgressBar(cnt, total=num_lines, prefix = cnt)
            cnt+=1
    
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
                    
                    # Parse data on "fields"
                    res = []
                    g.write(playlist_id+'\t')
                    for it in fields:
                        try:
                            tmp=item.get(it)
                            if type(tmp) is list:
                                tmp = '|'.join(str(e).replace('|','') for e in list(set(tmp)))
                            tmp = str(tmp).replace('\t', '').replace('\n',' ')
                            tmp = tmp.replace('T00:00:00.000Z','')
                        except:
                            tmp = 'NA'
                        res.append(tmp)
                    g.write('\t'.join(res)+'\t')
    
                    # Parse data on acoustic attributes
                    res=[]
                    for it in fields_audio:
                        try:
                            tmp=item.get('audio_features').get(it)
                            if type(tmp) is list:
                                tmp = '|'.join(str(e) for e in list(set(tmp)))
                            tmp = str(tmp).replace('\t', '').replace('\n',' ')
                            tmp = tmp.replace('T00:00:00.000Z','')
                        except:
                            tmp = 'NA'
                        res.append(tmp)
                    g.write('\t'.join(res)+'\n')
                    
                    # Parse position data
                    for pos in item.get('position_stats'):
                        pos_timestamp = pos.get('timestp').replace('T00:00:00.000Z','')
                        h.write(str(playlist_id)+'\t'+str(item.get('track_id'))+'\t'+pos_timestamp+'\t' + str(pos.get('position'))+'\n')
                    
       tmp_lines = f.readlines(buffer)
    print('Done with file. Proceed.')
    
g.close()
print('Done with all files.')
