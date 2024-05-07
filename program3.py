class Submit_Jawaban:
    respon= None
    submitted= False

    def __new__(cls):
        if cls.respon == None:
            cls.respon= super().__new__(cls)
        else:
            print(f"maaf jawaban sudah disubmit\n\tjawaban anda: {cls.respon.jawaban}\n")
        return cls.respon
        
    def __init__(self):
        if self.submitted== False:
            self.jawaban= input('masukkan jawaban: ')
            print(f"\tberhasil terkirim \n\trespon: {self.jawaban}\n")
            self.submitted= True
        
jawaban= Submit_Jawaban()
jawaban_baru= Submit_Jawaban()
print(jawaban==jawaban_baru)
