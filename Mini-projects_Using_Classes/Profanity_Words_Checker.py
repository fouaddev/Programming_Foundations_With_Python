import urllib

def read_text():
    text = open("C:\Users\hyg\.PyCharmCE2017.2\config\scratches\scratch.txt")
    content = text.read()
    print(content)
    text.close()
    check_profanity(content)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    result = connection.read()
    connection.close()
    if "true" in result:
        print("Profanity alert!")
    elif "false" in result:
        print("This text has no curse words.")
    else:
        print("The program could not scan the text properly...")

read_text()
