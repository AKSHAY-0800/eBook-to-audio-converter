import pygame
import time
from gtts import gTTS
from PyPDF2 import PdfReader
import tkinter
from tkinter import filedialog
def say():
    file_path = filedialog.askopenfilename(
    title="Select a PDF file",
    filetypes=[("PDF files", "*.pdf")]
    )
    if file_path:
        pygame.init()
        pygame.mixer.init()
        file=PdfReader(file_path)
        num=len(file.pages)
        for i in range(0,num):
            page=file.pages[i]
            x=page.extract_text()
            tts = gTTS(text=x, lang='en')
            a="output.mp3"
            tts.save(a)
            try:
        # Load and play the music
                pygame.mixer.music.load(a)
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play(-1)  # Play indefinitely
                sound=pygame.mixer.Sound(a)
                lent=sound.get_length()
        # Keep the program running to hear the music
                time.sleep(lent)
            except pygame.error as e:
                print(f"Error playing music: {e}")
            finally:
                pygame.quit()
    else:
        print("no file selected")
say()
