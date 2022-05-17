import bencode

def main():
    data = ["This is a string", 1923, b'What else could be done?', {'perfect': 'world', 'sun': 'passion', 'a': 0, 'animals': ['cat', 'dog'], b'raw': 'meat'}]
    encoded = bencode.encode(data)
    print(encoded)

if __name__ == '__main__':
    main()