import png
from copy import deepcopy

class PNG_Editor():

    def read_file(self, filename):
        reader = png.Reader(filename)
        return reader.read()

    def write_file(self, data, filename):
        outfile = open(filename, "wb")
        writer = png.Writer(data[0], data[1], bitdepth=data[3]["bitdepth"])
        try:
            writer.write_passes(outfile, data[2])
        except Exception: 
            pass
        print "closing...?"
        outfile.close()
    
    def insert_junk2(self, data):
        pixels = [64 if i==80 else i for n, i in enumerate(data[2])]
        return [data[0], data[1], pixels, data[3]]
        
edit = PNG_Editor()
data = edit.read_file("windows386soul.png")
data = edit.insert_junk2(data)
edit.write_file(data, "script3.png")

    
 



