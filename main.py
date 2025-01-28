from module.sprite_creator import*
from imports2 import*

fire_rate_time = 0
y1 = 0
y2 = -1080

p.init()

font = p.font.SysFont('Arial', 40, True)
small_font = p.font.SysFont('Arial', 30, False)

boss_health = small_font.render('Boss health: ?', True, (255, 0, 0))

defeat_txt = font.render('defeat!', True, (255, 0, 0))
win_txt = font.render('win!', True, (0, 255, 0))



finish = False
while True:
    if not finish:
        fire_rate_time +=1
        SCREEN.blit(background, (0,y1))  
        SCREEN.blit(background, (0,y2))

        if enemyboss:
            boss_health = small_font.render(f'Boss health: {enemyboss.health}', True, (255, 0, 0))
            SCREEN.blit(boss_health, (0, 0))

        y1+=3
        y2+=3

        if y1 > 1080:
            y1 = -1080
        if y2> 1080:
            y2 = -1080

        player.move()
        player.draw_img()

        if enemyboss:
            enemyboss.move()
            enemyboss.draw_img()

        for event in p.event.get():
            if event.type == p.MOUSEBUTTONDOWN:
                if fire_rate_time > 30:
                    bullets.append(BULLET(player))
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

                    if not enemy_list:
                        enemyboss = ENEMYBOSS()

        for enemy in enemy_list:
            enemy.shooting(enemy_bullets, ENEMY_BULLET, enemy)

        
        for bull in enemy_bullets:
            bull.draw_img()
            bull.move()

            if player.rect.colliderect(bull.rect):
                    enemy_bullets.remove(bull)
                    finish = True
                    SCREEN.blit(defeat_txt, (210, 250))
            
            if enemyboss:
                if enemyboss.rect.colliderect(bullet.rect):
                    bullets.remove(bullet)
                    enemyboss.health -= 1

                    if enemyboss.health <= 0:
                        enemyboss = None
                        finish = True
                        SCREEN.blit(win_txt, (210, 250))

    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()

        if event.type == p.KEYDOWN and event.key == p.K_SPACE and finish == True:
            finish = False
        
        if event.type == p.K_k:
            enemy_list.clear()
                

    clock.tick(FPS)
    p.display.flip()
