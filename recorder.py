#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyaudio
import wave


# In[2]:


# In[7]:

audio = pyaudio.PyAudio()


# In[ ]:


stream = audio.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=44100,
    input=True,
    frames_per_buffer=1024
)


# In[ ]:


frames = []
try:
    print('Recording...')
    while True:
        data = stream.read(1024)
        frames.append(data)
except KeyboardInterrupt:
    print("Done")


# In[ ]:


stream.stop_stream()
stream.close()
audio.terminate()


# In[ ]:


sound_file = wave.open("foo.mp3", "wb")
sound_file.setnchannels(1)
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.writeframes(b''.join(frames))
sound_file.close()

