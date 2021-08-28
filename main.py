import os
from data.textmap import text_map
import nessmith

print(list(map(lambda x: hex(x), nessmith.assemble("LDA $6000", []))))
# file_in = open("./test/cv2.nes", "rb")
# data = file_in.read()
# file_in.close()

# with open("./test/cv2r.nes", "wb") as file_out:
#     file_out.write(data)
#     file_out.seek(0x0101A2)
#     file_out.write(bytearray([0x1A, 0x1A, 0x1A, 0x1A, 0x1A, 0x1A,0x1A, 0x1A, 0x1A]))

# os.system("./test/Nestopia.app/Contents/MacOS/Nestopia ./test/cv2r.nes")
