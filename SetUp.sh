sudo apt update && sudo apt upgrade -y
sudo apt install wget gpg
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'


sudo apt update
sudo apt install -y code
sudo apt install -y git
sudo apt install -y gh
sudo apt install -y python3
sudo apt install -y python3-pip
sudo apt install -y build-essential
sudo apt install -y dkms
sudo apt install -y curl

sudo sh -c "wget -O - https://dl.openfoam.org/gpg.key | apt-key add -"
sudo add-apt-repository http://dl.openfoam.org/ubuntu
sudo apt-get update

sudo apt install -y openfoam13
if ! grep -Fxq "source /opt/openfoam13/etc/bashrc" ~/.bashrc; then
  echo "source /opt/openfoam13/etc/bashrc" >> ~/.bashrc
fi
source ~/.bashrc
gh auth login
git config --global user.name "Chlorine1Trifluoride"
git config --global user.email "s2510423@siheung.hs.kr"


if [ ! -d "forCFD" ]; then
    git clone --branch Linux-personal https://github.com/Chlorine1Trifluoride/forCFD
else
    echo "등신아 이미 레포 클론 되어있다"
fi
