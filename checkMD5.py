import hashlib
import os
from urllib import request

fMD5_list = {}
Note_list = {}
dir = "./CheckFile" # directory path

def DownloadLink():
    f = open("./DownloadLink.txt", 'r')
    while True:
        url = f.readline()
        if not url : break
        if url[0:4] != "http" : url = "http://"+url
        url = url.strip()
        
        savename = url.rsplit('/', 1)[1]

        request.urlretrieve(url, dir+"/"+savename)

    f.close()

def GetNote(path):
    f = open(path, 'r')
    while True:
        line = f.readline()
        if not line : break
        data = line.split()
        Note_list[data[0].upper()] = data[1]
    f.close()

def GetFileMD5():
    for path in os.listdir(dir):
        file = os.path.join(dir, path)
        
        if os.path.isfile(file):
            fMD5_list[path.upper()] = calc_file_hash(file)
            

def calc_file_hash(path):
    f = open(path, 'rb')
    data = f.read()
    hash = hashlib.md5(data).hexdigest()
    return hash

if __name__ == "__main__":
    
    DownloadLink()  # 다운링크에서 파일 다운로드
    GetFileMD5()  # 다운받은 파일 MD5값 추출
    GetNote("./CheckValue.txt")   # 추출한 값과 비교할 값
    
    num = 0

    print("\nO : 바뀜 | X : 안바뀜\n")

    for CheckFile in fMD5_list:
        for Note in Note_list:
            if(CheckFile == Note):
                if(fMD5_list[CheckFile] == Note_list[Note]):
                    num+=1
                    print("{} | X | {} : {} = {}".format(num, CheckFile, fMD5_list[CheckFile], Note_list[Note]))
                    break
                else :
                    num+=1
                    print("{} | O | {} : {} = {}".format(num, CheckFile, fMD5_list[CheckFile], Note_list[Note]))

    a = input()
