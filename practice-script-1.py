sample_sequence1 = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
#sample_sequence = sample_sequence1.upper()
sample_sequence = list(sample_sequence1)
acceptable_nucloetides = ['A','T','C','G']
As = 0 
Ts = 0 
Gs = 0 
Cs = 0 
def individual_nucleotide_display(sample_sequence):
    '''Sample sequence is a list of nucleotides'''
    acceptable_nucloetides = ['A','T','C','G']
    for i in range(0,len(sample_sequence)):
        if sample_sequence[i] not in acceptable_nucloetides:
            print('Error, fix  '+ sample_sequence[i] + ' at position ' + str(i))
            break
        else:
            print(sample_sequence[i] + ' ' + str(i))

def dna_sequence_check(sample_sequence):
    acceptable_nucloetides = ['A','T','C','G']
    error_list = []
    for i in range(0,len(sample_sequence)):
        if sample_sequence[i] not in acceptable_nucloetides:
            error_list.append('Nucleotide Error, fix  '+ sample_sequence[i] + ' at position ' + str(i))
        elif sample_sequence[i].islower == False:
            error_list.append('Case Error ' + sample_sequence[i] + ' ' + str(i))
    if len(error_list) == 0:
        print('Good Sequence')
    else:
        print(error_list)


dna_sequence_check(sample_sequence)
#print(type(sample_sequence) == list)
#print(type(sample_sequence1))