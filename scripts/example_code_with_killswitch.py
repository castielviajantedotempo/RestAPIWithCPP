# Example of a code with kill switch
# For web status you need to have the binary of executable file (getJson)
# You need to create a ref.json file for comparisson with web status
import sys
import compare_status as cs
import read_json_status as rs

def main():
    print("starting your application")
    # The sequence below is for check the status of kill switch and save it on ref.json file
    cs.compare_status()
    ks_status=rs.get_status()
    
    # Comparing the result
    if ks_status != "online":
        print("Exiting Program...")
        sys.exit()
	
	# Enter your program code below
    print("Program is running...")
	
if __name__ == '__main__':
  main()
