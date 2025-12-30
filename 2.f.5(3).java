// wrapper класс для конвейерной обработки
public class Pipeline<T> {
    private final T value;
    
    private Pipeline(T value) {
        this.value = value;
    }
    
    public static <T> Pipeline<T> of(T value) {
        return new Pipeline<>(value);
    }
    
    public <R> Pipeline<R> pipe(Function<T, R> func) {
        return new Pipeline<>(func.apply(value));
    }
    
    public T get() {
        return value;
    }
}


public static BoardState processCascade(BoardState currentState) {
    List<Match> matches = findMatches(currentState.board);
    
    if (matches.isEmpty()) {
        return currentState;
    }
    
    // Конвейерная обработка
    return Pipeline.of(currentState)
        .pipe(state -> removeMatches(state, matches))
        .pipe(Game::fillEmptySpaces)
        .pipe(Game::processCascade)
        .get();
}