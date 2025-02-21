import time

'''for i in range(10):
    print(f"Progress: {i*10}%", end='\r') 
    time.sleep(0.5) 

print("Progress: 100%")  # Print a final message on a new line
'''
'''import os

def clear_line():
    print("\033[2K\033[G", end="")  # ANSI escape sequences for clearing line and moving to beginning

print("Line 1")
print("Line 2")
print("Line 3")
time.sleep(3) 


clear_line()  # Attempt to clear the last line
print("New Line 1") 
'''
import os

def clear_console():
  """Clears the console screen."""
  if os.name == 'nt':
    os.system('cls')  # For Windows
  else:
    os.system('clear')  # For macOS and Linux

# Example usage:
print("Line 1")
print("Line 2")
print("Line 3")
time.sleep(3) 

clear_console()
print("This line will be printed on a cleared screen.")
print("\033[31mHello, World!\033[0m")
print("\033[32mHello, World!\033[0m")
print("\033[42mHello, World!\033[0m")
input()

k = 1
j = 1

print("COMP: ", end='')
print(str(-k), end='')

for i in range(j):
	print(" [X][X][X] ", end='')
	print(-k-4)
    
print("\U0001F0BF")
print("\U0001F600")

war = """   ,., '                                        ,.,   '           ,. -  .,              
 ,'   '`;                 ,·;'                 ;´   '· .,        ,' ,. -  .,  `' ·,       
 ;    ,':\     ,'´¨';     '; ;'\              .´  .-,    ';\      '; '·~;:::::'`,   ';\    
 ;    ';::'\  ,'   ,'\   ,' ,'::'\            /   /:\:';   ;:'\'     ;   ,':\::;:´  .·´::\'  
 ',    ';::;','    ,'::\,'  ,':::;          ,'  ,'::::'\';  ;::';     ;  ·'-·'´,.-·'´:::::::'; 
  ';   ';:';,'     ;:::;' ,'::::;'      ,.-·'  '·~^*'´¨,  ';::;   ;´    ':,´:::::::::::·´'  
   ';  ';:;' ,:';  ';:;'  ,'::::;       ':,  ,·:²*´¨¯'`;  ;::';    ';  ,    `·:;:-·'´       
    ';  '·' ,'::';  '·´ ,':::::;        ,'  / \::::::::';  ;::';    ; ,':\'`:·.,  ` ·.,      
     \   /::::;\·-·'´\::::;·''       ,' ,'::::\·²*'´¨¯':,'\:;     \·-;::\:::::'`:·-.,';    
      \'´\:::;'  '\::::'\;'´          \`¨\:::/          \::\'      \::\:;'` ·:;:::::\::\'  
       '\:'\:/     '·-·'´'             '\::\;'            '\;'  '     '·-·'       `' · -':::'' 
         '´                            `¨'                                              

"""

print(war)

war2 = """░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓█████████████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                                
                                                

"""

print(war2)

war3 = """                                                                             
                                                                             
WWWWWWWW                           WWWWWWWW                                  
W::::::W                           W::::::W                                  
W::::::W                           W::::::W                                  
W::::::W                           W::::::W                                  
 W:::::W           WWWWW           W:::::Waaaaaaaaaaaaa  rrrrr   rrrrrrrrr   
  W:::::W         W:::::W         W:::::W a::::::::::::a r::::rrr:::::::::r  
   W:::::W       W:::::::W       W:::::W  aaaaaaaaa:::::ar:::::::::::::::::r 
    W:::::W     W:::::::::W     W:::::W            a::::arr::::::rrrrr::::::r
     W:::::W   W:::::W:::::W   W:::::W      aaaaaaa:::::a r:::::r     r:::::r
      W:::::W W:::::W W:::::W W:::::W     aa::::::::::::a r:::::r     rrrrrrr
       W:::::W:::::W   W:::::W:::::W     a::::aaaa::::::a r:::::r            
        W:::::::::W     W:::::::::W     a::::a    a:::::a r:::::r            
         W:::::::W       W:::::::W      a::::a    a:::::a r:::::r            
          W:::::W         W:::::W       a:::::aaaa::::::a r:::::r            
           W:::W           W:::W         a::::::::::aa:::ar:::::r            
            WWW             WWW           aaaaaaaaaa  aaaarrrrrrr            
                                                                             
                                                                             
                                                                             
                                                                             
                                                                             
                                                                             
                                                                             

"""

print(war3)

war4 = """

                                                                                                
                                                                                                
WWWWWWWW                           WWWWWWWW        AAA                  RRRRRRRRRRRRRRRRR   
W::::::W                           W::::::W       A:::A                 R::::::::::::::::R  
W::::::W                           W::::::W      A:::::A                R::::::RRRRRR:::::R 
W::::::W                           W::::::W     A:::::::A               RR:::::R     R:::::R
 W:::::W           WWWWW           W:::::W     A:::::::::A                R::::R     R:::::R
  W:::::W         W:::::W         W:::::W     A:::::A:::::A               R::::R     R:::::R
   W:::::W       W:::::::W       W:::::W     A:::::A A:::::A              R::::RRRRRR:::::R 
    W:::::W     W:::::::::W     W:::::W     A:::::A   A:::::A             R:::::::::::::RR  
     W:::::W   W:::::W:::::W   W:::::W     A:::::A     A:::::A            R::::RRRRRR:::::R 
      W:::::W W:::::W W:::::W W:::::W     A:::::AAAAAAAAA:::::A           R::::R     R:::::R
       W:::::W:::::W   W:::::W:::::W     A:::::::::::::::::::::A          R::::R     R:::::R
        W:::::::::W     W:::::::::W     A:::::AAAAAAAAAAAAA:::::A         R::::R     R:::::R
         W:::::::W       W:::::::W     A:::::A             A:::::A      RR:::::R     R:::::R
          W:::::W         W:::::W     A:::::A               A:::::A     R::::::R     R:::::R
           W:::W           W:::W     A:::::A                 A:::::A    R::::::R     R:::::R
            WWW             WWW     AAAAAAA                   AAAAAAA   RRRRRRRR     RRRRRRR
                                                                                                
                                                                                                
                                                                                                
                                                                                                
                                                                                                
                                                                                                
                                                                                                

"""

print(war4)
