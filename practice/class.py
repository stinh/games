
# class Chair():
#     pass

# a_chair = Chair()
# a_chair.color = 'green' 

# b_chair = Chair()
# b_chair.color = 'yellow' 

# print(a_chair.color)
# print(b_chair.color)

# =====================

# class Chair():
#     def set_color(self,c):
#         self.color = c

# =====================

# a_chair = Chair()
# #a_chair.color = 'green'
# a_chair.set_color('green')

# b_chair = Chair()
# #b_chair.color = 'yellow' 
# b_chair.set_color('yellow')

# print(a_chair.color)
# print(b_chair.color)

# =====================

# class Chair():
#     def __init__(self,c):
#         self.color = c


# a_chair = Chair('Green')


# b_chair = Chair('Yellow')


# print(a_chair.color)
# print(b_chair.color)

# =====================

class Chair():
    def __init__(self,c):
        self.color = c
    
    def seat(self):
        print(self.color,'的椅子很舒服')


a_chair = Chair('Green')
a_chair.seat()

b_chair = Chair('Yellow')
b_chair.seat()

Chair.seat(a_chair)