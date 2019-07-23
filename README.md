[Workshop Slides](https://docs.google.com/presentation/d/1BQx3ZReDnjDdIJN4Kz1ygR5nz9YN453YfnQerO85pmo/edit#slide=id.g5dd4449d37_1_17)

Example of text classification(sentiment analysis) used for mental health. We use a Naïve Bayes classifier on data from Twitter to distinguish tweets with positive sentiment from tweets about anxiety and depression. CONTENT WARNING: some of the tweets might have disturbing content. Positive tweets are taken from the open-source Sentiment140 dataset and tweets about anxiety and depression are taken from the TWINT (Twitter Intelligence) scraping tool.

For this workshop, please create an Anaconda environment (Python 3) using the command `conda create -n[NAME] python=3.x`. Once you've done that, install the following packages using `pip`, a tool that manages your Python packages: `numpy`, `pandas`, `sklearn`. Access them from the command line using `pip install [PACKAGE NAME]`

The code covered in the workshop is in sentiment-analysis-demo.ipynb. If you're interested in how the data was collected and processed, take a look at `data-prep.py`.


