// 50.2.1
let fac_seq = 
    let rec factorial n =
        match n with
        | 0 | 1 -> 1
        | _ -> n * factorial(n-1)
    seq {
        let mutable n = 0
        while true do
            yield factorial n
            n <- n + 1
    }

// 50.2.2
let seq_seq = 
    seq {
        yield 0
        let mutable n = 1
        while true do
            yield -n
            yield n
            n <- n + 1
    }
