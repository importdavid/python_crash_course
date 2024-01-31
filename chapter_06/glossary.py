"""6-3. Glossary: pg 99
    A Python dictionary can be used to model an actual dictionary. However, 
to avoid confusion, let's call it a glossary.
    Think of five programming words you've learned about in the previous 
chapters. Use these words as the keys in your glossary, and store their 
meainings as values.
    Print each word and its meaning as neatly formatted output. You might 
print the word followed by a colon and then its meaning, or print the word 
on one line and then print its meaning indented on a second line. Use the 
newline character (\n) to insert a blank line between each word-meaning pair 
in your output."""

glossary = {
    'Python': 'An object-oriented, dynamically-typed programming language.',
    'loop': 'A block of code meant to be iterated more than once.',
    'dictionary': 'A list of key-value pairs.',
    'list': 'An iterable list of related or unrelated objects.',
    'tuple': 'An unmutable list of objects.',
}

for word, definition in glossary.items():
    print('\n', word, '\n\t', definition)
