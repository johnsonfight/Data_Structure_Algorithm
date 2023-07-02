class Solution:
    def isValid(self, s: str) -> bool:
        valid_p = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        tmp_l = ['']

        for i in s:
            if i in valid_p.keys():
                tmp_l.append(i)
            elif tmp_l[-1] in valid_p.keys() and (i == valid_p[tmp_l[-1]]):
                tmp_l.pop()
            else:
                return False


        if len(tmp_l) == 1:
            return True
        else:
            return False