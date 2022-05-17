# bencode-python
Library used Encoding and Decoding .torrent files

# Encoding
Running encoding over
> ["This is a string", 1923, b'What else could be done?', {'perfect': 'world', 'sun': 'passion', 'a': 0, 'animals': ['cat', 'dog'], b'raw': 'meat'}]

as a result, will give

> l16:This is a stringi1923e24:What else could be done?d7:perfect5:world3:sun7:passion1:ai0e7:animalsl3:cat3:doge3:raw4:meatee

# Decoding
Decoding a torrent file returns
```python
OrderedDict([(b'announce', b'udp://tracker.leechers-paradise.org:6969'),
             (b'announce-list',
              [[b'udp://tracker.leechers-paradise.org:6969'],
               [b'udp://tracker.coppersurfer.tk:6969'],
               [b'udp://tracker.opentrackr.org:1337'],
               [b'udp://explodie.org:6969'],
               [b'udp://tracker.empire-js.us:1337'],
               [b'wss://tracker.btorrent.xyz'],
               [b'wss://tracker.openwebtorrent.com'],
               [b'wss://tracker.fastcast.nz']]),
             (b'comment', b'WebTorrent <https://webtorrent.io>'),
             (b'created by', b'WebTorrent <https://webtorrent.io>'),
             (b'creation date', 1490916601),
             (b'encoding', b'UTF-8'),
             (b'info',
              OrderedDict([(b'files',
                            [OrderedDict([(b'length', 140),
                                          (b'path',
                                           [b'Big Buck Bunny.en.srt'])]),
                             OrderedDict([(b'length', 276134947),
                                          (b'path', [b'Big Buck Bunny.mp4'])]),
                             OrderedDict([(b'length', 310380),
                                          (b'path', [b'poster.jpg'])])]),
                           (b'name', b'Big Buck Bunny'),
                           (b'piece length', 262144),
                           (b'pieces', b'Replaced for demonstration purposes')])),
             (b'url-list', [b'https://webtorrent.io/torrents/'])])
```
