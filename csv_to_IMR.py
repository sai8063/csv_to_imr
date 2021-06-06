import struct
import pandas 
import os

PrintFlag=0
gyro_scale_factor = 1000000
acc_scale_factor = 1000000
InertialSen_to_novatel_frame_transform_Flag =1
def IMR_header(szHeader=b'$IMURAW\0',  # 8B char[8] 
                bIsIntelOrMotorola= 0,  # 1B int8_t
                dVersionNumber=8.80,    # 8B double
                bDeltaTheta= 1,         # 4B int32_t
                bDeltaVelocity=0,       # 4B int32_t
                dDataRateHz=100,        # 8B double
                dGyroScaleFactor=1,     # 8B double
                dAccelScaleFactor=1,    # 8B double
                iUtcOrGpsTime=2,        # 4B int32_t
                iRcvTimeOrCorrTime=0,   # 4B int32_t
                dTimeTagBias=0,         # 8B double
                szImuName=b'x'*32,       # 32B char[32]
                reserved1=b'xxxx',       # 4B char[4]
                szProgramName=b'x'*32,   # 32B char[32]
                tCreate=b'x'*12,              # 12B time_type
                bLeverArmValid=False,       # 1B bool
                lXoffset=0,             # 4B int32_t
                lYoffset=0,             # 4B int32_t
                lZoffset=0,             # 4B int32_t
                Reserved=b'x'*354):        # 354B int8_t[354]
                pass
                p0 = struct.pack('8s',b'$IMURAW\0')          # 8B char[8]
                p1 = struct.pack('b',bIsIntelOrMotorola)    # 1B int8_t
                p2 = struct.pack('<d', dVersionNumber)      # 8B double
                p3 = struct.pack( '<i',bDeltaTheta)         # 4B int32_t
                p4 = struct.pack('<i', bDeltaVelocity)      # 4B int32_t
                p5 = struct.pack('<d', dDataRateHz)         # 8B double
                p6 = struct.pack('<d', dGyroScaleFactor)    # 8B double
                p7 = struct.pack('<d', dAccelScaleFactor)   # 8B double
                p8 = struct.pack('<i',iUtcOrGpsTime)        # 4B int32_t
                p9 = struct.pack('<i',iRcvTimeOrCorrTime)   # 4B int32_t
                p10= struct.pack('<d', dTimeTagBias)        # 8B double
                p11= struct.pack('32s',szImuName)           # 32B char[32]
                p12= struct.pack('4s',reserved1)            # 4B char[4]
                p13= struct.pack('32s',szProgramName)       # 32B char[32]
                p14= struct.pack('12s',tCreate)             # 12B time_type
                p15= struct.pack('?',bLeverArmValid)        # 1B bool
                p16= struct.pack('<i',lXoffset)             # 4B int32_t
                p17= struct.pack('<i', lYoffset)            # 4B int32_t
                p18= struct.pack('<i',lZoffset)             # 4B int32_t
                p19= struct.pack('354s',Reserved)           # 354B int8_t[354]
                p= p0   +p1     +p2     +p3     +p4     +p5\
                        +p6     +p7     +p8     +p9     +p10\
                        +p11    +p12    +p13    +p14    +p15\
                        +p16    +p17    +p18    +p19
                # print(len(p))
                if (PrintFlag==1):
                    #op= struct.unpack('8scd',p)
                    # op= struct.unpack(''8s b d i i d d d i i d 32s 4s 32s 12s ? i i i 354s',p)
                    # print(struct.unpack_from('8s',p,0))
                #     print(op[0])
                    idx=0
                    print('header:',struct.unpack_from('8s',p,idx)[0]) 
                    idx+=8
                    print('bIsIntelOrMotorola:',struct.unpack_from('b',p,idx)[0])
                    idx+=1
                    print('dVersionNumber:',struct.unpack_from('<d',p,idx)[0])
                    idx+=8
                    print('bDeltaTheta',struct.unpack_from('<i',p,idx)[0])
                    idx+=4
                    print('bDeltaVelocity',struct.unpack_from('<d',p,idx)[0])
                    idx+=4
                    print('dDataRateHz',struct.unpack_from('<d',p,idx)[0])
                    idx+=8
                    print('dGyroScaleFactor',struct.unpack_from('<d',p,idx)[0])
                    idx+=8
                    print('dAccelScaleFactor',struct.unpack_from('<i',p,idx)[0])
                    idx+=8
                    print('iUtcOrGpsTime',struct.unpack_from('<i',p,idx)[0])
                    idx+=4
                    print('iRcvTimeOrCorrTime',struct.unpack_from('<d',p,idx)[0])
                    idx+=4+8
                    print('szImuName',struct.unpack_from('32s',p,idx)[0])
                    idx+=32+4
                    print('szProgramName',struct.unpack_from('32s',p,idx)[0])
                    idx+=32
                    print('tCreate',struct.unpack_from('12s',p,idx)[0])
                    idx+=12
                    print('bLeverArmValid',struct.unpack_from('b',p,idx)[0])
                    idx+= 1
                    print('lXoffset',struct.unpack_from('<i',p,idx)[0])
                    idx+=4
                    print('lYoffset',struct.unpack_from('<i',p,idx)[0])
                    idx+=4
                    print('lZoffset',struct.unpack_from('<i',p,idx)[0])
                    idx+=4
                    pass
                return p

