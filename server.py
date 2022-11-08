
import glob
import os, time, sys
import socket 

#get the name of the sever and pass it as a file name.txt 
s_name = socket.gethostname() + '.txt'


dirs_list = ['/ldmodels/AMZ_POS_A/logs/*', '/ldmodels/AMZ_POS_B/logs/*', '/ldmodels/AMZ_PRICE_A/logs/*', '/ldmodels/AMZ_PRICE_B/logs/*', '/ldmodels/AU_LEGACY_EXTRACT_A/logs/*', '/ldmodels/AU_LEGACY_EXTRACT_B/logs/*', 
'/ldmodels/BAT_FSP_A/logs/*', '/ldmodels/BAT_FSP_B/logs/*', '/ldmodels/COLES_FSP_A/logs/*', '/ldmodels/COLES_FSP_B/logs/*', 
'/ldmodels/COLES_MARKET_READ_A/logs/*', '/ldmodels/COLES_MARKET_READ_B/logs/ *', '/ldmodels/COLES_MARKET_READ_LIQUOR_A/logs/*',
'/ldmodels/COLES_MARKET_READ_LIQUOR_B/logs/*', '/ldmodels/COLES_PANEL_A/logs/*', '/ldmodels/COLES_PANEL_B/logs/*', '/ldmodels/COLES_SCAN_A/logs/*', 
'/ldmodels/COLES_SCAN_B/logs/*', '/ldmodels/COLES_SCAN_EXTRACT_A/logs/*', '/ldmodels/COLES_SCAN_EXTRACT_B/logs/*', '/ldmodels/ILD_USAGE/logs/*', '/ldmodels/KRAFTHEINZ_ANZ_MA_A/logs/*', 
'/ldmodels/KRAFTHEINZ_ANZ_MA_B/logs/*', '/ldmodels/KRAFTHEINZ_ANZ_MA_EXTRACT_A/logs/*', '/ldmodels/KRAFTHEINZ_ANZ_MA_EXTRACT_B/logs/*', '/ldmodels/KRAFTHEINZ_PANEL_A/logs/*', 
'/ldmodels/KRAFTHEINZ_PANEL_B/logs/*', '/ldmodels/LOREAL_ANZ_MA_A/logs/*', '/ldmodels/LOREAL_ANZ_MA_B/logs/*', 
'/ldmodels/LOREAL_ANZ_MA_EXTRACT_A/logs/*', '/ldmodels/LOREAL_ANZ_MA_EXTRACT_B/logs/*', '/ldmodels/PRICELN_AU_FSP_A/logs/*', 
'/ldmodels/PRICELN_AU_FSP_B/logs/*', '/ldmodels/PRICELN_SUP_AU_FSP_A/logs/*', '/ldmodels/PRICELN_SUP_AU_FSP_B/logs/*'
]

length = len(dirs_list)
# counter = 0
days = 7
now = time.time()
counter = 0
size = 0.0
file_list = []
while counter <= length - 1:
    path_li = dirs_list[counter]# going by the index incrementally 
    files = glob.glob(path_li)
    for i in files:
         if os.stat(os.path.join(path_li,i)).st_mtime < now - days * 86400:
            file_list.append(i)
            size += os.path.getsize(i)
    counter += 1
d = float(size) // 1024 // 1024
print(str(len(file_list)) + ' files have been deleted')
line = s_name,len(file_list),'with total size of', d, 'MB have been deleted'
with open ('d_files.txt', 'w') as ff:
    ff.writelines(", ".join(file_list))
with open(s_name, 'w') as f:
    f.write(str(line))

    # f.seek(0, 2)
    # f.write(str(line) + ',')
        

length1 = len(file_list) - 1

counter1 = 0

while counter1 <= length1:
    if os.path.isdir(file_list[counter1]):
        os.removedirs(file_list[counter1])
        counter1 += 1
    elif os.path.isfile(file_list[counter1]):

        # os.chmod(file_list[counter1], 0o777)
        os.remove(file_list[counter1])
        counter1 += 1
    else:
        continue


