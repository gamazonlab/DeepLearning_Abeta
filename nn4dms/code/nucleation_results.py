import pandas as pd
import collections

import constants as con
import encode as enc


def nucleation_res(args) :
    
    wt_aa = con.DATASETS["nucleation_1iyt"]["wt_aa"]
    wt_ofs = 1
    chrs = con.CHARS[1:]

    variants = []
    num_mutations = []
    score = []

    for i in range(len(wt_aa)):
        for ch in chrs:
            variants.append(wt_aa[i]+str(i+wt_ofs)+ch)
            num_mutations.append(1)
            score.append(0)
        
        
    ds = {"variant": variants, "num_mutations": num_mutations, "score": score}
    ds = pd.DataFrame(data=ds)


    data = collections.defaultdict(dict)
    data["ds"] = ds

    idxs = ds.index.values.tolist()

    set_name = "tune"

    data["idxs"][set_name] = idxs
    data["variants"][set_name] = ds.iloc[idxs]["variant"].tolist()
    data["scores"][set_name] = ds.iloc[idxs]["score"].to_numpy()
    
    data["encoded_data"][set_name] = enc.encode(encoding=args.encoding, variants=data["variants"][set_name],
                                                        wt_aa=wt_aa, wt_offset=wt_ofs)
    
    return data
