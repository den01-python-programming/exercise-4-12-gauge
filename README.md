# Exercise 4.12 Gauge

Create the class `Gauge`. The gauge has the instance variable `value`, a constructor without parameters (sets the initial value of the meter variable to 0), and also the following four methods:

- Method `def increase()` grows the `value` instance variable's value by one. It does not grow the value beyond five.
- Method `def decrease()` decreases the `value` instance variable's value by one. It does not decrease the value to negative numbers.
- Method `def value()` returns the `value` variable's value.
- Method `def full()` returns `True` if the instance variable `value` has the value five. Otherwise, it returns false.

An example of the class in use.

```python
g = Gauge(0)

while not g.full():
    print("Not full! Value: " + str(g.value))
    g.increase()

print("Full! Value: " + str(g.value))
g.decrease()
print("Not full! Value: " + str(g.value))

```

```plaintext
Not full! Value: 0
Not full! Value: 1
Not full! Value: 2
Not full! Value: 3
Not full! Value: 4
Full! Value: 5
Not full! Value: 4
```
