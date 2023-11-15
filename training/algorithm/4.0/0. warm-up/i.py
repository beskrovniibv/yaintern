#! usr/bin/python

# I. Правильная скобочная последовательность

class Solution:
    def solve(self, value: str) -> bool:
        if not value:
            return False
        s = []
        for v in value:
            if v in ('(', '[', '{'):
                s.append(v)
            elif v == ')':
                if not s:
                    return False
                e = s.pop()
                if e != '(':
                    return False
            elif v == ']':
                if not s:
                    return False
                e = s.pop()
                if e != '[':
                    return False
            elif v == '}':
                if not s:
                    return False
                e = s.pop()
                if e != '{':
                    return False
        return not s


if __name__ == ('__main__'):
    v = input()
    solver = Solution()
    print('yes') if solver.solve(v) else print('no')
