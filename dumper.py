# from subprocess import call
import subprocess
import os
import gpxpy
import pandas as pd

if __name__ == "__main__":
    video_path = 'gps_dumper/video'
    gps_path = 'gps_dumper/gps'
    video_list = os.listdir(video_path)
    video_numbers = len(video_list)
    column = ['VIDEO_NAME', 'UNIX_TIME', 'LATITUDE', 'LONGITUDE', 'TIME_SPAN']
    video_gps_data = pd.DataFrame(columns=column)

    for number, video_name in enumerate(video_list):
        print(video_name+' dumping...')
        subprocess.call(['bash', './gps_dumper/dump_gpx.sh', video_path+'/'+video_name, gps_path])

        points = []
        indexes = []
        name = video_name.split('.')[0]
        gpx_file = open('./'+gps_path+'/'+name+'.gpx', 'r')
        gpx = gpxpy.parse(gpx_file)
        i = 0
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    indexes.append(name+'_'+str(i))
                    data = [video_name, point.time.timestamp(), point.latitude, point.longitude]
                    if i == 0:
                        data.append(0)
                    else:
                        data.append(point.time.timestamp()-points[0][1])
                    points.append(data)
                    i += 1

        data_frame_buffer = pd.DataFrame(points, columns=column, index=indexes)
        video_gps_data = pd.concat([video_gps_data, data_frame_buffer])
        print(video_name+' dump finished')
        print('=======================STATUS=====================')
        print(str(number+1/video_numbers*100)+'% of all process [{}/{}]'.format(number+1, video_numbers))
        print('==================================================')

    video_gps_data.to_pickle('./output/video_gps_data.zip')
    video_gps_data.to_csv('./output/video_gps_data.csv')

    # subprocess.run(('sudo', 'rm', '-rf', gps_path+u'/*.bin'), check=True)

    print('all process finished')
