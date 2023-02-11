def add_songs(*args):
    songs = {}
    result = []
    for x in args:
        if x[0] not in songs:
            songs[x[0]] = []
        songs[x[0]].append(x[1])

    for k, v in songs.items():
        result.append([f'- {k}'])
        for value in v:
            result.append("\n".join(value)) if value else None

    result_to_string = ["".join(x) for x in result]
    return "\n".join(result_to_string)

print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))