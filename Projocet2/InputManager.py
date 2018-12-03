from pico2d import*
from  globalParamiter import*

def handle_events(events):
    global Global,Texture,Timer
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            Global.MyMouse[0] = event.x
            Global.MyMouse[1] = Global.WindowY - event.y
            num = (int)(Global.g_Time) % 50
            Global.MouseStar[num].X = event.x + random.randint(-5, 6)
            Global.MouseStar[num].Y = Global.WindowY - event.y + random.randint(-5, 6)
            Global.MouseStar[num].dirX = Global.MouseStar[num].dirY = 0
            Global.MouseStar[num].Life = random.randint(12, 20)
            Global.MouseStar[num].live = True
            if(Global.stage == "level"):
                for i in range(0,8):
                    if(180-25+60*i < Global.MyMouse[0] <180+25+60*i):
                        if (250-25 < Global.MyMouse[1] < 250+25):
                            Global.Itemshow = i
                            break
                        else:
                            Global.Itemshow = -1
                    else:
                        Global.Itemshow = -1
            if(Global.stage=="stage"):
                if(Global.g_Clear == True):
                    for i in range(0,3):
                        if(110+140*i-32 < Global.MyMouse[0] <110+140*i+32):
                            if (410 < Global.MyMouse[1] < 490):
                                Global.Itemshow = i
                                break
                            else:
                                Global.Itemshow = -1
                        else:
                            Global.Itemshow = -1

        if event.type == SDL_MOUSEBUTTONDOWN:
            for i in range(0,50):
                Global.ClickStar[i].live = True
                Global.ClickStar[i].Life = 5
                Global.ClickStar[i].X = event.x
                Global.ClickStar[i].Y = Global.WindowY -event.y
                Global.ClickStar[i].dirX = Global.ClickStar[i].dirY = 0
            Global.ClickCnt = 0

        if(Global.stage == "main"):
            if event.type == SDL_MOUSEBUTTONDOWN:
                if (100 < Global.MyMouse[0] < 700):
                    if (400 < Global.MyMouse[1] < 500):
                        Timer.TimeReset()
                        Global.stage = "level"

                if (100 < Global.MyMouse[0] < 700):
                    if (250 < Global.MyMouse[1] < 350):
                        close_canvas()
                        exit(1);

        elif(Global.stage == "level"):
            if event.type == SDL_MOUSEBUTTONDOWN:
                if ( 620 < Global.MyMouse[0] < 780):
                    if (40 < Global.MyMouse[1] < 120):
                        #reset
                        Timer.TimeReset()
                        Global.stage = "stage"
                        Global.g_Level = Global.g_Level + 1
                        Global.g_Player.X,Global.g_Player.Y = Global.WindowX / 8 * 2.5, Global.WindowY / 8 * 1
                        Global.g_Player.Life = Global.g_Player.MaxLife
                        Global.g_Clear = False
                        Global.g_StageTime = 0
                        Global.stageback = 1
                        for arr in Global.g_BulletArr:
                            arr.Draw = False
                        for arr in Global.g_MonsterBulletArr:
                            arr.Live = False
                        Global.MonsterSet()
                        Global.SetItem()


                if ( 490 < Global.MyMouse[0] < 610):
                    if (40 < Global.MyMouse[1] < 120):
                        Timer.TimeReset()
                        Global.stage = "main"
                        Global.g_Level = -1

                if(330-70 < Global.MyMouse[0] <330+70):
                    if (470-65 < Global.MyMouse[1] < 470+65):
                        Global.g_Hard = 0

                if(450-70 < Global.MyMouse[0] <450+70):
                    if (470-65 < Global.MyMouse[1] < 470+65):
                        Global.g_Hard = 1

                if(570-70 < Global.MyMouse[0] <570+70):
                    if (470-65 < Global.MyMouse[1] < 470+65):
                        Global.g_Hard = 2

                if(330-70 < Global.MyMouse[0] <330+70):
                    if (670-65 < Global.MyMouse[1] < 670+65):
                        Global.g_Type = 0

                if(450-70 < Global.MyMouse[0] <450+70):
                    if (670-65 < Global.MyMouse[1] < 670+65):
                        Global.g_Type = 1

                if(570-70 < Global.MyMouse[0] <570+70):
                    if (670-65 < Global.MyMouse[1] < 670+65):
                        Global.g_Type = 2



                if(Global.g_Level == -1):
                    pass

        elif(Global.stage == "stage"):
            if event.type == SDL_MOUSEBUTTONDOWN:#mouse
                if(Global.g_Clear == True):
                    check = False
                    for ITEM in Global.MyItem.inven:
                        if ITEM.Num == 21:
                            check = True
                            break
                    if(check == False):
                        for i in range(0,3):
                            if(110+140*i-32 < Global.MyMouse[0] <110+140*i+32):
                                if (410 < Global.MyMouse[1] < 490):
                                    Global.GiftCheck1 = i
                    else:
                        for i in range(0,3):
                            if(110+140*i-32 < Global.MyMouse[0] <110+140*i+32):
                                if (410 < Global.MyMouse[1] < 490):
                                    temp = i
                                    if(temp == 0 ):
                                        Global.GiftCheck1 = 1
                                        Global.GiftCheck2 = 2
                                    elif(temp == 1):
                                        Global.GiftCheck1 = 0
                                        Global.GiftCheck2 = 2
                                    else:
                                        Global.GiftCheck1 = 0
                                        Global.GiftCheck2 = 1
                                    break

                    if (150 < Global.MyMouse[0] < 350):
                        if (250 < Global.MyMouse[1] < 350):
                            if (check == True):
                                Global.MyItem.Insert(Global.Gift[Global.GiftCheck2])
                                ItemEffect(Global.GiftCheck2)
                            Global.MyItem.Insert(Global.Gift[Global.GiftCheck1])

                            ItemEffect(Global.GiftCheck1)




                            #Global.g_Level = Global.g_Level+1
                            Global.stage = "level"

            if event.type == SDL_KEYDOWN:  # key down
                if event.key == SDLK_LSHIFT:
                    Global.g_Player.slow = True
                if event.key == SDLK_RIGHT:
                    Global.g_Player.forceX = 1
                elif event.key == SDLK_LEFT:
                    Global.g_Player.forceX = -1
                elif event.key == SDLK_UP:
                    Global.g_Player.forceY = 1
                elif event.key == SDLK_DOWN:
                    Global.g_Player.forceY = -1

                if event.key == SDLK_a:
                    Global.g_ATT = True

                if event.key == SDLK_TAB:#치트
                    Global.g_Type = (Global.g_Type+1) % 3
                if event.key == SDLK_n:
                    Global.g_Player.BulletNum += 1
                if event.key == SDLK_m:
                    if(Global.g_Player.BulletNum>3):
                        Global.g_Player.BulletNum -= 1




            if event.type == SDL_KEYUP:  # key up
                if event.key == SDLK_LSHIFT:
                    Global.g_Player.slow = False
                if event.key == SDLK_RIGHT:
                    if(Global.g_Player.forceX == 1):
                        Global.g_Player.forceX = 0
                if event.key == SDLK_LEFT:
                    if(Global.g_Player.forceX == -1):
                        Global.g_Player.forceX = 0

                if event.key == SDLK_DOWN:
                    if(Global.g_Player.forceY == -1):
                        Global.g_Player.forceY = 0
                if event.key == SDLK_UP:
                    if(Global.g_Player.forceY == 1):
                        Global.g_Player.forceY = 0

                if event.key == SDLK_a:
                    Global.g_ATT = False
                    Global.g_BulletCnt = Global.g_BulletDelay

                if event.key == SDLK_ESCAPE:
                    if(Global.pause == True):
                        Global.pause = False
                    else:
                        Global.pause = True
                if event.key == SDLK_F1:
                    Global.g_Boss.live = True

        else:
            pass


