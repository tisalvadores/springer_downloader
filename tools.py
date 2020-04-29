import time
import requests
import pandas as pd

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
    df = pd.read_excel(metadata_file)
    df = df[['Book Title', 'DOI URL', 'Subject Classification']]
    df.columns = ['title', 'pdf_url', 'subject']

    df['subject'] = df['subject'].apply(lambda subs: subs.split('; ')[0])
    url = df['pdf_url']
    df['pdf_url'] = url.apply(lambda url: pdf_url(url))
    df['epub_url'] = url.apply(lambda url: epub_url(url))
    return df


if __name__ == '__main__':
    begin = time.time()
    meta = get_metadata('Free+English+textbooks.xlsx')
    print(time.time()-begin)
#    print(meta['subject'].drop_duplicates())
    print(','.join(list(meta['subject'].drop_duplicates())))
    print(time.time()-begin)
#print(meta['epub_url'].isnull())
#print(meta[~meta['epub_url'].isnull()]['epub_url'])
#print(meta['epub_url'][0]!=None)
#with open('/Volumes/HDD/Carpetas/Springer Books/hello.epub','wb') as file:
#    book = get_book(meta['epub_url'][0])
#print([bool(i) for i in meta['epub_url']])

#for index, row in meta.iterrows():
#    print(row['pdf_url'])
