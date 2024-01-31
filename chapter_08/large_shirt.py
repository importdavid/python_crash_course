# 8-4. Large Shirts: pg 136
# MODIFIES 8-3. T-shirt: pg 136

def make_shirt(size='large', text='I love Python'):
    print(f"Printing a {size} size shirt with text: {text}")

make_shirt()
make_shirt('medium')
make_shirt(text='Voldemort Drools!', size='small')