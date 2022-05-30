from viphoneme import syms, vi2IPA_split
from synthesizer.utils.frontend_origin import FrontEnd

symbols = syms

_symbol_to_id = {s: i for i, s in enumerate(symbols)}
_id_to_symbol = {i: s for i, s in enumerate(symbols)}



def sequence_to_text(sequence):
    
    result = ''
    for symbol_id in sequence:
        if symbol_id in _id_to_symbol:
            result += _id_to_symbol[symbol_id]     
    return result

def text_to_sequence(text, cleaner_names):
    if cleaner_names == "lex_vinphon":
        frontend = FrontEnd("synthesizer/utils/lex.txt")
        return frontend.text2seq(text, letter=False)
    elif cleaner_names == "lex_viphoneme":
        frontend = FrontEnd("synthesizer/utils/lexphon.txt")
        return frontend.text2seq_viphoneme(text, letter=False)
    elif cleaner_names == "raw_viphoneme":
        sequence = []
        text = text.replace('\s+',' ').lower()
        phon = vi2IPA_split(text,"/")
        phon = phon.split("/")[1:]

        eol = -1
        for i,p in reversed(list(enumerate(phon))):
            if p not in ["..",""," ",".","  "]:
                eol = i
                break
        phones = phon[:i+1]+[" ","."]
        phones_id =[]
        for i in phones:
            if i in _symbol_to_id:
                phones_id.append(_symbol_to_id[i])
                #phones_id = [_symbol_to_id[i] for i in phones]
        sequence.extend(phones_id)  
        
        return sequence
    elif cleaner_names == "prenorm_viphoneme":
        sequence = []
        phon = text.split("/")[1:]

        eol = -1
        for i,p in reversed(list(enumerate(phon))):
            if p not in ["..",""," ",".","  "]:
                eol = i
                break
        phones = phon[:i+1]+[" ","."]
        phones_id =[]
        for i in phones:
            if i in _symbol_to_id:
                phones_id.append(_symbol_to_id[i])
                #phones_id = [_symbol_to_id[i] for i in phones]
        sequence.extend(phones_id)

        return sequence
    return ""

# from synthesizer.utils.symbols import symbols
# from synthesizer.utils import cleaners
# import re


# # Mappings from symbol to numeric ID and vice versa:
# _symbol_to_id = {s: i for i, s in enumerate(symbols)}
# _id_to_symbol = {i: s for i, s in enumerate(symbols)}

# # Regular expression matching text enclosed in curly braces:
# _curly_re = re.compile(r"(.*?)\{(.+?)\}(.*)")


# def text_to_sequence(text, cleaner_names):
#     """Converts a string of text to a sequence of IDs corresponding to the symbols in the text.

#       The text can optionally have ARPAbet sequences enclosed in curly braces embedded
#       in it. For example, "Turn left on {HH AW1 S S T AH0 N} Street."

#       Args:
#         text: string to convert to a sequence
#         cleaner_names: names of the cleaner functions to run the text through

#       Returns:
#         List of integers corresponding to the symbols in the text
#     """
#     sequence = []

#     # Check for curly braces and treat their contents as ARPAbet:
#     while len(text):
#         m = _curly_re.match(text)
#         if not m:
#             sequence += _symbols_to_sequence(_clean_text(text, cleaner_names))
#             break
#         sequence += _symbols_to_sequence(_clean_text(m.group(1), cleaner_names))
#         sequence += _arpabet_to_sequence(m.group(2))
#         text = m.group(3)

#     # Append EOS token
#     sequence.append(_symbol_to_id["~"])
#     return sequence


# def sequence_to_text(sequence):
#     """Converts a sequence of IDs back to a string"""
#     result = ""
#     for symbol_id in sequence:
#         if symbol_id in _id_to_symbol:
#             s = _id_to_symbol[symbol_id]
#             # Enclose ARPAbet back in curly braces:
#             if len(s) > 1 and s[0] == "@":
#                 s = "{%s}" % s[1:]
#             result += s
#     return result.replace("}{", " ")


# def _clean_text(text, cleaner_names):
#     for name in cleaner_names:
#         cleaner = getattr(cleaners, name)
#         if not cleaner:
#             raise Exception("Unknown cleaner: %s" % name)
#         text = cleaner(text)
#     return text


# def _symbols_to_sequence(symbols):
#     return [_symbol_to_id[s] for s in symbols if _should_keep_symbol(s)]


# def _arpabet_to_sequence(text):
#     return _symbols_to_sequence(["@" + s for s in text.split()])


# def _should_keep_symbol(s):
#     return s in _symbol_to_id and s not in ("_", "~")
