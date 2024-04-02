# 0 김민경
# 1 김승연
# 2 김차은
# 3 김창용
# 4 김초희
# 5 김현우
# 6 남희수
# 7 박주호
# 8 박지원
# 9 배유림
# 10 백영웅
# 11 변상원
# 12 송은비
# 13 우민규
# 14 유길상
# 15 이미소
# 16 이상철
# 17 이성휘
# 18 정민지
# 19 하예종
import os

file_list = os.listdir("./img")
file_list_mp4 = [file for file in file_list if file.endswith(".mp4")]
for idx,i in enumerate(file_list_mp4):
    # name = i[0:3]
    name = i.replace(".mp4","")
    idx = str(idx).zfill(2)
    os.mkdir(f"./pre01/{idx}")
    print(f"{idx} {name}")
    
    
    
    
    