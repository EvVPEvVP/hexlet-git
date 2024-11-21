// 17.1
let rec pow (s: string, n: int) : string = 
    match n with
    | n when n <= 0 -> ""
    | 1 -> s
    | _ -> s + pow(s, n-1)

// 17.2
let rec isIthChar (s: string, n: int, c: char) : bool =
    if n < 0 || n >= s.Length then false
    else s.[n] = c

// 17.3
let rec occFromIth (s: string, n: int, c: char) : int =
    if n >= s.Length || n < 0 then 0
    elif s.[n] = c then 1 + occFromIth(s, n+1, c)
    else occFromIth(s, n+1, c)