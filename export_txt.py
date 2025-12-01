"""Moldule that groups classes to traform DAT and CSV data into Tabular TXT file and plot the data into curves"""

class Data:
    """Represent the data save in DAT or CSV to analyse and treat into tabular save as TXT file"""
    def __init__(self, filename):
        """Instance initialisation with data into a file"""
        self.filename = filename

        #Transforme CSV/DAT file into  TXT file
        if filename.endswith ('.csv') or filename.endswith('.dat'):
            #suppress the last 4 characters
            self.new_file = filename[:-4] + '.txt'
            #if it doesn't end with .csv or .dat
        else: self.new_file = filename + '.txt'
        
    def detect_separator(line):
        """Detection of separator type"""
        for sep in [',', ';', '"','|']:
            if sep in line:
                return sep
        return ',' #default if None found

    def to_txt(self):
        """Convert the CSV/DAT file into a space-separated TXT file"""
        with open(self.filename) as data_object:
            
            first_line = data_object.readline() #read the first line
            sep = self.detect_separator(first_line) #auto-detect separator
            data_object.seek(0) #retunr at the begining

            lines = data_object.readlines()  # stock each line in a list
            new_lines = []
            for line in lines:
                #remove space between each new line
                line = line.rstrip()
                #split lines into column by coma       
                elements = line.split(sep)
                #join column with space
                new_lines.append('\t'.join(elements)+ '\n') #tabulation

        with open(self.new_file, 'w') as file_out:
           
            file_out.writelines(new_lines)

class LinePlot:
    """"""        





            

    