import csv_to_IMR


from csv_to_IMR import *
from merge_dat_file import*

Imu_data_folderPath= "D:\\NSV\\data\\20210601_sparrow_field_data\\car_runs\\run1\\20210531_181858\\"

imu_file_path= merge_file(Imu_data_folderPath,Imu_data_folderPath,file_type='csv',file_extension='_imuDual.csv')
gps_file_path = merge_file(Imu_data_folderPath,Imu_data_folderPath,file_type='csv',file_extension='_gps1Pos.csv')

print(imu_file_path)
print(gps_file_path)
inertialsense_csv_to_bin(imu_file_path=imu_file_path,gps_file_path=gps_file_path,bin_file_path=Imu_data_folderPath)
