python
import os
import subprocess

def generate_docs():
    # Generate documentation using Sphinx
    subprocess.run(["sphinx-apidoc", "-o", "docs/source", "your_module"])
    subprocess.run(["sphinx-build", "-b", "html", "docs/source", "docs/build/html"])

def main():
    generate_docs()
    print("Documentation generated successfully.")

if __name__ == "__main__":
    main()
