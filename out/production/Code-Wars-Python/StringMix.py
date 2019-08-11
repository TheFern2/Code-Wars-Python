import re


def mix(s1, s2):

    # get rid of non a-z
    regex = re.compile('[^a-z]')
    #First parameter is the replacement, second parameter is your input string
    regex.sub('', 'ab3d*E')
    #Out: 'abdE'

    return ""

mix("fArneio")