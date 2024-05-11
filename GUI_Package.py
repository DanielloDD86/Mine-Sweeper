import pygame
from time import sleep
import sqlite3 as sql
import Default_ruleset as dr

#test commit
class MAIN():

    def __init__(self) -> None:
        """instantiates the GUI"""

        pygame.init()
        pygame.mixer.init()
        self.splayer = pygame.mixer.Channel(0)
        self.screen = pygame.display.set_mode([1536,864])
        #self.FONT = pygame.font.Font("Caffeinated Design/Assets/font.ttf", 32)
        self.global_y_offset = 0

        self.buttons = []
        self.sbuttons = []
        self.popups = []
        self.textboxes = []
        self.tables = []

        self.sounds = []

        self.running = True
        self.status = "setup"

        self.BUTTONS()
        self.SBUTTONS()
        self.POPUPS()
        self.TEXTBOXES()
        self.TABLES()
        self.SOUNDS()

        self.bonus_operation = ""

        self.size = (10,8)
        self.guess_num = 0
        self.ruleset = "Normal"
        self.game = dr.GAME(self.size,15)
        self.button_offset = len(self.buttons)
        self.render_board(self.game.get_board())

        self.main_loop()

    def BUTTONS(self):
        """used to instantiate all buttons"""

        #self.buttons.append(Button_2_func(pygame.image.load(r"Assets/Normal_Unflagged.png").convert_alpha(),(100,100),self.guess,self.flag))

        #self.buttons.append(Button(pygame.image.load(r"Testing folder\IMG_9440.png").convert_alpha(),(-500,0),self.func,False,pygame.image.load(r"Testing folder\IMG_9441.png")))

    def SBUTTONS(self):
        """Used for system buttons that dont move with scrolling aka on the overlay"""

        pass

    def TEXTBOXES(self):
        """used to instantiate all textboxes"""

        pass

    def POPUPS(self):
        """used to instantiate all popups (aka non interactable image)"""
        pass

    def TABLES(self):
        """used to instantiate all the Tables (2d arrays)"""
        pass


    def SOUNDS(self):
        """used to instantiate sounds that will be used later"""

        pass

    def display_update(self):
        """updates the display each frame,
        no need to touch"""

        self.screen.fill("#C0C0C0")
        #self.screen.blit(pygame.image.load("Caffeinated Design/Assets/Background.png").convert_alpha(),(0,0))

        for table in self.tables:
            if table.visible == True:

                try:
                    #print("trying")
                    self.screen.blit(table.rendered, (table.rect.x,table.rect.y))
                    table.frame_update()

                except:
                    pass

        for popup in self.popups:
            if popup.visible == True:

                try:
                    self.screen.blit(popup.image_shown, popup.rect)
                    popup.update(self.screen)

                except:
                    pass

        for button in self.buttons:
            if button.visible == True:

                try:
                    self.screen.blit(button.image_shown, button.rect)
                    button.update(self.screen)

                except:
                    pass

        for box in self.textboxes:
            if box.visible == True:

                try:
                    box.draw(self.screen)

                except:
                    pass

        #self.screen.blit(pygame.image.load("Caffeinated Design/Assets/Overlay_Final.png").convert_alpha(),(0,0))

        for button in self.sbuttons:
            if button.visible == True:

                try:
                    self.screen.blit(button.image_shown, button.rect)
                    button.update(self.screen)

                except:
                    pass

        pygame.display.update()

    def update_screen(self):
        """the main bit,
        add statments for self.status to trigger events"""

        for box in self.textboxes:
            if box.visible == True:
                box.update()

        if self.game.running == False and (self.status != "Lost" or self.status != "finished"):
            self.status = "Lost"

        if self.status == "setup":
            
            #self.buttons[0].show()
            pass       


        #elif self.status == "animation_test1":

        #    if int(5.0*(round(self.buttons[0].position[0]/5.0))) == int(5.0*(round(self.buttons[0].final_pos[0]/5.0))) or int(5.0*(round(self.buttons[0].position[1]/5.0))) == int(5.0*(round(self.buttons[0].final_pos[1]/5.0))): 
        #        self.buttons[0].animate((200,700),100)

        #    if int(5.0*(round(self.textboxes[0].rect.x/5.0))) == int(5.0*(round(self.textboxes[0].final_pos[0]/5.0))) or int(5.0*(round(self.textboxes[0].rect.y/5.0))) == int(5.0*(round(self.textboxes[0].final_pos[1]/5.0))): 
        #        self.textboxes[0].animate((300,300),240)

        #    self.status = "animation_test2"

        #elif self.status == "animation_test2":

        #    if int(5.0*(round(self.buttons[0].position[0]/5.0))) == int(5.0*(round(self.buttons[0].final_pos[0]/5.0))) or int(5.0*(round(self.buttons[0].position[1]/5.0))) == int(5.0*(round(self.buttons[0].final_pos[1]/5.0))): 
        #        self.buttons[0].animate((200,self.buttons[0].position[1]),100)

        #    if int(5.0*(round(self.textboxes[0].rect.x/5.0))) == int(5.0*(round(self.textboxes[0].final_pos[0]/5.0))) or int(5.0*(round(self.textboxes[0].rect.y/5.0))) == int(5.0*(round(self.textboxes[0].final_pos[1]/5.0))): 
        #        self.textboxes[0].animate((300,self.textboxes[0].position[1]),240)


        elif self.status == "Lost":
            for y,row in enumerate(self.game.get_board()):
                for x,item in enumerate(row):
                    if item.get_mines() == -1:
                        self.buttons[self.button_offset+x+y*self.size[0]].hide()
            self.display_update()
            sleep(3)
            self.status = "finished"   

        if self.status == "finished":

            pygame.quit()
            sleep(1)
            quit()

    def event_loop(self):
        """takes user input,
        no need to touch"""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
                quit()

            for box in self.textboxes:
                if box.visible == True:
                    box.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:

                    if button.visible == True:
                        button.on_click(event)
                
                for button in self.sbuttons:

                    if button.visible == True:
                        button.on_click(event)

            if event.type == pygame.MOUSEWHEEL:
                #self.scroll(event.y)
                pass
            
            if event.type == pygame.KEYDOWN:
                pass

        for button in self.buttons:
            button.check_hover()

        for button in self.sbuttons:
            button.check_hover()

        for popup in self.popups:
            popup.check_hover()

    def main_loop(self):
        """main loop,
        updates everything every frame,
        no need to touch"""
        while self.running == True:

            self.update_screen()
            self.event_loop()
            self.display_update()

    def scroll(self,direction):
        """enables scrolling,
        no need to touch"""

        multiplier = 30
        for item in self.buttons:
            if item.scrollable == True:
                item.animate((item.position[0],item.final_pos[1]+multiplier*direction),multiplier/5)

        for item in self.popups:
            if item.scrollable == True:
                item.animate((item.position[0],item.final_pos[1]+multiplier*direction),multiplier/5)

        for item in self.textboxes:
            if item.scrollable == True:
                item.animate((item.position[0],item.final_pos[1]+multiplier*direction),multiplier/5)

        for item in self.tables:
            if item.scrollable == True:
                item.animate((item.position[0],item.final_pos[1]+multiplier*direction),multiplier/5)

    # Add callbacks from buttons and textboxes here
    # always include param as it sends it regardless of whether its necessary

    #def func(self,param):
    #    self.status = "animation_test1"

    def shutdown(self,param):
        """shuts down the gui"""
        self.status = "finished"
        self.update_screen()

    def close_all(self):
        """closes all active scrollable objects"""
        for item in self.buttons:
            item.hide()

        for item in self.popups:
            item.hide()

        for item in self.textboxes:
            item.hide()

        for item in self.tables:
            item.hide()
            
    def guess(self,pos):
        self.buttons[self.button_offset+pos[0]+pos[1]*self.size[0]].hide()
        self.guess_num +=1
        if self.guess_num == 1:
            clears = self.game.first_tile(pos)
            self.rerender_back(self.game.get_board())
        else:
            clears = self.game.guess(pos)
        
        if len(clears) > 0:
            for item in clears:
                self.buttons[self.button_offset+item[0]+item[1]*self.size[0]].hide()

    def flag(self,pos):
        print("flag")
        print(pos)
        self.game.flag(pos)
        if self.game.get_flagged(pos) == True:
            self.buttons[self.button_offset+pos[0]+pos[1]*self.size[0]].image = pygame.image.load(fr"Assets/{self.ruleset}_flagged.png")
            self.buttons[self.button_offset+pos[0]+pos[1]*self.size[0]].hover_over_image = pygame.image.load(fr"Assets/{self.ruleset}_flagged_Hover.png")
        else:
            self.buttons[self.button_offset+pos[0]+pos[1]*self.size[0]].image = pygame.image.load(fr"Assets/{self.ruleset}_Unflagged.png")
            self.buttons[self.button_offset+pos[0]+pos[1]*self.size[0]].hover_over_image = pygame.image.load(fr"Assets/{self.ruleset}_Unflagged_Hover.png")


    def render_board(self,board):
        #del self.buttons[self.button_offset:]
        back = pygame.Surface((len(board[0])*30,len(board)*30))
        for y, row in enumerate(board):
            for x, item in enumerate(row):
                back.blit(pygame.image.load(fr"Assets/{self.ruleset}_{item.get_mines()}.png").convert_alpha(),(x*30,y*30))
        self.popups.append(PopUp(back,(5,5)))
        self.popups[-1].show()
        for y, row in enumerate(board):
            for x, item in enumerate(row):
                self.buttons.append(Button_2_func(pygame.image.load(fr"Assets/{self.ruleset}_Unflagged.png"),(self.popups[-1].rect.x + x*30,self.popups[-1].rect.y + y*30),self.guess,self.flag,False,pygame.image.load(fr"Assets/{self.ruleset}_Unflagged_Hover.png"),(x,y),scrollable=False))
                self.buttons[-1].show()

    def rerender_back(self,board):
        self.popups.pop()
        back = pygame.Surface((len(board[0])*30,len(board)*30))
        for y, row in enumerate(board):
            for x, item in enumerate(row):
                back.blit(pygame.image.load(fr"Assets/{self.ruleset}_{item.get_mines()}.png").convert_alpha(),(x*30,y*30))
        self.popups.append(PopUp(back,(5,5)))
        self.popups[-1].show()



