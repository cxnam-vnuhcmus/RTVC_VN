# from synthesizer.utils.text import text_to_sequence
# import numpy as np

# text = "Nhiều quy định cũ liên quan đến du khách nước ngoài nhập cảnh vào Việt Nam đang được đề xuất gỡ bỏ. Điều này sẽ giúp Việt Nam có thêm sức hút."
# inputs = text_to_sequence(text.strip(), "lex_vinphon")
# print(inputs)
# result = ' '.join([str(cid) for cid in inputs])
# print(result)

# textlist = [int(cid) for cid in result.split(' ')]
# print(textlist)
# textnp = np.asarray(textlist).astype(np.int32)
# print(textnp)

# from viphoneme import syms, vi2IPA_split


# text = text.replace('\s+',' ').lower()
# print(text)
# phon = vi2IPA_split(text,"/")
# phon = phon.split("/")[1:]
# print(phon)

from vinorm import TTSnorm
from tqdm import tqdm

with open('./transcript_all_new.txt', 'wt') as f:
    for line in tqdm(open('datasets_fpt/fpt/transcript_all.txt', 'rt').readlines()):
        parts = line.strip().split('\t')
        text = TTSnorm(parts[1])
        text = text.replace('.', '')
        new_transcript = '{}\t{}\n'.format(parts[0], text)
        f.write(new_transcript)