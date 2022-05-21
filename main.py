from pysubparser import parser
from googletrans import Translator

# This is the input srt file
inputSrt = "14.srt"
subtitles = parser.parse(inputSrt)
arabic_output = open("Arabic_"+inputSrt, "w+", encoding="utf-8")

for subtitle in subtitles:
    arabic_output.write(str((subtitle.index) +1))
    arabic_output.write("\n")  

    while str(subtitle.start)[-1] == "0":
        subtitle.start = str(subtitle.start)[:-1]
    while str(subtitle.end)[-1] == "0":
        subtitle.end = str(subtitle.end)[:-1]
        
    arabic_output.write(f'{subtitle.start} --> {subtitle.end}')
    arabic_output.write("\n")
        
    translator = Translator()
    result = translator.translate(subtitle.text , dest='ar')
    #print(result.text)

    arabic_output.write(str(result.text)) 
    arabic_output.write("\n")
    arabic_output.write("\n")
