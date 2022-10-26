import pyfiglet
import os

# Regular Colors
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
P ='\033[0;36m' # Cyan
W ='\033[0;37m' # White

print("")
logo = pyfiglet.figlet_format("                 INFO")
loga = pyfiglet.figlet_format("  USERNAME")
print(W+logo)
print(Z+loga)
print('''
               \033[0;37m BY: ENG MOHAMMED ALOBAIDY
                \033[2;32mGITHUB: @Engmohammedalobaidy
                \033[2;36mTWITTER: @eng_m_alobaidy ''')
print("")
print("\033[1;31m×\033[0;37m===============\033[1;31m×\033[0;37m===============\033[1;31m×\033[0;37m==============\033[1;31m×\033[0;37m===============\033[1;31m×")
print("")
user = input(" \033[0;37m[\033[1;31m#\033[0;37m] Enter The \033[1;31mUsername\033[0;37m: "+F)
print("")
print("")
print(' \033[0;37m[\033[1;31m1\033[0;37m] \033[2;36mTwitter > \033[0;37mhttps://mobile.twitter.com/'+user+'')
print("")
print(' \033[0;37m[\033[1;31m2\033[0;37m] \033[2;35mInstagram > \033[0;37mhttps://www.instagram.com/'+user+'')
print("")
print(' \033[0;37m[\033[1;31m3\033[0;37m] \033[2;34mFacebook > \033[0;37mhttps://m.facebook.com/'+user+'')
print("")
print(' \033[0;37m[\033[1;31m4\033[0;37m] \033[2;32mTikTok > \033[0;37mhttp://www.tiktok.com/'+user+'')
print("")
print(' \033[0;37m[\033[1;31m5\033[0;37m] \033[1;33mSnapchat > \033[0;37mhttps://www.snapchat.com/add/'+user+'')
print("")
print(' \033[0;37m[\033[1;31m6\033[0;37m] \033[1;31mYoutube > \033[0;37mhttps://m.youtube.com/'+user+'')
print("")
print(' \033[0;37m[\033[1;31m7\033[0;37m] \033[1;34mTelegram > \033[0;37mhttps://t.me/s/'+user+'')
print("")
print(' \033[0;37m[\033[1;31m8\033[0;37m] \033[1;31mPinterest > \033[0;37mhttps://www.pinterest.com/'+user+'')
print("")
print(' \033[0;37m[\033[1;31m9\033[0;37m] \033[0;37mBigo Live > \033[0;37mhttps://www.bigo.tv/ar/'+user+'')
print("")
print(' \033[0;37m[\033[1;31m10\033[0;37m] \033[2;32mGitHub > \033[0;37mhttps://www.bigo.tv/ar/'+user+'')
print("")
print(' \033[0;37m[\033[1;31m11\033[0;37m] \033[2;35mTellonym > \033[0;37mhttps://www.pinterest.com/'+user+'')
print("")
print(' \033[0;37m[\033[1;31m12\033[0;37m] \033[2;32mCareem Taxi > \033[0;37mhttps://www.careem.com/'+user+'')
print("")
print(' \033[0;37m[\033[1;31m13\033[0;37m] \033[1;33mAmazon > \033[0;37mhttps://www.amazon.eg/'+user+'')
print("")
print(' \033[0;37m[\033[1;31m14\033[0;37m] \033[2;34mPalystation > \033[0;37mhttps://www.playstation.com/'+user+'')
print("")
print(' \033[0;37m[\033[1;31m15\033[0;37m] \033[2;32mXbox > \033[0;37mhttps://www.xbox.com/'+user+'')
print("")
print("\033[2;32m×\033[0;37m===============\033[2;32m×\033[0;37m===============\033[2;32m×\033[0;37m==============\033[2;32m×\033[0;37m===============\033[2;32m×")
