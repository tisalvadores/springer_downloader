import time
import requests
import pandas as pd
from tqdm import tqdm

def get_book(url):
    r = requests.get(url)
    return r.content

def epub_exists(url):
    r = requests.head(url, allow_redirects=True)
    return r.status_code == 200

def pdf_url(url):
    isbn = url.split('/')[-1]
    new_url = f'http://link.springer.com/content/pdf/10.1007/{isbn}.pdf'
    return new_url

def epub_url(url):
    isbn = url.split('/')[-1]
    new_url = f'http://link.springer.com/download/epub/10.1007/{isbn}.epub'
    if epub_exists(new_url):
        return new_url
    return None

def get_metadata(metadata_file):
    print('''Generating metadata.
This should take a couple minutes and will only happen on the fist execution.''')
    df = pd.read_excel(metadata_file)
    df = df[['Book Title', 'DOI URL', 'Subject Classification']]
    df.columns = ['title', 'pdf_url', 'subject']

    df['title'] = df['title'].apply(lambda title: title.replace('/', '-'))
    df['subject'] = df['subject'].apply(lambda subs: subs.split('; ')[0])
    url = df['pdf_url']
    df['pdf_url'] = url.apply(lambda url: pdf_url(url))
    tqdm.pandas()
    df['epub_url'] = url.progress_apply(lambda url: epub_url(url))
    print("Done.\n")
    return df

def parse_params(params):
    params = {i[0]: i[1].strip() for i in [j.split(':') for j in params]}

    if params['destination_folder'][-1] != '/':
        params['destination_folder'] += '/'
    params['subject_classify'] = params['subject_classify'] == 'True'
    params['download_epubs'] = params['download_epubs'] == 'True'
    params['filter_subjects'] = params['filter_subjects'] == 'True'
    params['subjects'] = [i.strip() for i in params['subjects'].split(',')]
    params['chunks'] = params['chunks'] == 'True'
    params['chunk'] = [int(i) for i in params['chunk'].split('-')]

    return params

def apply_params(meta, params):
    if params['subject_classify']:
        meta['path'] = meta.apply(lambda row:
        params['destination_folder'] + row['subject'] + '/', axis=1)
    else:
        meta['path'] = params['destination_folder']

    if not params['download_epubs']:
        meta['epub_url'] = None

    if params['chunks']:
        first = params['chunk'][0]
        last = params['chunk'][1]
        meta.drop(meta[~meta.index.isin(list(range(first, last)))].index,
                    inplace=True)

    if params['filter_subjects']:
        meta.drop(meta[~meta['subject'].isin(params['subjects'])].index,
                    inplace=True)
    return meta
