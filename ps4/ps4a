# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

#char = 'a'
#li = ['ust','stu','tus']
def insert_char(char, li):
    assert len(char) == 1, "Length of 1st arg is not 1."
    assert isinstance(li, list), "2nd arg is not a list object." # is this needed
    new_li = []
    for phrase in li:
        for pos in range(0,len(phrase)+1):
            new_phrase = phrase[:pos] + char + phrase[pos:]
            #print(new_phrase)
            new_li.append(new_phrase)
    return new_li

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return list(sequence) # need to return as a list or insert_char() will throw Assertion Error
    else:
        return insert_char(sequence[0], get_permutations(sequence[1:]))

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    seq1 = "abd"
    print('Input:', seq1)
    print('Expected Output:', ['abd', 'adb', 'bad', 'bda', 'dab', 'dba'])
    print('Actual Output:', get_permutations(seq1))

    seq2 = "ab1"
    print('Input:', seq2)
    print('Expected Output:', ['ab1', 'a1b', 'ba1', 'b1a', '1ab', '1ba'])
    print('Actual Output:', get_permutations(seq2))

    seq3 = "hoe"
    print('Input:', seq3)
    print('Expected Output:', ['hoe', 'heo', 'ohe', 'oeh', 'eoh', 'eho'])
    print('Actual Output:', get_permutations(seq3))
