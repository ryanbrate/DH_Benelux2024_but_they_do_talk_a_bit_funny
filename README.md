# Source Code for ... DHBenelux 2024 submission: but they do talk a bit funny, don't they?

## Bayesian estimation

Refer to jupyter notebook, for the analysis conducted in the paper: (bayesian\_estimation.ipynb)[bayesian_estimation.ipynb]

Note: this jupyter notebook relies on data files:
* (American Literature Fiction Corpus)[extract_project_gutenberg_quotes/quotes_en_PS_fiction_020524.csv] -- this file, when built, is approx 715.7MB of data, hence is not included. To build this file, follow the steps in the next section;
* (news quotes)[quotes_news.txt];

## Building the American Literature Fiction Corpus

* the book urls comprising the American Literature Fiction corpus can be found here: (book urls)[PG_sample/book_urls.csv]; run the (jupyter notebook)[PG_sample/main.ipynb], starting from the import of the book urls, to wget the corpus to the location of choosing;

* run (main.py)[extract_project_gutenberg_quotes/main.py] to extract quotes from corpus of downloaded books. Note: need to change the hardcoded path to dir of American Literature Fiction dir;
