import os
from tools import get_metadata, get_book


meta = get_metadata('Free+English+textbooks 2.xlsx')

with open('params.txt') as file:
    lines = file.read().strip().split('\n')
    params = {i[0]: i[1].strip().lower() for i in [j.split(':') for j in lines]}

if params['destination_folder'][-1] != '/':
    params['destination_folder'] += '/'

if params['subject_clasification'] == 'true':
    meta['path'] = meta.apply(lambda row:
    params['destination_folder'] + row['subject'] + '/', axis=1)
else:
    meta['path'] = params['destination_folder']

for index, row in meta.iterrows():
    title = row['title']
    if not os.path.exists(row['path']):
        os.mkdir(row['path'])

    file_path = row['path'] + row['title'] + '.pdf'
    if not os.path.exists(file_path):
        with open(row['path'] + row['title'] + '.pdf', 'wb') as file:
            try:
                book = get_book(row['pdf_url'])
                file.write(book)
            except:
                print(f'Error descargando {title}.pdf')
                if os.path.exists(file_path):
                    os.remove(file_path)

    if row['epub_url']:
        file_path = row['path'] + row['title'] + '.epub'
        if not os.path.exists(file_path):
            with open(row['path'] + row['title'] + '.epub', 'wb') as file:
                try:
                    book = get_book(row['epub_url'])
                    file.write(book)
                except:
                    print(f'Error descargando {title}.epub')
                    if os.path.exists(file_path):
                        os.remove(file_path)
