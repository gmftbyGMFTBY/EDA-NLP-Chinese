# Easy data augmentation techniques for text classification
# Jason Wei and Kai Zou
# Fixed by GMFTBY, 2019.8.3

from eda import *
import argparse
from tqdm import tqdm

# generate more data with standard augmentation
def gen_eda(input_file, output_file, alpha, num_aug=9):
    print('[!] Begin to generate the augmentation data')
    writer = open(output_file, 'w')
    
    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        print(f'[!] Total lines: {len(lines)}')
        pbar = tqdm(enumerate(lines))
        for i, line in pbar:
            sentence = line.strip()
            aug_sentences = eda(sentence, 
                                alpha_sr=alpha, 
                                alpha_ri=alpha, 
                                alpha_rs=alpha, 
                                p_rd=alpha, 
                                num_aug=num_aug)
            for aug_sentence in aug_sentences:
                f.write(aug_sentence + '\n')
            pbar.set_description(f'Progress: {i} / {len(lines)}, {100 * round(i / len(lines), 4)}%')
            
        pbar.close()
    print(f"[!] Over. EDA-Chinese for {input_file} to {output_file} with num_aug={str(num_aug)}")


if __name__ == "__main__":
    # args parse
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, type=str, 
                    help="input file of unaugmented data")
    ap.add_argument("--output", required=False, type=str, 
                    help="output file of unaugmented data")
    ap.add_argument("--num_aug", required=False, type=int, default=5, 
                    help="number of augmented sentences per original sentence")
    ap.add_argument("--alpha", required=False, type=float, default=0.1,
                    help="percent of words in each sentence to be changed")
    args = ap.parse_args()
    
    output = None
    if args.output:
        output = args.output
    else:
        from os.path import dirname, basename, join
        output = join(dirname(args.input), 'eda_' + basename(args.input))

    # number of augmented sentences to generate per original sentence
    num_aug = args.num_aug
    alpha = args.alpha
    
    # generate augmented sentences and output into a new file
    gen_eda(args.input, output, alpha=alpha, num_aug=num_aug)