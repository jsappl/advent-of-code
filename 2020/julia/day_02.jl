"Load data from file."
function loaddata(file::String)
    return readlines(file)
end

"Check password according to sled rental policy."
function checksled(low::Int, up::Int, char::Char, password::AbstractString)
    return count(string(char), password) ∈ low:up
end

"Check password according to toboggan rental policy."
function checktoboggan(low::Int, up::Int, char::Char, password::AbstractString)
    return (password[low] == char) ⊻ (password[up] == char)
end

"Count valid passwords according to given policy."
function countvalid(data::Array, rule::Function)
    n_count = 0
    for line in data
        low, up, char, password = split(replace(line, r"[-:]" => " "))
        n_count += rule(parse(Int, low), parse(Int, up), char[1], password)
    end
    return n_count
end

function main()
    data = loaddata("../assets/data/02.txt")

    # part one
    n_valid = countvalid(data, checksled)
    println("The product of the two numbers is ", n_valid, ".")

    # part two
    n_valid = countvalid(data, checktoboggan)
    println("The product of the two numbers is ", n_valid, ".")
end

main()