class PopUp:
    def __init__(self, image, position = (0,0),hover_over_image = None, text = "", offset_x = 5, offset_y = 5,scrollable = True):
        """image is the image of the popup,
        position is the coordinate of the top left corner where it spawns in,
        hover_over_image is an option to have it change how it looks when a user hovers over it,
        text is what is printed on the popup image,
        offsets are for the number of pixels of text from the top left corner"""

        self.image = image
        self.image_shown = image
        self.hovered_over = False

        if hover_over_image == None:
            self.hover_over_image = image
        else:
            self.hover_over_image = hover_over_image

        self.position = position
        self.original_pos = position
        self.final_pos = position

        self.step_size = (0,0)
        self.rect = image.get_rect(topleft=position)
        self.text = text

        self.offset_x = offset_x
        self.offset_y = offset_y
        self.visible = False
        self.scrollable = scrollable

    def update(self,screen):
        """internal works, ignore"""
        self.FONT = pygame.font.Font("Assets/font.ttf", 32)

        if self.text != "":
            surface_text = self.FONT.render(self.text,True,"white")
            screen.blit(surface_text, (self.rect.x+self.offset_x, self.rect.y+self.offset_y))

        if int(5.0*(round(self.position[0]/5.0))) != int(5.0*(round(self.final_pos[0]/5.0))) or int(5.0*(round(self.position[1]/5.0))) != int(5.0*(round(self.final_pos[1]/5.0))):
            self.position = (self.position[0]+self.step_size[0],self.position[1]+self.step_size[1])
            self.rect = self.image.get_rect(topleft=self.position)

        elif int(5.0*(round(self.position[0]/5.0))) == int(5.0*(round(self.final_pos[0]/5.0))) or int(5.0*(round(self.position[1]/5.0))) == int(5.0*(round(self.final_pos[1]/5.0))):
            self.step_size = (0,0)


    def move(self,position):
        """position is a tuple of coordinates
        teleports popup/button to new cords,
            avoid, use animate instead"""
        
        self.rect = self.image.get_rect(topleft=position)
        self.position = position

    def animate(self,final_pos,duration):
        """Gradually moves the popup/button to new position,
        Final_pos is tuple of coordinates,
           Duration is the length in frames"""
        
        self.original_pos = self.position
        self.final_pos = final_pos
        self.step_size = ((self.final_pos[0]-self.original_pos[0])/duration,(self.final_pos[1]-self.original_pos[1])/duration)

        if self.step_size[0]<1 and self.step_size[0] > 0:
            self.step_size = (1,self.step_size[1])
        elif self.step_size[0]>-1 and self.step_size[0] < 0:
            self.step_size = (-1,self.step_size[1])

        """elif self.step_size[0]>5:
            self.step_size = (5,self.step_size[1])
        elif self.step_size[0]<-5:
            self.step_size = (-5,self.step_size[1])"""
        
        if self.step_size[1]<1 and self.step_size[1] > 0:
            self.step_size = (self.step_size[0],1)
        elif self.step_size[1]>-1 and self.step_size[1] < 0:
            self.step_size = (self.step_size[0],-1)

        """elif self.step_size[1]>5:
            self.step_size = (self.step_size[0],5)
        elif self.step_size[1]<-5:
            self.step_size = (self.step_size[0],-5)"""

    def check_hover(self):
        """internal works, ignore"""

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hovered_over = True
            self.image_shown = self.hover_over_image
            self.rect = self.image_shown.get_rect(topleft=self.position)

        else:
            self.hovered_over = False
            self.image_shown = self.image
            self.rect = self.image_shown.get_rect(topleft=self.position)

    def show(self):
        """used to make the popup/button visible"""
        self.visible = True

    def hide(self):
        """used to make the popup/button hidden"""
        self.visible = False

