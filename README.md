# wordle-solver
solver of [Wordle](https://www.powerlanguage.co.uk/wordle/) easy mode

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
[turn1] input 'SERAI' to Wordle and enter the reply
31231
start calculation. wait a minute...
[turn2] input 'FLONG' to Wordle and enter the reply
11112
start calculation. wait a minute...
[turn3] input 'SUGAR' to Wordle and enter the reply
33333
solved
```

# note
* this solver can solve any Wordle answer before 5 turn by simulation.
* mean turn is 3.60648 
