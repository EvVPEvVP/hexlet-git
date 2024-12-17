// 43.3
let try_find key m = 
    match Map.containsKey key m with
    | true -> Some(Map.find key m)
    | false -> None