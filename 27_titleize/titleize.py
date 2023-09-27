def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase = phrase.lower()

    return [word.capitalize() for word in phrase]

    """
    OR...

    return phrase.title()
    
    """
