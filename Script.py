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

def ids_getter():
    search = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi\?db\="{database}"\&term\="{organism}"\&usehistory\=y'
    url_maker = f'wget {search} -O Ids.xml'
    subprocess.run(url_maker, shell=True)

def ids_parser():
    with open(current_path + '/Ids.xml', 'r') as xml_file:
        ids = xml_file.readlines()
    t1 = []
    for line in ids:
        t1.append(line.split("><"))
    QueryKey = t1[2][4].strip("QueryKey></QueryKey")
    WebEnv = t1[2][5].strip("WebEnv></WebEnv")
    return QueryKey, WebEnv

def fasta_printer(QueryKey, WebEnv):
    fetch = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi\?db\="{database}"\&usehistory\=y\&query_key\="{QueryKey}"\&WebEnv\="{WebEnv}"\&rettype\=fasta'
    url_maker = f'wget {fetch} -O sequences.fasta'
    printer = f'cat sequences.fasta'
    subprocess.run(url_maker, shell=True)
    subprocess.run(printer, shell=True)

ids_getter()
QueryKey, WebEnv = ids_parser()
fasta_printer(QueryKey, WebEnv)