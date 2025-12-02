"""Moldule that groups classes to transform DAT and CSV data into Tabular TXT file and plot the data into curves"""

import os

class DataFolderProcess:
    """Collect all files DAT or CSV to analyse and treat into tabular save as TXT file"""
    def __init__(self, folder):
        """Instance initialisation with the folder to read"""
        self.folder = folder
        self.data_files = []
        for file in os.listdir(self.folder):
            # Collect all CSV/DAT files excluding README.md
            if file.endswith(('.csv', '.dat')) and file != 'README.md':
                self.data_files.append(file)
        if self.data_files:
            print(f"Files to process : {', '.join(self.data_files)}.")  
        if not self.data_files:
            print('None CSV/DAT file found')
        
class ConvertData(DataFolderProcess):
    """Convert CSV/DAT files into a tabular TXT file with tab separator"""
    def __init__(self, folder):
        """Initialisation with folder and filename to change"""
        super().__init__(folder)

    def detect_separator(self, line):
        """Detect which separator is used in a line"""
        for sep in [',', ';', '"', '|']:
            if sep in line:
                return sep
        return ',' # default if None found
    
    def to_txt(self):
        """Convert all CSV/DAT files into TXT files with tabulation"""
        # suppress the last 4 characters and replace by .txt
        files_to_convert = self.data_files.copy()
        converted_files = []

        while files_to_convert:
            file = files_to_convert.pop(0)
            txt_file = file[:-4] + '.txt'
            
            with open(file) as f:
                header = f.readline()
                # Detect separator
                sep = self.detect_separator(header)

                # Split header avec le bon séparateur
                header_col = header.split(sep)
                
                # Clean column name
                for i in range(len(header_col)):
                    header_col[i] = header_col[i].rstrip().lower()
                
                f.seek(0) # return at the beginning
                lines = f.readlines()  

            new_lines = []
            for line in lines:
                line = line.rstrip()
                elements = line.split(sep)
    
                new_lines.append('\t'.join(elements) + '\n') # tabulation

            with open(txt_file, 'w') as out:
                out.writelines(new_lines)

            converted_files.append(txt_file)
        print(f"Files converted to tabular TXT : {', '.join(converted_files)} ")
        return converted_files
