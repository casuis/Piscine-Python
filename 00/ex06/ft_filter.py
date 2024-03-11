def ft_filter(function, iterable):
    '''
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    '''
    ret = []
    if function is not None:
        ret = [obj for obj in iterable if function(obj) is True]
    else:
        ret = [obj for obj in iterable if obj]
    return ret


def main():
    # test = ["salut", "Salut", "test", "T"]
    # ret = ft_filter(lambda object: object.isupper(), test)
    # for x in ret:
    print(ft_filter.__doc__)
    return


if __name__ == "__main__":
    main()
