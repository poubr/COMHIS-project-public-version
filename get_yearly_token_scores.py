import csv
import requests
from requests.auth import HTTPBasicAuth


#sorting the data:
def sort_yearly_scores():
    

    with open('FULL_yearly_score_all_eds_unsorted.csv', 'r', encoding='utf-8') as all_works:
        with open('FULL_yearly_score_all_eds.csv', 'w', encoding='utf-8', newline = '') as all_sorted:
            reader = csv.reader(all_works)
            writer = csv.writer(all_sorted)
            writer.writerow(['publication_year', 'public_score', 'publik_score', 'publick_score', 'catholic_score', 'catholik_score', 'catholick_score'])
            aux_list = sorted(reader, key=lambda x: x[0])
            for i in aux_list:
                row = i[0],i[1],i[2],i[3],i[4],i[5],i[6]
                writer.writerow(row)

    with open('FULL_yearly_score_unique_eds_unsorted.csv', 'r', encoding='utf-8') as unique:
        with open('FULL_yearly_score_unique_eds.csv', 'w', encoding='utf-8', newline = '') as unique_sorted:
            reader = csv.reader(unique)
            writer = csv.writer(unique_sorted)
            writer.writerow(['publication_year', 'public_score', 'publik_score', 'publick_score', 'catholic_score', 'catholik_score', 'catholick_score'])
            aux_list = sorted(reader, key=lambda x: x[0])
            for i in aux_list:
                row = i[0],i[1],i[2],i[3],i[4],i[5],i[6]
                writer.writerow(row)            

# getting yearly aggreggates; at this stage it is saved by appearance, not chronologically
def yearly_difference_unsorted():

    with open('FULL_list_of_works_freq.csv', 'r', encoding='utf-8') as all_works:
        with open('FULL_yearly_score_all_eds_unsorted.csv', 'w', encoding='utf-8', newline = '') as yearly_all:
            reader = csv.DictReader(all_works, delimiter = ',')
            writer = csv.writer(yearly_all, delimiter = ',')
           
            yearly_aggreggate = {}
            for row in reader:
                if len(row['publication_year']) ==6:
                    year = row['publication_year'][0:4]
                    if year not in yearly_aggreggate: 
                        yearly_aggreggate[year] = [row['public_score'], row['publik_score'], row['publick_score'], row['catholic_score'], row['catholik_score'], row['catholick_score']]
                        
                    else:
                        aux_key = year
                        new_public = int(yearly_aggreggate[aux_key][0]) + int(row['public_score'])
                        new_publik = int(yearly_aggreggate[aux_key][1]) + int(row['publik_score'])
                        new_publick = int(yearly_aggreggate[aux_key][2]) + int(row['publick_score'])
                        new_catholic = int(yearly_aggreggate[aux_key][3]) + int(row['catholic_score'])
                        new_catholik = int(yearly_aggreggate[aux_key][4]) + int(row['catholik_score'])
                        new_catholick = int(yearly_aggreggate[aux_key][5]) + int(row['catholick_score'])

                        yearly_aggreggate[year] = [new_public, new_publik, new_publick, new_catholic, new_catholik, new_catholick]

                else:
                    year = 'uknown'        
                    if year not in yearly_aggreggate: 
                        yearly_aggreggate[year] = [row['public_score'], row['publik_score'], row['publick_score'], row['catholic_score'], row['catholik_score'], row['catholick_score']]
                    else:
                        aux_key = year
                        new_public = int(yearly_aggreggate[aux_key][0]) + int(row['public_score'])
                        new_publik = int(yearly_aggreggate[aux_key][1]) + int(row['publik_score'])
                        new_publick = int(yearly_aggreggate[aux_key][2]) + int(row['publick_score'])
                        new_catholic = int(yearly_aggreggate[aux_key][3]) + int(row['catholic_score'])
                        new_catholik = int(yearly_aggreggate[aux_key][4]) + int(row['catholik_score'])
                        new_catholick = int(yearly_aggreggate[aux_key][5]) + int(row['catholick_score'])

                        yearly_aggreggate[year] = [new_public, new_publik, new_publick, new_catholic, new_catholik, new_catholick]
                
            for key, value in yearly_aggreggate.items():
                row = key, value[0], value[1], value[2], value[3], value[4], value[5]
                writer.writerow(row)
    
    with open('FULL_unique_works_freq.csv', 'r', encoding='utf-8') as unique:
        with open('FULL_yearly_score_unique_eds_unsorted.csv', 'w', encoding='utf-8', newline = '') as yearly_unique:
            reader = csv.DictReader(unique, delimiter = ',')
            writer = csv.writer(yearly_unique, delimiter = ',')
           
            yearly_aggreggate = {}
            for row in reader:
                if len(row['publication_year']) ==6:
                    year = row['publication_year'][0:4]
                    if year not in yearly_aggreggate: 
                        yearly_aggreggate[year] = [row['public_score'], row['publik_score'], row['publick_score'], row['catholic_score'], row['catholik_score'], row['catholick_score']]
                        
                    else:
                        aux_key = year
                        new_public = int(yearly_aggreggate[aux_key][0]) + int(row['public_score'])
                        new_publik = int(yearly_aggreggate[aux_key][1]) + int(row['publik_score'])
                        new_publick = int(yearly_aggreggate[aux_key][2]) + int(row['publick_score'])
                        new_catholic = int(yearly_aggreggate[aux_key][3]) + int(row['catholic_score'])
                        new_catholik = int(yearly_aggreggate[aux_key][4]) + int(row['catholik_score'])
                        new_catholick = int(yearly_aggreggate[aux_key][5]) + int(row['catholick_score'])

                        yearly_aggreggate[year] = [new_public, new_publik, new_publick, new_catholic, new_catholik, new_catholick]

                else:
                    year = 'uknown'        
                    if year not in yearly_aggreggate: 
                        yearly_aggreggate[year] = [row['public_score'], row['publik_score'], row['publick_score'], row['catholic_score'], row['catholik_score'], row['catholick_score']]
                    else:
                        aux_key = year
                        new_public = int(yearly_aggreggate[aux_key][0]) + int(row['public_score'])
                        new_publik = int(yearly_aggreggate[aux_key][1]) + int(row['publik_score'])
                        new_publick = int(yearly_aggreggate[aux_key][2]) + int(row['publick_score'])
                        new_catholic = int(yearly_aggreggate[aux_key][3]) + int(row['catholic_score'])
                        new_catholik = int(yearly_aggreggate[aux_key][4]) + int(row['catholik_score'])
                        new_catholick = int(yearly_aggreggate[aux_key][5]) + int(row['catholick_score'])

                        yearly_aggreggate[year] = [new_public, new_publik, new_publick, new_catholic, new_catholik, new_catholick]

            for key, value in yearly_aggreggate.items():
                row = key, value[0], value[1], value[2], value[3], value[4], value[5]
                writer.writerow(row)

