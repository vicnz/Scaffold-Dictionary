# Scaffolding

### Page Resource

> <a href="https://sil-philippines-languages.org/online/ivb/dict/lexicon/lx00001.html">https://sil-philippines-languages.org/online/ivb/dict/lexicon/lx00001.html</a>

## COMMANDS

start the environment of the project using
the `activate` command inside the **/Scripts/** directory

## Required Packages

```yaml
- bs4 (BeautifulSoup4)
- requests
```

### Install Packages

```bash
# recommend installation inside an venv environment

pip install bs4, requests
```

### **Run**

---

```bash
python src/main.py
```

> command parameters
> - `--count` - number (optional)
> - `--start` - number (opional)
> - `--init` - null (first-run only / or consecutive database rebuild)
---

### Initialize Database and Table

> The command initialized the Database on add *default* Ten(10) Items

```bash
python src/main.py --init
```

---

### Specify **Start** and **End** Count

```bash
# lets assume that you already run the above statement, then run this after

python src/main.py --count 50 --start 11
```

> This will add items from Page 11 to 50

> **NOTE**: we already added 10 items from 10 pages upon initialization so it says we have to *start* at **11**
---

### Single Line

```bash
python src/main.py --init --count 50
```

> This will initialize Database and add 50 items from 
50 Pages

> Be sure when specifying a `--start` value it must not overlapped with your previous `--count` value command


```bash
python src/main.py --init --count 100
# and then subsequently run
python src/main.py --start 99 --count 500
```
> this will return an error because item **99** and **100** overlapped already
 
---

## Generate Words List

generate a list of words as a **JSON** file

```bash
python src/words.py
```

> This will give an **error** if the database has not been created yet