type TimeOfDay = { hours: int; minutes: int; f: string }

let (.>.) x y =
    match (x.f, y.f) with
    | ("AM", "PM") -> false
    | ("PM", "AM") -> true
    | _ -> 
        if x.hours = y.hours then
            x.minutes > y.minutes
        else
            x.hours > y.hours