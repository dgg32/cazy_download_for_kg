from pyphy import pyphy
import sys
import json

cazy_download = sys.argv[1]

cache = {}

desired_ranks = ["superkingdom", "phylum", "class", "order", "family", "genus", "species"]

genome_cazy = {}

for line in open(cazy_download):
    line = line.strip()
    fields = line.split("\t")
    cazy = fields[0]
    name = fields[2].split("type strain:")[0].strip()
    #print (name)
    taxid = 0
    taxonomy_container = {}

    if name in cache:
        taxonomy_container = cache[name]
        #taxid = container["taxid"]
    else:
        taxid = pyphy.getTaxidByName(name)[0]
        taxonomy_container = {"taxonomy": {}}
        if str(taxid) != "-1":
            taxonomy_container["taxonomy"]["taxid"] = taxid
            current_id = int(taxid)
            while current_id != 1 and current_id != -1:
                current_id = int(pyphy.getParentByTaxid(current_id))
                if pyphy.getRankByTaxid(current_id) in desired_ranks:
                    taxonomy_container["taxonomy"][pyphy.getRankByTaxid(current_id)] = [pyphy.getNameByTaxid(current_id), current_id]

        cache[name] = taxonomy_container

    if name not in genome_cazy:
        genome_cazy[name] = {"name": name, "cazy": {}, "taxonomy": taxonomy_container}
    
    if cazy not in genome_cazy[name]["cazy"]:
        genome_cazy[name]["cazy"][cazy] = 0
    genome_cazy[name]["cazy"][cazy] += 1

#print (pyphy.getTaxidByName('Bacteroidetes'))

for name in genome_cazy:
    print (json.dumps(genome_cazy[name]))