# splitting the list into two docs; one with all the works, another with unique frequencies
def split_works():

    with open('FULL_list_of_works_freq.csv', 'r', encoding='utf-8') as list_of_works:
        with open('FULL_unique_works_freq.csv', 'w', encoding='utf-8', newline = '') as unique_editions_freq:
            reader = csv.DictReader(list_of_works, delimiter = ',')
            writer = csv.writer(unique_editions_freq, delimiter = ',')
            writer.writerow(['id', 'title', 'remaining_title', 'publication_year', 'finalWorkField', 'public_score', 'publik_score', 'publick_score', 'catholic_score', 'catholik_score', 'catholick_score'])
            aux_workfield = []
            for line in reader:
                if line['finalWorkField'] not in aux_workfield:
                    aux_workfield.append(line['finalWorkField'])
                    line = line['id'], line['title'], line['remaining_title'], line['publication_year'], line['finalWorkField'], line['public_score'], line['publik_score'], line['publick_score'], line['catholic_score'], line['catholik_score'], line['catholick_score']
                    writer.writerow(line)

           
# fetching the frequencies
def get_frequencies():
    
    public = (get_matches('https://vm0824.kaj.pouta.csc.fi/octavo/ecco/search?query=%3CDOCUMENT%C2%A7public%C2%A7DOCUMENT%3E&pretty&limit=-1&field=documentID&field=ESTCID&field=publication_year&field=title&field=author'))
    publik = (get_matches('https://vm0824.kaj.pouta.csc.fi/octavo/ecco/search?query=%3CDOCUMENT%C2%A7publik%C2%A7DOCUMENT%3E&pretty&limit=-1&field=documentID&field=ESTCID&field=publication_year&field=title&field=author'))
    publick = (get_matches('https://vm0824.kaj.pouta.csc.fi/octavo/ecco/search?query=%3CDOCUMENT%C2%A7publick%C2%A7DOCUMENT%3E&pretty&limit=-1&field=documentID&field=ESTCID&field=publication_year&field=title&field=author'))
    catholic = (get_matches('https://vm0824.kaj.pouta.csc.fi/octavo/ecco/search?query=%3CDOCUMENT%C2%A7catholic%C2%A7DOCUMENT%3E&pretty&limit=-1&field=documentID&field=ESTCID&field=publication_year&field=title&field=author'))
    catholik = (get_matches('https://vm0824.kaj.pouta.csc.fi/octavo/ecco/search?query=%3CDOCUMENT%C2%A7catholik%C2%A7DOCUMENT%3E&pretty&limit=-1&field=documentID&field=ESTCID&field=publication_year&field=title&field=author'))
    catholick = (get_matches('https://vm0824.kaj.pouta.csc.fi/octavo/ecco/search?query=%3CDOCUMENT%C2%A7catholick%C2%A7DOCUMENT%3E&pretty&limit=-1&field=documentID&field=ESTCID&field=publication_year&field=title&field=author'))

    with open('FULL_list_of_works.csv', 'r', encoding='utf-8') as list_of_works:
        with open('FULL_list_of_works_freq.csv', 'w', encoding='utf-8', newline = '') as list_of_works_freq:
            reader = csv.DictReader(list_of_works, delimiter = ',')
            writer = csv.writer(list_of_works_freq, delimiter = ',')
            
            writer.writerow(['id', 'title', 'remaining_title', 'publication_year', 'finalWorkField', 'public_score', 'publik_score', 'publick_score', 'catholic_score', 'catholik_score', 'catholick_score'])

            for row in reader:
                public_score = 0
                publik_score = 0
                publick_score = 0
                catholic_score = 0
                catholik_score = 0
                catholick_score = 0

                if row['id'] in public:
                    public_score = public[row['id']]
                    
                if row['id'] in publik:
                    publik_score = publik[row['id']]

                if row['id'] in publick:
                    publick_score = publick[row['id']]    
               
                if row['id'] in catholic:
                    catholic_score = catholic[row['id']]

                if row['id'] in catholik:
                    catholik_score = catholik[row['id']]

                if row['id'] in catholick:
                    catholick_score = catholick[row['id']]    
              
                
                new_row = row['id'], row['title'], row['remaining_title'], row['publication_year'], row['finalWorkField'], public_score, publik_score, publick_score, catholic_score, catholik_score, catholick_score
                writer.writerow(new_row)   
            
