import glob
import os
# import merge_dat_file

def merge_file(input_folder_path,output_folder_path,file_type, file_extension):
    ip_files= glob.glob(input_folder_path+"/*"+file_extension)
    # print(ip_files)

    if len(ip_files)==0:
        return

    try:
        opfileName= ((os.path.basename(ip_files[0])).split('.'))[0] + '_merged_.'+(file_extension.split('.'))[1]
        print('merged file name:',opfileName)
    except:

        opfileName =  '_merged_'+(file_extension.split('.'))[1]
        print('merged file name:',opfileName)
        pass

    opfile= output_folder_path+'/'+ opfileName
    

    if file_type!='b':
        file_type=''
        
    merged_op_file = open(opfile,'w'+file_type)

    for i in ip_files:
        f = open(i,'r'+file_type)
        data= f.read()
        merged_op_file.write(data)
        f.close()
        print("merging ", i)

    merged_op_file.close()
    print(opfile)
    return opfile


# input_folder_path="D:\\NSV\\data\\20210601_sparrow_field_data\\car_runs\\run2\\20210531_182636"
# merge_file(input_folder_path,input_folder_path,file_type='csv',file_extension='imuDual.csv')

# Imu_data_folderPath= "D:\\NSV\\data\\20210601_sparrow_field_data\\car_runs\\run1\\20210531_181858"


# imu_file_path= merge_file(Imu_data_folderPath,Imu_data_folderPath,file_type='csv',file_extension='imuDual.csv')
# gps_file_path = merge_file(Imu_data_folderPath,Imu_data_folderPath,file_type='csv',file_extension='gps1Pos.csv')

# inertialsense_csv_to_bin(imu_file_path=imu_file_path,gps_file_path=gps_file_path,bin_file_path=Imu_data_folderPath)
