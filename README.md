# Summary
A trie-based, no-dependency pure python solver for the NY Times "Strands" game. Invoke like so:

```bash
strand_solver -p 2024_03_12_Rulers_decree.puzzle
```

which produces output like:

![image](https://github.com/Tossrock/strands_solver/assets/284311/50c2b81c-53ea-4430-a772-a7497ae8b70a)


Supports some additional options like `--min X`, to only output words of length X (defaults to 2).

# Requirements
Relies on `python` resolving to a modern version of python, as well as the existence of `/usr/share/dict/words`. No attempt is made to fix the color formatting on non-POSIX platforms.
