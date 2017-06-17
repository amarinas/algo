# // function hill(v) {
# //     var copy  = v.slice(0).sort();
# //     var max   = 0;
# //
# //     for(var i = 0; i < v.length; i++) {
# //         var a = v[i];
# //         var b = copy[i];
# //
# //         // Difference
# //         if(a < b && ((b-a) > max)) {
# //             max = b - a;
# //         } else if(a-b > max) {
# //             max = a - b;
# //         }
# //     }
# //
# //     return max;
# // }
# //
# // console.log(hill([5,4,3,2,8, 9]))

def hill(v):
    duplicate = sorted(v)
    max = 0

    for i in range(len(v)):
        for i in range(len(duplicate)):
            x = v[i]
            y = duplicate[i]
            # print x, y

            if x < y and ((x-y) > max):
                max = x - y

            elif x-y >max:
                max = x-y
    return max




print(hill([5,4,3,2,8, 9]))
