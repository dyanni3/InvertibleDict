import collections
import pickle

class InvertibleDict(collections.UserDict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k, v in self.items():
            if not k.__hash__:
                k = pickle.dumps(k)
            self.__setitem__(k, v)

    def __invert__(self):
        d = collections.defaultdict(list)
        for k, v in self.items():
            if not v.__hash__:
                v = pickle.dumps(v)
            d[v].append(k)

        for k, v in d.items():
            if len(v) > 1 and not isinstance(v, bytes):
                d[k] = tuple(v)
            else:
                d[k] = v[0]
        return InvertibleDict(d)

    def __getitem__(self, key):
        if not key.__hash__:
            key = pickle.dumps(key)
        try:
            value = super().__getitem__(key)
        except KeyError as e:
            raise
        if isinstance(value, bytes) or isinstance(value, collections.abc.Iterable):
            value = self.decode_nested(value)
        return value

    def decode_nested(self, value):
        if not isinstance(value, bytes):
            if isinstance(value, collections.abc.Iterable):
                if not any([isinstance(element, bytes) for element in value]):
                    return value
                else:
                    ret = []
                    for element in value:
                        if isinstance(element, bytes):
                            element = self.decode_nested(element)
                            ret.append(element)
                        else:
                            ret.append(element)
                    return ret
            else:
                return value
        else:
            value = pickle.loads(value)
            return self.decode_nested(value)




    def __setitem__(self, key, value):
        if not key.__hash__:
            key = pickle.dumps(key)
        if not value.__hash__:
            value = pickle.dumps(value)
        super().__setitem__(key, value)

    def __repr__(self):
        keys, values = [], []
        for k, v in self.items():
            if isinstance(k, bytes):
                k = self.decode_nested(k)
            if isinstance(v, bytes):
                v = self.decode_nested(v)
            keys.append(k)
            values.append(v)
        s = "{"
        for k, v in zip(keys, values):
            s += f"{k}:{v}, "
        s = s[:-2] + "}"
        if s == "}":
            return "{}"
        return s