def ItemEffect(num):
    global Global
    if (Global.Gift[num].Num == 0):
        Global.g_Player.BulletPower += 1
    if (Global.Gift[num].Num == 1):
        Global.g_Player.BulletNum += 1
    if (Global.Gift[num].Num == 2):
        Global.g_Player.MaxLife += 1
    if (Global.Gift[num].Num == 3):
        Global.g_Player.BulletPower += 1
    if (Global.Gift[num].Num == 4):
        Global.g_Player.BulletSpeed += 1
    if (Global.Gift[num].Num == 5):
        Global.g_Player.BulletPower += 1
        Global.g_Player.MaxLife += 1
        for Item in  Global.MyItem.inven:
            if(Item.Name =="미술작품"):
                Global.g_Player.BulletPower += 2
    if (Global.Gift[num].Num == 6):
        for i in range(0,8):
            if Global.MyItem.inven[i].Name == "랜덤상자":
                import Item
                Global.Gift[0] = Item.ItemIndex[random.randint(0,21)]
                ItemEffect(0)
                Global.MyItem.inven[i] = Global.Gift[0]
                break
    if (Global.Gift[num].Num == 7):
        Global.g_Player.BulletPower += 2
        Global.g_Player.MaxLife -= 1
        for Item in  Global.MyItem.inven:
            if(Item.Name =="저주의 보석"):
                Global.g_Player.MaxLife += 4
    if (Global.Gift[num].Num == 8):
        pass#완
    if (Global.Gift[num].Num == 9):
        pass#완
    if (Global.Gift[num].Num == 10):
        Global.g_Player.MaxLife += 1
    if (Global.Gift[num].Num == 11):
        Global.g_Player.MaxLife += 2
        for Item in  Global.MyItem.inven:
            if(Item.Name =="오래된 양피지"):
                Global.g_Player.BulletPower += 2

    if (Global.Gift[num].Num == 12):
        import Item
        for i in range(0,8):
            if Global.MyItem.inven[i].Num != -1:
                Global.Gift[0] = Item.ItemIndex[random.randint(0,21)]
                Global.MyItem.inven[i] = Global.Gift[0]
                ItemEffect(0)

    if (Global.Gift[num].Num == 13):
        for i in range(0,8):
            if Global.MyItem.inven[i].Name == "고급 랜덤박스":
                import Item
                temp = []
                tempnum = 0
                for arr in Item.ItemIndex:
                    if arr.Level == 2 or  arr.Level == 3:
                        temp.append(arr)
                        tempnum += 1
                Global.Gift[0] = temp[(random.randint(0,tempnum))]
                ItemEffect(0)
                Global.MyItem.inven[i] = Global.Gift[0]
                break

    if (Global.Gift[num].Num == 14):
        Global.g_Player.MaxLife -= 1
        Global.g_Player.BulletPower += 5
        for Item in  Global.MyItem.inven:
            if(Item.Name =="저주"):
                Global.g_Player.MaxLife += 4
    if (Global.Gift[num].Num == 15):
        Global.g_Player.MaxLife += Global.g_Player.MaxLife
    if (Global.Gift[num].Num == 16):
        pass#완
    if (Global.Gift[num].Num == 17):
        pass#완
    if (Global.Gift[num].Num == 18):
        pass#완
    if (Global.Gift[num].Num == 19):
        Global.g_Player.BulletPower += 5
        Global.g_Player.MaxLife += 4
        Global.g_Player.BulletNum += 3
        Global.g_Player.BulletSpeed += 2
    if (Global.Gift[num].Num == 20):
        pass#완
    if (Global.Gift[num].Num == 21):
        pass#완
    print(Global.g_Player.BulletNum)
    print(Global.g_Player.BulletSpeed)
    print(Global.g_Player.BulletPower)
    print(Global.g_Player.MaxLife)