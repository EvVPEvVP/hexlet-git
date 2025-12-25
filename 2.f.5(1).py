public static BoardState processCascade(BoardState currentState) {
    // Шаг 1 Находим комбинации
    List<Match> matches = findMatches(currentState.board);
    
    // Шаг 2 Если комбинаций нет - возвращаем текущее состояние
    if (matches.isEmpty()) {
        return currentState;
    }
    
    // Шаг 3 Удаляем комбинации, обновляем счёт
    BoardState stateAfterRemoval = removeMatches(currentState, matches);
    
    // Шаг 4 Заполняем пустые клетки
    BoardState stateAfterFill = fillEmptySpaces(stateAfterRemoval);
    
    // Шаг 5: Рекурсия
    return processCascade(stateAfterFill);
}
