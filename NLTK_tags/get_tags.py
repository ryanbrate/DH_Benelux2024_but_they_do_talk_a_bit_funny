"""
    Return a dict of tokens, and corresponding pos tags in context
"""
import json
import pathlib
import re
import sys
import typing
from collections import Counter, defaultdict

import numpy as np
from nltk import pos_tag
from scipy.stats import bernoulli
from tqdm import tqdm

from Loaders.PG_book import gen_paragraphs, gen_sentences


def main(args: list):

    # load the fps to consider
    split_i = args[0]
    split_fp = args[1]
    with open(split_fp, "r") as fp:
        fps = [pathlib.Path(fp_str) for fp_str in json.load(fp)]

    # load the tokenization patterns
    token_patterns: re.Pattern = re.compile(
        r"(?:Mr.|Mrs.|Ms.)" + r"|"  # english salutations
        r"(?:[A-Z]\.)+[A-Z]"  # abbreviations type 1 (initalism), e.g., U.S.A.
        + r"|"
        + r"\d+(?:/\d+)+"  # fractions, dates
        + r"|"
        + r"[\$£]{0,1}\d+(?:\.\d+)*%*"  # numbers, currency, percentages
        + r"|"
        # + r"[a-zA-Z]+(?:-[a-zA-Z]+)*(?:['’][a-zA-Z]+)*"  # words, optionally hyphenated, include apostrophe chunks [supersedes the next 2]
        # + r"|"
        + r"[a-zA-Z]+(?:-[a-zA-Z]+)*"  # words, optionally hyphenated, not including aprostrophe chunks
        + r"|"
        + r"['’][a-zA-Z]+"  # apostrophe chunks
        + r"|"
        + r"\.\.\."  # elipsis
        + r"|"
        + r"[\[\].,;\"'?!():-_`]"  # misc separate tokens
        # + r"|"
        # + r"[•*■„~»><]"  # bad ocr tokens
        ,
        flags=re.IGNORECASE,
    )

    ## load the dictionary for reparing paragraph split words
    lexicon_fp = pathlib.Path("../dictionaries/english.txt").expanduser().resolve()
    with open(lexicon_fp, "r", encoding="utf-8") as f:
        lexicon: set[str] = set([w.strip("\n") for w in f.readlines()])
    print("lexicon loaded")

    ## consider each sentence, of each paragraph, of each book in-turn
    samples = []
    token2tags = {}
    for fp in tqdm(fps):

        # collect token & tag pairs
        for paragraph in gen_paragraphs(fp, dictionary=lexicon):
            # for paragraph in [
            #     "They went for a run around the park. They can run fast."
            # ]:  # test! run should be return 2 pos tags!
            for i, sentence in enumerate(gen_sentences(paragraph)):

                try:
                    tokens: list[str] = re.findall(token_patterns, sentence)
                    tagged_tokens: list[tuple] = pos_tag(tokens)

                    # collect
                    for token, tag in tagged_tokens:
                        add(token2tags, token, tag)

                    # flip a coint, print sentence & tokenised for (for refernece) with a 1/1000 probability
                    if bernoulli.rvs(p=1 / 10000) == 1:
                        samples.append([sentence, tags])
                except:
                    pass

    # save
    with open(f"token2tags_{split_i}.json", "w") as f:
        json.dump(token2tags, f)
    with open(f"samples_{split_i}.json", "w") as f:
        json.dump(list(samples), f)


def add(token2tags: dict, token: str, tag: str):
    if token in token2tags.keys():
        if tag in token2tags[token]:
            token2tags[token][tag] += 1
        else:
            token2tags[token][tag] = 1
    else:
        token2tags[token] = {tag: 1}


if __name__ == "__main__":
    main(sys.argv[1:])
