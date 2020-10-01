s = input("Enter your Name: ")
change = {'a':'4','b':'8','c':'¢','e':'3','g':'9','h':'#','i':'!','j':'√','o':'0','p':'9','r':'®','s':'5','t':'7','v':'√','y':'¥'}
print("".join([change[c.lower()] if c.lower() in change.keys() else c for c in s ]))
