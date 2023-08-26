# THE SOLUTION OF TERMINAL WIZARD

## PREREQUISITES

### Installing Github Cli
sudo pacman -S github-cli

### Setting up gh
gh auth login 

## ENTER THE MAZE

### This will clone the repository that the challenge is held
git clone https://github.com/KshitijThareja/TerminalWizard.git

### Make a directory named codes in the cloned repository.
cd TerminalWizard/
mkdir codes

## FIRST CHALLENGE
To fight blast-ended-skrewt, you need to find the right spell which is stored in 0x/Spell_0y.txt where x is the first perfect number which is 6 and y=d/dx (x^2-7x) and x=6 so y=5. So, the spell is stored at 06/Spell_5.txt<br>
The spell is Impedimenta and when you execute it from spellbook you get a code. Copy it in Part_1.txt in codes

## SECOND CHALLENGE
You need the right spell to fight the giant spider. The spell is in 0y/Spell_0x.txt. To determine the file name, take the atomic number of the element that was first used to make semiconductors, and use its units place digit for 'y' and its tenths place digit for 'x'.<br>
The element is Germanium and its atomic number is 32. So the spell is in 02/Spell_03.txt<br>
The spell is Stupefy and when you execute it from spellbook you get a code. Copy it in Part_2.txt in codes

## THIRD CHALLENGE

###In this challenge we need to switch to a branch which has the name of the subject Professor Lupin teached, which is defenceAgainstTheDarkArts.
git branch -a<br>
git checkout defenceAgainstTheDarkArts<br>

The sphinx asked a riddle. The answer is "A Boggart". The spell used to counter a boggart is Riddikulus. When you execute it from spellbook you get a code. Copy it in Part_3.txt in codes

## FORTH CHALLENGE


