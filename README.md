# springer_downloader

## Usage

You can download the books on a variety of configurations, which can be selected
in the *params.txt* file. Note that the parameters are case-sensiteve,
write booleans as shown in the file and subjects exactly how they are shown in
the excel file provided by Springer. Do not write line jumps inside one
parameter.

- destination_folder

  Here you must write the full path to the folder were you want to save the books.

- subject_classify

  You can download all the books directly into the destination folder, or you
  can have them classified by subject into subfolders. Write True to classify
  them, False otherwise.

- download_epubs

  Most of the books are available in .epub format as well as in .pdf, write True
  if you want to download in both formats or False if you just want the pdfs.

- filter_subjects

  There is a good chance that you won't be interested in every available
  subject, write True if you want to manually select the subjects to be
  downloaded or False if you want them all.

- subjects

  Only relevant if you chose True in the previous parameter.
  Here you must write all the subjects to be downloaded separated by comas.
  Do not make a line jump if you reached the border of the .txt editor, just
  keep writing. The subjects are considered as the first category mentioned in
  the 'Subject Classification' column of the excel file for each book. The
  subjects are case-sensitive. A list of the subjects is provided at the end of
  this readme.

- chunks

  Downloading the books can take several hours depending on the quality of your
  internet connection. If you can't afford to have your computer downloading for
  an undetermined amount of hours, you can download the books in smaller chunks.
  If you want to do so, write True, False otherwise.

- chunk

  Only relevant if you chose True in the previous parameter. There are 407 books
  available, here you must write the range of the chunk that you want to
  download as initial-final. The range will be interpreted as in python style,
  so the first book is listed as zero.


## Dependencies

The program Pandas, NumPy and tqdm libraries, so make sure to have them
installed. tqdm's version must be higher than 4.8. Then you are ready to pull
clone the repository and run it.


## Subjects
- Engineering
- Social Sciences
- Mathematics
- Psychology
- Biomedicine
- Life Sciences
- Materials Science
- Chemistry
- Medicine & Public Health
- Business and Management
- Criminology and Criminal Justice
- Computer Science
- Statistics
- Geography
- Physics
- Energy
- Philosophy
- Economics
- Earth Sciences
- Popular Science
- Education
- Environment
- Law
- Cultural and Media Studies
- Literature
