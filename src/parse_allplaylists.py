import json
import os
import sys

# Print iterations progress (from https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console)
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()

# Open file
inputfn = sys.argv[1]
outputfn = sys.argv[2]   

if not os.path.exists(os.path.dirname(outputfn)):
    try:
        os.makedirs(os.path.dirname(outputfn))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

print("Loading " + inputfn + "...")
buffer = 1000

f = open(inputfn, 'r')
num_lines = sum(1 for line in f)
print('num lines: '+str(num_lines))

f = open(inputfn, 'r')
tmp_lines = f.readlines(buffer)


# THIS IS THE FULL  SCRIPT
g=open(outputfn, 'w', encoding='utf-8')

fields = ['position', 'id', 'code2', 'playlist_id', 'name', 'personalized', 'followers',
          'last_updated', 'owner_name', 'owner_id', 'user_id', 'editorial', 'fdiff_week',
          'fdiff_percent_week', 'fdiff_month', 'fdiff_percent_month',
          'genre', 'monthly_listeners', 'listeners_to_followers_ratio', 'catalog', 'active_ratio']
# header
g.write('retrieval_unix\t'+'\t'.join(fields)+'\n')
cnt=0

print('Starting to parse')

while tmp_lines:
   #if (cnt>10000): break
   for line in tmp_lines:
        parsingobj = json.loads(line.replace('\n',''))

        printProgressBar(cnt, total=num_lines)
        cnt+=1

        for retr in parsingobj.get('retrievals'):
            if retr.get('status_code')!=200: continue
            resp = retr.get('response')
            try:
                if resp.get('obj') is None: continue
            except:
                continue

            for item in resp.get('obj'):
                res = []
                g.write(str(retr.get('timestamp'))+'\t')
                for it in fields:
                    try:
                        tmp=item.get(it)
                        tmp = str(tmp).replace('\t', '').replace('\n',' ')
                    except:
                        tmp = 'NA'
                    res.append(tmp)
                g.write('\t'.join(res)+'\n')
   tmp_lines = f.readlines(buffer)

g.close()
print('Done.')
