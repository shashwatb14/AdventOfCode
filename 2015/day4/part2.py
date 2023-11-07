from hashlib import md5

x = 0
md5hash = md5(f"iwrupvqb{x}".encode("utf-8")).hexdigest()

while md5hash[:6] != "000000":
    md5hash = md5(f"iwrupvqb{x}".encode("utf-8")).hexdigest()
    if md5hash[:6] == "000000": break
    x += 1

print(x)

# answer: 9958218