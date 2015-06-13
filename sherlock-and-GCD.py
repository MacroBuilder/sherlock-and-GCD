def subsets(array, length_of):

    from fractions import gcd
    
    subsets = []
    
    for a in range(length_of):
        for b in range(a + 1, length_of + 1):
            subsets.append(array[a:b])
            
    for element in subsets:
        if reduce(gcd,element) == 1 and all(element.count(item) == 1 for item in element):
            return 'YES'
    return 'NO'
                
test_cases = int(raw_input().strip())

for _ in range(test_cases):
    m = int(raw_input().strip())
    eval_list = [int(i) for i in raw_input().strip().split()]
    print subsets(eval_list, m)
