import sys
from pathlib import Path
from .transpile import transpile

def create_new_file(filename):
    if not filename.endswith(".uwu"):
        filename += ".uwu"
    path = Path(filename)
    if path.exists():
        print(f"Error: {filename} alread exists.")
        return
    template = '''# Uwulang uwu template

fwunc hewwo(name) {
  pwint("hewwo, " + name + "!")
  if twue {
    pwint("this is an if bwock")
  } 
  ewse {
    pwint("this won't wun")
  }
}

hewwo("usew")
'''
    path.write_text(template)
    print(f"Created new uwu file: {filename}")

def run_file(filename):
    if not Path(filename).exists():
        print(f"Error: file '{filename}' not found.")
        return
    src = Path(filename).read_text()
    py_code = transpile(src)

    try:
        exec(py_code, {})
    except Exception as e:
        print(f"Runtime error: {e}")

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print(" uwu new <filename.uwu>  # create new uwu file")
        print(" uwu run <filename.uwu>  # run uwu file")
        return
    cmd = sys.argv[1].lower()
    filename = sys.argv[2]

    if cmd == "new":
        create_new_file(filename)
    elif cmd == "run":
        run_file(filename)
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
