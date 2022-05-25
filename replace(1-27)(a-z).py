def encode(message, key):
    a = [chr(j) for j in range(97, 123)]
    new_message = []
    for i in message:
        new_message.append(a.index(i) + 1)
    new_key = []
    while len(new_key) < len(new_message):
        for i in key:
            new_key.append(int(i))
    result = []
    for i in range(len(new_message)):
        result.append(new_message[i] + key[i])
    return result


