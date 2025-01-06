import subprocess

def run_curl_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print("Command executed successfully.")
        print("Output:", result.stdout)
    else:
        print("Error executing command.")
        print("Error:", result.stderr)

def get_request():
    curl_command = ["curl", "-X", "GET", "https://httpbin.org/get"]
    run_curl_command(curl_command)

def post_request():
    curl_command = ["curl", "-X", "POST", "-d", "key=value", "https://httpbin.org/post"]
    run_curl_command(curl_command)

def put_request():
    curl_command = ["curl", "-X", "PUT", "-d", "key=value", "https://httpbin.org/put"]
    run_curl_command(curl_command)

def delete_request():
    curl_command = ["curl", "-X", "DELETE", "https://httpbin.org/delete"]
    run_curl_command(curl_command)

if __name__ == "__main__":
    get_request()
    post_request()
    put_request()
    delete_request()
