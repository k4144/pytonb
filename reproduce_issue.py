import os
import subprocess
import sys
import venv
import shutil

def run_command(cmd, cwd=None, env=None):
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {result.stderr}")
    return result

def reproduce():
    base_dir = os.getcwd()
    temp_dir = os.path.join(base_dir, "xxx_repro_xxx")
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)

    print(f"Created temp dir: {temp_dir}")

    # Copy necessary files
    shutil.copytree("src", os.path.join(temp_dir, "src"))
    shutil.copytree("tests", os.path.join(temp_dir, "tests"))
    if os.path.exists("data"):
        shutil.copytree("data", os.path.join(temp_dir, "data"))
    shutil.copy("pyproject.toml", temp_dir)
    shutil.copy("README.md", temp_dir)
    shutil.copy("LICENSE", temp_dir)

    # Create venv
    venv_dir = os.path.join(temp_dir, ".venv")
    venv.create(venv_dir, with_pip=True)
    
    bin_dir = os.path.join(venv_dir, "bin")
    pip_cmd = os.path.join(bin_dir, "pip")
    pytest_cmd = os.path.join(bin_dir, "pytest")

    env = os.environ.copy()
    env["PATH"] = f"{bin_dir}:{env['PATH']}"

    # Install dependencies and package (non-editable, like CI)
    print("Installing package...")
    run_command([pip_cmd, "install", ".", "pytest", "pytest-cov"], cwd=temp_dir, env=env)

    # Run with CI-like arguments (--cov=src)
    print("\n--- Running with --cov=src (CI-like) ---")
    res_src = run_command([pytest_cmd, "--cov=src", "tests"], cwd=temp_dir, env=env)
    with open("result_src.txt", "w") as f:
        f.write(res_src.stdout)
        f.write(res_src.stderr)

    # Run with pyproject.toml arguments (--cov=pytonb)
    print("\n--- Running with --cov=pytonb (Local-like/Proposed Fix) ---")
    res_pkg = run_command([pytest_cmd, "--cov=pytonb", "tests"], cwd=temp_dir, env=env)
    with open("result_pkg.txt", "w") as f:
        f.write(res_pkg.stdout)
        f.write(res_pkg.stderr)

    # Cleanup
    # shutil.rmtree(temp_dir)

if __name__ == "__main__":
    reproduce()
