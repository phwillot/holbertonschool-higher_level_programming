#!/usr/bin/python3
"""
Module for matrix_mul function
"""


def matrix_mul(m_a, m_b):

    msg1 = "m_a should contain only integers or floats"
    msg2 = "m_b should contain only integers or floats"
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    for elements in m_a:
        if type(elements) != list:
            raise TypeError("m_a must be a list of lists")
    
    for elements in m_b:
        if type(elements) != list:
            raise TypeError("m_b must be a list of lists")
    
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    for elements in m_a:
        if not isinstance(all(elements), (int, float) == False):
            raise TypeError(msg1)
    
    for elements in m_b:
        if not isinstance(all(elements), (int, float) == False):
            raise TypeError(msg2)
    
