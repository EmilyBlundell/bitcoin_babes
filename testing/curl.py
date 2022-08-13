import os 

tests = """
# get header
curl -i http://127.0.0.1:5000

curl -i http://127.0.0.1:5000/leader/selection
# new

curl -i -H "Content-Type: application/json" -X POST -d  '{"investor_first_name":"Promise"}' http://127.0.0.1:5000/new
"""
for line in tests.strip().split('\n'):
    print('\n{}'.format(line))
    if not line.startswith('#'):
        cmd = line.strip() 
        os.system(cmd)
