#!/bin/bash
#!/bin/bash
source /Users/rwcuffney/.venv/LN_API_library_venv/bin/activate

# Keep the terminal open
bash
/Users/rwcuffney/.venv/LN_API_library_venv/Python_pkg/lexisnexisapi/python3 -m build
/Users/rwcuffney/.venv/LN_API_library_venv/Python_pkg/lexisnexisapi/python3 -m twine upload dist/* 
