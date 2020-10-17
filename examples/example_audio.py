
import os
import struct
import wave

INT_MAX = 2147483647
INT_MIN = -2147483648

def audio_load_signed_int32_raw(filename, channels=1):
    audio_buffer = None

    with open(filename, 'rb') as rf:
        buffer = rf.read()
        byteslen = len(buffer)
        wordlen = (byteslen >> 2)
        upfmt = '<' + ('i' * wordlen)
        audio_buffer = struct.unpack(upfmt, buffer)

    return audio_buffer

def audio_save_signed_int32_raw(filename, abuffer):

    with open(filename, 'wb') as wf:
        wordlen = len(abuffer)
        upfmt = '<' + ('i' * wordlen)
        outbuffer = struct.pack(upfmt, *abuffer)
        wf.write(outbuffer)

    return

def audio_mix_buffers_int32_raw(audio_buffers):

    outputlen = None
    for abuffer in audio_buffers:
        ablen = len(abuffer)
        if outputlen is None:
            outputlen = ablen
        elif ablen < outputlen:
            outputlen = ablen

    mbuffer = [0] * outputlen

    for bpos in range(0, outputlen):
        mword = 0
        for abuffer in audio_buffers:
            mword += abuffer[bpos]
        if mword > INT_MAX:
            mword = INT_MAX
        elif mword < INT_MIN:
            mword = INT_MIN
        mbuffer[bpos] = mword
    
    return mbuffer

if __name__ == "__main__":
    audio_buffers = []
    for i in range(0, 32):
        afilename = os.path.expanduser("~/Chirps/refchirp-ch%d.raw" % i)
        abuffer = audio_load_signed_int32_raw(afilename)
        audio_buffers.append(abuffer)

    print("Audio Loaded")

    mixed_audio = audio_mix_buffers_int32_raw(audio_buffers)

    print("Audio Mixed")

    ofilename = os.path.expanduser("~/Chirps/mixedchirp.raw")
    audio_save_signed_int32_raw(ofilename, mixed_audio)

    import audioop

    audioop.add()