// 16.1
let notDivisible (n, m) = m % n <> 0

// 16.2
let prime n =
    if n <= 1 then false
    else
        let rec check i =
            if i * i > n then true
            elif n % i = 0 then false
            else check (i + 1)
        check 2