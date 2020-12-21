using DelimitedFiles

"Load numbers from file."
function loaddata(file::String)::Array{Int,2}
    return readdlm(file, Int)
end

"Find the two entries that sum to 2020."
function findtwoentries(data::Array{Int,2})::Tuple{Int,Int}
    for index in 1:size(data)[1]-1
        for second in data[index+1:end, 1]
            if data[index, 1] + second == 2020
                return data[index], second
            end
        end
    end
end

"Find the three entries that sum to 2020."
function findthreeentries(data::Array{Int,2})::Tuple{Int,Int,Int}
    for index in 1:size(data)[1]-2
        for second in data[index+1:end, 1]
            for third in data[index+2:end, 1]
                if data[index, 1] + second + third == 2020
                    return data[index], second, third
                end
            end
        end
    end
end

function main()
    file = "../assets/data/01.txt"
    data = loaddata(file)

    # part one
    first, second = findthreeentries(data)
    println("The product of the two numbers is ", first*second, ".")

    # part two
    first, second, third = findthreeentries(data)
    println("The product of the three numbers is ", first*second*third, ".")
end

main()
