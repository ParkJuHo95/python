from shutil import copyfile

arr = [
    "김도희","김종명","김찬수","노태현","안희건",
    "유대석","이경민","이주연","임경빈","전아현",
    "정시윤","정지은","조태희","최경규","최수영"
]

arr_en = [
    "00kdh","01kjm","02kcs","03nth","04ahg",
    "05yds","06lkm","07ljy","08ikb","09jah",
    "10jsy","11jje","12cth","13cgg","14csy"
]


for idx,nm in enumerate(arr):
    for n in range(1,3+1):
        nm_en = arr_en[idx]
        copyfile(f'C:/workspace_python/HELLO_AI3/day02/voice/fruit/05/{nm}{n}.wav',f'C:/workspace_python/HELLO_AI3/day02/voice_en/fruit/05/{nm_en}{n}.wav')