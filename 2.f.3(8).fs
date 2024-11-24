let curry f = 
    fun x -> 
        fun y -> f (x, y)

let uncurry g = 
    fun (x, y) -> g x y