def game(heap,moves,to):
    if heap >= 40:
        return moves %2 == to %2
    if moves == to:
        return 0
    h = [game(heap + 1, moves + 4,to),
         game(heap * 2, moves + 4, to)]
    return any(h)

