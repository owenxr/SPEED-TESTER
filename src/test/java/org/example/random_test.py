import random
from io import TextIOBase


TESTS_PER_CLASS = 100
NUM_CLASSES = 2000
MAX = 2147483647
MIN = -2147483648


def create_random_test(n: int, f: TextIOBase) -> None:
    """Creates a random test with test id n"""
    sum_ab = MIN-1
    while sum_ab < MIN or sum_ab > MAX:
        a = random.randint(MIN, MAX)
        b = random.randint(MIN, MAX)
        sum_ab = a + b

    f.write(f'@Test public void testRandom{n}() ' + '{')
    f.write(f'assertTrue(Calc.add({a}, {b}) == {sum_ab});' + '}\n')


def create_random_test_class(n: int) -> None:
    """Creates a random test class with class id n"""
    with open(f'RandomCalcTest{n}.java','w') as f:
        f.write("""package org.example;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;\n""")
        
        f.write(f'public class RandomCalcTest{n}' + '{\n')
        for i in range(TESTS_PER_CLASS):
            create_random_test(i, f)
        f.write('}\n')


def main():
    for i in range(NUM_CLASSES):
        create_random_test_class(i)

main()
