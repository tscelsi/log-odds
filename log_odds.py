#!/usr/bin/env python
""" Calculate token log-odds-ratios using frequency distributions of two corpora and 
    a background corpus. Defaults to z-score scaling unless '--raw' flag is used. """

import argparse
import logging
import math
from typing import Iterator


def _tsv_reader(filepath: str) -> Iterator[str]:
    with open(filepath, "r") as src:
        for line in src:
            yield line.rstrip().split("\t")


def _get_dict(filepath: str) -> dict:
    freqs = dict()
    for token, freq in _tsv_reader(filepath):
        freqs[token] = int(freq)
    return freqs


def _size(corpus: dict) -> int:
    return sum(corpus.values())


def log_odds(word: str, c1: dict, c2: dict, bg: dict, scale: bool) -> float:
    if word in c1 and word in c2 and word in bg:
        numerator_1 = c1[word] + bg[word]
        numerator_2 = c2[word] + bg[word]
        denom_1 = _size(c1) + _size(bg) - numerator_1
        denom_2 = _size(c2) + _size(bg) - numerator_2
        raw_logodds = math.log(numerator_1 / denom_1) - math.log(
            numerator_2 / denom_2
        )
        variance = (1 / numerator_1) + (1 / numerator_2)
        if scale:
            return raw_logodds / math.sqrt(variance)
        else:
            return raw_logodds


def main(args: argparse.Namespace) -> None:

    freq_1 = _get_dict(args.corpus_1)
    freq_2 = _get_dict(args.corpus_2)
    freq_bg = _get_dict(args.corpus_bg)

    if args.raw:
        logging.info("Calculating token log-odds-ratios scaled by z-score.")
    else:
        logging.info("Calculating token log-odds-ratios.")

    ratios = []
    for tok in freq_1:
        rat = log_odds(tok, freq_1, freq_2, freq_bg, args.raw)
        if rat:
            ratios.append((tok, rat))

    ratios.sort(key=lambda x: x[1], reverse=True)

    with open(f"{args.prefix}_top50.tsv", "w") as sink:
        for tok, rat in ratios[:50]:
            sink.write(f"{tok}\t{rat}\n")

    logging.info(
        "Top 50 tokens from %s written to %s", args.corpus_1, sink.name
    )

    with open(f"{args.prefix}_btm50.tsv", "w") as sink:
        for tok, rat in sorted(ratios, key=lambda x: x[1])[:50]:
            sink.write(f"{tok}\t{rat}\n")

    logging.info(
        "Bottom 50 tokens from %s written to %s", args.corpus_2, sink.name
    )


if __name__ == "__main__":
    logging.basicConfig(level="INFO", format="%(levelname)s: %(message)s")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--corpus_1", required=True, help="target corpus for ranking"
    )
    parser.add_argument(
        "--corpus_2", required=True, help="target corpus for comparison"
    )
    parser.add_argument("--corpus_bg", required=True, help="backgroud corpus")
    parser.add_argument(
        "--prefix", required=True, help="prefix for ranked tsv outputs"
    )
    parser.add_argument(
        "--raw",
        default=True,
        action="store_false",
        help="flag to use unscaled log-odds-ratios",
    )
    main(parser.parse_args())
