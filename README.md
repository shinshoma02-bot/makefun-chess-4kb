# makefun-chess-4kb
4KB Python chess engine for make.fun tiny-chess-01. Run: `MAKEFUN_ENV_URL=... python3 main.py`

- Search: negamax alpha-beta, iterative deepening, TT, null move, quiescence; fixed node budget (L=80000), no clock/randomness.
- Eval: material + PST formula, endgame king centralisation. Castling added; en passant/underpromotion not searched (root filtered by env legal moves).
- Size: main.py 3.4KB (<4,096).
- Local check (kit env, practice trials 0-2, 6 games): ~1,100-1,200 Elo (noisy). Below sunfish baseline (~1,365): a prize is unlikely without further work.
