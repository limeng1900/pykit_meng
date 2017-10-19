# 2017-10-19
#通过照片exif信息获取拍摄地点经纬度坐标 getCorrdinate(图片文件路径)
from PIL import Image
from PIL.ExifTags import TAGS

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

def getPicCoordinate(fn):
    ret=get_exif(fn)
    try:
        gpsInfo=ret['GPSInfo']
    except:
        lat=0
        lon=0
    try:
        latInfo=gpsInfo[2]
        lat=latInfo[0][0]/float(latInfo[0][1])+(latInfo[1][0]/float(latInfo[1][1]))/60.0+(latInfo[2][0]/float(latInfo[2][1]))/3600.0
    except:
        lat=0
    try:
        lonInfo=gpsInfo[4]
        lon=lonInfo[0][0]/float(lonInfo[0][1])+(lonInfo[1][0]/float(lonInfo[1][1]))/60.0+(lonInfo[2][0]/float(lonInfo[2][1]))/3600.0
    except:
        lon=0
    return(lon,lat)