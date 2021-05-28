# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Pelajar")


# The game starts here.

label start:

    # Menunjukkan paparan latarbelakang

    scene pelajar

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show 

    # These display lines of dialogue.

    Pelajar_1 "You've created a new Ren'Py game."

    Pelajar_2 "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