#getting matches (see previous function)
def get_matches(url: str):

    data = requests.get(url, auth = HTTPBasicAuth('REDACTED', 'REDACTED')).json()
    lista = data['results']['docs']
    matched = {}
    

    works = 'FULL_list_of_works.csv'
    with open(works, 'r', encoding='utf-8') as list_of_works:
        reader = csv.DictReader(list_of_works, delimiter = ',')  

        for row in reader:
            for item in lista:
                if row['id'] == item['ESTCID']:
                    key = item['ESTCID']
                    matched[key] = int(item['score'])
  
    return matched



# getting a clean list of works from estc_student_edition:
def get_list_of_works():
    with open('estc_student_edition.csv', 'r', encoding='utf-8') as estc_student_edition:
        with open('FULL_list_of_works.csv', 'w', encoding='utf-8', newline = '') as list_of_works:
            reader = csv.DictReader(estc_student_edition, delimiter = ',')
            writer = csv.writer(list_of_works, delimiter = ',')
            writer.writerow(['id', 'title', 'remaining_title', 'publication_year', 'finalWorkField'])
            aux_workfield = []
            aux_id = []
            for line in reader:
                if line['finalWorkField'] not in aux_workfield:
                    aux_workfield.append(line['finalWorkField'])
                    if len(line['id']) != 7:
                        ecco_id = convert_id(line['id']) # converting ID to the ECCO format
                    else:
                        ecco_id = line['id']
                    aux_id.append(line['id'])
                    line = ecco_id,line['title'],line['remaining_title'],line['publication_year'],line['finalWorkField']
                    writer.writerow(line)
                else:
                    if line['id'] not in aux_id:
                        aux_id.append(line['id'])
                        if len(line['id']) != 7:
                            ecco_id = convert_id(line['id']) # converting ID to the ECCO format
                        else:
                            ecco_id = line['id']
                        line = ecco_id,line['title'],line['remaining_title'],line['publication_year'],line['finalWorkField']
                        writer.writerow(line)       

# converting ID:
def convert_id(id_nr: str):
    with open('idpairs_even_richer_ecco_eebo_estc.csv', 'r', encoding='utf-8') as idpairs:
        reader = csv.DictReader(idpairs, delimiter = ',')
        for line in reader:
            if line['estc_id_student_edition'] == id_nr:
                return line['estc_id']
            else:
                esct_id = id_nr
                letter = esct_id[0]
                zeroes = '0'*(7-len(esct_id))
                digits = esct_id[1:]
                ecco_id = f'{letter}{zeroes}{digits}'
                return ecco_id


if __name__ == "__main__":
    get_list_of_works()
    print('list done')
    get_frequencies()
    print('freq done')
    split_works()
    print('split done')
    yearly_difference_unsorted()
    print('yearly done')
    sort_yearly_scores()
    print('all done')
