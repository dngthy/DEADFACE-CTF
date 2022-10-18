Pandora's box, we have found it! Even better, the last travelers knew the numbered code to get in but they couldn't figure out the transcription. Figure out the the transcription's translation to find the flag!

Download Image
SHA1: 8e613787658d2d5828448aa182e2bb4904c124a8

Submit the flag as: flag{word_word_word_word}

----------------------------------------------------------------

code = "3686_526_814_518"
translation = "guvz_qgz_pfv_tvb"

transcript = ""
index = 0

for char in translation:
    if (char == "_"): 
        transcript += "_"
        index += 1
        continue
    decode_char = ord(char)-(ord(code[index])-48)
    if (decode_char < 97):
        decode_char += 26
    transcript += chr(decode_char)
    index+=1

print(transcript)

>> dont_let_her_out
