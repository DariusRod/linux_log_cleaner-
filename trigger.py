import paramiko

ip=['10.76.60', '10.76.6','10.76.6', '10.76.6', '10.76.6']
servers = len(ip) - 1
# print(servers)
port=22
username='user'
password='pass'
idx = 0
fails = []
print('fail list', fails)

cmd='touch man.txt' 
while idx <= servers:
    print(idx)
    try:
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip[idx],port,username,password)
        stdin,stdout,stderr=ssh.exec_command(cmd)
        outlines=stdout.readlines()
        resp=''.join(outlines)
        print(resp)
        idx += 1

    except:
        print(ip[idx], 'has failed')
        fails.append(ip[idx])
        idx += 1
   
# stdin,stdout,stderr=ssh.exec_command('some really useful command')
# outlines=stdout.readlines()
# resp=''.join(outlines)
# print(resp)

# site= ftplib.FTP('10.76.6.81', 'user', 'pass','22')
# site.cwd('/home/drod01/tdir') # if it's '.', you can skip this line
# folder= FTPDirectory()
# folder.getdata(site) # get the filenames
# for path, ftpfile in folder.walk():
#         print(path, ftpfile)
#     # if ftpfile.mtime < quite_old:
#     #     site.delete(ftpfile.name)

# /lddata2/au/pos/dimensions/prd/filter/kraft/outputs
