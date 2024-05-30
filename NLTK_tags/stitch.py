import pathlib
import json
from tqdm import tqdm

def main():

    # fps to output splits to stitch together
    split_fps_str = [
        "output/token2tags_0.json",
        "output/token2tags_1.json",
        "output/token2tags_2.json",
        "output/token2tags_3.json",
        "output/token2tags_4.json",
        "output/token2tags_5.json",
    ]

    # convert to pathlib.Path objects
    split_fps = [
        pathlib.Path(split_fp_str).expanduser().resolve()
        for split_fp_str in split_fps_str
    ]

    # stitch together
    joined = {}
    for i, split_fp in tqdm(enumerate(split_fps)): 

        # open next split
        with open(split_fp, 'r') as f:
            split = json.load(f)

        if i == 0:
            joined = split
        else:
            for token, counts in split.items():

                # ensure token exists in joined
                if token not in joined:
                    joined[token] = {}

                # for add each tag:count entry into joined
                for tag, count in counts.items():

                    if tag in joined[token]: 
                        joined[token][tag] += count
                    else:
                        joined[token][tag] = count

    # save the joined object
    with open('joined.json', 'w') as f:
        json.dump(joined, f, ensure_ascii=False)
        
if __name__ == "__main__":
    main()

