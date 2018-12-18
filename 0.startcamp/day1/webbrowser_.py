import webbrowser

keywords = [
    '여행',
    '맛집',
    '영화',
    'bts'
]

for keyword in keywords:
    url = 'https://google.com/search?q=' + keyword
    webbrowser.open_new(url)
