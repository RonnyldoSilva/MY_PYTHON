import csv

def add_flag_csv(csv_file):
    with open(csv_file,'r') as read_obj:
        reader = csv.reader(read_obj, delimiter=';')
        writer = csv.writer(open(csv_file + '_flag.csv','w'), delimiter=';')
        
        for row in reader:
            if row[3] == 'protestos':
                row.append('tem_protesto')
            elif row[3] == '0':
                row.append('0')
            else:
                row.append('1')
            
            writer.writerow(row)

add_flag_csv('data/pontos_nas_dimensoes_porte_uf_idade.csv')