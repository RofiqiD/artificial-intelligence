browse = "Pada malam hari terlihat bintang bintang di jendela kamar andi lalu ibu andi masuk kamar andi untuk memberi susu agar tidur nya nyenyak."
words = browse.lower().replace(".", "").split()
counts = {}
count = 0

for i in range(len(words)):
    kata1 = words[i]
    for j in range(len(words)):
        kata2 = words[j]
        if kata1 == kata2:
            count += 1
    counts[kata1] = count
    count = 0

print(counts)
