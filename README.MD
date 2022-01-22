# Scaffolding
### Page Resource

> https://sil-philippines-languages.org/online/ivb/dict/lexicon/lx00001.html
> 

## COMMANDS
start the environment of the project using
the `activate` command inside the **/Scripts/** directory

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
> This will initialize Database and add 50 items from 50 Pages

> Be sure when specifying a `--start` value it must not overlapped with your previous command

> `python src/main.py --init --count 100` and subsequently run `python src/main.py --count 500 --start 99` this will return an error because item *99* and *100* overlapped already <br>

> **NOTE** this bug will fixed on the next *commmit*
