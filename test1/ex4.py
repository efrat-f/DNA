def my_reduce(function, arr, initial=0):
    for num in arr:
        initial = function(initial, num)
    return initial