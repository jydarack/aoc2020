
function get_inputs(fn::String="toy")::Array{Int64}
    map(x->(x=tryparse(Int64,x)), readlines("./inputs/day01/"*fn*"inputs.txt"))
end


function get_two(fn::String="toy")
    s = 1 
    for i in [x for x in get_inputs(fn) if (2020 - x) in get_inputs(fn)]
        s = s * i
    end
    return s
end

@assert(get_two("toy") == 514579)
@assert(get_two("puzzle") == 889779)

function get_three(fn::String="toy")
    s = 1 
    k = get_inputs(fn)
    # println(unique([x for x in k for y in k if (2020 - x - y) in k]))

    for i in unique([x for x in k for y in k if (2020 - x - y) in k])
        s = s * i
    end
    return s
end

@assert(get_three() == 241861950)
@assert(get_three("puzzle") == 76110336)