from hashtable.repeated_word import repeated_word


def test_repeated_word1():
    string="Once upon a time, there was a brave princess who..."
    actual=repeated_word(string)
    expected="a"
    assert actual==expected

def test_repeated_word2():
    string="It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual=repeated_word(string)
    expected="it"

    assert actual==expected

def test_repeated_word3():
    string="It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    actual=repeated_word(string)
    expected="summer"
    assert actual==expected

def test_repeated_no_duplicate():
    string="I'm Issa Salman"
    actual=repeated_word(string)
    expected="no repeated"
    assert actual==expected

def test_repeated_empty_string():
    string=""
    actual=repeated_word(string)
    expected="not a string"
    assert actual==expected


