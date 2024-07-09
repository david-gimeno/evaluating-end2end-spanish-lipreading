import sys
import pandas as pd
from jiwer import wer, cer

pred_path = sys.argv[1]
dest_path = sys.argv[2]

stats = []
# ISO-8859-1
with open(pred_path, "r", encoding="utf-8") as f:
    for line in f:
        ref = line.split("#")[0].strip()
        hyp = line.split("#")[-1].strip()

        l = len(ref.split())
        w = round(wer(ref, hyp) * 100.0, 1)
        c = round(cer(ref, hyp) * 100.0, 1)

        stats.append( (ref, hyp, w, c, l) )

stats_df = pd.DataFrame(stats, columns=["ref", "hyp", "wer", "cer", "nwords"])
stats_df.to_csv(dest_path)
