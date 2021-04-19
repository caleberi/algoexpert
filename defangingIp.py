def defangingIP(string):
    return "[.]".join(string.split("."))


print(defangingIP("127.0.0.1"))