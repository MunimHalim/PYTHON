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

    u "Kamu nampaknya bersemangat hari ini. Ada apa ? (Terdengar suara dari belakang)"

    p "Menoleh ke belakang dan ternampak gurunya sedang berdiri sambil tersenyum."

    p "Bulan kemerdekaan sudah dekat cikgu ! Saya tengok balik kenangan kemerdekaan negara kita ini."

    g "Baguslah, cuma saya nak uji semangat patriotisme kamu ini !!!"

    p "Boleh cikgu, saya bersedia ! (Sahut dengan berkobar-kobar)"

    g "Baiklah, begini, cuba sebutkan rukun negara kita ini." 

    p "Satu!"

    g "Sure, but what's a \"visual novel?\""

menu:

    "Kepercayaan kepada tuhan":
        jump dua 

    "Ketaatan kepada raja":
        jump salah
    
    p "Satu kepercayaan kepada tuhan, dua ketaatan kepada raja ,tiga kesetiaan kepada negara, keempat kedaulatan undang-undang, kelima kesopanan dan kesusilaan."     
   
label dua:

menu:

    p "Dua!"

    "Kepercayaan kepada tuhan":
        jump salah

    "Ketaatan kepada raja":
        jump tiga

label tiga:

menu:

    p "Tiga!"

    "Kepercayaan kepada tuhan":
        jump salah

    "Ketaatan kepada raja":
        jump salah

    "Kesetiaan kepada negara":
        jump empat

label empat:

menu:

    p "Empat!"

    "Kepercayaan kepada tuhan":
        jump salah

    "Ketaatan kepada raja":
        jump salah

    "Kesetiaan kepada negara":
        jump salah

    "Kedaulatan undang-undang":
        jump lima

    "Kesopanan dan kesusilaan":
        jump salah

label lima:

menu:

    p "Lima!"

    "Kepercayaan kepada tuhan":
        jump salah

    "Ketaatan kepada raja":
        jump salah

    "Kesetiaan kepada negara":
        jump salah

    "Kedaulatan undang-undang":
        jump salah

    "Kesopanan dan kesusilaan":
        jump tamat  

label salah: 
    
    jump dua  

label tamat:

    g "Siapakah bapa kemerdekaan tanah air ini ?"

    # Tamat

    return
