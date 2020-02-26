# A simple class that create a new GUI for the game
# v. 1.0
#
# Next version of this module will improved with a division of the various element in the GUI and a loose coupling
#
#

import tkinter as tk
from tkinter import *
import utils
import fire_water_ice

class game_gui:

    
    def __init__(self):
        """Create a new GUI to play Fire, Water and Ice Game.
        
        """

        self.root = tk.Tk()
        self.root.geometry("500x500")                                        # Height and Width Specification
        self.root.configure(background='#6290c3')                            # Background will be Silver Lake Blue  
        self.root.title("Fire Water Ice")
        self.root.resizable(False,False)                                     # Gui is not resizable


        
        # This function helps me to not write complete pathname
        utils.move_to_png_img_directory()
        
        # Creating a photoimage object to use image 
        fire_photo = PhotoImage(file = r"fire.png") 
        water_photo = PhotoImage(file = r"water.png")
        ice_photo = PhotoImage(file = r"snow.png")
        man_photo = PhotoImage(file = r"man.png")
        bot_photo = PhotoImage(file = r"bot.png")
        # Resizing image to fit on button 
        fire_photo_image = fire_photo.subsample(1, 1) 
        water_photo_image = water_photo.subsample(1, 1) 
        ice_photo_image = ice_photo.subsample(1, 1) 
        man_photo_image = man_photo.subsample(1, 1) 
        bot_photo_image = bot_photo.subsample(1, 1) 
        
        # A simple welcome label to the game
        self.welcome_label = tk.Label(self.root, text = "Welcome to Fire, Water and Ice ",
        padx = 240,
        pady = 10,
        bg = "#2a2a72",
        fg = "white",
        font=("Helvetica",12,"bold"))

        self.welcome_label.pack()
        
        # This frame is a container for all his children
        self.frame = tk.Frame(self.root, bg = "#f1f1f1")
        self.frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1,rely = 0.1)
       
        # This frame contains user logo and partial score
        self.user_frame = tk.Frame(self.frame, bg = "#f1f1f1")
        self.user_frame.place(relwidth = 0.5, relheight = 0.3, rely = 0) 

        self.user_icon_label = tk.Label(self.user_frame, image = man_photo_image)
        self.user_icon_label.place(relx = 0.2, rely = 0.2)
        self.user_points_labels = tk.Label(self.user_frame, text = 0,  font=('Futura',40,'bold'))
        self.user_points_labels.place(relx = 0.7, rely = 0.2)

        # This frame contains computer logo and partial score
        self.computer_frame = tk.Frame(self.frame, bg = "#f1f1f1")
        self.computer_frame.place(relwidth = 0.5, relheight = 0.3, relx = 0.5, rely = 0)

        self.computer_icon_label = tk.Label(self.computer_frame, image = bot_photo_image)
        self.computer_icon_label.place(relx = 0.4, rely = 0.2)
        self.computer_points_labels = tk.Label(self.computer_frame, text = 0, font=('Futura',40,'bold'))
        self.computer_points_labels.place(relx = 0.07, rely = 0.2)


        # This frame is a container for the 3 buttons in the GUI
        self.buttons_frame = tk.Frame(self.frame, bg = "#b8c5d6")
        self.buttons_frame.place(relwidth = 1, relheight = 0.5, rely = 0.3)
        
        # Grid layout
        self.fire_button = tk.Button(self.buttons_frame, relief = RAISED, text = "Fire", image = fire_photo_image, padx = 10, pady = 5, bg = "white", fg = "black", command = lambda : self.buttons_handler(1))  
        self.fire_button.grid(row = 0, column = 0, padx = (60,20), pady = 65)  # I need an extra space to the left
        
        self.water_button = tk.Button(self.buttons_frame, relief = RAISED, text = "Water", image = water_photo_image, padx = 10, pady = 5, bg = "white", fg = "black", command = lambda : self.buttons_handler(2) )  
        self.water_button.grid(row = 0, column = 1, padx =20, pady = 15)
        
        self.ice_button = tk.Button(self.buttons_frame, relief = RAISED, text = "Ice", image = ice_photo_image ,padx = 10, pady = 5, bg = "white", fg = "black", command = lambda : self.buttons_handler(3))  
        self.ice_button.grid(row = 0, column = 2, padx = 20, pady = 15)
        

        # Last frame displays computer choice and game result
        self.game_result_frame = tk.Frame(self.frame, bg = "#b8c5d6")
        self.game_result_frame.place(relwidth = 1, relheight = 0.3, rely = 0.7)

        # This label shows computer's choice
        self.computer_choice_label = tk.Label(self.game_result_frame, text = "", font=('Futura',14, 'bold',"italic"),bg = "#b8c5d6", fg = "blue")
        self.computer_choice_label.place(relx = 0.2, rely = 0.1)

        # This label shows final result
        self.result_messagge_label = tk.Label(self.game_result_frame, text = "", font=('Futura',18,'bold',"italic"),bg = "#b8c5d6", fg = "green")
        self.result_messagge_label.place(relx = 0.35, rely = 0.4)
        
        # Show window
        self.root.mainloop()

     
    
    def get_user_score(self):
        """ Return the value read in the corresponding label converted in an integer"""
        return int(self.user_points_labels["text"])

    def get_computer_score(self):
        """ Return the value read in the corresponding label converted in an integer"""
        return int(self.computer_points_labels["text"])

    def update_user_points(self,new_value):
        """ Set the corresponding label to a new specified value
            GUI now shows a new score """
        self.user_points_labels["text"] = new_value 

    def update_computer_points(self,new_value):
        """ Set the corresponding label to a new specified value
            GUI now shows a new score """
        self.computer_points_labels["text"] = new_value     

    def update_computer_choice_label(self,new_text):
        """ Set the corresponding label to a new specified value
            GUI now shows a new computer's choice """
        self.computer_choice_label["text"] = new_text

    def update_result_message_label(self,new_text):
        """ Display the winner of the match in last label"""
        self.result_messagge_label["text"] = new_text

    def update_result_message_label_text_color(self,new_color):
        """ Change color of last label. Possible colors are Green, Yellow and Red"""
        self.result_messagge_label.config(fg = new_color)
    
    def buttons_handler(self,button_pressed):
        """ Manage buttons clicks invoke method to start a new a game

            Parameters:
            button_pressed (int): A value that represents last pressed button. 
                Fire  -> 1
                Water -> 2
                Ice   -> 3
        """ 
        # Invokes a function to start a new game and get a list of two values: winner and computer's choice
        list_returned = fire_water_ice.get_user_choice(button_pressed)

        winner = list_returned[0]


        print("The winner is ",winner)
        if(winner == 1):
            # Case 1: Player Won
            self.update_user_points(self.get_user_score() + 1)
            label_text = "You Won!"
            font_color = "green"
        elif(winner == 2):
            # Case 2: Computer Won
            self.update_computer_points(self.get_computer_score() + 1)
            label_text = "You Lost!"
            font_color = "red"
        elif(winner == 3):
            # Case 3: Draw
            label_text = "It's a Draw"
            font_color = "yellow"


        # Update winner label
        self.update_result_message_label(label_text)
        self.update_result_message_label_text_color(font_color)
        self.update_computer_choice_label("Computer's choice is {}".format(list_returned[1]))


if __name__ == "__main__":
    gioco = game_gui()
   
        # Start a new game
        # Update GUI and scores with proper methods
    
 
    
