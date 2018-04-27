tz_dict = {"a": 2, "b": 6, "c": 1, "d": 9}
tz_dict = dict(sorted(tz_dict.items(), key=lambda kv: (-kv[1], kv[0])))
print(tz_dict)
a = [1, 4, 2, 3, 5]
a = sorted(a)
print(a)
