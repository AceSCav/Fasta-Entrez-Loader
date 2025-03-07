import sys
import subprocess
import os
#wget https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi/\?db\=nucleotide\&term\="Psammodromus algirus[organism],cytb[gene]" -O ~/Pal_Ids.xml
#https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi/\?db\=nucleotide\&usehistory\=y\­&query_key\=1\&­WebEnv\=MCID_67c86d8c425d01644607ea69\&rettype\=fasta -O ~/q1.fasta

if len(sys.argv) != 3:
    print("Usage: Script.py 'database' 'organism'")
    sys.exit(1)
current_path = os.getcwd()
database = sys.argv[1]
organism = sys.argv[2]

def get_ids():
    search = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi/\?db\={database}\&term\={organism}'
    url_maker = f'wget "{search}" -O ~Ids.xml'
    subprocess.run(url_maker, shell=True)

get_ids()

