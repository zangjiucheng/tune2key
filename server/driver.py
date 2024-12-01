# from Tune2key import TUNE2KEY

# test = TUNE2KEY()
# test.upload_file("resources/upload/PERFECT.mp3")

from music_process import *

file_name = "ROSÉ & Bruno Mars - APT"

simplify_midi(f"resources/midi/{file_name}.mid", f"resources/simple_sheet/{file_name}.mid")
generate_sheet_pdf(f"resources/simple_sheet/{file_name}.mid", f"resources/simple_sheet/{file_name}.pdf")