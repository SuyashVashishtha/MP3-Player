import os
import threading
import time
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from tkinter import ttk



from mutagen.mp3 import MP3
from pygame import mixer






root =Tk()

root.title("Fire Music Player")
root.geometry('874x500+250+130')
root.iconbitmap("images/mfireicon.ico")





#create a menubar
menubar = Menu(root)
root.config(menu=menubar)

#create the sub menu File+++++++++++++++++++++++++++++++++++++++

def asks():
    Msg = tkinter.messagebox.askquestion ("Confirmation","Do you want to Exit?",icon = 'warning')
    if Msg == 'yes':
        root.destroy()




submenu = Menu(menubar, tearoff=0)

playlist = []

def browse():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)

def add_to_playlist(filename):

    file_data = os.path.splitext(filename)

    if file_data[1] == '.mp3':
        audio = MP3(filename)

        filename = os.path.basename(filename_path)
        index=0
        playlistbox.insert(index, filename)
        playlist.insert(index, filename_path)

        playlistbox.pack()

        index += 1

    else:
        tkinter.messagebox.showerror('Incorrect File',' Incorrect File Format , please add a Audio file (.mp3)')




menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open", command=browse)
submenu.add_command(label="Exit", command=asks)



#create the sub menu Help

def about_us():
    # tkinter.messagebox.showinfo('About us','This is a MUSIC Player ')
    top = Toplevel()
    top.title("About")
    top.geometry("400x350+300+100")
    top.iconbitmap("images\\mfireicon.ico")

    about = Label(top, image=aboutusphoto)
    about.pack(fill=BOTH)

    top.resizable(0,0)

def inst():
    top = Toplevel()
    top.title("Instructions")
    top.geometry("600x540+300+100")
    top.iconbitmap("images\\mfireicon.ico")
    instr = Label(top, image=instaphoto)
    instr.pack(fill=BOTH)
    def backins():
        instr.config(image=instaphoto)


    def nextins():
        instr.config(image=insta2photo)


    nextin = Button(top,text="2", command=nextins, bg="darkorange")
    nextin.place(y=505, x=280)

    back = Button(top, text="1", command=backins, bg="darkorange")
    back.place(y=505, x=260)

    top.resizable(0,0)













submenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="About us", command=about_us)
submenu.add_command(label="Instructions", command=inst)

instaphoto = PhotoImage(file="images\\inst1.png")
insta2photo = PhotoImage(file="images\\inst2.png")

aboutusphoto = PhotoImage(file="images\\maboutus.png")



#menu in menu

#mood

def happy():
    wallpaper.config(image=happyphoto)

def sad():
    wallpaper.config(image=sadphoto)

def moti():
    wallpaper.config(image=motivphoto)

def study():
    wallpaper.config(image=studyphoto)

def game():
    wallpaper.config(image=gamephoto)

def defaultwall():
    wallpaper.config(image=partyphoto)



## cold  theme

def dark():
    leftframe.config(bg="RoyalBlue4")
    rightframe.config(bg="RoyalBlue4")
    root.config(bg="black")
    info.config(fg="white", bg="RoyalBlue4")
    buttonframeleft.config(bg="RoyalBlue4")
    controlpanel.config(bg="RoyalBlue4")
    playlistframe.config(bg="RoyalBlue4")
    playBtn.config(bg="RoyalBlue4", bd=0, image=darkplayPhoto)
    stopBtn.config(bg="RoyalBlue4", bd=0, image=darkstopPhoto)
    pauseBtn.config(bg="RoyalBlue4", bd=0, image=darkpausePhoto)
    nxtBtn.config(bg="RoyalBlue4", bd=0, image=darknextPhoto)
    prevBtn.config(bg="RoyalBlue4", bd=0, image=darkpevPhoto)
    volumeBtn.config(bg="RoyalBlue4", bd=0, image=darkvolumePhoto, command=darkmute_music)
    wallpaper.config(bg="RoyalBlue4")
    currenttimelable.config(fg="white", bg="RoyalBlue4")
    lengthlable.config(fg="white", bg="RoyalBlue4")
    addbtn.config(image=adddarkPhoto, bg="RoyalBlue4")
    delbtn.config(image=deldarkPhoto, bg="RoyalBlue4")
    scale.config(bg="RoyalBlue4", fg="white", activebackground='white')
    buttoncon.config(bg="RoyalBlue4")

