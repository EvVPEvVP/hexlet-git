// 40.1
let rec sum (p, xs) = 
    match xs with
    | [] -> 0
    | x::xs -> if p(x) then x + sum(p,xs) else sum(p,xs)

// 40.2.1
let rec count (xs, n) = 
    match xs with
    | [] -> 0
    | x::xs -> 
        if x < n then count(xs, n)
        elif x = n then 1 + count(xs, n)
        else 0

// 40.2.2
let rec insert (xs, n) = 
    match xs with
    | [] -> [n]
    | x::xs' -> 
        if n <= x then n::x::xs'
        else x::insert(xs', n)

// 40.2.3
let rec intersect (xs1, xs2) = 
    match (xs1, xs2) with
    | ([], _) | (_, []) -> []
    | (x1::xs1', x2::xs2') ->
        if x1 < x2 then intersect(xs1', xs2)
        elif x2 < x1 then intersect(xs1, xs2')
        else x1::intersect(xs1', xs2')

// 40.2.4
let rec plus (xs1, xs2) = 
    match (xs1, xs2) with
    | ([], xs2) -> xs2
    | (xs1, []) -> xs1
    | (x1::xs1', x2::xs2') ->
        if x1 <= x2 then x1::plus(xs1', xs2)
        else x2::plus(xs1, xs2')

// 40.2.5
let rec minus (xs1, xs2) = 
    match (xs1, xs2) with
    | ([], _) -> []
    | (xs1, []) -> xs1
    | (x1::xs1', x2::xs2') ->
        if x1 < x2 then x1::minus(xs1', xs2)
        elif x2 < x1 then minus(xs1, xs2')
        else minus(xs1', xs2')

// 40.3.1
let rec smallest = function
    | [] -> None
    | [x] -> Some(x)
    | x::xs -> match smallest xs with
               | None -> Some(x)
               | Some(y) -> Some(min x y)

// 40.3.2
let rec delete (n, xs) = 
    match xs with
    | [] -> []
    | x::xs -> if x = n then xs else x::delete(n, xs)

// 40.3.3
let rec sort xs = 
    let rec smallest = function
        | [] -> None
        | [x] -> Some x
        | x::xs -> 
            match smallest xs with
            | None -> Some x
            | Some m -> Some(min x m)
            
    let rec delete (n, xs) = 
        match xs with
        | [] -> []
        | x::xs' -> if x = n then xs' else x::delete(n, xs')
        
    match xs with
    | [] -> []
    | _ -> 
        match smallest xs with
        | None -> []
        | Some n -> n::sort(delete(n, xs))

// 40.4
let rec revrev = function
    | [] -> []
    | xs -> List.map List.rev (List.rev xs)