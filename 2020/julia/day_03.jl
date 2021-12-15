"Load data from file."
function loaddata(file::String)
    return readlines(file)
end

"Take toboggan down the slope on map."
function toboggan(map::Array, go::Array)::Int
    pos = [1, 1]
    n_trees = 0
    while pos[1] < length(map)
        pos += go
        pos[2] -= div(pos[2], length(map[1]) + 1)*length(map[1])
        n_trees += (map[pos[1]][pos[2]] == '#')
    end
    return n_trees
end

function main()
    map = loaddata("../assets/data/03.txt")

    # part one
    n_trees = toboggan(map, [1, 3])
    println("Encountered ", n_trees, " trees while tobogganing.")

    # part two
    n_trees = 1
    for go in [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
        n_trees *= toboggan(map, go)
    end
    println("Product of trees while tobogganing is ", n_trees, ".")
end

main()