####### Lovely theme ###########

def lovely():

    leftframe.config(bg="plum1")
    rightframe.config(bg="plum1")
    root.config(bg="red3")
    info.config(fg="red3", bg="plum1", font='Times 15 bold')
    buttonframeleft.config(bg="plum1")
    controlpanel.config(bg="plum1")
    playlistframe.config(bg="plum1")
    playBtn.config(bg="plum1", bd=0, image=lovelyplayPhoto)
    stopBtn.config(bg="plum1", bd=0, image=lovelystopPhoto)
    pauseBtn.config(bg="plum1", bd=0, image=lovelypausePhoto)
    nxtBtn.config(bg="plum1", bd=0, image=lovelynextPhoto)
    prevBtn.config(bg="plum1", bd=0, image=lovelyprevPhoto)

    volumeBtn.config(bg="plum1", bd=0, image=lovelyvolumePhoto, command=lovelymute_music)
    wallpaper.config(bg="plum1")
    currenttimelable.config(fg="red3", bg="plum1")
    lengthlable.config(fg="red3", bg="plum1")
    addbtn.config(image=lovelyaddPhoto, bg="plum1")
    delbtn.config(image=lovelydelPhoto, bg="plum1")
    scale.config(bg="plum1", fg="red", activebackground='red')
    buttoncon.config(bg="plum1")


def default():
    leftframe.config(bg="white smoke")
    rightframe.config(bg="white smoke")
    root.config(bg="white smoke")
    info.config(fg="black", bg="white smoke")
    buttonframeleft.config(bg="white smoke")
    controlpanel.config(bg="white smoke")
    playlistframe.config(bg="white smoke")
    playBtn.config(bg="white smoke", bd=0, image=playPhoto)
    stopBtn.config(bg="white smoke", bd=0, image=stopPhoto)
    pauseBtn.config(bg="white smoke", bd=0, image=pausePhoto)
    nxtBtn.config(bg="white smoke", bd=0, image=nextPhoto)
    prevBtn.config(bg="white smoke", bd=0, image=prevPhoto)
    volumeBtn.config(bg="white smoke", bd=0, command=mute_music, image=volumePhoto)
    wallpaper.config(bg="white smoke")
    currenttimelable.config(fg="black", bg="white smoke")
    lengthlable.config(fg="black", bg="white smoke")
    addbtn.config(image=addPhoto, bg="white smoke")
    delbtn.config(image=delPhoto, bg="white smoke")
    scale.config(bg="white smoke", fg="black", activebackground='dark orange')
    buttoncon.config(bg="white smoke")





optionMenu = Menu(menubar,  tearoff=0)

########### MOOD #############

submenu = Menu(optionMenu,  tearoff=0)
submenu.add_command(label="Happy", command=happy)
submenu.add_command(label="Sad", command=sad)
submenu.add_command(label="Motivation", command=moti)
submenu.add_command(label="Study", command=study)
submenu.add_command(label="Gaming", command=game)
submenu.add_command(label="Default", command=defaultwall)
optionMenu.add_cascade(label='Mood', menu=submenu, underline=0)

############# Themes #################

submenu = Menu(optionMenu,  tearoff=0)
submenu.add_command(label="Cold", command=dark)
submenu.add_command(label="Lovely", command=lovely)
submenu.add_command(label="Default", command=default)
optionMenu.add_cascade(label="Themes", menu=submenu ,underline=0)




menubar.add_cascade(label="Options", underline=0, menu=optionMenu)


######

mixer.init()


#########################################################################################################################
#----------------------------------------------------------------------------------------------------------------#
#--------#----------------------------                                                         -------------------------#
#--------#-----------        |\  /|   /\   |  |\  |       |`````` |```\    /\    |\  /| |``````    -------------------------#
#--------#-----------        | \/ |  /--\  |  | \ |       |````   |.../   /--\   | \/ | |---       -------------------------#
# -------#-----------        |    | /    \ |  |  \|       |       |   \  /    \  |    | |_____     -------------------------#
#--------#-----------------------------                                                         ----------------------#
#----------------------------------------------------------------------------------------------------------------#
#########################################################################################################################




leftframe = Frame(root, relief=FLAT, bd=4)
leftframe.place(x=0,y=0,width=280, height=350 )

