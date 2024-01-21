package org.example;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertTrue;

public class CalcTest1 {

    @Test
    public void testSuccess() {
        assertTrue(Calc.add(2, 2) == 4);
    }

    @Test
    public void testFailure() {
        assertTrue(Calc.add(2, 2) == 5);
    }

}
