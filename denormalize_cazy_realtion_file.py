import sys
import pandas as pd
import os

input_file = sys.argv[1]
output_folder = sys.argv[2]

df = pd.read_csv(input_file, sep='\t')

df["doi"] = "CAZy"

df["primary"] = 1

subfiles = df.action.unique()

for s in subfiles:
    #print (df[df.action == s])
    
    newfile = os.path.join(output_folder, s + ".tsv")

    df[df.action == s].to_csv(newfile, sep="\t", index=False) 