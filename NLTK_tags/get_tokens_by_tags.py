import json
import pathlib

from collections import defaultdict


def main():

    # load the catalogue
    catalogue_fp = pathlib.Path("output/joined.json").expanduser().resolve()

    # load the {token: {tag:count, ...}, ...} dict, d
    with open(catalogue_fp, "r") as f:
        d = json.load(f)

    # convert d to tag2tokens
    tag2tokens = defaultdict(set)  # {tag: tokens list, ...}
    for token, counts in d.items():
        for tag, count in counts.items():
            tag2tokens[tag].add(token)

    # save
    with open("tag2token.json", "w") as f:
        json.dump({tag: list(tokens) for tag, tokens in tag2tokens.items()}, f)


if __name__ == "__main__":
    main()
