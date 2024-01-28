if play == 1 and pc == 3:
    print('\033[1;32mVocê ganhou.\033[m')
elif play == 2 and pc == 1:
    print('\033[1;32mVocê ganhou.\033[m')
elif play == 3 and pc == 2:
    print('\033[1;32mVocê ganhou.\033[m')

if pc == 1 and play == 3:
    print('\033[1;33mVocê perdeu.\033[m')
elif pc == 2 and play == 1:
    print('\033[1;33mVocê perdeu.\033[m')
elif pc == 3 and play == 2:
    print('\033[1;33mVocê perdeu.\033[m')

elif play == pc:
    print('\033[1;36mEmpate\033[m')
else:
    print('\033[1;31mOpção invalida\033[m')