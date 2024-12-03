// 34.1
let rec upto = function
    | 1 -> [1]
    | n when n > 1 -> upto (n-1) @ [n]
    | _ -> []

// 34.2
let rec dnto = function
    | 1 -> [1]
    | n when n > 1 -> n :: dnto (n-1)
    | _ -> []

// 34.3
let rec evenn = function
    | 0 -> []
    | n when n > 0 -> evenn (n-1) @ [2*(n-1)]
    | _ -> []