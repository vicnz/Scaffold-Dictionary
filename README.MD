# Scaffolding
### Page Resource

> https://sil-philippines-languages.org/online/ivb/dict/lexicon/lx00001.html
> 

## COMMANDS
start the environment of the project using
the `activate` command inside the **/Scripts/** directory

### Run
**Command**
```bash
python  src/main.py
```

initialize the Database First Using
```bash
python src/main.py --init
```

by default the fetching each page *(summing to almost 6_0000 Pages)* you need to limit the count

> specify the count using the `--count int` and starting number `--start int`

```bash
python src/main.py --count 10 --start 1
```