class Button(PopUp):
    def __init__(self, image, position, callback,hide_after_use = True,hover_over_image = None, param = "", text = "", offset_x = 5, offset_y = 5,scrollable = True):
        """image is the image of the button,
        position is the coordinate of the top left corner where it spawns in,
        callback is the function which is triggered upon clicking,
        hide_after_use is self explanatory,
        param is what is what parameter is supplied to the callback function - often used for multiple buttons to same function,
        hover_over_image is an option to have it change how it looks when a user hovers over it,
        text is what is printed on the button image,
        offsets are for the number of pixels of text from the top left corner"""

        super().__init__(image, position,hover_over_image, text, offset_x, offset_y,scrollable)
        self.callback = callback
        self.param = param
        self.HAU = hide_after_use
 
    def on_click(self, event):
        """Internal works, ignore"""

        if event.button == 1:
            if self.rect.collidepoint(event.pos):

                if self.HAU == True:
                    self.hide()
                if self.param == "#pos#":
                    self.callback(event.pos)
                else:
                    self.callback(self.param)
                    

class Button_2_func(Button):

    def __init__(self, image, position, callback, callback_2, hide_after_use=True, hover_over_image=None, param="", text="", offset_x=5, offset_y=5, scrollable=True):
        super().__init__(image, position, callback, hide_after_use, hover_over_image, param, text, offset_x, offset_y, scrollable)
        self.callback_2 = callback_2

    def on_click(self, event):
        """Internal works, ignore"""

        if event.button == 1:
            if self.rect.collidepoint(event.pos):

                if self.HAU == True:
                    self.hide()
                if self.param == "#pos#":
                    self.callback(event.pos)
                else:
                    self.callback(self.param)

        elif event.button == 3:
            if self.rect.collidepoint(event.pos):

                if self.HAU == True:
                    self.hide()
                if self.param == "#pos#":
                    self.callback_2(event.pos)
                else:
                    self.callback_2(self.param)
                    
    
