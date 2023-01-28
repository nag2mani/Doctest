def number_vowels(word):
    '''
	Returns :number of vowels in string word.

	Vowels are defined to be 'a','e','i','o' and 'u'.
	Repeatedbvowels are counted separately.
	Both upper and lower case vowels are counted separately.

    >>> number_vowels('hat')
    1
    >>> number_vowels('hate')
    2
    >>> number_vowels('put')
    1
    >>> number_vowels('butu')
    2
    >>> number_vowels('but')
    1
    >>> number_vowels('beet')
    2

    Parameterword :The text to check for vowels
	prcondition :Word string w/ at least one letter and only letters.
    '''


    a=word.count('a') + word.count('A')
    e=word.count('e') + word.count('E')
    i=word.count('i') + word.count('I')
    o=word.count('o') + word.count('O')
    u=word.count('u') + word.count('U')
    return(a+e+i+o+u)

if __name__=='__main__':
    import doctest
    doctest.testmod()
    
# if every thing is fine then code return nothing.
# if any faliure then it will give data about it.

