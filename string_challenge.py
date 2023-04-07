def StringChallenge(strParam):
    new_str = strParam.replace('<', '?').replace('>', '?').split('?')
    tag_dict = {'/div': 'div', '/b': 'b', '/em': 'em', '/p': 'p', '/i': 'i'}
    open = []
    close = []
    print(new_str)
    for s in new_str:
        if s in tag_dict.values():
            open.append(s)
        elif s in tag_dict.keys():
            close.append(s)
    print(open, close)
    open.reverse()

    for i, j in zip(open, close):
        if tag_dict[j] != i:
            return j
    return True
    # return strParam


# keep this function call here
print(StringChallenge("<div><b><p>hello world</p></b>"))

