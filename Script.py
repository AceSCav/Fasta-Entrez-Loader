import sys
import subprocess
import os
import xml.etree.ElementTree as ET

current_path = os.getcwd()
database = sys.argv[1]
organism = sys.argv[2]
x = sys.argv[3]
def validade_input():
    """
    Validates the input arguments.
    
    Checks if the script is executed with the correct number of arguments.
    If not, it prints the correct usage format and exits the program.
    """
    if len(sys.argv) != 4:
        print("Usage: Script.py 'database' 'organism' x")
        print("x is the maximum number of sequences displayed")
        sys.exit(1)

def ids_getter():
    """
    Retrieves sequence IDs from the NCBI Entrez database.
    
    Uses the eSearch API to search for sequences based on the specified database and organism.
    The retrieved IDs are stored in an XML file named 'Ids.xml'.
    """
    search = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi\?db\="{database}"\&term\="{organism}"\&usehistory\=y\&retmax\={x}'
    url_maker = f'wget {search} -O Ids.xml'
    subprocess.run(url_maker, shell=True)

def ids_parser():
    """
    Parses the retrieved XML file to extract QueryKey and WebEnv values.
    Returns:
        QueryKey and WebEnv as strings.
    """
    with open(current_path + '/Ids.xml', 'r') as xml_file:
        ids = xml_file.read()
    root = ET.fromstring(ids)   
    QueryKey = None 
    WebEnv = None
    if root.find('QueryKey') is not None:
        QueryKey = root.find('QueryKey').text 
    if root.find('WebEnv') is not None:
        WebEnv = root.find('WebEnv').text 
    return QueryKey, WebEnv

def fasta_printer(QueryKey, WebEnv):
    """
    Retrieves and prints FASTA sequences from the NCBI Entrez database.
    
    Uses the eFetch API to download the sequences in FASTA format using the QueryKey and WebEnv.
    The retrieved sequences are stored in a file named 'sequences.fasta' and printed to the console.
    """
    fetch = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi\?db\="{database}"\&usehistory\=y\&query_key\={QueryKey}\&WebEnv\={WebEnv}\&rettype\=fasta\&retmax\={x}'
    url_maker = f'wget {fetch} -O sequences.fasta'
    printer = f'cat sequences.fasta'
    subprocess.run(url_maker, shell=True)
    subprocess.run(printer, shell=True)

def main():
    """
    Main function to execute the workflow.
    
    Calls functions in sequence to retrieve sequence IDs, parse them,
    fetch the corresponding FASTA sequences, and print them.
    """
    ids_getter()
    QueryKey, WebEnv = ids_parser()
    fasta_printer(QueryKey, WebEnv)

main()