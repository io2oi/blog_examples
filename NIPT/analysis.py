import sys
from numpy import array, median

def get_chr21(autosome, refchrn: str):
    refidx = int(refchrn.replace("chr","")) - 1
    chr21idx = 20
    ref_val = autosome[refidx]
    chr21_val = autosome[chr21idx]
    print(f"ref chr{refidx+1}: {ref_val}")
    print(f"chr21: {chr21_val}")
    res = chr21_val/ref_val
    return res

def norm_med(autosome):
    medians = median(autosome, axis=0)
    res = autosome/medians
    return res

def norm_len(autosome):
    chr_len = array([249250621, 243199373, 198022430, 191154276, 180915260, 171115067, 159138663, 146364022, 141213431, 135534747, 135006516, 133851895, 115169878, 107349540, 102531392, 90354753, 81195210, 78077248, 59128983, 63025520, 48129895, 51304566])
    res = autosome/chr_len.reshape(22,1)
    return res

def printout(autosome, header):
    print("\t".join(header))
    for chrn, rec in enumerate(list(autosome)):
        tmplist = [f"{chrn+1}"]
        tmplist.extend(list(rec))
        tmplist = [f"{v:.3}" for v in tmplist]
        print("\t".join(tmplist))

def main(in_file: str):
    cont = []
    with open(in_file, "r") as handle:
        for rec in handle:
            cols = rec.strip().split()
            if cols[0] == "chrn":
                header = cols
                continue
            cont.append([int(v) for v in cols[1:]])
    cont = array(cont)
    autosome = cont[0:22,:]
    # print(autosome)
    autosome = norm_len(autosome)
    # print(autosome)
    autosome = norm_med(autosome)
    printout(autosome, header)
    res = get_chr21(autosome, refchrn="chr9")
    print(header[1:])
    print(res)


if __name__ == "__main__":
    IN_FILE = sys.argv[1]
    main(IN_FILE)
