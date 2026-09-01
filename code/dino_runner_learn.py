import raylib as rl
from pyray import *
from os.path import join

init_window(1280, 800, 'dino runner') #to draw the picture
init_audio_device()#if we want to play sound need this
set_target_fps(60)
x_pos=200
y_pos=400
r_deg=0
target_color=BLUE
floor_pos=500
start_pos=Vector2(int(x_pos),int(y_pos))
dino_texture=load_texture(join('assets','dino','run0.png'))#to load the picture
#join('assets','dino','run0.png') will give you the correct file path with the correct slash according to your os
cs_forn=load_font(join('fonts','RETRO_SPACE.ttf'))#to load the font
jump_sound=load_sound(join('audio','jump.wav'))#to load the sound
music = load_music_stream(join('audio','music.mp3'))
#play_music_stream(music)

while not window_should_close():
   # update_music_stream(music)
    begin_drawing()
    clear_background(WHITE)
    draw_line_ex(Vector2(0,floor_pos),Vector2(1280,floor_pos),20,GRAY)

    y_pos=400
    #inputs
    if is_key_down(rl.KEY_DOWN) or is_key_down(rl.KEY_S):
        y_pos += 2
    if is_key_down(rl.KEY_UP) or is_key_down(rl.KEY_W):
        y_pos -= 2
    if is_key_down(rl.KEY_RIGHT) or is_key_down(rl.KEY_D):
        x_pos += 2
        #r_deg +=2
    if is_key_down(rl.KEY_LEFT) or is_key_down(rl.KEY_A):
        x_pos -= 2
        #r_deg -=2
        play_sound(jump_sound)#to play the sound  
    if is_key_down(rl.KEY_SPACE):
        y_pos -= 100
    if is_key_pressed(rl.KEY_ESCAPE):
        close_window()# to close the window


    #drawing basic shapes
    #draw_circle(x_pos,y_pos,80,RED)
    #draw_circle(500,600,80,target_color)
    #draw_line(x_pos,y_pos,500,600,YELLOW)
    #draw_line_ex(Vector2(x_pos,y_pos),Vector2(800,200),40,BROWN)

    draw_texture_ex(dino_texture,Vector2(x_pos,y_pos),r_deg,3,WHITE)# to draw the image the we imported with scaling option
    #draw_rectangle(200,0,400,200,GRAY)

    #collision
    #rect_colli=check_collision_recs(
     #   Rectangle(200,0,400,200),
      #  Rectangle(x_pos,y_pos,dino_texture.width*5,dino_texture.height*5)#x-position,y position,width,height
    #)
      #print(rect_colli)
  
        
    
    #if check_collision_circles(Vector2(x_pos,y_pos),80,Vector2(500,600),80):
     #   target_color=BLACK
    #else:
     #   target_color=BLUE

    #text
    #draw_text(f'hi azia your time start now :{int(get_time())}' ,10,10,40,ORANGE)
   # text_width= measure_text(cs_forn,'hello bizhar',40,1).x
    # draw_text_ex(cs_forn,'hello bizhar ',Vector2(150,200),40,1,RED)
    # draw_text_ex(cs_forn,'hello kadheeaj ',Vector2(150,250),40,1,PURPLE)
    draw_text_ex(cs_forn,'welcome to dino game  ',Vector2(300,50),40,1,GRAY)
    
    end_drawing()