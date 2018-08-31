def camelCase(st):
    print('Enter your sentence')
    st = input()

    output = ''.join(x for x in st.title() if x.isalnum())
    return output[0].lower() + output[1:]
print(camelCase('st'))