rightframe = Frame(root,relief=FLAT, bd=4)
rightframe.place(x=280,y=0,width=596, height=350 )



##################################################################################################################################
##################################################################################################################################
##################################################################################################################################


#----------------------------------------------------------......
#       |       |``````  |``````  ```|```                       /
#       |       |---     |----       |                         /
#       |______ |_____   |           |                        /                                                       /
#------------------------------------------------------------/




info = Label(leftframe, text="PLAYLIST",font='Times 15 italic')
info.pack(pady=1)



playlistframe = Frame(leftframe)
playlistframe.place(x=30, y=25)

scroll_y=Scrollbar(playlistframe,orient=VERTICAL)
scroll_y.pack(side=RIGHT, fill=Y)

scroll_x=Scrollbar(playlistframe,orient=HORIZONTAL)
scroll_x.pack(side=BOTTOM, fill=X)

playlistbox = Listbox(playlistframe, height=12, width=25, font="Times", xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
playlistbox.pack()

scroll_y.config(command=playlistbox.yview)
scroll_x.config(command=playlistbox.xview)

buttonframeleft = Frame(leftframe)
buttonframeleft.place(y=290, x=25)

def del_song():
    Msg = tkinter.messagebox.askquestion ("Confirmation","Are you sure ,you want to Delete this Song?",icon = 'warning')
    if Msg == 'yes':
        selected_song = playlistbox.curselection()
        selected_song = int(selected_song[0])
        playlistbox.delete(selected_song)
        playlist.pop(selected_song)

        tkinter.messagebox.showinfo("Task Completed", "Song Deleted Sucessfully", icon="info")

    else:
        pass




adddarkPhoto = PhotoImage(file='images\madddark.png')
deldarkPhoto = PhotoImage(file='images\deldark.png')


lovelyaddPhoto = PhotoImage(file='images\lovelyadd.png')
lovelydelPhoto = PhotoImage(file='images\lovelydel.png')


addPhoto = PhotoImage(file='images\madd.png')
delPhoto = PhotoImage(file='images\del.png')



addbtn = Button(buttonframeleft, image=addPhoto, width=105,command=browse, bd=0)
addbtn.grid(row=0, column=0)
delbtn = Button(buttonframeleft, image=delPhoto, width=105, command=del_song, bd=0)
delbtn.grid(row=0, column=1)

############ CONTROL PANEL  FRAME###################

controlpanel = Frame(root, relief=GROOVE, bd=2)
controlpanel.place(x=0, y=354, width=875, height=130)

buttoncon = Frame(controlpanel, bd=0)
buttoncon.place(x=180,y=45, width=570, height=70)


#################################### play



def play_music():
    global paused
    global filename_path

    if paused:

        mixer.music.unpause()
        statusbar['text']= "Music is Resumed"

        paused = False

    else:
        try:
            global index
            global selected_song
            global play_it
            global currentindex


            stop_music()
            time.sleep(1)
            selected_song = playlistbox.curselection()
            selected_song = int(selected_song[0])
            currentindex = selected_song
            play_it = playlist[selected_song]

            mixer.music.load(play_it)
            mixer.music.play()
            statusbar['text']= "Current playing song --" + '' + os.path.basename(play_it)
            show_details(play_it)

        except:
            tkinter.messagebox.showerror('NO song selected ','Please select a SONG from open menu')

lovelyplayPhoto = PhotoImage(file="images\lovelyplay.png")
darkplayPhoto = PhotoImage(file='images\darkplay.png')
playPhoto = PhotoImage(file='images\play.png')
playBtn = Button(buttoncon, image = playPhoto , command=play_music, bd=0)
playBtn.grid(row=0,column=0,padx=8)

############################## Pause music ##############################

paused = False

def pause_music():



    global paused
    paused = True

    mixer.music.pause()
    statusbar['text']= "Music is paused"



lovelypausePhoto = PhotoImage(file="images\lovelypause.png")
darkpausePhoto = PhotoImage(file='images\darkpause.png')
pausePhoto = PhotoImage(file='images\pause.png')
pauseBtn = Button(buttoncon, image = pausePhoto , command=pause_music, bd=0)
pauseBtn.grid(row=0,column=1, padx=8)

################################ Stop music ########################3########

def stop_music():
    global paused

    mixer.music.stop()
    statusbar['text']= "Music is stopped"
    paused = False

lovelystopPhoto = PhotoImage(file="images\lovelystop.png")
darkstopPhoto = PhotoImage(file='images\darkstop.png')
stopPhoto = PhotoImage(file='images\stop.png')
stopBtn = Button(buttoncon, image = stopPhoto , command=stop_music, bd=0)
stopBtn.grid(row=0,column=2, padx=8)



############################

lengthlable = Label(controlpanel, text="Total Length- 00:00", font=("Times", 15, "italic"))
lengthlable.grid(row=0, column=4, padx=200, pady=10)

currenttimelable = Label(controlpanel, text="Current Time- 00:00", font=("Times", 15, "italic"))
currenttimelable.grid(row=0, column=5, pady=10)


#####################################
def show_details(play_it):
    wallpaper['text']= "Current playing song --" + '' + os.path.basename(play_it)

    file_data = os.path.splitext(play_it)

    if file_data[1] == '.mp3':
        audio = MP3(play_it)
        total_length = audio.info.length
    else:
        a = mixer.Sound(play_it)
        total_length = a.get_length()

    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    lengthlable['text'] = "Total Length" + ' - ' + timeformat

    t1 = threading.Thread(target=start_count, args=(total_length,))
    t1.start()


def start_count(t):
    global paused
    currenttime = 0
    while currenttime<=t and mixer.music.get_busy() :


        if paused:
            continue
        else:
            mins, secs = divmod(currenttime, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            currenttimelable['text']= "Current time --" + '' + timeformat

            time.sleep(1)
            currenttime += 1






# % % % % % % % % % % % %% % % % % %% % % % % %% % % % % %% % % % % %% % % % % %% % % % % %% % % % % %

#----------------------------------------------------------......
#       |`````\   |  |````````\  |     |   `````|````          /
#       |_____/   |  |           |_____|        |             /
#       |     \   |  |    ```|   |     |        |            /
#       |      \  |  |_______|   |     |        |           /
#                                                          /
#---------------------------------------------------------/


#####################################
#                                   #
#        UPPER Frame                #
#                                   #
# ###################################
upperframe = Frame(rightframe)
upperframe.place(x=0, y= 0)

### upper frame componenets ########

sadphoto = PhotoImage(file='images\sad.png')
happyphoto = PhotoImage(file='images\happy.png')
motivphoto = PhotoImage(file='images\motivation.png')
studyphoto = PhotoImage(file='images\study.png')
gamephoto = PhotoImage(file='images\gaming.png')

partyphoto = PhotoImage(file='images\party.png')
wallpaper = Label(upperframe, image=partyphoto)
wallpaper.pack(fill=BOTH)












#######################################  Next music ####################################


def move_s():
    global indexm
    stop_music()
    time.sleep(1)
    filetoread = playlist[indexm]
    mixer.music.load(filetoread)
    mixer.music.play()
    show_detailsn(filetoread)
    statusbar['text']= "Current playing song --" + '' + os.path.basename(filetoread)

def move(cond):
    global currentindex
    global nextm
    global prevm
    global indexm
    if cond == "nextm":
        indexm = currentindex
        indexm +=1
        currentindex = indexm
        move_s()
    elif cond== "prevm":
        indexm = currentindex
        indexm -=1
        currentindex = indexm
        move_s()




def next_music():
    move("nextm")

def show_detailsn(filetoread):
    wallpaper['text']= "Current playing song --" + '' + os.path.basename(filetoread)

    file_data = os.path.splitext(filetoread)

    if file_data[1] == '.mp3':
        audio = MP3(filetoread)
        total_length = audio.info.length
    else:
        a = mixer.Sound(filetoread)
        total_length = a.get_length()

    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    lengthlable['text'] = "Total Length" + ' - ' + timeformat

    t2 = threading.Thread(target=start_countn, args=(total_length,))
    t2.start()


def start_countn(f):
    global paused
    currenttime = 0
    while currenttime<=f and mixer.music.get_busy() :


        if paused:
            continue
        else:
            mins, secs = divmod(currenttime, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            currenttimelable['text']= "Current time --" + '' + timeformat

            time.sleep(1)
            currenttime += 1







lovelynextPhoto = PhotoImage(file='images\lovelynext.png')
darknextPhoto = PhotoImage(file='images\darknext.png')
nextPhoto = PhotoImage(file='images\knext.png')
nxtBtn = Button(buttoncon, image = nextPhoto , command=next_music, bd=0)
nxtBtn.grid(row=0, column=5, padx=8)


#######################################  Prev music ####################################






def prev_music():
    move("prevm")




def show_detailsp(filetoreadprv):
    wallpaper['text']= "Current playing song --" + '' + os.path.basename(filetoreadprv)

    file_data = os.path.splitext(filetoreadprv)

    if file_data[1] == '.mp3':
        audio = MP3(filetoreadprv)
        total_length = audio.info.length
    else:
        a = mixer.Sound(filetoreadprv)
        total_length = a.get_length()

    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    lengthlable['text'] = "Total Length" + ' - ' + timeformat

    t2 = threading.Thread(target=start_countp, args=(total_length,))
    t2.start()


def start_countp(f):
    global paused
    currenttime = 0
    while currenttime<=f and mixer.music.get_busy() :


        if paused:
            continue
        else:
            mins, secs = divmod(currenttime, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            currenttimelable['text']= "Current time --" + '' + timeformat

            time.sleep(1)
            currenttime += 1







lovelyprevPhoto = PhotoImage(file='images\lovelyprev.png')
darkpevPhoto = PhotoImage(file='images\darkprev.png')
prevPhoto = PhotoImage(file='images\prev.png')
prevBtn = Button(buttoncon, image = prevPhoto , command=prev_music, bd=0)
prevBtn.grid(row=0, column=4, padx=8)


############################################# Mute music ####################################
muted = False

def darkmute_music():
    global muted
    if muted:
        mixer.music.set_volume(50)
        volumeBtn.config(image=darkvolumePhoto)
        scale.set(50)
        muted = False
        statusbar['text']= "Music is unmute"
    else:
        mixer.music.set_volume(0)
        volumeBtn.config(image=darkmutePhoto)
        scale.set(0)
        muted = True
        statusbar['text']= "Music is muted"



def lovelymute_music():
    global muted
    if muted:
        mixer.music.set_volume(50)
        volumeBtn.config(image=lovelyvolumePhoto)
        scale.set(50)
        muted = False
        statusbar['text']= "Music is unmute"
    else:
        mixer.music.set_volume(0)
        volumeBtn.config(image=lovelymutePhoto)
        scale.set(0)
        muted = True
        statusbar['text']= "Music is muted"




def mute_music():
    global muted
    if muted:
        mixer.music.set_volume(50)
        volumeBtn.config(image=volumePhoto)
        scale.set(50)
        muted = False
        statusbar['text']= "Music is unmute"
    else:
        mixer.music.set_volume(0)
        volumeBtn.config(image=mutePhoto)
        scale.set(0)
        muted = True
        statusbar['text']= "Music is muted"


lovelymutePhoto = PhotoImage(file='images\lovelymute.png')
lovelyvolumePhoto = PhotoImage(file='images\lovelyvol.png')


darkmutePhoto = PhotoImage(file='images\darkmute.png')
darkvolumePhoto = PhotoImage(file='images\darkvolu.png')

mutePhoto = PhotoImage(file='images\mute.png')
volumePhoto = PhotoImage(file='images\mvolume.png')
volumeBtn = Button(buttoncon, image = volumePhoto , command=mute_music, bd=0)

volumeBtn.grid(row=0, column=6,padx=8)

########################################### Volume adjuster ##########################33#######

def set_vol(val):
    Volume = float(val) / 100
    mixer.music.set_volume(Volume)



scale = Scale(buttoncon, from_=0, to=100, orient=HORIZONTAL, command=set_vol, sliderrelief=FLAT, activebackground='dark orange')
scale.set(50)
mixer.music.set_volume(50)
scale.grid(row=0, column=7, padx=8)






##############################################################################
#############################################################################
################################################################################

statusbar = ttk.Label(root, text="Welcome to Fire", relief=SUNKEN, anchor=W, font='Times 12 italic')
statusbar.pack(side=BOTTOM, fill=X)


def on_closing():

    Msg = tkinter.messagebox.askquestion ("Confirmation","Do you want to Close the Player ( music will be stopped) ?",icon = 'warning')

    if Msg == 'yes':
        stop_music()
        root.destroy()
    else:
        pass




root.protocol("WM_DELETE_WINDOW", on_closing)
root.resizable(0, 0)
root.mainloop()
