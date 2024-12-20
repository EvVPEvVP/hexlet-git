// 47.4.1
let f n = 
    let mutable result = 1
    let mutable i = 1
    while i <= n do
        result <- result * i
        i <- i + 1
    result

// 47.4.2
let fibo n = 
    if n = 0 then 0
    else
        let mutable prev = 0
        let mutable curr = 1
        let mutable i = 1
        while i < n do
            let temp = curr
            curr <- prev + curr
            prev <- temp
            i <- i + 1
        curr
