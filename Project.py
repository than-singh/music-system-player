def unmutemusic():
    global currentvol
    hk.unmutebutton.grid_remove()
    hk.mutebutton.grid()
    mixer.music.set_volume(currentvol)

def mutemusic():
    global currentvol
    hk.mutebutton.grid_remove()
    hk.unmutebutton.grid()
    currentvol=mixer.music.get_volume()
    mixer.music.set_volume(0)
def resumemusic():
    hk.ResumeButton.grid_remove()
    hk.PauseButton.grid()
    mixer.music.unpause()
    AudioStatusLabel.configure(text='Playing......')
def volumeup():
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol + 0.05)

    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value']=mixer.music.get_volume()*100


def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol - 0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
    ProgressbarVolume['value'] = mixer.music.get_volume() * 100
def stopmusic():
    mixer.music.stop()
    AudioStatusLabel.configure(text='Stop......')

def pausemusic():
    mixer.music.pause()
    hk.PauseButton.grid_remove()
    hk.ResumeButton.grid()
    AudioStatusLabel.configure(text='Pause......')

def playmusic():
    ad=audiotrack.get()
    mixer.music.load(ad)
    ProgressbarLabel.grid()
    hk.mutebutton.grid()
    MusicLabel.grid()
    mixer.music.set_volume(0.4)
    ProgressbarVolume['value']=40
    ProgressbarVolumeLabel['text']='40%'
    mixer.music.play()
    AudioStatusLabel.configure(text='Playing......')

    Song=MP3(ad)
    songlength=int(Song.info.length)
    ProgressbarMusic['maximum']=songlength
    MusicEndTime.configure(text='{}'.format(str(datetime.timedelta(seconds=songlength))))

    def ProgressbarMusictick():
        CurrentSongLength = mixer.music.get_pos()//1000
        ProgressbarMusic['value']= CurrentSongLength
        MusicStarTime.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrentSongLength))))
        ProgressbarMusic.after(2,ProgressbarMusictick)
    ProgressbarMusictick()



def skk():
    #dd=filedialog.askopenfilename()

    try:
        dd=filedialog.askopenfilename(initialdir='G:/New folder (4)',title='Select Audio File',
                                     filetype=(('Mp3','*.mp3'),('WAV','*.wav')))
    except:
        dd=filedialog.askopenfilename(title='Select Audio File',
                                      filetype=(('Mp3','*.mp3'),('WAV','*.wav')))
    audiotrack.set(dd)
