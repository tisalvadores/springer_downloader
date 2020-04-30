import os
import pandas as pd
import numpy as np
from tqdm import tqdm
from tools import get_metadata, get_book, parse_params, apply_params

if os.path.exists('./meta_cache.csv'):
    meta = pd.read_csv('meta_cache.csv')
    meta.replace({np.nan: None}, inplace=True)
else:
    meta = get_metadata('Free+English+textbooks 2.xlsx')
    meta.to_csv('meta_cache.csv', header=True)

with open('params.txt') as file:
    params = file.read().strip().split('\n')

params = parse_params(params)
meta = apply_params(meta, params)
print('Downloading books...')
loop = tqdm(total=meta.shape[0])

for index, row in meta.iterrows():
    title = row['title']
    if not os.path.exists(row['path']):
        os.mkdir(row['path'])

    file_path = row['path'] + row['title'] + '.pdf'
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as file:
            try:
                book = get_book(row['pdf_url'])
                file.write(book)
            except:
                print(f'Error descargando {title}.pdf')
                if os.path.exists(file_path):
                    os.remove(file_path)

    if row['epub_url'] and params['download_ePubs']:
        file_path = row['path'] + row['title'] + '.epub'
        if not os.path.exists(file_path):
            with open(file_path, 'wb') as file:
                try:
                    book = get_book(row['epub_url'])
                    file.write(book)
                except:
                    print(f'Error descargando {title}.epub')
                    if os.path.exists(file_path):
                        os.remove(file_path)
    loop.update(1)
