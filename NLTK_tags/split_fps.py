"""
```
python3 split_fps.py
```
"""
import numpy as np
import pathlib
import json

def main():

    # get a list of fps in a dir
    dp = pathlib.Path("~/surfdrive/Data/PG_en_PS_fiction_050204").expanduser().resolve()
    fps = list(dp.glob("*.txt"))

    # split the list into ...
    n_splits = 6
    splits = np.array_split(fps, n_splits)

    # save each fps split as a json
    for i, split in enumerate(splits):
        with open(f"split_{i}.json", "w") as f:
            json.dump([str(fp) for fp in split], f)

if __name__ == "__main__":
    main()
