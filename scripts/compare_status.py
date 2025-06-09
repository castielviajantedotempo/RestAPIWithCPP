import subprocess
import json

def execute_binary(binary_path, *args):
    """Executes a binary and returns its output.

    Args:
        binary_path (str): The path to the executable binary.
        *args: Additional arguments to pass to the binary.

    Returns:
        str: The output of the binary execution.
    """
    try:
        result = subprocess.run([binary_path, *args], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error executing binary: {e.stderr}"

def compare_status():
    web=""
    local_file=""
    binary_path = "./getJson" # Replace with the actual path
    output = execute_binary(binary_path, "--arg1", "value1", "--arg2", "value2")

    web=json.loads(output)
    #print(web["status"])


    # Open and read the JSON file
    with open('ref.json', 'r') as file:
        local_file = json.load(file)
    file.close()
    #print(local_file["status"])
    
    if web != local_file:
        #print("They are differents")
        with open('ref.json', 'w') as file:
            json.dump(web, file, indent=4)
        file.close()
    else:
        print("ok")

