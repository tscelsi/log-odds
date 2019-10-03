# log-odds
This is a Log-odds, informative Dirichlet prior method corpora comparison.
Running the script will produce two files, with the top 50 ranked log-odds ratios for each corpus.

Usage
=======
```
usage: log_odds.py [-h] --corpus_1 CORPUS_1 --corpus_2 CORPUS_2 
		   --corpus_bg CORPUS_BG --prefix PREFIX [--raw]

optional arguments:
  -h, --help            show this help message and exit
  --corpus_1 CORPUS_1   target corpus for ranking
  --corpus_2 CORPUS_2   target corpus for comparison
  --corpus_bg CORPUS_BG
                        backgroud corpus
  --prefix PREFIX       prefix for ranked tsv outputs
  --raw                 flag to use unscaled log-odds-ratios
```

