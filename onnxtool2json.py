obj = open("./result.txt")
data = obj.readlines()
obj.close()
# read data
prefix = "\"prefix\":["
postfix = "\"postfix\":["
layers = "\"layers\":["
index = range(len(data))
for id in index:
    tmp = data[id].replace("\n", "") # discard the "\n" at the end
    tmp = tmp.replace(",", "")   # discard the "," in number's format
    tmp = tmp.split()   # .split() discard empty strings from the result, we can skip multiple spaces
    if id <= 1:
        prefix += "["
        for p in tmp:
            prefix = prefix + "\"" + p + "\","
        prefix = prefix.strip(",") + "]," # discard the final ","
        if id == 1:
            prefix = prefix.strip(",") + "],"    # discard the final ","
            # end of prefix
    elif id < (len(data) - 1):
        layers += "["
        for p in tmp:
            layers = layers + "\"" + p + "\","
        layers = layers.strip(",") + "]," # discard the final ","
        if id == len(data) - 2:
            layers = layers.strip(",") + "],"    # discard the final ","
            # end of layers
    else:
        for p in tmp:
            postfix = postfix + "\"" + p + "\","
        postfix = postfix.strip(",") + "]"  # discard the final ","
        # end of postfix
# add overall info
json_str = "{" + prefix + layers + postfix + "}"
print(json_str)