class InputBox:

    def __init__(self, position, w, h,font,callback, text="", offset_x = 5, offset_y = 5,scrollable = True):
        """position is a tuple of coordinates of the top left corner,
        w is the width in pixels,
        h is the height in pixels,
        font is the pygame font definition - just use self.FONT,
        callback is the function to which the result of the text input is sent to,
        offsets are the spacing between the text and top and left edge"""
        self.rect = pygame.Rect(position[0], position[1], w, h)
        self.position = (position[0],position[1])
        self.original_pos = (position[0],position[1])
        self.final_pos = (position[0],position[1])

        self.step_size = (0,0)
        self.color = pygame.Color("White")
        self.text = text
        self.FONT = font

        self.txt_surface = self.FONT.render(text, True, self.color)
        self.callback = callback
        self.offset_x = offset_x
        self.offset_y = offset_y

        self.active = False
        self.visible = False
        self.scrollable = scrollable

    def handle_event(self, event):
        """internal works, ignore"""

        if event.type == pygame.MOUSEBUTTONDOWN:

            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active

            else:
                self.active = False

            # Change the current color of the input box.
            self.color = pygame.Color("white") if self.active else pygame.Color("blue")

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:

                    self.callback(self.text)
                    self.text = ''
                    self.hide()

                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]

                else:
                    self.text += event.unicode
                
                # Re-render the text.
                self.txt_surface = self.FONT.render(self.text, True, self.color)

    def update(self):
        """Internal works, ignore"""

        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width
        self.position = (self.rect.x,self.rect.y)

        if int(5.0*(round(self.rect.x/5.0))) != int(5.0*(round(self.final_pos[0]/5.0))) or int(5.0*(round(self.rect.y/5.0))) != int(5.0*(round(self.final_pos[1]/5.0))):
            self.rect.x = self.rect.x+self.step_size[0]
            self.rect.y = self.rect.y+self.step_size[1]

        elif int(5.0*(round(self.rect.x/5.0))) == int(5.0*(round(self.final_pos[0]/5.0))) or int(5.0*(round(self.rect.y/5.0))) == int(5.0*(round(self.final_pos[1]/5.0))):
            self.step_size = (0,0)

    def draw(self, screen):
        """Internal works, ignore"""

        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+self.offset_x, self.rect.y+self.offset_y))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def animate(self,final_pos,duration):
        """Gradually moves the textbox to new position,
        Final_pos is tuple of coordinates
        Duration is the length in frames"""

        self.position = (self.rect.x,self.rect.y)
        self.original_pos = self.position
        self.final_pos = final_pos
        self.step_size = ((self.final_pos[0]-self.original_pos[0])/duration,(self.final_pos[1]-self.original_pos[1])/duration)

        if self.step_size[0]<1 and self.step_size[0] > 0:
            self.step_size = (1,self.step_size[1])

        elif self.step_size[0]>-1 and self.step_size[0] < 0:
            self.step_size = (-1,self.step_size[1])

        elif self.step_size[0]>5:
            self.step_size = (5,self.step_size[1])

        elif self.step_size[0]<-5:
            self.step_size = (-5,self.step_size[1])

        if self.step_size[1]<1 and self.step_size[1] > 0:
            self.step_size = (self.step_size[0],1)

        elif self.step_size[1]>-1 and self.step_size[1] < 0:
            self.step_size = (self.step_size[0],-1)

        elif self.step_size[1]>5:
            self.step_size = (self.step_size[0],5)

        elif self.step_size[1]<-5:
            self.step_size = (self.step_size[0],-5)

    def show(self):
        """used to make the textbox visible"""

        self.visible = True
        self.active = True

    def hide(self):
        """used to make the textbox hidden"""

        self.visible = False
        self.active = False

