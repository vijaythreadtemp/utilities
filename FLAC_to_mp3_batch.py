import os
import sys
import glob
import argparse
from pathlib import Path



def convert_func(exec_path, src_dir, dest_dir):
    fs = glob.glob(src_dir + "/*.flac")
    Path(dest_dir).mkdir(parents=True, exist_ok=True)
    for f in fs:
        pos = f.rfind('/')
        if pos == -1:
            pos = f.rfind('\\')
        
        file_name = f[pos+1:]
        mp3_f = dest_dir + "/" + file_name.replace("flac", "mp3")
        cmd = exec_path + " -i \"" + f + "\" -ab 320k -map_metadata 0 -id3v2_version 3 \"" + mp3_f + "\"" 
        #print(cmd)
        os.system(cmd)



parser = argparse.ArgumentParser(description='Batch conversion of FLAC files to mp3 files using ffmpeg')
parser.add_argument('-e', '--ffmpeg_exec_path', required=True, type=str, help='Absolute path of FFMPEG executable')
parser.add_argument('-s', '--src_dir', type=str, required=True, help='Dircetory containing FLAC files')
parser.add_argument('-d', '--dest_dir', type=str, required=True, help='Dircetory to store mp3 files')

args = parser.parse_args()

if __name__ == '__main__':
    print("\nConverting files ... \n")
    convert_func(args.ffmpeg_exec_path, args.src_dir, args.dest_dir)
    print("\n\nConverted FLAC files to mp3 files.")
    


