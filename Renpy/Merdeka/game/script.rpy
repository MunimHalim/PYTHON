# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Pelajar")
define g = Character("Guru")
define r = Character("Rakaman Suara")
define u = Character("???")


# The game starts here.

label start:

    # Menunjukkan paparan latarbelakang

    scene classroom

    # Karakter

    show pelajar

    # These display lines of dialogue.

    play music "/audio/merdeka.ogg" fadeout 1.0

    r "Merdeka! Merdeka! Merdeka!"

    stop music

    p "Sungguh nostalgia suara ini...  Aku harap tahu ini dapat sambut merdeka di sekolah. (Monolog)"

    u "Terdengar suara dari belakang "

    u "Kamu nampaknya bersemangat hari ini. Ada apa ?"

    p "Menoleh ke belakang dan ternampak gurunya sedang berdiri sambil tersenyum."

    p "Bulan kemerdekaan sudah dekat cikgu ! Saya tengok balik kenangan kemerdekaan negara kita ini."

    # Tamat

    return
