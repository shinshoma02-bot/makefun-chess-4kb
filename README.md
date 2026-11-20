# makefun-chess-4kb
make.fun bounty `tiny-chess-01`: a chess engine in 4,096 bytes of Python.

- `main.py`: 2,656 bytes (limit 4,096). A latin-1 stub that lzma-decompresses
  and execs the engine; Python 3.13 stdlib only, no model calls.
- Search: 10x12 mailbox, pseudo-legal moves + king-safety test, negamax
  alpha-beta, check extension, null move, transposition table, killer moves,
  MVV-LVA ordering, quiescence, repetition avoidance (draw score).
- Eval: material + incremental piece-square terms.
- Deterministic: fixed budget of 200,000 nodes per move (iterative
  deepening, no clock, no randomness). About 1-2 s/move.
- Env: `POST /game`, `POST /move` loop at `MAKEFUN_ENV_URL`.

Local check (kit's env, practice trials 0-2, 18 games): 11.5/18 points,
about Elo 1,420 by the scorer's formula (entry bar 1,154). Replay of trial 0
twice gave identical moves in all 6 games. Final rungs 7-8 (1M/2M nodes)
were not measured locally.
