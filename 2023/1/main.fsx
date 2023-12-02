open System.IO
open System


let digits =
    File.ReadAllLines "input.txt"
    |> Array.map ((String.filter Char.IsDigit))
// use mapfold????
printfn "%A" digits
