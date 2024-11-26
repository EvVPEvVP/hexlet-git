// 23.4.1
let (.+.) (g1,s1,m1) (g2,s2,m2) =
    let totalMedyaks = m1 + m2
    let addSilver = totalMedyaks / 12
    let remainingMedyaks = totalMedyaks % 12
    
    let totalSilver = s1 + s2 + addSilver
    let addGold = totalSilver / 20
    let remainingSilver = totalSilver % 20
    
    let totalGold = g1 + g2 + addGold
    
    (totalGold, remainingSilver, remainingMedyaks)

let (.-.) (g1,s1,m1) (g2,s2,m2) =
    let m1Total = g1 * 20 * 12 + s1 * 12 + m1
    let m2Total = g2 * 20 * 12 + s2 * 12 + m2
    let diff = m1Total - m2Total
    
    let gold = diff / (20 * 12)
    let remainAfterGold = diff % (20 * 12)
    let silver = remainAfterGold / 12
    let medyaks = remainAfterGold % 12
    
    (gold, silver, medyaks)

// 23.4.2
let (.+) (a1,b1) (a2,b2) = 
    (a1 + a2, b1 + b2)

let (.-) (a1,b1) (a2,b2) = 
    (a1 - a2, b1 - b2)
    
let (.*) (a1,b1) (a2,b2) = 
    (a1*a2 - b1*b2, b1*a2 + a1*b2)
    
let (./) (a1,b1) (a2,b2) =
    let denom = a2*a2 + b2*b2
    ((a1*a2 + b1*b2)/denom, (b1*a2 - a1*b2)/denom)