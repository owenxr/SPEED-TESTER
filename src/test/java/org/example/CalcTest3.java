package org.example;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class CalcTest3 {

    @Test
    public void testFailure1() {
        assertFalse(Calc.add(2, 2) == 4);
    }

    @Test
    public void testFailure2() {
        assertTrue(Calc.add(2, 2) == 5);
    }

}
