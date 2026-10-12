def solution(sizes):
    
    the_longest_width = -float('inf')
    the_longest_height = -float('inf')
    for (w, h) in sizes:
        longer_length = max((w, h))
        shorter_length = min((w, h))
        
        if longer_length > the_longest_width:
            the_longest_width = longer_length
        if shorter_length > the_longest_height:
            the_longest_height = shorter_length
    answer = the_longest_width * the_longest_height
    return answer