def cwidth():
    global implay,impause,imsearch,imvolumeup,imvdown,imstop,imresume,immute,imunmute
    global AudioStatusLabel,ProgressbarLabel,ProgressbarVolumeLabel,Progressbar,MusicLabel,ProgressbarMusic,MusicEndTime
    global MusicStarTime
    ################################
    implay = PhotoImage(file='play.png')
    impause = PhotoImage(file='vupp.png')
    imsearch = PhotoImage(file='searchh.png')
    imvolumeup = PhotoImage(file='vup.png')
    imvdown = PhotoImage(file='vdown.png')

    imstop = PhotoImage(file='stop.png')
    imresume = PhotoImage(file='resume.png')
    immute = PhotoImage(file='mute.png')
    imunmute = PhotoImage(file='play.png')
    #########################
    ##############################
    implay = implay.subsample(20, 20)
    impause = impause.subsample(20, 20)
    imsearch = imsearch.subsample(20, 20)
    imvolumeup = imvolumeup.subsample(20, 20)
    imvdown = imvdown.subsample(20, 20)
    imstop = imstop.subsample(20, 20)
    imresume = imresume.subsample(20, 20)
    immute = immute.subsample(20, 20)
    imunmute = imunmute.subsample(20, 20)
    #########################

   ########################################Labels
    TrackLabel=Label(hk,text='SELECT SONG : ',bg='old lace',fg='orange red',font=('areal',15,'italic bold'))
    TrackLabel.grid(row=0,column=0,padx=20,pady=20)

    AudioStatusLabel=Label(hk,text='',bg="old lace",font=('areal',13,'italic bold'),width=20)
    AudioStatusLabel.grid(row=2,column=1)

    TrackEntry = Entry(hk,font=('areal', 16, 'italic bold'),width=35,textvariable=audiotrack)
    TrackEntry.grid(row=0,column=1,padx=20,pady=20)
    ########################################Search Buttons as Sbutton###
    SButton = Button(hk, text='Search', bg='orange red',fg='old lace', font=('areal', 13, 'italic bold'), width=200, bd=5,
                     activebackground='deeppink', image=imsearch, compound=RIGHT, command=skk)#
    SButton.grid(row=0, column=2, padx=20, pady=20)
    SButton.grid(row=0, column=2, padx=20, pady=20)

    PButton = Button(hk, text='Play', bg='orange red',fg='old lace', font=('areal', 13, 'italic bold'), width=200, bd=5,
                     activebackground='deeppink', image=implay, compound=RIGHT,command=playmusic)
    PButton.grid(row=1, column=0, padx=20, pady=20)

    hk.PauseButton = Button(hk, text='Pause', bg='orange red',fg='old lace', font=('areal', 13, 'italic bold'), width=200, bd=5,
                            activebackground='deeppink', image=impause, compound=RIGHT,command=pausemusic)
    hk.PauseButton.grid(row=1, column=1, padx=20, pady=20)

    hk.ResumeButton = Button(hk, text='Resume', bg='orange red',fg='old lace', font=('areal', 13, 'italic bold'), width=200, bd=5,
                             activebackground='deeppink', image=imresume, compound=RIGHT,command=resumemusic)
    hk.ResumeButton.grid(row=1, column=1, padx=20, pady=20)
    hk.ResumeButton.grid_remove()

    hk.mutebutton = Button(hk, text='Mute', bg='orange red',fg='old lace', width=100, activebackground='deeppink', bd=5, image=immute,
                           compound=RIGHT,command=mutemusic)
    hk.mutebutton.grid(row=3, column=3)
    hk.mutebutton.grid_remove()

    hk.unmutebutton = Button(hk, text='Unmute', bg='orange red',fg='old lace', width=100, activebackground='deeppink', bd=5,
                             image=imunmute,compound=RIGHT,command=unmutemusic)
    hk.unmutebutton.grid(row=3, column=3)
    hk.unmutebutton.grid_remove()

    Volumeup = Button(hk, text='Volume Up', bg='orange red',fg='old lace', font=('areal', 13, 'italic bold'), width=200, bd=5,
                      activebackground='deeppink', image=imvolumeup, compound=RIGHT, command=volumeup)
    Volumeup.grid(row=1, column=2, padx=20, pady=20)

    StopButton = Button(hk, text='Stop', bg='orange red',fg='old lace', font=('areal', 13, 'italic bold'), width=200, bd=5,
                        activebackground='deeppink', image=imstop, compound=RIGHT,command=stopmusic)
    StopButton.grid(row=2, column=0, padx=20, pady=20)

    VolumeDown = Button(hk, text='Volume Down', bg='orange red',fg='old lace', font=('areal', 13, 'italic bold'), width=200, bd=5,
                        activebackground='deeppink', image=imvdown, compound=RIGHT,command=volumedown)
    VolumeDown.grid(row=2, column=2, padx=20, pady=20)
############
#################

from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar

import datetime
from mutagen.mp3 import MP3

hk=Tk()
hk.geometry('1100x500+100+50')
hk.title("Music Player")
hk.iconbitmap('music.ico')
hk.resizable(False,False)
hk.configure(bg='old lace')
##############global
audiotrack=StringVar()
currentvol = 0
songlength=0
#############
###########################################Progressbar###############
ProgressbarLabel =Label(hk,text='',bg='yellow')
ProgressbarLabel.grid(row=0,column=3 ,rowspan=3,padx=20,pady=20)
ProgressbarLabel.grid_remove()
ProgressbarVolume=Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',value=0,length=198)
ProgressbarVolume.grid(row=0,column=0,ipadx=5)
ProgressbarVolumeLabel = Label(ProgressbarLabel,text='0%',bg='lightgrey',width=3)
ProgressbarVolumeLabel.grid(row=0,column=0)
#################
######################Progressbar music
MusicLabel=Label(hk,text='',bg='lightyellow')
MusicLabel.grid(row=3,column=0,columnspan=3,padx=20,pady=20)
MusicLabel.grid_remove()

MusicStarTime=Label(MusicLabel,text='0:00:0',bg='lightyellow',width=6)
MusicStarTime.grid(row=0,column=0)

ProgressbarMusic=Progressbar(MusicLabel,orient=HORIZONTAL,mode='determinate',value=0)
ProgressbarMusic.grid(row=0,column=1 ,ipadx=370,ipady=3)

MusicEndTime=Label(MusicLabel,text='0:00:0',bg='lightyellow')
MusicEndTime.grid(row=0,column=2)


##############################slider#########
slider='Created By Himanshu Gupta'
count=0
text=''
Slider1=Label(hk,text=slider,bg='old lace',font=('areal', 40, 'italic bold'))
Slider1.grid(row=4,column=0,padx=20,pady=20,columnspan=3)
def Ssslider():
    global count,text
    if(count>=len(slider)):
        count=-1
        text=''
        Slider1.configure(text=text)
    else:
        text=text+slider[count]
        Slider1.configure(text=text)
    count +=1
    Slider1.after(200,Ssslider)

Ssslider()
mixer.init()

cwidth()
hk.mainloop()