def IMR_Record_struct(  time,           #8B double
                        gx,gy,gz,       #4B int32_t
                        ax,ay,az):      #
                    pt  = struct.pack('<d',time)
                    pgx = struct.pack('<i',gx)
                    pgy = struct.pack('<i',gy)
                    pgz = struct.pack('<i',gz)
                    pax = struct.pack('<i',ax)
                    pay = struct.pack('<i',ay)
                    paz = struct.pack('<i',az)
                    p =  pt   +pgx    +pgy    +pgz\
                            +pax    +pay    +paz    
                    
                    if(PrintFlag==1):
                        #print(struct.unpack('d i ',pt +pgx ))
                        upt,upgx,upgy,upgz,upax,upay,upaz= struct.unpack('d i i i i i i ',p)
                        print ('Time:',upt)
                        print ('gx:',upgx)
                        print ('gy:',upgy)
                        print ('gz:',upgz)
                        print ('ax:',upax)
                        print ('ay:',upay)
                        print ('az:',upaz)
                        pass
                    return p


def inertialsense_csv_to_imr(imu_file_path,gps_file_path,imr_file_path):
    #get gps time offset
    gpsfile = pandas.read_csv(gps_file_path)
    imufile = pandas.read_csv(imu_file_path)
    #get the time offset value from the last line of the csv file.
    gps_timeoffset=0
    #print(len(gpsfile))
    #print(gpsfile)
    if len(gpsfile)>0:
        gps_timeoffset = gpsfile.loc[len(gpsfile)-1].at['towOffset']
    

    #create header packet of imr file
    bDeltaTheta = 0 # data is read as scaled angular rates
    bDeltaVelocity = 0 # data is read as scaled accelerations
    dDataRateHz = 1     
    dGyroScaleFactor = 1/gyro_scale_factor
    dAccelScaleFactor =1/ acc_scale_factor
    iUtcOrGpsTime = 2 # 1: UTC seconds of wee, 2: GPS seconds of week
    iRcvTimeOrCorrTime = 0 # 0: Unknown, will default to corrected time
    bLeverArmValid = False #True if lever arms from IMU to primary GNSS antenna are stored in this header

    header_packet_imr = IMR_header(bDeltaTheta=bDeltaTheta,
                                    bDeltaVelocity=bDeltaVelocity,
                                    dDataRateHz=dDataRateHz,
                                    dGyroScaleFactor=dGyroScaleFactor,
                                    dAccelScaleFactor=dAccelScaleFactor,
                                    iUtcOrGpsTime=iUtcOrGpsTime,
                                    iRcvTimeOrCorrTime=iRcvTimeOrCorrTime,
                                    bLeverArmValid=bLeverArmValid)

    #write 512B header
    opfile_name = ((os.path.basename(imu_file_path)).split('.'))[0] + '.imr'
    imrfile = open(imr_file_path+""+opfile_name,'wb')
    imrfile.write(header_packet_imr)

    for i in range(len(imufile)):
        line = imufile.loc[i]
        gps_sec = (line.at['time']) + gps_timeoffset
        gx = int(line.at['pqr1[0]']*gyro_scale_factor)
        gy = int(line.at['pqr1[1]']*gyro_scale_factor)
        gz = int(line.at['pqr1[2]']*gyro_scale_factor)
        ax= int(line.at['acc1[0]']*acc_scale_factor)
        ay= int(line.at['acc1[1]']*acc_scale_factor)
        az= int(line.at['acc1[2]']*acc_scale_factor)
        imr_data_packet = IMR_Record_struct(gps_sec,gx,gy,gz,ax,ay,az)
        imrfile.write(imr_data_packet)

    imrfile.close()

