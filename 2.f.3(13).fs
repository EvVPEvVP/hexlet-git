// 39.1
let rec rmodd = function
    | [] -> []
    | [x] -> []
    | _::x::xs -> x :: rmodd xs

// 39.2
let rec del_even = function
    | [] -> []
    | x::xs when x % 2 = 0 -> del_even xs
    | x::xs -> x :: del_even xs

// 39.3
let rec multiplicity x = function
    | [] -> 0
    | h::t when h = x -> 1 + multiplicity x t
    | _::t -> multiplicity x t

// 39.4
let rec split = function
    | [] -> ([], [])
    | [x] -> ([x], [])
    | x1::x2::xs ->
        let (odds, evens) = split xs
        (x1::odds, x2::evens)

// 39.5
let rec zip = function
    | ([], []) -> []
    | (x::xs, y::ys) -> (x,y) :: zip (xs,ys)
    | _ -> failwith "Lists have different lengths"