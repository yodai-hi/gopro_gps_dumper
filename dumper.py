# from subprocess import call
import subprocess
import os
import gpxpy
import pandas as pd

if __name__ == "__main__":
    video_path = 'gps_dumper/video'
    binary_path = 'gps_dumper/binary'
    video_list = os.listdir(video_path)
    video_numbers = len(video_list)
    column = ['VIDEO_NAME', 'UNIX_TIME', 'LATITUDE', 'LONGITUDE', 'TIME_SPAN']
    video_gps_data = pd.DataFrame()
    video_inertial_data = pd.DataFrame()

# 各ビデオに対して処理をする
    for number, video_name in enumerate(video_list):
        name, codec = os.path.splitext(video_name)
        if codec != '.MP4':
            continue
        print(video_name+' dumping...')
        subprocess.call(
            ['bash', './gps_dumper/dump_gpx.sh', video_path + '/' + video_name, binary_path]
        )

        accl = pd.read_csv(binary_path + '/' + name + '-accl.csv', header=0)
        gyro = pd.read_csv(binary_path + '/' + name + '-gyro.csv', header=0)
        inertial = pd.concat([accl, gyro], axis=1)
        gps = pd.read_csv(binary_path + '/' + name + '-gps.csv', header=0)

        inertial['filename'] = name
        gps['filename'] = name

        gps = gps.rename(index=lambda s: name + '_' + str(s))
        inertial = inertial.rename(index=lambda s: name + '_' + str(s))

        os.remove(binary_path + '/' + name + '-accl.csv')
        os.remove(binary_path + '/' + name + '-gyro.csv')
        os.remove(binary_path + '/' + name + '-gps.csv')

        video_inertial_data = pd.concat([video_inertial_data, inertial])
        video_gps_data = pd.concat([video_gps_data, gps])
        print(video_name+' dump finished')
        # print('=======================STATUS=====================')
        # print(str(number+1/video_numbers*100)+'% of all process [{}/{}]'.format(number+1, video_numbers))
        # print('=================================================')

    # データを保存
    video_gps_data.to_pickle('./output/video_gps_data.zip')
    video_inertial_data.to_pickle('./output/video_inertial_data.zip')
    video_gps_data.to_csv('./output/video_gps_data.csv')
    video_inertial_data.to_csv('./output/video_inertial_data.csv')

    print('all process finished')
