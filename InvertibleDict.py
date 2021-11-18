import collections


class InvertibleDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k, v in self.items():
            if (isinstance(v, collections.abc.Iterable)) and (not isinstance(v, str)):
                self.__setitem__(k, tuple(v))

    def __invert__(self):

        # get flat keys and values
        keys = []
        values = []
        for k, v in self.items():
            if (isinstance(v, collections.abc.Iterable)) and (not isinstance(v, str)):
                values += list(v)
                keys += [k] * len(list(v))
            else:
                values.append(v)
                keys.append(k)

        d = collections.defaultdict(list)
        for k, v in zip(keys, values):
            if (isinstance(v, collections.abc.Iterable)) and (not isinstance(v, str)):
                for element in v:
                    d[element].append(k)
            else:
                d[v].append(k)

        for k, v in d.items():
            if len(v) > 1:
                d[k] = tuple(v)
            else:
                d[k] = v[0]
        return InvertibleDict(d)
