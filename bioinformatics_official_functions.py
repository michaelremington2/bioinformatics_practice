class bioinformatics_exploratory_analysis:
    def __init__(self,dna_sequence):
        self.dna_sequence = dna_sequence
        self.a_count = 0 
        self.t_count = 0
        self.g_count = 0
        self.c_count = 0
        self.dna_nucleotide_count = self.nucleotide_count()
        self.gc_content = self.gc_content_calc() 
        self.acceptable_dna_nucloetides = ['A','T','C','G']
        self.rna_sequence = self.dna_to_rna()

    def individual_nucleotide_display(self):
        '''Sample sequence is a list of nucleotides'''
        for i in range(0,len(self.dna_sequence)):
            if self.dna_sequence[i] not in self.acceptable_dna_nucloetides:
                print('Error, fix  '+ self.dna_sequence[i] + ' at position ' + str(i))
                break
            else:
                print(self.dna_sequence[i] + ' ' + str(i))

    def dna_sequence_check(self):
        '''Function that checks if a inserted sequence is acceptable to work with. '''
        self.error_list = []
        for i in range(0,len(self.dna_sequence)):
            if self.dna_sequence[i] not in self.acceptable_dna_nucloetides:
                self.error_list.append('Nucleotide Error, fix  '+ self.dna_sequence[i] + ' at position ' + str(i))
            elif self.dna_sequence[i].islower == False:
                self.error_list.append('Case Error ' + self.dna_sequence[i] + ' ' + str(i))
        if len(self.error_list) == 0:
            print('Good Sequence')
        else:
            print(self.error_list)

    def nucleotide_count(self):
        ''' Counts DNA nucleotides and stores them as attributes'''
        for i in range(0,len(self.dna_sequence)):
            if self.dna_sequence[i] == 'A':
                self.a_count += 1
            elif self.dna_sequence[i] == 'T':
                self.t_count += 1
            elif self.dna_sequence[i] == 'G':
                self.g_count += 1
            elif self.dna_sequence[i] == 'C':
                self.c_count += 1
            else:
                print('error')
                break

    def gc_content_calc(self, decimals = 4):
        '''Calculates the GC content ratio. this ratio is the sum of guanines and cytosines over the total count of nucleotides.'''
        return round(((self.g_count+self.c_count)/sum([self.g_count,self.c_count,self.a_count,self.t_count])) * 100, decimals)

    def dna_to_rna(self):
      '''Returns the complementaRY rna sequence of a dna sequence.'''
        return self.dna_sequence.replace("T", "U")
