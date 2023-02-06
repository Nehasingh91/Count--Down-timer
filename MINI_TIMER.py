#importing packages----------------------------------------------------------------------------------------------------------------
import time
from tkinter import *
import multiprocessing
from tkinter import ttk, messagebox
from threading import *
#----------------------------------------------------------------------------------------------------------------------------------

#Lists For Combobox----------------------------------------------------------------------------------------------------------------
#Hour list for the combobox
Hour_List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,]

#Minute list for the combobox
Minute_List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 52, 53, 54, 55, 56, 57, 58, 59]

#Second list for the combobox
Second_List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 52, 53, 54, 55, 56, 57, 58, 59]
#----------------------------------------------------------------------------------------------------------------------------------



#Create a class for timer----------------------------------------------------------------------------------------------------------
class Countdown:
    #Constructor of the class Countdown
    def __init__(self, root):
        #Root Window Attributes-----------------------------------------------------------------------------------------------------
        self.root = root
        self.root.geometry("500x480")
        self.root.config(bg="lightblue")
        self.root.resizable(FALSE,FALSE)
        self.root.title("Count-Down Timer")
        self.pause=FALSE
        #--------------------------------------------------------------------------------------------------------------------------

        # CountDown Timer (Main Heading )------------------------------------------------------------------------------------------
        self.Title_Name = Label(self.root, text="Count-Down Timer", font="Times 30 bold",fg="Blue", bg="lightBlue")
        self.Title_Name.pack(pady=10)
       #---------------------------------------------------------------------------------------------------------------------------


        self.button_frame = Frame(self.root, bg="lightblue",width=240, height=40).place(x=230, y=150)
        # This frame is used to show the countdown time label
        self.time_frame = Frame(self.root, bg="lightblue",width=680, height=220).place(x=50, y=400)

    #Current Time --------------------------------------------------------------------------------
        def Current_time():
            ctime = time.strftime('%H:%M:%S %p')
            current_time.config(text=ctime)
            current_time.after(1000, Current_time)
        current_time = Label(root, font=("arial", 15, "bold"), text="", fg="black", bg="lightgrey", borderwidth=1, relief= "solid", height=2, width=20)
        current_time.place(x=100, y=70)
        Current_time()
    #-----------------------------------------------------------------------------------------------


    #Time Setting Display----------------------------------------------------------------------------
        Set_Time_Label= Label(self.root, text="Set Time:",font="Times 18 bold",bg="lightBlue", fg="Blue").place(x=10,y=150)
        hour_label = Label(self.root, text="Hour :", font=("times new roman", 15), bg="lightBlue", fg='black').place(x=10, y=190)
        minute_label = Label(self.root, text="Minute :", font=("times new roman", 15), bg="lightBlue", fg='black').place(x=170, y=190)
        second_label = Label(self.root, text="Second :", font=("times new roman", 15), bg="lightBlue", fg='black').place(x=340, y=190)
        Button_Option_Label= Label(self.root, text="Button Options:",font="Times 18 bold",bg="lightBlue", fg="Blue").place(x=10,y=230)
        #--------------------------------------------------------------------------------------------------

        #COMBOBOX Display -------------------------------------------------------------------------------------------------------
        
        #Hour Combo-Box Display
        self.hour= IntVar()
        self.hour_combobox=ttk.Combobox(self.root, width=5, height=5, textvariable=self.hour, font=("times new roman", 15))
        self.hour_combobox['values'] = Hour_List
        self.hour_combobox.current(0)
        self.hour_combobox.place(x=70, y=190)
        
        #Minute Combo-Box Display
        self.minute = IntVar()
        self.minute_combobox = ttk.Combobox(self.root, width=5, height=5, textvariable=self.minute, font=("times new roman", 15))
        self.minute_combobox['values'] = Minute_List
        self.minute_combobox.current(0)
        self.minute_combobox.place(x=245, y=190)

        #Second Combo-Box Display
        self.second = IntVar()
        self.second_combobox = ttk.Combobox(self.root, width=5, height=5, textvariable=self.second, font=("times new roman", 15))
        self.second_combobox['values'] = Second_List
        self.second_combobox.current(0)
        self.second_combobox.place(x=420, y=190)
        #-------------------------------------------------------------------------------------------------------------------------

       

        #SET/RESET BUTTON---------------------------------------------------------------------------------------------------------
        set_button = Button(self.root, text='Set/Reset',font=('Helvetica', 14), bg="RoyalBlue", fg="white",command=self.Get_Time, width=43)
        set_button.place(x=10, y=270)
        #-------------------------------------------------------------------------------------------------------------------------

    #STOP Function for Stop BUTTON-----------------------------------------------------------------------------------------------
    def stop(self):
        self.pause = True
        self.root.destroy()
    #-----------------------------------------------------------------------------------------------------------------------------

    
    #When Set Button is clicked this function is called-----------------------------------------------------------------------------
    def Get_Time(self):
        self.time_display = Label(self.time_frame,font=('Helvetica', 20, "bold"),bg='gray35', fg='yellow')
        self.time_display.place(x=150, y=370)
        #Exception Handling --------------------------------------------------------------------------------------------------------
        try:
            # Total amount of time in seconds------------------------------------------------------------------------
            h = (int(self.hour_combobox.get()) * 3600)
            m = (int(self.minute_combobox.get()) * 60)
            s = (int(self.second_combobox.get()))
            self.time_left = h + m + s
            #------------------------------------------------------------------------------------------------------------
            

            #Warning if combo-box is 0 and set button is clicked---------------------------------------------------------
            if s == 0 and m == 0 and h == 0:
                messagebox.showwarning('Warning!','Please select a right time to set')
            
            else:
                # Start Button------------------------------------------------------------------------------------------------------
                start_button = Button(self.button_frame,height=1, width=15, text='Start',font=('Helvetica', 12), bg="green", fg="white",command=self.Threading)
                start_button.place(x=10, y=320)
                #-------------------------------------------------------------------------------------------------------------------


                # Pause Button------------------------------------------------------------------------------------------------------
                pause_button = Button(self.button_frame,height=1, width=15, text='Pause', font=('Helvetica', 12), bg="red", fg="white", command=self.pause_time)
                pause_button.place(x=180, y=320)
                #-------------------------------------------------------------------------------------------------------------------

                 #STOP BUTTON--------------------------------------------------------------------------------------------------------------
                stop_button = Button(self.root, text='Stop',height=1, width=15, font=('Helvetica', 12), bg="white", fg="black", command=self.stop)
                stop_button.place(x=340, y=320)
                #------------------------------------------------------------------------------------------------------------------------
        except Exception as es:
            messagebox.showerror("Error!", f"Error due to {es}")
        #-----------------------------------------------------------------------------------------------------------------------------


    # Creating a thread to run the show_time function----------------------------------------------------------------------------------
    def Threading(self):
        self.x = Thread(target=self.start_time, daemon=True)
        self.x.start()
    #----------------------------------------------------------------------------------------------------------------------------------

    #Function to clear and destroy the widgets-----------------------------------------------------------------------------------------
    def Clear_Screen(self):
        self.root.destroy()
    #----------------------------------------------------------------------------------------------------------------------------------

    #Function to pause the timer-------------------------------------------------------------------------------------------------------
    def pause_time(self):

        self.pause = True
        mins, secs = divmod(self.time_left, 60)
        hours = 0
        if mins > 60:
            # hour minute
            hours, mins = divmod(mins, 60)

        self.time_display.config(text=f"Time Left: {hours}: {mins}: {secs}")
        self.time_display.update()

   #Function to start the timer after clicking the start button-----------------------------------------------------------------------
    def start_time(self):
        self.pause = False
        while self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)

            hours = 0
            if mins > 60:
                # hour minute----------------------------------------------------------------------------------
                hours, mins = divmod(mins, 60)

            self.time_display.config(text=f"Time Left: {hours}: {mins}: {secs}")
            self.time_display.update()
            # sleep function: for 1 second---------------------------------------------------------------------
            time.sleep(1)
            self.time_left = self.time_left - 1

            #if Time is over then message info show to exit program----------------------------------------------
            if self.time_left <= 0:
                messagebox.showinfo('Time Over', 'Time to exit program')
                # Clearing the 'self.button_frame' frame
                self.Clear_Screen()
            # if the pause button is pressed,the while loop will break----------------------------------------------
            if self.pause == True:
                break
    #--------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    root = Tk()
    # Creating a CountDown class object
    obj = Countdown(root)
    root.mainloop()
    #--------------------------------------------------------------------------------------------------