def inertialsense_csv_to_bin(imu_file_path,gps_file_path,bin_file_path):
    #get gps time offset
    gpsfile = pandas.read_csv(gps_file_path)
    imufile = pandas.read_csv(imu_file_path)
    #get the time offset value from the last line of the csv file.
    gps_timeoffset=0
    print('gps file len: ',len(gpsfile))
    print('imu file len: ',len(imufile))
    #print(gpsfile)
    if len(gpsfile)>0:
        gps_timeoffset = gpsfile.loc[len(gpsfile)-1].at['towOffset']
    
    print("gps time offset: ", gps_timeoffset)
    # #create header packet of imr file
    # bDeltaTheta = 0 # data is read as scaled angular rates
    # bDeltaVelocity = 0 # data is read as scaled accelerations
    # dDataRateHz = 1     
    # dGyroScaleFactor = 1/gyro_scale_factor
    # dAccelScaleFactor =1/ acc_scale_factor
    # iUtcOrGpsTime = 2 # 1: UTC seconds of wee, 2: GPS seconds of week
    # iRcvTimeOrCorrTime = 0 # 0: Unknown, will default to corrected time
    # bLeverArmValid = False #True if lever arms from IMU to primary GNSS antenna are stored in this header

    # header_packet_imr = IMR_header(bDeltaTheta=bDeltaTheta,
    #                                 bDeltaVelocity=bDeltaVelocity,
    #                                 dDataRateHz=dDataRateHz,
    #                                 dGyroScaleFactor=dGyroScaleFactor,
    #                                 dAccelScaleFactor=dAccelScaleFactor,
    #                                 iUtcOrGpsTime=iUtcOrGpsTime,
    #                                 iRcvTimeOrCorrTime=iRcvTimeOrCorrTime,
    #                                 bLeverArmValid=bLeverArmValid)

    #write 512B header
    binfile_name = ((os.path.basename(imu_file_path)).split('.'))[0] + '.bin'
    # binfile_name = "raw_imu.bin"
    binfile = open(bin_file_path+"/"+binfile_name,'wb')
    # imrfile.write(header_packet_imr)

    
    for i in range(len(imufile)):
        try:

            line = imufile.loc[i]
            gps_sec = (line.at['time']) + gps_timeoffset
            if(InertialSen_to_novatel_frame_transform_Flag==1):
                gx = int(line.at['pqr1[1]']*gyro_scale_factor)
                gy = int(line.at['pqr1[0]']*gyro_scale_factor)
                gz = -1*int(line.at['pqr1[2]']*gyro_scale_factor)
                ax= int(line.at['acc1[1]']*acc_scale_factor)
                ay= int(line.at['acc1[0]']*acc_scale_factor)
                az= -1*int(line.at['acc1[2]']*acc_scale_factor)
            else:
                gx = int(line.at['pqr1[0]']*gyro_scale_factor)
                gy = int(line.at['pqr1[1]']*gyro_scale_factor)
                gz = int(line.at['pqr1[2]']*gyro_scale_factor)
                ax= int(line.at['acc1[0]']*acc_scale_factor)
                ay= int(line.at['acc1[1]']*acc_scale_factor)
                az= int(line.at['acc1[2]']*acc_scale_factor)
            imr_data_packet = IMR_Record_struct(gps_sec,gx,gy,gz,ax,ay,az)
            binfile.write(imr_data_packet)
        except:
            pass

    binfile.close()
    



    


#IMR_header(lZoffset=2)
#IMR_Record_struct(654321,10,11,12,20,21,22)
# f= pandas.read_csv('gps_file.csv')
# print(f)
# print(len(f))
# print(f.loc[len(f)-1].at['towOffset'])

# inertialsense_csv_to_imr('LOG_SN40336_20210523_224752_0001_imuDual_sdat.csv','gps_file.csv','')
# inertialsense_csv_to_bin('LOG_SN40336_20210523_224752_0001_imuDual_sdat.csv','gps_file.csv','')
imuFilepath = 'D:\\NSV\data\\20210601_sparrow_field_data\\car_runs\\run2\\20210531_182636\\LOG_SN40336_20210531_182636_0001_imuDualimuDual_merged_.csv'
gpsFilepath = 'D:\\NSV\data\\20210601_sparrow_field_data\\car_runs\\run2\\20210531_182636\\LOG_SN40336_20210531_182636_0001_gps1Pos.csv'
binFilePath = 'D:\\NSV\data\\20210601_sparrow_field_data\\car_runs\\run2\\20210531_182636\\'

# inertialsense_csv_to_bin(imu_file_path=imuFilepath,gps_file_path=gpsFilepath,bin_file_path=binFilePath)
# imu_file_path= os.path.basename(imuFilepath)
# print(((os.path.basename(imu_file_path)).split('.'))[0] + '.bin')

    



