public static BoardState initializeGame(int boardSize) {
    // Создаём пустую доску
    Board emptyBoard = new Board(boardSize);
    
    // Создаём начальное состояние игры (пустая доска, 0 очков)
    BoardState emptyState = new BoardState(emptyBoard, 0);
    
    // Заполняем все пустые клетки случайными фишками
    BoardState filledState = fillEmptySpaces(emptyState);
    
    // Запускаем каскад
    return processCascade(filledState);
}



public static BoardState processCascade(BoardState currentState) {
    // Все комбинации на доске
    List<Match> matches = findMatches(currentState.board);
    
    if (matches.isEmpty()) {
        return currentState;
    }
    
    // Удаляем найденные комбинации
    BoardState afterRemoval = removeMatches(currentState, matches);
    
    // Заполняем пустоту новыми фишками
    BoardState afterFilling = fillEmptySpaces(afterRemoval);
    
    return processCascade(afterFilling);
}