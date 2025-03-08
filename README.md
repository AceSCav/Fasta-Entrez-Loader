# Fasta-Entrez-Loader
This Python script automates the search and retrieval of biological sequences from the NCBI Entrez database using the eSearch and eFetch services.

Requirements

	Note: This script may not work properly on Windows due to the use of wget. It is recommended to run it on a Linux system for the best experience.
	Python 3.x
	Internet connection
	wget installed on the system

Warnings

	This script only accepts precise inputs. Incorrect database names, incorrect organism names, or running the script with arguments that do not follow the provided 	examples may cause execution failures or return unexpected outputs.

Installation

	Clone this repository:
		git clone https://github.com/AceSCav/Fasta-Entrez-Loader
		cd your-repository
	Ensure wget is installed:
		sudo apt install wget

Usage
	Run the script with the following arguments:
		
  	python Script.py "database" "organism" x
	
	database: Name of the NCBI database (nucleotide, protein)
	organism: Name of the target organism (Homo sapiens)
	x: Maximum number of sequences to display

Example Execution:
	
 	python Script.py "nucleotide" "Homo sapiens" 10

License
	This project is licensed under the GNU General Public License Version 3, 29 June 2007. You are free to use, modify, and distribute it under the terms of this license.
	This project is licensed under the MIT License. Feel free to modify and distribute it.
