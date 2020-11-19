### Turn input json into python script and run it
import json
 
def expand_children(n, level=0):
    return '\n'.join(
        [expand_node(n2, level)
         for n2 in n.get('children',[])]
    )

def expand_function(n, level=0):
    return (level*" ")+f"def {n['name']} ():\n"+expand_children(n, level+1)

def expand_arguments(n):
    return ",".join([
        repr(arg)
        for arg in n['arguments']
    ])

def expand_call(n, level=0):
    arguments = expand_arguments(n)
    return (level*" ")+f"{n['name']}({arguments})"

def expand_node(n, level=0):
    if n['type'] == 'function':
        return expand_function(n, level)
    elif n['type'] == 'call':
        return expand_call(n, level)

def expand_nodes(nodes, level=0):
    return "\n".join([
        expand_node(n, level)
        for n in nodes
    ])

def run():
    with open("test_file.json") as f:
        code = json.loads(f.read())
        print('expanding')
        s = expand_nodes(code)
        print(s)
        exec(s)

run()
