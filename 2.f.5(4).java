// Конвейер функция
private static BoardState applyCascadeStep(BoardState state) {
    return Pipeline.of(state)
        .pipe(bs -> removeMatches(bs, findMatches(bs.board)))
        .pipe(Game::fillEmptySpaces)
        .pipe(Game::processCascade)
        .get();
}

// Основная функция
public static BoardState processCascade(BoardState currentState) {
    return findMatches(currentState.board).isEmpty()
        ? currentState
        : applyCascadeStep(currentState);
}