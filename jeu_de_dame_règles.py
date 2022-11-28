def jeu():
  dam = create_grid()
  numero_du_tour = -1
  while fin_du_jeu(dam) == False:
    print(grid_to_string(dam))
    numero_du_tour = numero_du_tour + 1
    qui_joue = qui_cest_qui_doit_jouer_au_fait(numero_du_tour)
    piece = piece_a_deplacer (dam, qui_joue)
     
    x = piece[0]
    y = piece[l] 
    dam[x][y] = '0'
    if dam[x][y] == 'N' or dam[x][y] == 'B': 
        while condi == False:
            r = bouger_dame(dam,piece,qui_joue) 
            oucaSTR = input('tu le met ou ?') 
            ou_ca = dico[ou_caSTR] 
            if ou_ca not in r:
                print("cette dame ne peut pas aller là”) 
            else:
                condi = True
        manger_dame(dam,[x,y],ou_ca)
    else:
        Chemin,peutMange = chemin(dam,x,y,qui_joue) 
        t = len(Chemin[0])
        X,Y = x,y
        for k in range(l, t): 
            condition = False 
            while condition == False:
                ou = tu_le_met_ou(dam,X,Y,qui_joue) 
                endroitx, endroity = ou[0] 
                liste = [] 
                for 1 in Chemin:
                    if [endroitx, endroity] == l[k]:
                        liste.append(l) 
                        condition = True 
                if liste == []:
                    print("il faut faire le meilleur coup possible")
            dam[endroitx][endroity] = fonction_utile(qui_joue)
            X,Y = endroitx, endroity 
            if ou[l] != []:
                mangex = ou[l][0] 
                mangey = ou[l][l] 
                dam[mangex][mangey] = '0’
                Chemin = liste.copy()
                if k != t-1:
                    print(grid_to_string(dam)) 
                    dam[endroitx][endroity] = '0'
    promotion en dame(dam)