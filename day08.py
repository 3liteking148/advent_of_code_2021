import re

def debug_print(n, x):
    pass
    #print("Value of {} is {}".format(n, x))

if __name__ == '__main__':
    with open('day8.txt') as inp:
        all = inp.read()
        test = re.findall(r'((?:\w+\s?){10})\s\|\s*((?:\w+\s?){4})\n', all)

        # digits 1, 7, 4, 8, respectively
        total = sum((len(re.findall(r'(\b(?:\w{2,4}|\w{7})\b)', t[1])) for t in test))

        # part 1 answer
        print(total)

        # num of segments per digit: 6, 2, 5, 5, 4, 5, 6, 3, 7, 6
        # solution without brute forcing (brute forcing also works)
        plswork = 0
        for t in test:
            out = [''] * 10
            case = t[0]

            # 1, 7, 4, 8 are known digits
            out[1] = re.search(r'\b\w{2}\b', case)[0]
            out[7] = re.search(r'\b\w{3}\b', case)[0]
            out[4] = re.search(r'\b\w{4}\b', case)[0]
            out[8] = re.search(r'\b\w{7}\b', case)[0]

            debug_print(1, out[1])
            debug_print(7, out[7])
            debug_print(4, out[4])
            debug_print(8, out[8])

            # a is the segment present in 7 but not in 1
            a = re.search(r'[^{}]'.format(out[1]), out[7])[0]

            # the remaining digits have either 5 or 6 segments
            case5 = ' '.join(re.findall(r'(\b\w{5}\b)', case))
            case6 = ' '.join(re.findall(r'(\b\w{6}\b)', case))

            # 9 is the only 6-segment number with a, the segments of 4, and an one unknown segment
            known_9 = a+out[4] # 5 segments are known
            unknown_9 = re.findall(r'[^{}]'.format(known_9), 'abcdefg')

            # ony one of the 2 unknown segments can appear
            out[9] = re.search(r'\b[{}]*(?:{}|{})[{}]*\b'.format(known_9, *unknown_9, known_9), case6)[0]
            debug_print(9, out[9])

            # g is the "unknown segment" segment in 9
            g = re.search(r'\w*([^{}])\w*'.format(a+out[4]), out[9]).groups()[0]

            # e is the only segment in 8 that is not in 9
            e = re.search(r'\w*([^{}])\w*'.format(out[9]), out[8]).groups()[0]

            # 2 is the only 5-segment digit with e
            out[2] = re.search(r'\b\w*{}\w*\b'.format(e), case5)[0]
            debug_print(2, out[2])

            # 3 is the only 5-segment digit with 7, 'g', and 1 unknown segment
            known_3 = g+out[7]
            unknown_3 = re.findall(r'[^{}]'.format(known_3), 'abcdefg')

            # only one of the 3 unknown segments can appear
            out[3] = re.search(r'\b[{}]*(?:{}|{}|{})[{}]*\b'.format(known_3, *unknown_3, known_3), case5)[0]
            debug_print(3, out[3])

            # 5 is the remaining 5-segment digit
            out[5] = re.search(r'\b(?!{}|{})\w+\b'.format(out[2], out[3]), case5)[0]
            debug_print(5, out[5])

            # 'c' is the only segment in 3 not in 5
            c = re.search(r'\w*([^{}])\w*'.format(out[5]), out[3]).groups()[0]

            # 6 is the only 6-segment digit without 'c'
            out[6] = re.search(r'\b[^{}\W]+\b'.format(c), case6)[0]
            debug_print(6, out[6])

            # 0 is the last unknown digit
            out[0] = re.search(r'\b(?!{}|{})\w+\b'.format(out[6], out[9]), case6)[0]
            debug_print(0, out[0])

            output_val = re.findall(r'\b\w+\b', t[1])
            x = 0
            for o in output_val:
                x *= 10
                regex = re.compile(r'^[{}]{{{}}}$'.format(o, len(o)))

                while x % 10 < 10 and regex.match(out[x % 10]) == None:
                    x += 1

            debug_print("four digit output value", x)
            plswork += x

        # part 2 answer
        print(plswork)
