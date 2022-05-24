

# Introduction
  

This repository contains code and data for my article "[Construct a Knowledge Graph on the Neo4j Cloud](https://medium.com/p/f8094e7bdbec)".

1. The scripts are for data processing.

  

2. The raw data folder contains the raw data.

3. The data_for_neo4j_bacteroidetes folder contains the data that are ready for import into Auradb.

  

# Prerequisite

Neo4j Desktop
  

# Run

The data folder contain data from 2022. If you want to download the newest data, do these:
  
1. Download the data from the DOWNLOAD CAZY button in the Cazy website

2. Run the download_cazy_info.py to download the individual cazy family descriptions
```console
python download_cazy_info.py > cazy_info.json
```
3. Download the [polysaccharide ontology from NCBI](https://www.ncbi.nlm.nih.gov/mesh/68011134). Only copy the section below "Polysaccharides".


# Processing

Run the three ipynb one by one in the following order: 1_format_the_data.ipynb, 2_inter_cazy_relation.ipynb and 3_post_process.ipynb. The 2_inter_cazy_relation.ipynb takes some manual curations to ensure the quality of text extractions. These processing notebooks will generate the files in data_for_neo4j_bacteroidetes for your import.
  

## Authors

  

*  **Sixing Huang** - *Concept and Coding*

  

## License

  

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
