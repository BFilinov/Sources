

# 3
def convert_dict_keys(dict):
    d_result = {}
    for k, v in dict.items():
        v_key = str(k)
        if d_result.get(v_key) is None:
            d_result[v_key] = v
    return d_result

v_dict = {'a':123, 0:12515, 0xffff:0b0000100000, 'xxx':[1231,1,1]}
v_dict_converted = convert_dict_keys(v_dict)
print(v_dict)
print(v_dict_converted)