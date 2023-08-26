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
In the commit files of TerminalWizard repository, there is a commit which is secretly a hint for last spell. The spell is in 0x.Spell_0y.txt where x is the number of horcruxes voldemort make which is 7, and y is a number with number of alphabets the number is equal to the number itself which is 4.<br>

## The spell is in a different branch named thegraveyard
git checkout thegraveyard<br>
## The spell is Priori Incantatem and when you execute the Priori Incantatem.py you get the code and copy it into Part_4.txt
python3 'Priori Incantatem.py'

## THE END

Navigate to the 'codes' folder and concatenate all the contents of the file into a text file called finalcode.txt. After concatenating delete all the files except finalcode.txt.<br>

# To decode the message,
echo aHR0cHM6Ly9naXRodWIuY29tL1RoZUh1bnRzbWFuNC9UaGVGaW5hbFNwZWxs | base64 --decode <br>
You get this link <br>
https://github.com/TheHuntsman4/TheFinalSpell

## THE FINAL SPELL

 You need to clone the repo and execute the python file and you ger this <br>

![Alt text](https://github.com/HrishikeshSNamputiri/amfoss-tasks/blob/main/Task-01/champion.png) <br>

Totally Worth it!!! <br>

I cloned my amfoss-tasks repo and used these commands to upload to my repo<br>
git add <file path> <br>
git commit <br> 
git push <br>
<br>
These command add to a bucket what you need to send, commit a what you want, and upload respectively.

