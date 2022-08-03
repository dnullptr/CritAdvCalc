import random
#------------------------------------------------------
# roll - RNG Roll function (integer rounded is more than enough) to determine hit or miss
def roll(chance) -> bool:
  rnd=random.randint(1,100)
  return rnd<=chance

  
#------------------------------------------------------
# calc - The main brain function.
# compares 2 sets of possible CRIT Rate/CRIT DMGs
# tells which is better statistically.
# can be fed with how many samples you want to "try";
# the more "samples" = the harder CPU wise and "true-to-life" the algorithm is.
# gets Old CRIT Rate,Old CRIT DMG,New CRIT Rate,New CRIT DMG,Number of samples to do "Damage"
# will print but also return value.

  
def calc(old_rate,old_cdmg,new_rate,new_cdmg,smpls) -> float:
  critted_old=100+(old_cdmg/100)*100
  critted_new=100+(new_cdmg/100)*100
  dmg_done_old=0
  dmg_done_new=0
  for i in range(smpls):
    dmg_done_old+=critted_old if roll(old_rate) else 100
  for i in range(smpls):
    dmg_done_new+=critted_new if roll(new_rate) else 100
  print("[-] ---------------------------------------")
  print(f'[-] Old/New Comparator Func is Running...')
  print(f'[-] Old DMG Done: {dmg_done_old}\n[-] New DMG Done: {dmg_done_new}')
  print(f"[-] Fraction of 'new' divided by 'old'.. = {dmg_done_new/dmg_done_old} ")
  print("[-] ---------------------------------------")
  return dmg_done_new/dmg_done_old

# calc_dmg - helper function, simpler than calc.
# internal function in sweet spot finder.
def calc_dmg(rate,cdmg,smpls) -> float:
   critted=100+(cdmg/100)*100
   dmg_done=0
   for i in range(smpls):
       dmg_done+=critted if roll(rate) else 100
   return dmg_done

  
#------------------------------------------------------
# find_sweet_crcd_spot - u're gonna love this one..I think
# this function THEORETICALLY calculates the sweetest spot of CR/CDMG distribution, given that was possible.
# the needed parameter is what I called "pot" for potential.
# potential equals to CR+CDMG. i.e if I got an option to do CR=55 CDMG=200 or CR=77 CDMG=178 (Using CR goblet instead of CDMG for example), then we can say my potential=255
# the luckier u are in game by getting better weapons/artifacts - the higher ur "potential" value.
# this function takes a paramter named "mul" as a multiplier of how much do u think CR% is rarer than CDMG%
# as a default, and given how the game does usually - I put it to be 2. If I don't decrease it from the CDMG during the loop - it will immediately decide that 99% CR is the best.. which is not really a something.
# this function takes samples as a variable as well.
# CR starts at 30. U can clearly change it.
  
def find_sweet_crcd_spot(pot,smpls,mul=2) -> tuple:
    crit=30
    cdmg=pot-30
    max=0
    tmax=tuple()
    while(crit<100):
        dmg_now=calc_dmg(crit,cdmg,smpls)
        if(dmg_now>max):
            max=dmg_now
            tmax=(crit,cdmg+(pot-crit-cdmg)) #gives back the decreased cdmg
        crit+=1
        cdmg-=mul 
    print(f'[-] Combination {tmax}\n[-] Output max DMG: {max}')
    return tmax
  
  
# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
# Here is the main function, I can add a more friendly GUI later, just remember I didn't actually plan to release it to the public so quickly but here we go :)
if __name__ == "__main__":
# V change these V
  old_crit=77
  old_cdmg=177
  new_crit=55
  new_cdmg=200
  samples=10000
  
  # here we call calc, you can of course feed the values directly down below inside the function parenthesis 
  print(calc(old_crit,old_cdmg,new_crit,new_cdmg,samples))
  
  # here we call CR/CR sweet spot finder with 254 potential value and 10000 tries..I mean.. "samples"
  print(find_sweet_crcd_spot(254,10000))
