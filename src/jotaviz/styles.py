"""jotaviz - A collection of plotting functions and styles used at jota.info"""

import matplotlib.pyplot as plt
from jotaviz import templates
from jotaviz import cycles

__all__ = ['Style']

class Style:
    def __init__(self, style_name="default"):
        '''
        style_name: name of the style to be applied
        '''
        if style_name in plt.style.available:
            self.style = plt.style.use(style_name)
        if style_name in templates.available:
            stylesheet = self.get_template(style_name)
            self.style = plt.style.use(stylesheet)
        else:
            print('WARNING: Given name |{}| is not a valid style name. Therefore matplotlib default will be used'.format(style_name))
            self.style = plt.style.use("default")
    
    def get_template(self,template_name):
        if template_name in templates.available:
            attribute = getattr(templates,template_name)
            return attribute
        else:
            print('WARNING: Given name |{}| is not a valid template name. Therefore matplotlib default will be used'.format(template_name))
            return 'default'
    
    def cycle(self,cycle_name):
        '''
        cycle_name: name of the cycle to be cycled
        TODO: A better else clause
        '''
        if cycle_name in cycles.available:
            method_to_call = getattr(cycles, cycle_name)
            return method_to_call()
        else:
            print('WARNING: Given name |{}| is not a valid cycle name. Therefore mplstyle default cycle will be used'.format(cycle_name))
            # Reurn error instead? 