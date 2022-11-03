import glob

def file_changer(filename):
    data_to_put = ''
    with open(filename, 'r+') as fasta_file:
        for line in fasta_file.readlines():
            line = line.rstrip()
            if '"ID_Frame":174,' in line:
                line = line.split('[')[-1]
                data_to_put += '>' + str(line[:-1]) + "\n"
            else:
                data_to_put += str(line) + "\n"
        fasta_file.write(data_to_put) 
        fasta_file.close()


for file in glob.glob('*.json'):
    file_changer(file)


with open("file.txt", "r") as in_file:
    buf = in_file.readlines()

with open("file.txt", "w") as out_file:
    for line in buf:
        if line == "; Include this text\n":
            line = line + "Include below\n"
        out_file.write(line)