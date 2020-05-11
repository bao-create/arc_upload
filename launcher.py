import pysftp
import sys
import string


cnopts = pysftp.CnOpts(knownhosts='C:\\Simulations\\Launcher\\known_hosts.txt')


with pysftp.Connection(host="newriver1.arc.vt.edu", username='knightkp', private_key= "C:\\Simulations\\Launcher\\newriver2", cnopts = cnopts) as sftp:
    print("Connection succesfully stablished ... ")

    path = sys.argv[1]
    localpath = path.replace("\\","\\\\")
    
    name_index = path.rfind("\\")
    name = path[name_index + 1:]
    
    
    if sftp.isdir(path[15:name_index].replace("\\","/")) != True:
        sftp.makedirs(path[15:name_index].replace("\\","/"))
    
    
    remotepath = "/home/knightkp" + path[14: ].replace("\\","/")
   
   
    sftp.put(path,remotepath)
    defaults = input("Accept Defaults (Y or N): ")
    if defaults == "Y" or defaults == 'y':
        walltime = "2:00:00"
        nodes = 1
        cores = 8
        queue = "dev_q"
        job_name = name
        output_file = name + "_output.txt"
    else:
        walltime = input("Walltime: ")
        nodes = input("Nodes: ")
        cores = input("Cores: ")
        queue = input("Dev_q? (Y or N): ")
        if queue == "Y" or queue == 'y':
            queue = "dev_q"
        else:
            queue = "normal_q"
        job_name = input("Name: ")
        output_file = input("Output File: ")
    work_dir = "/home/knightkp" + path[14:name_index ].replace("\\","/")

    flag_dict = {'flag1':walltime, 'flag2':str(nodes), 'flag3':str(cores), 'flag4':queue,'flag5':job_name,'flag6':work_dir,'flag7':name,'flag8':output_file}
    

    with open("C:\Simulations\Launcher\SMP_auto.sh") as main:
        with open(name+"_SMP.sh", 'w') as new_main:
            input_data = main.read()
            for key, value in flag_dict.items():
                input_data = input_data.replace(key, value)

            new_main.write(input_data)
    remote_ssh_path = "/home/knightkp" + path[14:name_index ].replace("\\","/") +"/" + name + "_SMP.sh"
    local_ssh_path = path[:name_index] + "\\" + name + "_SMP.sh"
    
    sftp.put(local_ssh_path,remote_ssh_path)
    
    
    fix_end = sftp.execute("dos2unix "+path[15:name_index].replace("\\","/")+"/"+ name + "_SMP.sh")
    
    submit = sftp.execute("qsub " +path[15:name_index].replace("\\","/")+"/"+ name + "_SMP.sh")
    
    for r in submit:
        print(r)
            
        
    


