A pipeline to catalogue tokens and their corresponding contextualised POS tags in the corpus

pipeline returns:

    {
        token: {
            tag: count,
            ...
        },
        ...
    }

# split the fps to be processed into sub-lists
```
python3 split_fps.py
```

# get {token:{tag:count, ... },... } counts for each sublist of fps via the get_tags.py script
```
sh run.sh
```

# stitch the counts together
```
python3 stitch.py
```

# convert to tag:token list format
```
python3 get_tokens_by_tags.py
```
