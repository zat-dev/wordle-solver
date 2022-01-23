# wordle-solver
solver of [Wordle](https://www.powerlanguage.co.uk/wordle/) easy mode
word list is made from https://www.bestwordlist.com/5letterwords.htm

# usage
* run `python solver.py`
* input word to Wordle following solver instruction
* input Wordle reply on the terminal following the bellow format
```
    the input reply format is:
       GRAY=1, YELLOW=2, GREEN=3
    
    for example, if Wordle reply is all gray, enter the following
       11111
```

# example terminal
```
> python .\solver.py
[turn1] input 'BRUSH' to Wordle and enter the reply
13111
start calculation. wait about 10 minute...
[turn2] input 'TEIND' to Wordle and enter the reply
11311
start calculation. wait about 10 minute...
[turn3] input 'POKAL' to Wordle and enter the reply
21111
start calculation. wait about 10 minute...
[turn4] input 'GAUCY' to Wordle and enter the reply
11121
start calculation. wait about 10 minute...
[turn5] input 'CRIMP' to Wordle and enter the reply
33333
solved
```
