from importss import*

fire_rate_time = 0
y1 = 0
y2 = -1080

p.init()

piy = p.mixer.Sound('piu.mp3')

spawn_enemys()
finish = False
menu = True
boss_fight = False
roundn = 1
points = 0

# texts
font = p.font.SysFont('Arial', 40, True)
small_font = p.font.SysFont('Arial', 30, False)
stat_font = p.font.SysFont('Arial', 15, False)
boss_health = small_font.render(f'Boss health: ?', True, (255, 0, 0))
defeat_txt = font.render('defeat!', True, (255, 0, 0))
win_txt = font.render('win!', True, (0, 255, 0))
roundn_txt = small_font.render(f'Round {roundn}', True, (255, 255, 0))
points_txt = stat_font.render(f'Points: {points}', True, (255, 255, 0))
menu_txt = font.render('SHUTER', True, (255, 255, 255))

# функція для перезапуску
def reset():
    global enemy_list, bullets, enemy_bullets, enemyboss, boss_fight, roundn, points
    enemy_list.clear()
    bullets.clear()
    enemy_bullets.clear()
    enemyboss = ENEMYBOSS()
    enemyboss.rect.x = 0
    enemyboss.rect.y = 0
    boss_fight = False
    spawn_enemys()
    roundn = 1
    points = 0


while True:
    if menu:
        SCREEN.blit(menu_bg, (0,0))
        SCREEN.blit(menu_txt, (170, 200))
        button.draw_img()
    if not finish and not menu:
        fire_rate_time += 1
        # відображення ----------------------------------
        SCREEN.blit(background, (0,y1))  
        SCREEN.blit(background, (0,y2))

        roundn_txt = small_font.render(f'Round {roundn}', True, (255, 255, 0))
        SCREEN.blit(roundn_txt, (400, 0))
        points_txt = stat_font.render(f'Points: {points}', True, (255, 255, 0))
        SCREEN.blit(points_txt, (400, 30))

        y1+=3
        y2+=3

        if y1 > 1080:
            y1 = -1080
        if y2> 1080:
            y2 = -1080
        # ------------------------------------------------


        # ігрок ----------------------------------------
        player.move()
        player.draw_img()
        #-----------------------------------------------


        # стрільба --------------------------------
        for event in p.event.get():
            if event.type == p.MOUSEBUTTONDOWN:
                if fire_rate_time > 30:
                    bullets.append(BULLET(player))
                    piy.play(0)
                    fire_rate_time = 0
        # -----------------------------------------


        # ворог ---------------------------------------
        for enemy in enemy_list:
            enemy.move()
            enemy.draw_img()
            #enemy.shooting(enemy_bullets, ENEMY_BULLET, enemy)

            if enemy.rect.y > SCREENSIZE[1]:
                reset()
        #-------------------------------------------


        # кулі --------------------------------------
        for bullet in bullets:
            bullet.move()
            bullet.draw_img()
            for enemy in enemy_list:
                if enemy.rect.colliderect(bullet.rect):
                    bullets.remove(bullet)
                    enemy_list.remove(enemy)
                    points += 1
                  
        for bull in enemy_bullets:
            bull.draw_img()
            bull.move()

            if bull.rect.colliderect(player.rect):
                enemy_bullets.remove(bull)
                SCREEN.blit(defeat_txt, (210, 250))
                reset()
                finish = True
        #--------------------------------------------


        # босс --------------------------------------
        if not enemy_list:
            boss_fight = True      
        
        if boss_fight:
            SCREEN.blit(boss_health, (0, 0))
            enemyboss.move()
            enemyboss.draw_img()
            enemyboss.shooting(enemy_bullets, ENEMY_BULLET, enemyboss)

            for bullet in bullets:
                if enemyboss.rect.colliderect(bullet.rect):
                    bullets.remove(bullet)
                    enemyboss.health -= 1
            
            boss_health = small_font.render(f'Boss health:  {enemyboss.health}', True, (255, 0, 0))

            if enemyboss.rect.y > SCREENSIZE[1]:
                reset()
            
            if enemyboss.health <= 0:
                boss_fight = False
                finish = True
                SCREEN.blit(win_txt, (210, 250))

                enemyboss.rect.x = 0
                enemyboss.rect.y = 0
                enemyboss.reverse = False
                roundn += 1
                enemyboss.health = roundn * 5
                spawn_enemys()
        #----------------------------------------------
        
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()
        
        if menu and event.type == p.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if button.rect.collidepoint(x, y):
                menu = False

        if event.type == p.KEYDOWN and event.key == p.K_ESCAPE:
            menu = True
            finish = True

        if event.type == p.KEYDOWN and event.key == p.K_SPACE and finish == True:
            finish = False
                

    clock.tick(FPS)
    p.display.flip()