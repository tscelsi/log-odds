# log-odds
This is a log-odds, informative Dirichlet prior method for corpora comparison as 
presented in:<br><br>
Monroe, B. L., Colaresi, M. P., and Quinn, K. M. 2008.  Fightin' words: lexical
feature selection and evaluation for identifying the content of political
conflict. Political Analysis 16(4): 372-40.

To run this script, you should first generate or get a hold of three tsv files,
i.e., two corpora for comparison and a third corpus for prior token frequency 
estimation. The tsv's should have one token and the its frequency count on each 
line.

Usage
=======
```
usage: log_odds.py [-h] --corpus_1 CORPUS_1 --corpus_2 CORPUS_2 
		   --corpus_bg CORPUS_BG --lim [--out] [--raw]

optional arguments:
  -h, --help            show this help message and exit
  corpus_1 CORPUS_1     first corpus, a tsv of token + counts
  corpus_2 CORPUS_2     second corpus tsv
  corpus_bg CORPUS_BG
                        backgroud corpus tsv
  --lim			number of ranked tokens for comparison
  --out		        optional path for ranked output
  --raw                 flag to use unscaled log-odds ratios
```

