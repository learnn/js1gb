import os

if not os.path.exists('./jscodefiles'):
    os.makedirs('./jscodefiles')

# Run this script in the directory containing .js and .py repos
# Ensure that the jscodefiles exist for dumping unique .js files
# Likewise for pythoncodefiles change the dest dir name in line 10
for root, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith(('.js')):
            filepath = os.path.join(root, filename)
            os.rename(filepath, './jscodefiles/'+filename)