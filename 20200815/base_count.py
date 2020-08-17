from numpy import array

cont = []
with open("./example.txt", "r") as handle:
    for rec in handle:
        rec = list(rec.strip())
        cont.append(rec)

acont = array(cont)
for iii in range(acont.shape[1]):
    anum = sum(acont[:,iii]=="A")
    tnum = sum(acont[:,iii]=="T")
    gnum = sum(acont[:,iii]=="G")
    cnum = sum(acont[:,iii]=="C")
    print(f"column#{iii}: A={anum}, T={tnum}, G={gnum}, C={cnum}")

recov_string = ""
for iii in range(acont.shape[1]):
    for base in "ATGC":
        if sum(acont[:,iii]==base) <= 2:
            continue
        recov_string += base
print(recov_string)