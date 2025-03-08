import sys
import subprocess
import os
import xml.etree.ElementTree as ET

if len(sys.argv) != 3:
    print("Usage: Script.py 'database' 'organism'")
    sys.exit(1)
current_path = os.getcwd()
database = sys.argv[1]
organism = sys.argv[2]

def ids_getter():
    search = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi\?db\="{database}"\&term\="{organism}"\&usehistory\=y\&retmax\=10000'
    url_maker = f'wget {search} -O Ids.xml'
    subprocess.run(url_maker, shell=True)

def ids_parser():
    with open(current_path + '/Ids.xml', 'r') as xml_file:
        ids = xml_file.read()
    root = ET.fromstring(ids)    
    QueryKey = root.find('QueryKey').text if root.find('QueryKey') is not None else None
    WebEnv = root.find('WebEnv').text if root.find('WebEnv') is not None else None
    print(QueryKey, WebEnv)
    return QueryKey, WebEnv

def fasta_printer(QueryKey, WebEnv):
    fetch = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi\?db\="{database}"\&usehistory\=y\&query_key\={QueryKey}\&WebEnv\={WebEnv}\&rettype\=fasta'
    url_maker = f'wget {fetch} -O sequences.fasta'
    printer = f'cat sequences.fasta'
    subprocess.run(url_maker, shell=True)
    subprocess.run(printer, shell=True)

ids_getter()
QueryKey, WebEnv = ids_parser()
fasta_printer(QueryKey, WebEnv)