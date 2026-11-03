parts = input().split()
values = []
missing = 0
for p in parts:
    if p == "NA":
        missing += 1
    else:
        values.append(float(p))
print("temiz olcmelerin sayi", len(values))
print("boslarin sayi", missing)



print("en kicik olcme", min(values))
print("en boyuk olcme", max(values))
ortaqiymet = round(sum(values) / len(values), 1)
print("orta qiymet", ortaqiymet)