# 100 days of python
## General
- According to the quiz, I can start at day 32. However, I wanna try some GUI stuff, so may start earlier
  - Starting at _Day 15_, as it is intermediate level and I want to practice OOP.

## Day 1: Lesson 15
- Made the coffee machine code
- Learnt that
  - Python assignments are by _reference_, not a copy!
  - List comprehension can be more lines than simple loops.
  - Breaking out of a "second level loop" is very hard; it's better to refactor the code.
- Improvements
  - Also, make more and smaller functions. They simplify everything
  - Work dirtier and faster.

## Day 2: Lesson 16
- Focuses on OOP (which I already know)
  - Skimmed through lectures just in case, but nothing too interesting.
- Task: Create the coffee machine code based on the provided class.
  - Look at the original project goals.
  - [Documentation](https://docs.google.com/document/d/e/2PACX-1vTragRHILyj76AvVgpWeOlEaLBXoxPM_43SdEyffIKtOgarj42SoSAsK6LwLAdHQs2qFLGthRZds6ok/pub)
- Learnt:
  - Not much, it was just nice OOP practice.
  - OOP is so much easier and nicer; use it more.

## Day 3: Lesson 17
- Quiz game
- [API database example] (https://opentdb.com/api_config.php)
- Learnt:
  - _SOMETHING IMPORTANT_: If working in sub-directories and importing modules, start with `.` so that intellisense knows where they are.
    - I.e. `import .custom_module` instead of `import custom_module`
    - Works when it wants to...
  - Use `\` when you want to break up a statement into multiple lines.
  - Break. It. Up. It's more useful in the long run.
  - Learnt how to deal with APIs using the `request` module.
    - Also, with a bit of decoding.

# Day 4: Lesson 18
- Topic: Turtle graphics & Tuples
- Notes:
  - Turtle graphics color uses a range of 0 to 1 unless specified in `scree.colormode()`.
  - `colorgram` module: extract colors from image
  - Nested list comprehension: It is fairly possible to do it, but it's a bit counter-untuitive.

```python
# Example of flattening a 2D array
list_array = [(1,2,3), (4,5,6)]
flattened = list()

for inner_list in list_array:
  for number in inner_list:
    flattened.append(number)

# This is equivalent to
flattened = [number for inner_list in list_array for number in inner_list]

# Which basically is:
list = [inner_elem for outer_element in outer_list for inner_elem in inner_list]

# You can also play around though:
colors = [tuple([color.rgb[i] for i in range(3)]) for color in colors]
```
  - List comprehension & If/Else
    - Only `if`: `[f(x) for x in list if condition]`
    - `if` and `else`: `[f(x) if condition1 else f2(x) for x in list]`