"""6-4. Glossary 2: pg 104
    Now that you know how to loop through a dictionary, clean up the code from 
Exercise 6-3 (page 99) by replacing your series of print() calls with a loop 
that runs through the dictionary's keys and values. When you're sure that your 
loop works, add five more Python terms to your gloassary. When you run your 
program again, these new words and meainings should automatically be included 
in the output."""


glossary = {
    'Python': 'An object-oriented, dynamically-typed programming language.',
    'loop': 'A block of code meant to be iterated more than once.',
    'dictionary': 'A list of key-value pairs.',
    'list': 'An iterable list of related or unrelated objects.',
    'tuple': 'An unmutable list of objects.',
    'bug': 'A small, squishable, but not deservedly, creature.',
    'library': "A building that house many books.",
    'chair': "You sit on it, but what is its purpose, really?",
    'food': 'For eating.',
    'final': 'The last word.',
}

for word, definition in glossary.items():
    print('\n', word, '\n\t', definition)