class Table:

    def __init__(self, x, y,font , data, headers, offset_x = 5, offset_y = 5,text_colour = "#000000", primary_colour = "#C0C0C0", secondary_colour = "#F0F0F0", border_colour = None,scrollable = True) -> None:
        self.data = data
        self.headers = headers
        self.FONT = font
        self.text_colour = text_colour

        self.primary_colour = primary_colour
        self.secondary_colour = secondary_colour
        self.border_colour = border_colour

        self.offset_x = offset_x
        self.offset_y = offset_y
        self.scrollable = scrollable

        #print(self.FONT.render(str("Orders"),True,self.color).get_width()+10)
        self.widths,self.total_width,self.cuttable_columns = self.max_width_generator()
        self.total_rows, self.rows, self.header_rows = self.row_counter()
        self.rect = pygame.Rect(x, y, self.total_width, (42+2*self.offset_y)*(self.total_rows))

        self.rendered = self.render()
        self.position = (x,y)
        self.original_pos = (x,y)
        self.final_pos = (x,y)

        self.step_size = (0,0)
        self.active = False
        self.visible = False
        self.quick_print()

    def row_counter(self):
        """Internal works, ignore:
        cuts down table columns that are too long to be able to fit on the page correctly,
        Returns the; number of extra lines added; the distribution of those lines and how many extra lines for the headers, 
        used to calculate table dimensions"""

        max_rows = []
        try:
            max_pos = 0
            while self.total_width > 1486:
                max_val = 0

                for i,width in enumerate(self.widths):
                    if self.cuttable_columns[i] == True and width > max_val:
                        max_pos,max_val = i,width

                target_val = max_val - 20
                lines = str(self.headers[max_pos]).splitlines()

                for current_line,line in enumerate(lines):
                    if self.width_checker(line)[0] >= target_val and len(line) > 1:
                        midpoint = len(line)//2
                        lines[current_line] = line[:midpoint] + "\n" + line[midpoint:]

                new_data = ""
                for o,line in enumerate(lines):
                    if o == 0:
                        new_data+= line

                    elif o != 0:
                        new_data+= "\n" + line

                self.headers[max_pos] = new_data

                for i,row in enumerate(self.data):
                    lines = str(row[max_pos]).splitlines()

                    for current_line,line in enumerate(lines):

                        if self.width_checker(line)[0] >= target_val and len(line) > 1:
                            midpoint = len(line)//2
                            lines[current_line] = line[:midpoint] + "\n" + line[midpoint:]

                    new_data = ""

                    for o,line in enumerate(lines):
                        if o == 0:
                            new_data+= line

                        elif o != 0:
                            new_data+= "\n" + line

                    self.data[i][max_pos] = new_data
                        
                self.widths,self.total_width,self.cuttable_columns = self.max_width_generator()

            for i in range(len(self.data)):
                max_rows.append(0)


            for i,row in enumerate(self.data):

                for o,data in enumerate(row):
                    if self.cuttable_columns[o] == True:
                        max_rows[i] = max(max_rows[i],int(str(data).count("\n"))+1)
                    # Trying to get image heights in rows here:  
                    else:
                        height = pygame.image.load(data).convert_alpha().get_height()
                        if height/42 > height//42:
                            max_rows[i] = max(max_rows[i],int((height//42)+1))
                        else:
                            max_rows[i] = max(max_rows[i],int(height//42))                  

            header_rows = 0

            for data in self.headers:
                header_rows = max(header_rows,int(str(data).count("\n"))+1)

            return sum(max_rows) + header_rows,max_rows,header_rows
        
        except:
            print("SHITNADO")
            return 0,[0],0

    def max_width_generator(self):
        """Internal works, ignore:
        returns the; distribution of widths per column; total width and distribution of what column can be trimmed"""

        max_widths = []
        cuttable_columns = []

        try:

            for i in range(len(self.headers)):
                max_widths.append(0)
                cuttable_columns.append(True)

            for i,item in enumerate(self.headers):
                max_widths[i] = max(max_widths[i],self.width_checker(item)[0])

            try:
                for row in self.data:

                    for i,item in enumerate(row):
                        max_widths[i] = max(max_widths[i],self.width_checker(item)[0])

                        if self.width_checker(item)[1] == False:
                            cuttable_columns[i] = False
            except:
                pass

            total_width = 0

            for width in max_widths:
                total_width+=width

            return max_widths,total_width,cuttable_columns

        except:

            print("VERY SHIT")
            return [0],0, [False]
        
    def width_checker(self,item):
        """Internal works, ignore:
        returns the width of the data and whether its cuttable"""

        try:
            if ".png" not in str(item) and ".jpeg" not in str(item) and ".jpg" not in str(item) and ".gif" not in str(item) and ".bmp" not in str(item) and ".tiff" not in str(item):
                widths = []
                lines = str(item).splitlines()

                for line in lines:
                    widths.append(self.FONT.render(str(line),True,self.text_colour).get_width()+2*self.offset_x)

                width = max(widths)
                cuttable = True

            elif ".png" in str(item) or ".jpeg" in str(item) or ".jpg" in str(item) or ".gif" in str(item) or ".bmp" in str(item) or ".tiff" in str(item):

                width = pygame.image.load(item).convert_alpha().get_width()+2*self.offset_x
                cuttable = False

            else:

                width = 0
                cuttable = False
            return width,cuttable
        
        except:
            print("SHIT")

            return 0,False
        
    def quick_print(self):
        """Internal works, ignore:
        testing script"""

        for header in self.headers:
            print(header,end=" |    ")
        print()

        for row in self.data:
            for item in row:
                print(item,end=" |    ")
            print()

    def render(self):
        """Internal works, ignore:
        renders the table,
        returns the pysurface of the table"""

        self.widths,self.total_width,self.cuttable_columns = self.max_width_generator()

        rendered = pygame.Surface((self.rect.w,self.rect.h))
        try:

            for o,data in enumerate(self.headers):
                item = pygame.Surface((self.widths[o],self.header_rows*(42+2*self.offset_y)))

                if self.border_colour == None:
                    if (1+o)%2 == 0:
                        item.fill(self.primary_colour)

                    else:
                        item.fill(self.secondary_colour)

                else:
                    item.fill(self.border_colour)

                    if (1+o)%2 == 0:
                        pygame.draw.rect(item,self.primary_colour,(2,2,self.widths[o]-4,(self.header_rows*(42+2*self.offset_y))-4))

                    else:
                        pygame.draw.rect(item,self.secondary_colour,(2,2,self.widths[o]-4,(self.header_rows*(42+2*self.offset_y))-4))

                #print(sum(self.widths[:o]))
                item.blit(self.FONT.render(str(data),True,self.text_colour),(self.offset_x,self.offset_y))
                rendered.blit(item,(sum(self.widths[:o]),0))

            for i,row in enumerate(self.data):
                for o,data in enumerate(row):
                    item = pygame.Surface((self.widths[o],self.rows[i]*(42+2*self.offset_y)))

                    if self.border_colour == None:
                        if (i+o)%2 == 0:
                            item.fill(self.primary_colour)

                        else:
                            item.fill(self.secondary_colour)

                    else:
                        item.fill(self.border_colour)

                        if (i+o)%2 == 0:
                            pygame.draw.rect(item,self.primary_colour,(2,2,self.widths[o]-4,(self.rows[i]*(42+2*self.offset_y))-4))

                        else:
                            pygame.draw.rect(item,self.secondary_colour,(2,2,self.widths[o]-4,(self.rows[i]*(42+2*self.offset_y))-4))

                    if self.cuttable_columns[o] == True:

                        lines = str(data).splitlines()

                        for p, line in enumerate(lines):
                            item.blit(self.FONT.render(str(line),True,self.text_colour),(self.offset_x,self.offset_y+p*(42+2*self.offset_y)))
                        rendered.blit(item,(sum(self.widths[:o]),(sum(self.rows[:i])+self.header_rows)*(42+2*self.offset_y)))
                    
                    else:

                        item.blit(pygame.image.load(data).convert_alpha(),(self.offset_x,self.offset_y))
                        rendered.blit(item,(sum(self.widths[:o]),(sum(self.rows[:i])+self.header_rows)*(42+2*self.offset_y)))
        except:
            pass

        return rendered
    
    def animate(self,final_pos,duration):
        """Gradually moves the table to new position,
        Final_pos is tuple of coordinates
           Duration is the length in frames"""
        
        self.position = (self.rect.x,self.rect.y)
        self.original_pos = self.position
        self.final_pos = final_pos
        self.step_size = ((self.final_pos[0]-self.original_pos[0])/duration,(self.final_pos[1]-self.original_pos[1])/duration)

        if self.step_size[0]<1 and self.step_size[0] > 0:
            self.step_size = (1,self.step_size[1])

        elif self.step_size[0]>-1 and self.step_size[0] < 0:
            self.step_size = (-1,self.step_size[1])

        elif self.step_size[0]>5:
            self.step_size = (5,self.step_size[1])

        elif self.step_size[0]<-5:
            self.step_size = (-5,self.step_size[1])

        if self.step_size[1]<1 and self.step_size[1] > 0:
            self.step_size = (self.step_size[0],1)

        elif self.step_size[1]>-1 and self.step_size[1] < 0:
            self.step_size = (self.step_size[0],-1)

        elif self.step_size[1]>5:
            self.step_size = (self.step_size[0],5)

        elif self.step_size[1]<-5:
            self.step_size = (self.step_size[0],-5)


    def frame_update(self):
        """Internal works, ignore:
        used to animate each frame"""

        self.position = (self.rect.x,self.rect.y)

        if int(5.0*(round(self.rect.x/5.0))) != int(5.0*(round(self.final_pos[0]/5.0))) or int(5.0*(round(self.rect.y/5.0))) != int(5.0*(round(self.final_pos[1]/5.0))):
            self.rect.x = self.rect.x+self.step_size[0]
            self.rect.y = self.rect.y+self.step_size[1]

        elif int(5.0*(round(self.rect.x/5.0))) == int(5.0*(round(self.final_pos[0]/5.0))) or int(5.0*(round(self.rect.y/5.0))) == int(5.0*(round(self.final_pos[1]/5.0))):
            self.step_size = (0,0)

    def replace_data(self,data,headers):
        """used to replace the data in the table,
        data is the new table as specified in the testing purposes function at the bottom of the document or in SQL_GUIDE.py,
        Headers is the list of headers for the table"""

        self.data = data
        self.headers = headers
        self.widths,self.total_width,self.cuttable_columns = self.max_width_generator()

        self.total_rows, self.rows, self.header_rows = self.row_counter()
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.total_width, (42+2*self.offset_y)*(1+self.total_rows))
        self.rendered = self.render()

    def show(self):
        """used to make the table visible"""

        self.visible = True

    def hide(self):
        """used to make the table hidden"""

        self.visible = False



class BOARD:

    def  __init__(self,ruleset,size,mines):

        if ruleset == "Normal":
            self.game = dr.GAME(size,mines)
        else:
            self.game = dr.GAME(size,mines)

        self.board = self.game.get_board()











"""# this crap is just here for testing purposes so i have some data to actually render
conn = sql.connect("database.db") # creates a connection object for the database
db = conn.cursor() # creates the object that allows SQL commands to be executed

def SQL_to_array(database,command):
    """#database: the python database object
#    command: the sql statment
#    ONE COMMAND AT ONCE
"""

    database.execute(command)
    rows = database.fetchall()
    table = []

    for row in rows:
        data_row = []

        for data in row:
            data_row.append(data)
            
        table.append(data_row)
    return table


example_data = SQL_to_array(db,"SELECT * FROM books")



conn.commit() # saves all changes to the DB

conn.close()"""



GUI = MAIN()
GUI.main_loop()