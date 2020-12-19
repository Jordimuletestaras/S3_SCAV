import subprocess as sp

if __name__ == '__main__':

    print("""Select de video:
        1. 1280x720
        2. 640x480
        3. 360x240
        4. 160x120""")
    option = int(input())
    n=0
    filename="inicializamos"
    newname="0x0"
    while(n==0):
        if option==1:
            filename="720_10sec_bbb.mp4"
            newname= "1280x720"
            w=1280
            h=720
            n=1
            break
        elif option==2:
            filename = "480_10sec_bbb.mp4"
            newname= "640x480"
            w=640
            h=480
            n = 1
            break
        elif option==3:
            filename = "360x240_10sec_bbb.mp4"
            newname= "360x240"
            w=360
            h=240
            n = 1
            break
        elif option==4:
            filename = "160x120_10sec_bbb.mp4"
            newname= "160x120"
            w=160
            h=120
            n = 1
            break
        else:
            print("invalid option")

        # Change the codecs to vp8,vp9,h.265 and av1
    sp.run('ffmpeg -i ' + filename + ' -c:v vp8 ' + newname + 'vp8.webm', shell=True)
    sp.run('ffmpeg -i ' + filename + ' -c:v vp9 ' + newname + 'vp9.webm', shell=True)
    sp.run('ffmpeg -i ' + filename + ' -c:v libx265 ' + newname + 'H265.mp4', shell=True)
    sp.run('ffmpeg -i ' + filename + ' -strict -2 -c:v av1 ' + newname + 'av1.mkv', shell=True)

    line = 'ffmpeg -i ' + newname + 'vp8.webm -i ' + newname + 'vp9.webm -i ' + newname + 'H265.mp4 -i ' + newname + 'av1.mkv -filter_complex "nullsrc=size=' + str(int(w)) + 'x' + str(int(h)) + ' [base]; [0:v] setpts=PTS-STARTPTS, scale=' + str(int(w/2)) + 'x' + str(int(h/2)) + ' [upperleft]; [1:v] setpts=PTS-STARTPTS, scale=' + str(int(w/2)) + 'x' + str(int(h/2)) + ' [upperright]; [2:v] setpts=PTS-STARTPTS, scale=' + str(int(w/2)) + 'x' + str(int(h/2)) + ' [lowerleft]; [3:v] setpts=PTS-STARTPTS, scale=' + str(int(w/2)) + 'x' + str(int(h/2)) + ' [lowerright]; [base][upperleft] overlay=shortest=1 [tmp1]; [tmp1][upperright] overlay=shortest=1:x=' + str(int(w/2)) + ' [tmp2]; [tmp2][lowerleft] overlay=shortest=1:y=' + str(int(h/2)) + ' [tmp3]; [tmp3][lowerright] overlay=shortest=1:x=' + str(int(w/2)) + ':y=' + str(int(h/2)) + '" -c:v libx265 ' + newname + '_mosaico.mp4'

    sp.run( line, shell=True )

