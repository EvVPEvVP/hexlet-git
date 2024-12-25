// 49.5.1
let even_seq = Seq.initInfinite (fun i -> (i + 1) * 2)

// 49.5.2
let fac_seq = 
    let rec factorial n =
        match n with
        | 0 -> 1
        | n -> n * factorial(n-1)
    Seq.initInfinite factorial

// 49.5.3
let seq_seq = 
    Seq.initInfinite (fun i -> 
        if i % 2 = 0 then i/2 
        else -(i+1)/2)