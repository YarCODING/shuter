from importss import*

fire_rate_time = 0
y1 = 0
y2 = -1080

p.init()

font = p.font.SysFont('Arial', 40, True)
small_font = p.font.SysFont('Arial', 30, False)

boss_health = small_font.render(f'Boss health: ?', True, (255, 0, 0))

defeat_txt = font.render('defeat!', True, (255, 0, 0))
win_txt = font.render('win!', True, (0, 255, 0))

piy = p.mixer.Sound('piu.mp3')

spawn_enemys()
finish = False
boss_fight = False
roundn = 1
roundn_txt = font.render(f'Round {roundn}', True, (255, 255, 0))

while True:
    if not finish:
        fire_rate_time += 1
        SCREEN.blit(background, (0,y1))  
        SCREEN.blit(background, (0,y2))
        SCREEN.blit(roundn_txt, (325, 0))

        y1+=3
        y2+=3

        if y1 > 1080:
            y1 = -1080
        if y2> 1080:
            y2 = -1080

        player.move()
        player.draw_img()

        

        for event in p.event.get():
            if event.type == p.MOUSEBUTTONDOWN:
                if fire_rate_time > 30:
                    bullets.append(BULLET(player))
                    piy.play(0)
                    fire_rate_time = 0

        for enemy in enemy_list:
            enemy.move()
            enemy.draw_img()

        for bullet in bullets:
            bullet.move()
            bullet.draw_img()
            for enemy in enemy_list:
                if enemy.rect.colliderect(bullet.rect):
                    bullets.remove(bullet)
                    enemy_list.remove(enemy)


        for enemy in enemy_list:
            enemy.shooting(enemy_bullets, ENEMY_BULLET, enemy)
        
    
        for bull in enemy_bullets:
            bull.draw_img()
            bull.move()

            if bull.rect.colliderect(player.rect):
                enemy_bullets.remove(bull)
                SCREEN.blit(defeat_txt, (210, 250))
                finish = True

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
            
            if enemyboss.health <= 0:
                boss_fight = False
                finish = True
                SCREEN.blit(win_txt, (210, 250))

                boss_fight = False
                roundn += 1
                enemyboss.health = roundn * 5
                spawn_enemys()

    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()

        if event.type == p.KEYDOWN and event.key == p.K_SPACE and finish == True:
            finish = False
                

    clock.tick(FPS)
    p.display.flip()