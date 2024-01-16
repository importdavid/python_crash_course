# 8-14. Cars: pg 149

# Import pprint for nicer display
from pprint import pprint as pp

def build_profile(manufacturer, model, **kwargs):
    """Build a dictionary containing evertyhing we know about a car."""
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

car = build_profile('Ford', 'Focus',
                    color='blue',
                    wheels=4,
                    year=2009,)

pp(car)