package org.example;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class CalcTest2 {

    @Test
    public void testSuccess1() {
        assertTrue(Calc.add(2, 2) == 4);
    }

    @Test
    public void testSuccess2() {
        assertFalse(Calc.add(2, 2) == 5);
    }

}
