import csv
from tkinter import *
from tkinter import messagebox 
import playsound,vlc
import time,numpy as np
import matplotlib.pyplot as plt
import random
from gtts import gTTS 
from PIL import ImageTk ,Image
root=Tk()
root.geometry("800x500")
root.title("Quiz 2020")
class quiz: 
      v=IntVar()
      def __init__(self):
        self.setup()
        self.compliments=["Marvelous!! ","You hit the bull in the eye","Correct! You are a Genius","Superb!! Thats absolutely correct"]
      
      optlist=["ques","ans","opt1","opt2","opt3","opt4"]
      def setup(self):
           self.points=0
           self.a=0
           self.fifdis=False
           self.auddis=False
           self.phonedis=False

           self.mainframe=Frame(root,background="red",height=350,width=500)
           self.mainframe.pack(pady=100)
           Button(self.mainframe,text="Add Questions(Admin)",background="yellow",font=("Georgia",22,"bold"),command=lambda:self.main(1)).place(x=70,y=30)
           Button(self.mainframe,text="  ---->   Play Quiz  <----    ",background="yellow",font=("Georgia",22,"bold"),command=lambda:self.main(2)).place(x=70,y=150)

      def write(self,*ar):
          try:
               with open("pujan.txt","a") as f:
                    cv=csv.DictWriter(f,fieldnames=self.optlist)
                    cv.writerow(dict(zip(self.optlist,ar)))
               messagebox.showinfo("Saved","Question saved sucessfully")
                
          except:
              messagebox.showerror("Error","Cannot write in the file")
      def calcprob(self):
          list1=[i for i in range(20)]
          for i in range(5):
              random.shuffle(list1) 
          if list1[0]%2==0:
              return 0
          elif list1[1]<12:
                  return 1
          else:
                  return 2
                   
      def phonefunc(self):
          ans=self.selectedques["ans"]
          random.shuffle(self.btnlist)
          newone=list()
          for i in self.btnlist:
              if i["text"]!=ans:
                  newone.append(i["text"])
          random.shuffle(newone)
          newone2=[ans,newone[1]]
          random.shuffle(newone2)

          welcomelist=["Greetings my friend","Hello dear How can I help you?","Hello Hello dont worry I will help you"]
          surelist=["I am pretty sure the answer is "+ans,"You Lucky Dear the answer to this question is surely "+ans,
          "Ok my general knowledge says its "+ans+" for sure","I have read this somewhere it must be "+ans]
          confusedlist=["I am confused the answer can be either "+newone2[0]+" or "+newone2[1],"Not sure but it can be "+newone2[1]]
          guessinglist=["Sorry Dear i really dont have any idea about this","Never heard of it sorry friend i couldnt help","Oh my god I really dont know oh dear","Thanks for your faith upon me but i dont know the answer"]
          for i in range(10):
              random.shuffle(welcomelist)
              random.shuffle(surelist)
              random.shuffle(confusedlist)
              random.shuffle(guessinglist)
          for i in self.btnlist:
              i.configure(state="disabled")
          k=self.calcprob()
          if k==0:val=surelist[1]
          elif k==1:val=confusedlist[1]
          else:val=guessinglist[1]
          try:
              wlc = gTTS(text=welcomelist[1], lang='en', slow=False) 
              wlc.save("welcome.mp3") 
              
              wlc = gTTS(text=val, lang='en', slow=False) 
              wlc.save("phoneafriend.mp3") 
              puj=vlc.MediaPlayer("phonering.mp3")
              puj.play()
              time.sleep(6)
              puj.stop()
              playsound.playsound("welcome.mp3")
              playsound.playsound("phoneafriend.mp3")
              self.btnphone.configure(state="disabled")
              self.phonedis=True
          except:
              messagebox.showerror("Error","Cannot connect to your friend.\nWe use wireless phone calls so make sure you are connected to internet!")
              
          for i in self.btnlist:
              i.configure(state="normal")
          
      def makeplot(self,lis):
          ind1=lis.index(max(lis))
          list2=list()
          k=0
          for i in self.btnlist:
              list2.append(i["text"])
              if i["text"]==" ":lis[k]=0
              k+=1
          ind2=list2.index(self.selectedques["ans"])
          temp=lis[ind1]
          lis[ind1]=lis[ind2]
          lis[ind2]=temp
          ypos=np.arange(4)
          plt.xticks(ypos,list2)
          plt.bar(ypos,lis)
          self.auddis=True
          self.btnaud.configure(state="disabled")
          plt.show()
          
      def audiencefunc(self):
         list1=list()
         k=0
         try:
              for i in range(4):
                 list2=list(range(100-k))
                 for j in range(1,10):random.shuffle(list2)
                 if i!=3:val=list2[1]
                 else:val=100-k
                 
                 if val>95:continue
                 list1.append(val)
                 k=k+val
              self.makeplot(list1)
              

         except:
              pass
              
          
              
              

      
      
      
      def fiftyfunc(self):
          self.fifdis=True
          answ=self.selectedques["ans"]
          self.btnfif.configure(state="disabled")
          k=0
          random.shuffle(self.btnlist)
          for i in self.btnlist:
              if k==2:
                  break
              if i["text"]==answ:
                  continue
              else:
                  i.configure(text=" ")
                  k+=1
          
      def  unwrap(self,ques,*ar):
          opt=list()
          for i in ar:
              opt.append(i.get())
          ans=opt[self.v.get()-1]
          self.write(ques.strip(),ans,*opt)
          self.mainframe1.destroy()
          self.mainframe=Frame()
          self.main(1)
      def back(self):
          self.mainframe1.destroy()
          self.setup()
        
      def checkans(self,answer):
          random.shuffle(self.compliments)
          if self.selectedques["ans"]==answer:
              messagebox.showinfo("Hurray",self.compliments[0])
              self.points+=1
              self.mainframe1.destroy()
              self.mainframe=Frame()
              self.main(2)
              
          else:
              messagebox.showerror("Oops","Wrong answer the right answer is "+self.selectedques["ans"]+"\n Your score is: "+str(self.points))
              self.mainframe1.destroy()
              self.setup()
      def main(self,a):
           self.mainframe.destroy()
           self.mainframe1=Frame(root,background="red",height=400,width=750)
           self.mainframe1.pack(pady=60)
           aud=ImageTk.PhotoImage(Image.open("audience.png").resize((150,70)))
           phone=ImageTk.PhotoImage(Image.open("phoneafriend.png").resize((150,70)))
           fifty=ImageTk.PhotoImage(Image.open("fifty.png").resize((150,70)))
           if a==2:
               self.label1=Label(self.mainframe1,text="",height=2,width=40,font=("Georgia",15,"bold"))
               self.label1.place(x=50,y=70)
               self.pointlabel=Label(self.mainframe1,text="Your points:"+str(self.points),height=1,width=14,font=("Georgia",15,"bold"))
               self.pointlabel.place(x=500,y=10)
               Label(self.mainframe1)
               btn1=Button(self.mainframe1,text="",height=1,width=20,font=("Georgia",14,"bold"))
               btn1.place(x=30,y=180)
               btn2=Button(self.mainframe1,text="",height=1,width=20,font=("Georgia",14,"bold"))
               btn2.place(x=350,y=180)
               btn3=Button(self.mainframe1,text="",height=1,width=20,font=("Georgia",14,"bold"))
               btn3.place(x=30,y=230)
               btn4=Button(self.mainframe1,text="",height=1,width=20,font=("Georgia",14,"bold"))
               btn4.place(x=350,y=230)
               self.btnaud=Button(self.mainframe1,image=aud,bd=0,bg="red",command=lambda :self.audiencefunc())
               self.btnaud.image=aud
               if self.auddis==True:
                  self.btnaud.configure(state="disabled") 
               self.btnaud.place(x=30,y=300)
               self.btnfif=Button(self.mainframe1,image=fifty,bd=0,bg="red",command=lambda :self.fiftyfunc())
               self.btnfif.image=fifty
               self.btnfif.place(x=280,y=300)
               if(self.fifdis==True):
                   self.btnfif.configure(state="disabled")
               
               self.btnphone=Button(self.mainframe1,image=phone,justify="left",bd=0,bg="red",command=lambda :self.phonefunc())
               self.btnphone.image=phone
               self.btnphone.place(x=540,y=300)
               if(self.phonedis==True):
                   self.btnphone.configure(state="disabled")
               self.btnlist=[btn1,btn2,btn3,btn4]
               with open("pujan.txt","r") as f:
                   cv=list(csv.DictReader(f,fieldnames=self.optlist))
               indexlist=list(a for a in range(len(cv)))
               random.shuffle(indexlist)
               self.selectedques=cv[indexlist[0]]
               self.label1.configure(text=self.selectedques["ques"])
               optionlist=[self.selectedques["opt1"],self.selectedques["opt2"],self.selectedques["opt3"],self.selectedques["opt4"]]
               random.shuffle(optionlist)
               for i in range(len(optionlist)):
                       self.btnlist[i].configure(text=optionlist[i])
               btn1.configure(command=lambda:self.checkans(optionlist[0]))
               btn2.configure(command=lambda:self.checkans(optionlist[1]))
               btn3.configure(command=lambda:self.checkans(optionlist[2]))
               btn4.configure(command=lambda:self.checkans(optionlist[3]))

           else:
               Label(self.mainframe1,text="Question",font=("Georgia",18,"bold")).place(x=10,y=30)
               qu=Text(self.mainframe1,height=2,width=40,font=("Georgia",15,"bold"))
               qu.place(x=150,y=20)
               Label(self.mainframe1,text="Options",font=("Georgia",18,"bold")).place(x=10,y=110)
               en1=Entry(self.mainframe1,width=15,font=("Georgia",18,"bold"))
               en1.place(x=150,y=110)
               en2=Entry(self.mainframe1,width=15,font=("Georgia",18,"bold"))
               en2.place(x=450,y=110)
               en3=Entry(self.mainframe1,width=15,font=("Georgia",18,"bold"))
               en3.place(x=150,y=150)
               en4=Entry(self.mainframe1,width=15,font=("Georgia",18,"bold"))
               en4.place(x=450,y=150)
               Label(self.mainframe1,text="Answer",font=("Georgia",18,"bold")).place(x=10,y=200)
               values = {"a" : 1,"b" : 2,"c" : 3,"d" : 4} 
               xv=150
               for (text, value) in values.items(): 
                        Radiobutton(self.mainframe1, text = text, font=("Georgia",18,"bold"),variable = self.v, value = value).place(x=xv,y=200) 
                        xv+=80
               Button(self.mainframe1,relief=RAISED,bd=5,text="  Save  ",font=("Times New Roman",22,"bold"),command=lambda:self.unwrap(qu.get(1.0,END),en1,en2,en3,en4)).place(x=300,y=280)
               Button(self.mainframe1,relief=RAISED,bd=5,text="<--",font=("Times New Roman",22,"bold"),command=lambda:self.back()).place(x=600,y=280)
quiz()
root.mainloop()
