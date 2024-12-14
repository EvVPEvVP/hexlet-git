// 42.3
let rec allSubsets n k =
    let rec generate current remaining size =
        if size = 0 then 
            Set.singleton(Set.empty)
        elif remaining < size then 
            Set.empty
        elif remaining = size then
            Set.singleton(Set.ofList [current..current+size-1])
        else
            let withFirst = 
                generate (current+1) (remaining-1) (size-1)
                |> Set.map (fun subset -> Set.add current subset)
            let withoutFirst = generate (current+1) (remaining-1) size
            Set.union withFirst withoutFirst

    if k < 0 || k > n then Set.empty
    else generate 1 n k