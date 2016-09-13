# this is short enough that it really should be in side of the `main.py`
# but I put it here as a quick and easy function example
def read_file(file_name):
    with open(file_name, 'r') as readme_file:
        content = readme_file.read()
    return content
