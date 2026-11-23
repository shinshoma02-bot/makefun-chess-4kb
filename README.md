# makefun-chess-4kb

make.fun bounty tiny-chess-01: a chess engine in at most 4,096 bytes of Python.

## Engine (main.py)
- Packed with the kit's `makefun compress` (lzma stub). Source is kept outside the repo (`engine_src.py`, not committed) so the repo stays under 8,192 bytes.
- Search: iterative deepening alpha-beta with transposition table, null-move pruning, quiescence search, check extension, killer and TT move ordering, and late-move reduction (LMR) for quiet moves.
- Eval: material plus simple piece-square tables.
- Deterministic: fixed node budget (400,000 nodes per move), no clock, no randomness.

## Local practice results (kit env, practice trials 0-2)
| version | trial Elo | mean |
|---|---|---|
| previous main.py (200k nodes, no LMR) | 1364 / 1451 / 1451 | 1422 |
| current main.py (400k nodes, LMR) | 1654 / 1451 / 2112 | 1739 |
| tested, not adopted (500k nodes, LMR) | 1545 / 1451 / 2112 | 1703 |

Measured with the kit's env server and the rules' Elo formula (the docker grader is not available here, so the bot was run as a plain python3.13 process against the kit env).

## Size
- main.py: 2,588 bytes (cap 4,096)
- whole repo snapshot: under 8,192 bytes
