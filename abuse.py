#written by @doctorvicky /runs commands inspired by Rose.
#Join in my channel @hikariplugins

import random
filipino = ["tumatakbo na nga eto na oh!","Pag ako napagod wala kanang bot...","Oh no! Nakalayo na siya!","Tumingin ka sa dinaraanan mo..","Wala pa akong jowa...","Pogi ng owner ko yieee","3% battery kaya pag diko na to na type ibig sab- ","Uutot ka pa eh amoy utot na bibig mo.","Run sige run! Habulin mo kahit dika mahal.","Ayos ng sistema ko gusto mo bang sirain ko?","Maayos akong tumatakbo... sa maling tao nga lang."," Ayoko nang tumakbo napapagod nako. Itigil na natin 'to..","Pag ba tumigil ako sa pagtakbo ikaka saya mo?"," 1% nalang battery ko kapag diko na naituloy to-"]
@ultroid_cmd(pattern="/rruns")
async def coinflip(ult):
  await ult.edit("Running...")
  f = random.choice(filipino)
  return await ult.edit(f"**{f}**")

english = ["Watch out for the wall.","Oh no, hes getting away!","Keep it up, you look like you need the exercise.","Legend has it, they're still running...","RELEASE THE KRAKENNNNN","Roll back to the kitchen.","You just keep on running...","Once upon a time, there was a - Oy, don't interrupt me.","Whoops, who let the dogs out?","Run fatboy, run!","You call that running? Pathetic.","I don't want to run! Lmao!","Eeeny, meeny, miny, moe, I don't care, so out you go","You just keep on running... to the girl that don't like you...","Oh look! Someone who thinks I give a damn.","If I run, Who's your bot? Lmao!"]
@ultroid_cmd(pattern="/runs")
async def coinflip(ult):
  await ult.edit("Running...")
  e = random.choice(english)
  return await ult.edit(f"**{e}**")