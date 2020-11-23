import json
import re
from auxilary import printProgressBar
import sys
import glob

jsonpath = sys.argv[1]
outfn = sys.argv[2]  

#jsonpath='e:/projects/data-spotify-playlist-ecosystem/rawdata-confidential/database2_2020_04/playlist-placements_*'

#outfn='../output/playlist-placements.csv'
logfile = '../temp/errlog.log'

# Load data in chunks of 'buffersize' lines
buffer = int(10000E5)

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
    
    
# THIS IS THE FULL  SCRIPT
g=open(outfn, 'w', encoding='utf-8')
    
# header
g.write('playlist_id\t'+'\t'.join(fields)+'\t'+'\t'.join(fields_audio)+'\n')
    
    
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
    
                    # acoustic attributes
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
       tmp_lines = f.readlines(buffer)
    print('Done with file. Proceed.')
    
g.close()
print('Done with all files.')
