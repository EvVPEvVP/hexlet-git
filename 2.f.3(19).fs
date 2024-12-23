// 48.4.1
let rec fibo1 n n1 n2 = 
    match n with
    | 0 -> n2
    | 1 -> n1
    | _ -> fibo1 (n-1) (n1 + n2) n1

// 48.4.2
let rec fibo2 n c =
    match n with
    | 0 -> c 0
    | 1 -> c 1
    | n -> fibo2 (n-1) (fun f1 -> 
           fibo2 (n-2) (fun f2 -> 
           c(f1 + f2)))

// 48.4.3
let rec bigList n k =
    let rec loop n acc =
        if n = 0 then k acc
        else loop (n-1) (1::acc)
    loop n []
