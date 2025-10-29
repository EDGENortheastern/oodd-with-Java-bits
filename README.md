# OOP Example Repository

This project demonstrates **Encapsulation**, one of the four pillars of Object-Oriented Programming (OOP), using both **Java** and **Python**.


---

## 🧩 Java Files

### `Student.java`
Defines a simple `Student` class with two private fields: `name` and `age`.  
These fields are **encapsulated**, meaning they cannot be accessed directly from outside the class.  
Instead, they can be accessed through public **getter** and **setter** methods.

Key ideas:
- Private fields: `private String name;` and `private int age;`
- Public getters: `getName()` and `getAge()`
- Public setters (not shown in screenshot but typically included) ensure data validation

### `EncapsulationDemo.java`
Contains the `main()` method that creates a `Student` object, sets its properties using setters, and prints the results.  
This file demonstrates how to **safely interact** with encapsulated data.

---

## 🐍 `python_example.py`

Provides a Python equivalent of the encapsulation concept using private attributes (with `__name`) and getter/setter methods.

---

## 🧠 Learning Outcome

This repository helps understand:

1. How to define and access private attributes in Java and Python.

# Difference Between Encapsulation in Python and Java

Encapsulation means hiding data inside a class and controlling access through methods.  
Both Python and Java support encapsulation, but they handle it differently.

In **Java**, encapsulation is strict.  
Private variables cannot be accessed directly from outside the class.  
The compiler enforces access control, so a private field can only be read or changed through public getter and setter methods.  
This guarantees that data remains protected and consistent.

In **Python**, encapsulation relies on convention rather than enforcement.  
A variable with two leading underscores (like `__name`) becomes name-mangled to prevent accidental access,  
but it can still be reached deliberately using its mangled name (for example, `_ClassName__name`).  
Python trusts developers to use this responsibly rather than forbidding access outright.

In summary, Java enforces encapsulation through compiler rules,  
while Python uses naming conventions to encourage good practice without strict restriction.
