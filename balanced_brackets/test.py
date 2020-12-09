import unittest
import run

class test_cases(unittest.TestCase):

    def test1_ping(self):

        for item in TO_TEST:

            response = run.is_valid_bracket( item['inp_str'] )

            print(item['inp_str'], response, '?=', item['is valid'])
            self.assertEqual(response, item['is valid'])

TO_TEST = [
    {
        'inp_str': '()',
        'is valid': 'valid'
    },
    {
        'inp_str': '[]',
        'is valid': 'valid'
    },
    {
        'inp_str': '[()]',
        'is valid': 'valid'
    },
    {
        'inp_str': '[({})]',
        'is valid': 'valid'
    },
    {
        'inp_str': '[nosds(hi)]',
        'is valid': 'valid'
    },
    {
        'inp_str': 'asdg)[()]',
        'is valid': 'invalid'
    },
    {
        'inp_str': '}{}',
        'is valid': 'invalid'
    },
    {
        'inp_str': '{{{{where is [this,]}}oo}}',
        'is valid': 'valid'
    },
    {
        'inp_str': '(}{)',
        'is valid': 'invalid'
    },
    {
        'inp_str': '()[{(})]',
        'is valid': 'invalid'
    },
    {
        'inp_str': 'function thing(inp) {return inp/2};',
        'is valid': 'valid'
    },
    {
        'inp_str': 'asdgsdga(jsidgh{]}asdg[)',
        'is valid': 'invalid'
    },
    {
        'inp_str': '({(}))',
        'is valid': 'invalid'
    },
    {
        'inp_str': '()[]{asgdasdg[]([]{})}',
        'is valid': 'valid'
    },
    {
        'inp_str': '()[]{[]([]{})}({(}))',
        'is valid': 'invalid'
    },
    {
        'inp_str': 'sum = (9 + (8/(TOTAL//3()))',
        'is valid': 'invalid'
    },
]

if __name__ == '__main__':
    unittest.main()
