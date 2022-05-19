import sys

mesh_indent_file = sys.argv[1]
sugar_file = sys.argv[2]

def tab_level(astr):
    """Count number of leading tabs in a string
    """
    return len(astr)- len(astr.lstrip(' '))

sugar_set = set()
is_header = False
for line in open(sugar_file, 'r'):
    if is_header == False:
        is_header = True
    else:
        sugar_set.add(line.strip())

indent_space = 4
indent_text = {}

relation = "from\tto\n"

n = 0
for i, line in enumerate(open(mesh_indent_file, 'r')):
    if line.strip() != "":
        line = line.lower()
        indent = tab_level(line)
        indent_text[indent] = line.strip()
        sugar_set.add(line.strip())

        if n == 1:
            indent_space = indent
        #print (indent, line)
        if indent != 0:
            relation += f'{line.strip()}\t{indent_text[indent-indent_space]}' + "\n"
        n += 1

with open("./data_for_neo4j_bacteroidetes/polysaccharide_is_a.tsv", 'w') as f:
    f.write(relation)

with open(sugar_file, 'w') as f:
    f.write("substrate\n" + "\n".join(list(sugar_set)))