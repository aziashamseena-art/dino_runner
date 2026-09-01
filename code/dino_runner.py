import raylib as rl
from pyray import *
from os.path import join

init_window(1280, 800, 'dino runner')
init_audio_device()
set_target_fps(60)

#VARIABLES
floor_pos=500
velocity=0
gravity=0.8
dino_pos=Vector2(200,400)
cac_pos=1000
cac_timer=0
cac_intervel=3
obs_list=[]



#LOAD MULTIMEDIA
dino_texture=load_texture(join('assets','dino','run0.png'))
cac_1=load_texture(join('assets','cactii','cactus0.png'))
cs_forn=load_font(join('fonts','RETRO_SPACE.ttf'))
jump_sound=load_sound(join('audio','jump.wav'))
music = load_music_stream(join('audio','music.mp3'))
play_music_stream(music)

while not window_should_close():
    update_music_stream(music)
  # obstracle logic
    cac_timer += 0.02
    if cac_timer > cac_intervel:
        cac_timer=0
        obs_list.append(Vector2(1280,floor_pos))

    for obstacle in obs_list:
       obstacle.x -= 8
      
    begin_drawing()
    clear_background(WHITE)
    draw_line_ex(Vector2(0,floor_pos + 105),Vector2(1280,floor_pos + 105),20,GRAY)
    #text
    score = f'SCORE : {int(get_time())}'
    text_width=measure_text_ex(cs_forn,score,40,1).x
    draw_text_ex(cs_forn,score,Vector2(640 - text_width /2,50),40,1,GRAY)
    
  #inputs
    if is_key_pressed(rl.KEY_ESCAPE):
       close_window()

  #GAME CHARACTERS
    draw_texture_ex(dino_texture,dino_pos,0,5,WHITE)
    for obstacle_pos in obs_list:
     draw_texture_ex(cac_1,obstacle_pos,0,4,WHITE)

    #player movement
    velocity += gravity
    dino_pos.y += velocity
    if dino_pos.y > floor_pos:
        dino_pos.y=floor_pos
    if is_key_pressed(rl.KEY_SPACE):
        velocity = -25
       

        play_sound(jump_sound)

    #collision
    rino_rect = Rectangle(dino_pos.x,dino_pos.y,dino_texture.width*5,dino_texture.height*5)
    for obst in obs_list:
       cac_rect = Rectangle(obst.x,floor_pos,cac_1.width*4,cac_1.width*4)
       if check_collision_recs(rino_rect,cac_rect):
        exit()
      
    end_drawing()