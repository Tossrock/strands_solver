# Summary
A trie-based, no-dependency pure python solver for the NY Times "Strands" game. Invoke like so:

```bash
strand_solver -p 2024_03_12_Rulers_decree.puzzle
```

which produces output like:


gurus:
**G** A E L M T
**U** E F E A H
**R** **U** A F O M
L **S** U R E T
O N C H M O
M G N N E O
E I R T Y F
T E S D R A

auger:
**G** **A** E L M T
**U** **E** F E A H
**R** U A F O M
L S U R E T
O N C H M O
M G N N E O
E I R T Y F
T E S D R A

...etc. In the terminal, the path is colored.

Supports some additional options like `--min X`, to only output words of length X (defaults to 2).

# Requirements
Relies on `python` resolving to a modern version of python, as well as the existence of `/usr/share/dict/words`. No attempt is made to fix the color formatting on non-POSIX platforms.