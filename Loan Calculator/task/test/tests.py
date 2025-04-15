from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult
import re

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class LoanCalcTest(StageTest):
    def generate(self):
        return [
            TestCase(
                stdin='1000\nm\n200',
                attach=5,
            ),
            TestCase(
                stdin='1000\nm\n150',
                attach=7,
            ),
            TestCase(
                stdin='1000\nm\n1000',
                attach=1,
            ),
            TestCase(
                stdin='1000\np\n10',
                attach=100,
            ),
            TestCase(
                stdin='1000\np\n9',
                attach=['112', '104'],
            ),
            TestCase(
                stdin='1350\nm\n140',
                attach=10,
            ),
            TestCase(
                stdin='300\nm\n400',
                attach=1,
            ),
            TestCase(
                stdin='5555\np\n11',
                attach=505,
            ),
            TestCase(
                stdin='5576\np\n10',
                attach=['558', '554'],
            ),
        ]

    def check(self, reply, attach):
        reply = reply.lower()
        if isinstance(attach, int):
            if not any(char.isdigit() for char in reply):
                return CheckResult.wrong('Your program didn\'t print the number of months required to replay the loan.')

            # If attach value is more than 100, the int in attach represents the monthly payment, 'p'
            if attach >= 100 and str(attach) not in reply:
                return CheckResult.wrong('Incorrect monthly payment.\n'
                                         f'Expected: {attach}')
            elif str(attach) not in reply:
                return CheckResult.wrong('Incorrect number of months required to replay the loan.\n'
                                         f'Expected: {attach}')

        if isinstance(attach, list):
            if attach[0] not in reply or attach[1] not in reply:
                numbers = re.findall(r'[-+]?(\d*\.\d+|\d+)', reply)
                if len(numbers) == 0:
                    return CheckResult.wrong(f'The correct monthly payment is {attach[0]}, and the last payment is '
                                             f'{attach[1]}, but your program didn\'t print these values.')
                elif len(numbers) == 1:
                    return CheckResult.wrong(f'The correct monthly payment is {attach[0]}, and the last payment is '
                                             f'{attach[1]}, but there is only {numbers[0]} in your output.')
                else:
                    return CheckResult.wrong(f'The correct monthly payment is {attach[0]}, and the last payment is '
                                             f'{attach[1]}, but there are {numbers[0]} and {numbers[1]} in your output.')

        return CheckResult.correct()


if __name__ == '__main__':
    LoanCalcTest('creditcalc.creditcalc').run_tests()