# arc_upload
This script pushs files to the newriver1 login node using the right-click send to functionality. General idea is that you send a file from a windows machine that is connected to the vt network direcctly (not VPN), then this script generates the submission script. It either uses defualts or you can input parameters yourself. It then submits the job. This script also creates the file structure that is on the windows machine. So if your .k is in C:\Simulations\SPH\run1.k and on arc you have no directories. It creates the path ~/Simulations/SPH and puts the .k file in ./SPH. The job output will also be routed to ./SPH. 
