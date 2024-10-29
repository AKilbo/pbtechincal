#Part 1
def calculate_gc_content(seq_list):
    # iterate through each sequence
    print ("------------------------------------")
    for seq in seq_list:
        seq_name = seq[0]
        seq_bases = seq[1]
        # capture number of g's and c's 
        gcount = seq_bases.count('G')
        ccount = seq_bases.count('C')
        # log total number of bases
        total_bases = len(seq_bases)
        # calc gc content with this formula GC content = ((g + c) / total) * 100 = 50%
        gc_content = ((gcount+ccount)/total_bases) * 100
        # round to 2 digits 
        gc_content= round(gc_content,2)

        print(seq_name + ": GC Content = " + str(gc_content) )

    print ("------------------------------------")
    

#Part 2
def longest_consecutive_a(seq_list):
    for seq in seq_list:
        seq_name = seq[0]
        seq_bases = seq[1]
        a_max = 0
        a_current = 0
        for base in seq_bases:
            if base == 'A':
                a_current += 1
                if a_current > a_max:
                    a_max = a_current
            else:
                a_current = 0
        print(seq_name + ": Longest consecutive A = " + str(a_max) )
    print ("------------------------------------")
   
def read_fasta(fasta_name):
    fastafile = open(fasta_name,'r')
    lines = fastafile.readlines()
    seq_list = []
    i = 0
    for line in lines:
        if i % 2 == 0:      
            seq_name = line.strip('>').strip('\n')
        if i % 2 == 1:
            sequence = line.strip('\n')
            seq_list.append([seq_name,sequence])

        i +=1
    return seq_list


if __name__ == "main":
    fasta_file = 'sequence.fasta'
    #read fasta
    seq_list = read_fasta(fasta_file)
    # gc content
    calculate_gc_content(seq_list)
    # longest consecutive a
    longest_consecutive_a(seq_list)
    

