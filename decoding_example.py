import bencode

def main():
    with open('example.torrent', 'rb') as file:
        decoded = bencode.decode(file.read())
    
    print(decoded)

if __name__ == '__main__':
    main()