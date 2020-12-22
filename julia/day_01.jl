using DelimitedFiles

"Load numbers from file."
function loaddata(file::String)
    return readdlm(file, '\t', Int, '\n')
end

"Find the two entries that sum to 2020."
function findtwo(data::Array{Int64,2})
    return [x * y for x in data, y in data if x + y == 2020][1]
end

"Find the three entries that sum to 2020."
function findthree(data::Array{Int64,2})
    return [x * y * z for x in data, y in data, z in data if x + y + z == 2020][1]
end

function main()
    data = loaddata("../assets/data/01.txt")
    println(typeof(data))

    # part one
    println("The product of the two numbers is ", findtwo(data), ".")

    # part two
    println("The product of the three numbers is ", findthree(data), ".")
end

main()
