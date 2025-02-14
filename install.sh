#!/bin/bash
echo "$USER ALL=(ALL) NOPASSWD: ALL" | sudo EDITOR='tee -a' visudo
sudo apt-get -y update
sudo apt-get -y install tmux python3-full pipx
pipx install termcolor
python3 -m pip config set global.break-system-packages true
sudo mkdir /pinecone
sudo mkdir /pinecone/bin
sudo mkdir /pinecone/bin/restarters
wget https://github.com/BobReed24/pinecone/raw/refs/heads/main/command_pinecone
sleep 4
sudo mv command_pinecone /pinecone/command_pinecone
sudo chmod +x /pinecone/command_pinecone
wget https://raw.githubusercontent.com/BobReed24/hunkon-os/refs/heads/main/bin/upgrade.sh
sudo mv upgrade.sh /pinecone/bin/upgrade.sh
wget https://raw.githubusercontent.com/BobReed24/hunkon-os/refs/heads/main/bin/restarters/restart-sys-soft.sh
sudo mv restart-sys-soft.sh /pinecone/bin/restarters/restart-sys-soft.sh
wget https://raw.githubusercontent.com/BobReed24/hunkon-os/refs/heads/main/bin/build.sh
sudo mv build.sh /pinecone/bin/build.sh
wget https://raw.githubusercontent.com/BobReed24/hunkon-os/refs/heads/main/bin/pinecone
sudo chmod +x /pinecone/pinecone
sudo mv pinecone /bin/pinecone
sudo chmod +x /bin/pinecone
sudo mkdir /pinecone/lib
wget https://github.com/BobReed24/pinecone/raw/refs/heads/main/lib/__init__.py
sudo mv __init__.py /pinecone/lib/__init__.py
wget https://github.com/BobReed24/pinecone/raw/refs/heads/main/lib/help.py
sudo mv help.py /pinecone/lib/help.py
wget https://github.com/BobReed24/pinecone/raw/refs/heads/main/lib/package_handler.py
sudo mv package_handler.py /pinecone/lib/package_handler.py
wget https://github.com/BobReed24/pinecone/raw/refs/heads/main/lib/packages.py
sudo mv packages.py /pinecone/lib/packages.py
sudo chmod 777 /pinecone
sudo chmod 777 /pinecone/lib
sudo chmod 777 /pinecone/bin
cd $main
clear
echo "Finished installing Pinecone!"
echo "
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                              .==-+:-=.                                             
                                            .-+#*=+*-==-.                                           
                                          .:.-=:*=-*-#+#....                                        
                                         ..=-==#--*=*%#**=-.                                        
                                        .-=:+*+-+##%---#*::..                                       
                                       .+=+#**+###*+%#*#=+*:.                                       
                                       ..=*::=##%+-#*%*=:-----.                                     
                                     .--*=+#*%#*-+#%%#%#+%%*=.                                      
                                     .:-***%--+-*##%%*=-**+-:-=.                                    
                                   ..--:.:*%=+##*%%%-#*+#%#*=..                                     
                                   .:+:+*=*%#%%%#--*#%%%%%%%%%#*.                                   
                                   .:-:-+#=.:+##+%%%#%#+--=+#%%#:                                   
                                  .*=-+++*#*#%*+%%%%%*#%%#+#%+-..                                   
                                   ...-*+-=#%%%%%%%%%%%%%%%%####+.                                  
                                  .*...-:::===%#.....=%%.....=%#+.                                  
                                 .:-=+*#%%%+%%%::=*%#-++*%%%%#----.                                 
                                .-++-+**+---=+*#%%%%%%%%%%%%%%%#*+:.                                
                                .:*-:+%*:-=*...:=%=:..::##-::..-*#+.                                
                                .-=:....*%%%%##%#.:.#=#-.+#%%%%%-.                                  
                                 ...+%#*-:-+*#%%*%%%%%%%%%%%%##%%%*..                               
                                .--::++-.-#=...-%+-...-+%%*====++=-..                               
                               .-=*:....*%%%%%%#....===..=%%%%%####=.                               
                               .--.:%%%%*---+#%%%%%%%%%%%%%%=...#%:.                                
                               . .:*+#%:..+-....=%####%%%%+:-##%#=....                              
                               :-.-+..=*%%%%%%%%+. .--::=*%%%%%%#*=+#.                              
                               --:=%#=:--*#+%%%***++#%%%%%%*#--*%%%#-.                              
                               ..-#*+%%%=......=%%%%%%%%%%#-.=%%%=...                               
                              :-...-###%%%=-%*::-*%#*#%%%%%%%%%%%....                               
                              .+==*.....=#%%%%%%%#-..:=..+%%%%%%%%%=-.                              
                               .:-*+*#*:.=#%%%%%%*++**%%%%%*-.+#%%%#=.                              
                               .===.=#%%%#-...:=%%%%%%%%%#=*#%%%%%*..                               
                                .-*+*-.+#%%**%==#%%#-*#%%%%%##%%%#*:.                               
                                 .:.-*#%#++%%%%%%+.:+*-=%%*-+%%*-:..                                
                                  .-+**%%%*-:=*%%%%%%%%*=+%%%%%*=:.                                 
                                   ..-+%#**%%%%%%%%%%%%#%%#+-.:-.                                   
                                      ..:+#%%%%%%%%%%%%%%%#+-..                                     
                                       .... ..:#%%%%%*...                                           
                                              .=+##%%=.                                             
                                              .:#+#%%-                                              
                                              .--+%%%.                                              
                                               .#-+%#:                                              
                                               .*=#%=                                               
                                                :**%-                                               
                                                .-=%-                                               
                                                .-#=.                                               
                                                 ...                                                
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    "
echo "                             ____  _"
echo "                            |  _ \(_)_ __   ___  ___ ___  _ __   ___ "
echo "                            | |_) | | '_ \ / _ \/ __/ _ \| '_ \ / _ \   "
echo "                            |  __/| | | | |  __/ (_| (_) | | | |  __/ "
echo "                            |_|   |_|_| |_|\___|\___\___/|_| |_|\___| "     
echo "Made by @BobReed24 on github"
echo "Repo at https://github.com/BobReed24/pinecone"
