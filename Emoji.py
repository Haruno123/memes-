import random

def gen_emodji(pass_right):
    emoj = ["(╥︣﹏᷅╥)", "(͡• ͜ʖ ͡•)", "(っ＾▿＾)💨", "( ◑‿◑)ɔ┏🍟--🍔┑٩(^◡^ )", "✍(◔◡◔)"]
    faces = ""
    for i in range(pass_right):
        faces += random.choice(emoj) + " "
        
    return faces.strip()

