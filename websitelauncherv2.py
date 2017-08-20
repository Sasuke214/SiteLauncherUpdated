import webbrowser
from tkinter import *
import os

class WebSiteLauncher:
         def __init__(self):
                  #initialize the sourceFile to the file containing urls
                  #if no list file is there create 1 giving default techsanjal.com
                  self.EntryVariable=StringVar()
                  self.PlayListVariable=StringVar()
                  
                  self.InputUrlStore=[]
                  self.PlayListVariable.set("")

                  #initial file name
                  self.CurrentlySelectedFile="PlayList.txt"
                  
                  #checking whether main file is there or not
                  self.CheckForFile(self.CurrentlySelectedFile)
                  
                  #Creating Frame for all different windows
                  self.Frame1=Frame(root)
                  self.Frame2=Frame(root)
                  self.Frame3=Frame(root)
                  self.MainFrame=Frame(root)
                  self.ViewFrame=Frame(root)
                  self.AddPlayListFrame=Frame(root)
                  self.DeletePlayListFrame=Frame(root)
                  self.DeletePlayList=False
                  
                  self.FirstPhase()
         #checks for availability of file if not create one
         def CheckForFile(self,fname):
                  try:
                           d=open(fname)
                           d.close()
                  except:
                           d=open(fname,'w+')
                           d.close()
                  
         
         ##Main Phase 
         def Main2NormalConnector(self,fname,index):
                  if self.DeletePlayList:
                           #deleting content from  file
                           with open("PlayList.txt","w+") as newfile:
                                    counter=0
                                    for s in self.AllList:
                                             counter+=1
                                             if not s==fname:
                                                      if counter==len(self.AllList): 
                                                               newfile.write(s)
                                                      else:
                                                               newfile.write(s+'\n')
                                    
                                    #removing  if it has its own text file
                                    try:
                                             os.remove(fname+".txt")
                                    except:
                                             a=a
                                    finally:
                                             self.AllList.remove(fname)
                                             self.listboxPlaylist.delete(index)
                                    
                  else:
                           self.ViewFrame.destroy()
                           self.CheckForFile(self.CurrentlySelectedFile)
                           #check if file is empty
                           sourceFile=open(self.CurrentlySelectedFile,"r+")
                           alldata=sourceFile.read().split('\n')
                           if alldata[0]=="":
                                    sourceFile=open(self.CurrentlySelectedFile,mode='w+')
                                    sourceFile.write("www.google.com")
                                    sourceFile.close()
          
                           #
                           self.SetMainGui()
                  
         #call this whenever any item from list is clicked
         def ClickedList(self,event):
                  try:
                           #event.widget is listbox
                           w=event.widget
                           index=int(w.curselection()[0])
                           name=w.get(index)
                           self.CurrentlySelectedFile=name+'.txt'
                           self.Main2NormalConnector(name,index)
                  except:
                           self.CurrentlySelectedFile="PlayList.txt"
                           return
         #will take the playlist name, saves in file and return to mainframe
         def FromAddToFirst(self):
                  inputList=self.PlayListVariable.get()
                  self.PlayListVariable.set("")
                  if inputList=="":
                           return
                  with open(self.CurrentlySelectedFile,"a+") as csf:
                           csf.write('\n'+inputList)
                  self.AddPlayListFrame.destroy()
                  self.FirstPhase()
         #For Deleting Playlist
         def DeleteList(self):
                  self.DeletePlayList=True
                  self.ViewAll()
         #for adding new playlist
         def AddPlayList(self):
                  #destroy and creation
                  self.MainFrame.destroy()
                  self.AddPlayListFrame=Frame(root)
                  self.AddPlayListFrame.pack()
                  
                  self.PlistLabel=Label(self.AddPlayListFrame,text="Enter yourPlayListName:")
                  self.Plistinputbox=Entry(self.AddPlayListFrame,textvariable=self.PlayListVariable)
                  self.Nextbtn=Button(self.AddPlayListFrame,text="Next",command=self.FromAddToFirst)                  
                  self.PlistLabel.pack()
                  self.Plistinputbox.pack()
                  self.Nextbtn.pack()

                  
         def ViewAll(self):
                  #destroy and creation
                  self.MainFrame.destroy()
                  self.ViewFrame=Frame(root)
                  self.ViewFrame.pack()
                  
                  self.MainmainMenu=Button(self.ViewFrame,text="MainMenu",command=self.FirstPhase)
                  
                  ##list and scrollbar
                  ##
                  scrlbarV=Scrollbar(self.ViewFrame,orient=VERTICAL)
                  scrlbarH=Scrollbar(self.ViewFrame,orient=HORIZONTAL)

                  scrlbarV.pack(side=RIGHT,fill=Y)
                  scrlbarH.pack(side=BOTTOM,fill=X)

                  self.listboxPlaylist=Listbox(self.ViewFrame,yscrollcommand=scrlbarV.set,xscrollcommand=scrlbarH.set)
                  self.listboxPlaylist.pack(expand=YES,fill=BOTH)
                  #call the function choosebyclick when clicked in listbox
                  self.listboxPlaylist.bind('<<ListboxSelect>>', self.ClickedList)
                  for i in range(0,len(self.AllList)):
                           if self.AllList[i]!="":
                                    self.listboxPlaylist.insert(i,self.AllList[i])
                  scrlbarV.config(command=self.listboxPlaylist.yview)
                  scrlbarH.config(command=self.listboxPlaylist.xview)                  

                  self.MainmainMenu.pack()
                  
         #Main Phase of all        
         def FirstPhase(self):
                  self.DeletePlayList=False
                  try:
                           self.DeletePlayListFrame.destroy()
                           self.ViewFrame.destroy()
                  except:
                           a=a
                  self.MainFrame=Frame(root)
                  self.MainFrame.pack()
                  
                  #clearing the previous inputs
                  self.InputUrlStore.clear()
                  #retreiving names of all playlists
                  with open("PlayList.txt") as Pl:
                           self.AllList=Pl.read().split('\n')         

                  ##Main GUI
                  LabelDetail=Label(self.MainFrame,text="Your PlayList:")
                  ButtonAdd=Button(self.MainFrame,text="Add",command=self.AddPlayList)
                  ButtonView=Button(self.MainFrame,text="View All",command=self.ViewAll)
                  ButtonDelete=Button(self.MainFrame,text="Delete",command=self.DeleteList)
                  LabelDetail.pack()
                  ButtonAdd.pack()
                  ButtonView.pack()
                  ButtonDelete.pack()
                  ##
                  
         
         
         ##Main Phase End               
                  
         #setting GUI for main window
         def SetMainGui(self):
                  try:
                           self.Frame2.destroy()
                  except:
                           a=a
                  try:
                           self.Frame3.destroy()
                  except:
                           a=a
                           
                  self.Frame1=Frame(root)
                  self.Frame1.grid()
                  
                  self.StartBtn=Button(self.Frame1,text="Launch",command=self.StartLaunch)
                  self.UrlInputBtn=Button(self.Frame1,text="InputUrl",command=self.SetInputGui)
                  self.DeleteUrlBtn=Button(self.Frame1,text="DeleteUrl",command=self.SetDeleteGui)
                  self.StartBtn.grid(row=0)
                  self.UrlInputBtn.grid(row=1)
                  self.DeleteUrlBtn.grid(row=2)

         ##InputStart
         #Setting GUI for input             
         def SetInputGui(self):
                  self.Frame1.destroy()
                  self.Frame2=Frame(root)
                  self.Frame2.grid()
                  
                  self.label=Label(self.Frame2,text="Enter your FileName:")
                  self.inputBox=Entry(self.Frame2,textvariable=self.EntryVariable)
                  self.nextbtn=Button(self.Frame2,text="Next",command=self.UrlInput)
                  self.MainMenu=Button(self.Frame2,text="MainMenu",command=self.LoadUrl)
                  self.label.grid()
                  self.inputBox.grid(row=1)
                  self.nextbtn.grid(row=2)
                  self.MainMenu.grid(row=3)
                  
         #Gettin url in entry box
         def UrlInput(self):
                  
                  inputUrl=str(self.inputBox.get())
                  self.EntryVariable.set("")
                  #checking if the given url is empty
                  if inputUrl=="":
                           #messagebox.showerror("Error","Please Assign the url")
                           return
                  #if not empty adding it to list
                  self.InputUrlStore.append(inputUrl)
                  
         #Loading url in database
         def LoadUrl(self):
                  self.UrlInput()
                  self.GetUrlList()
                  with open(self.CurrentlySelectedFile,'a+') as sourceFile:
                           counter=0
                           for s in self.InputUrlStore:
                                    counter+=1
                                    if not s in self.UrlList:
                                                      sourceFile.write('\n'+s)
                  self.InputUrlStore.clear()
                  self.SetMainGui()
                  
         ##InputEnd
                  


         ##LaunchStart 
         #launch the url got as siteUrl argument         
         def Launch(self,siteUrl):    
                  webbrowser.open(siteUrl)
                  
         #Extracts all urls from url input file
         def GetUrlList(self):
                  with open(self.CurrentlySelectedFile) as sourceFile:
                           self.UrlList=sourceFile.read().split('\n')
                  
         #start the siteLaunch
         def StartLaunch(self):
                  self.GetUrlList()
                  for s in self.UrlList:
                           if(str(s)!=""):
                                    self.Launch(str(s))
                  #To Exit The File 
                  root.destroy()
         ##LaunchEnd

         ##DeleteStart

         #delete completely
         def DeleteFile(self,urlindex,url):
                  self.listbox.delete(urlindex)
                  #getting the current item in file
                  self.GetUrlList()
                  #deleting content from  file
                  with open(self.CurrentlySelectedFile,"w+") as newfile:
                           counter=0
                           for s in self.UrlList:
                                    counter+=1
                                    if not s==url:
                                             if counter==len(self.UrlList): 
                                                      newfile.write(s)
                                             else:
                                                     newfile.write(s+'\n') 
                  
         #to choose whether to launch that or delete
         def ChooseByClick(self,clickedEvent):
                  #getting widget which send this event
                  try:
                           w=clickedEvent.widget
                           index=int(w.curselection()[0])
                           #getting link from listbox
                           urllink=w.get(index)
                           self.Launch(urllink)
                           self.DeleteFile(index,urllink)
                  except:
                           return

                  
                  
                  
         #setting GUI for delete
         def SetDeleteGui(self):
                  self.Frame1.destroy()
                  self.Frame3=Frame(root)
                  self.Frame3.pack()
                  
                  

                  self.MainMenu=Button(self.Frame3,text="MainMenu",command=self.SetMainGui)
                  
                  ##List to list all available links
                  self.GetUrlList()

                  ##list and scrollbar
                  self.lasFrame=Frame(self.Frame3)
                  self.lasFrame.pack()
                  ##
                  scrlbarV=Scrollbar(self.Frame3,orient=VERTICAL)
                  scrlbarH=Scrollbar(self.Frame3,orient=HORIZONTAL)

                  scrlbarV.pack(side=RIGHT,fill=Y)
                  scrlbarH.pack(side=BOTTOM,fill=X)

                  self.listbox=Listbox(self.Frame3,yscrollcommand=scrlbarV.set,xscrollcommand=scrlbarH.set)
                  self.listbox.pack(expand=YES,fill=BOTH)
                  #call the function choosebyclick when clicked in listbox
                  self.listbox.bind('<<ListboxSelect>>', self.ChooseByClick)
                  for i in range(0,len(self.UrlList)):
                           if self.UrlList[i]!="":
                                    self.listbox.insert(i,self.UrlList[i])
                  scrlbarV.config(command=self.listbox.yview)
                  scrlbarH.config(command=self.listbox.xview)
                  ##
                  self.MainMenu.pack()
                  
         ##DeleteEnd
         
root=Tk()
wlauncher=WebSiteLauncher()
root.mainloop()
