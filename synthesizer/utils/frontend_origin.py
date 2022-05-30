class FrontEnd:
    def __init__(self, dict_file):
        self.word2phone = {}
        self.phone2num = {} 
        self.dict_file = dict_file
        self.letters=' aáàạãảăắằặẵẳâấầậẫẩbcdđeéèẹẽẻêếềệễểghiíìịĩỉklmnoóòọõỏôốồộỗổơớờợỡởpqrstuúùụũủưứừựữửvxyýỳỵỹỷj~,.*#_-'
        self.letter2num = {letter:i for i,letter in enumerate(self.letters)}
        self.load_dict()
        self.phone2numeric()
        self.get_syms()
    def get_syms(self):
        return list(self.phone2num.keys())
    def load_dict(self):
        with open(self.dict_file) as fread:
            for line in fread:
                line = line.strip()
                if line.strip():
                    parts = line.split(' ', 1)
                    if len(parts) == 2:
                        self.word2phone[parts[0]] =  parts[1]
    
    def phone2numeric(self):
        phone_lst = sorted(set([_phoneme for word in self.word2phone.values() for _phoneme in word.split()]))
        self.phone2num = {phoneme: i for i, phoneme in enumerate(phone_lst)}


    def text2seq(self, text, letter=True):
        sequence = []
        text = text.replace('\s+',' ').lower()
        if letter:
            for word in text.split(' '):
                #print(word)
                for l in word:
                    if l in self.letter2num.keys():
                        sequence.append(self.letter2num[l])
                sequence.append(self.letter2num[' '])
            sequence[-1] = self.letter2num['#'];
            return sequence
        else:
            sequence.append(self.phone2num['*'])
            
            for word in text.split(' '):
                if word in self.word2phone:
                    #print(word)
                    #if word not in self.word2phone:
                    #    print(word)
                    #    word = 'unk'
                    phones = self.word2phone[word]
                    phones_id = [self.phone2num[i] for i in phones.split()]
                    sequence.extend(phones_id)
                #sequence.append(self.phone2num[' '])
                else:
                    print(word)
            sequence.append(self.phone2num['#'])       
            return sequence

if __name__ == '__main__':
    fontend = FrontEnd('lex.txt')
    #print(fontend.word2phone)
    #print(fontend.phone2num)
    #print(fontend.letter2num)
    
    print(fontend.text2seq('do hôm nay là unknown ba', letter=False))
    print(fontend.get_syms())
