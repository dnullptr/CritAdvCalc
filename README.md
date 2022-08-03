**An advanced Crit Rate/Crit DMG calculator and possibility analysis tool (Built for Genshin Impact but can work on any lifetime-sucking RPG)**

**About the functions:**
# roll Function
RNG Roll function (integer rounded is more than enough) to determine hit or miss

# calc Function
The main brain function.
compares 2 sets of possible CRIT Rate/CRIT DMGs
tells which is better statistically.
can be fed with how many samples you want to "try";
the more "samples" = the harder CPU wise and "true-to-life" the algorithm is.
gets Old CRIT Rate,Old CRIT DMG,New CRIT Rate,New CRIT DMG,Number of samples to do "Damage"
will print but also return value.


# calc_dmg Function
helper function, simpler than calc.
internal function in sweet spot finder.


# find_sweet_crcd_spot Function
You're gonna love this one..
this function THEORETICALLY calculates the sweetest spot of CR/CDMG distribution, given that was possible.

the needed parameter is what I called "pot" for potential.
potential equals to CR+CDMG. i.e if I got an option to do CR=55 CDMG=200 or CR=77 CDMG=178 (Using CR goblet instead of CDMG for example), then we can say my potential=255
the luckier u are in game by getting better weapons/artifacts - the higher ur "potential" value.
this function takes a paramter named "mul" as a multiplier of how much do u think CR% is rarer than CDMG%
as a default, and given how the game does usually - I put it to be 2. If I don't decrease it from the CDMG during the loop - it will immediately decide that 99% CR is the best.. which is not really a something.
this function takes samples as a variable as well.
CR starts at 30. U can clearly change it.
