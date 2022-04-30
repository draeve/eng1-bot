import discord
from discord.ext import commands
#https://discordpy.readthedocs.io/en/stable/quickstart.html
from discord import Webhook, RequestsWebhookAdapter
import os

TOKEN = 'x'

description = 'Custom (Text) Commands for Eng1\n\n//Use Dyno for role-related commands'
bot = commands.Bot(command_prefix='?', description=description)

client = discord.Client()

blacklisted = []


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----')
    
    activity = discord.Game(name="Eng 1 bot || ?help")
    await bot.change_presence(status=discord.Status.online, activity=activity)


class Copypasta(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    def check_blacklist(ctx):
        return ctx.author.id not in blacklisted    

    @commands.check(check_blacklist)
    @commands.command(
        brief="\t\"power tripping child\"",
        description="")
    #lupin - power tripping child
    async def lupin(self, ctx):        
        await ctx.send('''> I understand you wanna be all "look at me im doing a good job for this community" but unnecessary policing is just toxic and only feeds your own ego. most of the other mods are fine, but aiden you are nothing but a power tripping child. goodbye.''')

    #lupin2
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tur TROLLING",
        description="")
    async def lupin2(self, ctx):
        await ctx.send("u're tROLLIN")


    #lupin3
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tknif",
        description="")
    async def lupin3(self, ctx):
        await ctx.send("hehehe knif :knife:")


    #oli - uwu touch some grass
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tUwU go touch some grass!")
    async def oli(self, ctx):
        embedVar = discord.Embed(description=" ")
        embedVar.set_image(url="https://media.discordapp.net/attachments/569334002507579416/828777858552823868/catKISS.gif")
        await ctx.send(content="""> uwu ♡¨•°'•°~
> 
> I ☆noticed•°¨ that you haven\'t °•♡ touched any grass ♡ •° in a while cause of •°Loncapa¨•°♡~ and ☆•° Dr. Child's Silly Mathematics°•° I know you're in eng and all... but I don't think I can be your discord gf anymore until you go outside and take a shower stinky☆♡•°•¨~ <33 (≧▽≦)"""
                       ,embed=embedVar)

    #anna - long copypasta thing
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tAnna cares <3",
        description="")
    async def anna(self, ctx):
        await ctx.send("> do care + did ask + smile today + be happy + stay cool + W + lets hold hands + girlbosses + cool + kiss kiss + wholesome + any askers (me, I asked) + get a life that includes me+ ok and? Tell me more please + amazing + touch grass with me it’s a picnic date +  based + your're a beautiful human being + very funny currently laughing + perfect spelling + keep on improving + upvoted + gg let’s do that again + ur mom is a lovely woman + I miss you")

    #anna2- slay
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tomg slay",
        description="")
    
    async def anna2(self, ctx):
        await ctx.send("slay")

#julia - long copypasta thing
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tJulia doesn't care </3",
        description="")
    async def julia(self, ctx):
        await ctx.send("> don't care + didn't ask + cry about it + stay mad + get real + L + mald seethe cope harder + hoes mad + basic + skill issue + ratio + you fell off + the audacity + triggered + any askers + redpilled + get a life + ok and? + cringe + touch grass + donowalled + not based + your're a (insert stereotype) + not funny didn't laugh + you're* + grammar issue + go outside + get good + reported + ad hominem + gg ez+ ur mom + rip bozo")



    #julia2 slay
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tok lupin",
        description="")
    
    async def julia2(self, ctx):
        await ctx.send("ok lupin")

    #dear dr childs - copy pasta
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tDear DR. CHILDS ... ",
        description="")
    async def childs(self, ctx):
        await ctx.send("""> DEAR DR. CHILDS, hope you are doing well.
    > 
    > I know I am not. specially after this test.
    > Not just myself, but most of the students in this course are not well.
    > The practice tests and problems you gave us, were of no help. The format of these questions were not good. The test was made specially hard and difficult because we are doing this online. IS THAT FAIR??? NO.
    > 
    > Professor Childs. I on behalf of my fellow classmates ask you to please be generous while marking. We have tried out best to do this test in a timely manner, but the time was NOT enough. These questions required READING, THINKING, and then WRITING the solution. And the time given to us to solve these questions was simply. NOT ENOUGH, specially looking at the difficulty of the test.
    > 
    > We ask you to please help us in this Test and give us generous marks. And please make the test EASIER.
    > 
    > Thank You, sir.
    """)

    #haha fuckboi
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tHey! I saw that you ...",
        description="")
    async def haha(self, ctx):
        await ctx.send("Hey! I saw that you haha-reacted to my message in the course group chat and just wanted to say O M G you are CUTE! I know it's quarantine and case numbers are going up, but would you want to get a drink sometime? I'd be happy to drive out to you if you're not in Hamilton!")

    #nuclear reactor
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tWe love the nuclear reactor!!",
        description="")
    async def nuclear(self, ctx):
        await ctx.send("""> Is anyone else lowkey scared about an impending nuclear disaster happening? Like chernobyl but in hamaltin? As a person living in residence I am afraid.
    > 
    > I live worryingly close to the nuclear reactor and I often notice a gaseous byproduct emanating from the top of the tower. It serves as a reminder to treat every day like it is my last and cherish every moment.
    > 
    > As I type this I am realizing it is not fear but anticipatory glee that I feel towards radiation exposure. It is a double edged swordâ€¦ An end to the onslaught of daysâ€¦ coupled with the Unknownâ€¦ fear itselfâ€¦ I hope that when I am faced with Death himself.""")

    #loncapa - copypasta lmao
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tWe Love LONCAPA <3",
        description="")
    async def loncapa(self, ctx):
        await ctx.send("""> I just love the loncapa experience and hopefully relate with you guys, the moment right after you submit a question, those 10 seconds of refresh time.
    > 
    > Like damn, that is an out of body experience, it is suspended out of time. I feel enlighted every time the submit button is pressed. It has the same thrill of finally asking a girl out and waiting for her response; a fear of rejection, but at the same time the feeling of accomplishment; the excitement of taking your shot, and the chill down your spine to think your investment in such was futile.
    >  
    > The true meaning of superposition, the question is both right and wrong, you can see the red and the green at the same time in front of your eyes. "If you think you understand quantum mechanics, you don't understand quantum mechanics."- a quote by Richard Feynman, a man who did not get to experience the unreasonably and questionably long refreshing times of a strange 1D03 physics exercise.
    >  
    > Submitting a problem is more than an attempt to understand angular momentum, it is the duality of man, it represents the right and wrong, the dark and the light. Loncapa shows us that there is no right or wrong for the 10 seconds that you are waiting, to then decide, to judge our minds and to give us the path to enlightenment.
    """)

    #bosco my beloved
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tbosco my beloved <3")
    async def bosco(self, ctx):
        embedVar = discord.Embed(description=" ")
        embedVar.set_image(url="https://media.discordapp.net/attachments/749823476642218019/908846144354943056/bosco.gif")
        await ctx.send(content="""ENGINEER 1P13 is the best course at McMaster, possibly in the whole world. This is for one simple reason. Bosco. When I see Bosco, I am happy. When I see Bosco, I am whole. Watching Dr. Bosco's amazing Materials Science lectures has reignited my will to live and my passion for engineering. When I see Bosco on his bike, or with a special treat just for me, I know everything will be okay. Truly, one of the few things that helps me sleep at night in this horrid world is knowing that Bosco is also sleeping in it."""
                       ,embed=embedVar)

    #qlabs copypasta
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tQlabs :pain:",
        description="")
    async def lines(self, ctx):
        await ctx.send("""
> I love Q labs so much. The feeling of waiting for 10 seconds every time I press play and watching everything load is such a surreal experience. It feels as if I'm a creator, that I own something. I feel accended almost as if I were more than what I am. However, all good things come to an end. As my code runs onward so does my happiness. And eventually, everything breaks and I'm left with nothing. My once happiness is quickly flooded by a turbulent ocean of anger and confusion as my code doesn't work. Alas, there are no errors. I struggle frantically to fix it to feel once more. However, this moment doesn't come. As I sulk into my chair at each passing minute while watching my Qbot drift away into a wall I look back and ask myself. What is this for, why am I here? With a heavy heart, I run the code again hoping for something... ANYTHING to be different but with little avail. I let out a shrill, almost maniacally laugh as I stare endlessly at my Qbot spinning merrily on my screen for it does not know the pain it has caused me.
""")

    #noura's go to line/phrase
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tgood morning!",
        description="")
    async def noura(self, ctx):
        await ctx.send("hey lil buddies")

    #lines 2 - red name wtf
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tred name ?? das weird",
        description="")
    async def lines2(self, ctx):
        await ctx.send("https://tenor.com/view/red-name-cringe-gif-20534051")

    #anna4 - mitski
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tmitski my beloved",
        description="")
    async def anna4(self, ctx):
        await ctx.send(".wk mitski")

    
    #anna2- slay
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tomg slay",
        description="")
    
    async def anna2(self, ctx):
        await ctx.send("slay")

    #anna3 - fuccboi again
    @commands.command(
        brief="\they haha~",
        description="")
    async def anna3(self, ctx):
        await ctx.send("hey haha")
        await ctx.send("<:ahahafuccboi:821094615955538012> <:ahahafuccboi:821094615955538012> <:ahahafuccboi:821094615955538012> ")


    #anna 5 - wahoo
    @commands.check(check_blacklist)
    @commands.command(
        brief="\twahoo!")
    async def anna5(self, ctx):
        embedVar = discord.Embed(description="")
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/844304464776003606/964607823763869696/unknown.png")
        await ctx.send(embed=embedVar)


    #niraj
    @commands.check(check_blacklist)
    @commands.command(
        brief="\till do anything ;-;",
        description="")
    
    async def niraj(self, ctx):
        await ctx.send("> bruh ill do anything for ?Niraj fr")


    #insk
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tL",
        description="")
    
    async def insk(self, ctx):
        await ctx.send("L")


    #chenisa
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tstronk",
        description="")
    
    async def chenisa(self, ctx):
        await ctx.send("ᕦ(ò_óˇ)ᕤ")

#matthew's free command
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tsadge :(",
        description="")
    async def matthew(self, ctx):
        await ctx.send(":(")


#wola2 - eng1p13 moment
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tGood Job! - 42%")
    async def wola2(self, ctx):
        embedVar = discord.Embed(description="")
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/844304464776003606/966036581586718840/IMG_8112.jpg")
        await ctx.send(embed=embedVar)

#emre - rip basem
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tlet's have an F in chat")
    async def emre(self, ctx):
        embedVar = discord.Embed(description="")
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/844304464776003606/964755338240860260/unknown.png")
        await ctx.send(embed=embedVar)


    #ryan - his sad list of emotes
    @commands.check(check_blacklist)
    @commands.command(
        brief="\t:(",
        description="")
    async def ryan(self, ctx):
        await ctx.send("<:boohoo:855679877956239360> <:sobbing:894394957182435349> <:oksad:844281703036092446> <:sadcat:879152751253274645> <:wawa:905938335686610964> <:birdsob:905937635988615189> <:sadcatcry:910541587329732619> <:friedbirdsob:958823503157678110>")

    #gulk donf command
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tdonf",
        description="")
    async def gulk(self, ctx):
        await ctx.send('donf')

    #draeve - 3 kirbies
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tKirby goes brr",
        description="")
    async def draeve(self, ctx):
        embedVar = discord.Embed(description="")
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/844304464776003606/964752079367311430/unknown.png")
        await ctx.send(embed=embedVar)
        
    #alco - ya got this
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tYOU GOT THIS!!!!!",
        description="")
    async def alco(self, ctx):
        await ctx.send("ya got this!!!")
        await ctx.send("<:birdheart:858364373821816834> <:birdheart:858364373821816834> <:birdheart:858364373821816834>")

    #frog
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tfrog")
    async def frog(self, ctx):
        embedVar = discord.Embed(description="frog")
        embedVar.set_image(url="https://media.discordapp.net/attachments/883897507426471966/909805296250159124/5F6D82A8-3D67-4332-9D68-947089FEE39C.jpg")
        await ctx.send(embed=embedVar)


    #nejat
    @commands.check(check_blacklist)
    @commands.command(
        brief="\trecursive nejat")
    async def nejat(self, ctx):
        embedVar = discord.Embed(description=" ")
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/854819152505995350/909981663059144754/unknown.png")
        await ctx.send(embed=embedVar)
    #bender - nice
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tnice",
        description="")
    
    async def bender(self, ctx):
        await ctx.send("nice!")

    #jazm - i aint even down bad
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tjayzm be like:",
        description="")
    
    async def jayzm(self, ctx):
        await ctx.send("<:jayzm_downbad:953713636071841872>")
    

    #chilly- run it bac
    @commands.check(check_blacklist)
    @commands.command(
        brief="\ttyperacer goes hard",
        description="")
    
    async def chilly(self, ctx):
        await ctx.send("run\nit\n\nBAC")

    #wola - when do i get my shitpost :(
    @commands.check(check_blacklist)
    @commands.command(
        brief="\t</3 no catchphrase?",
        description="")
    
    async def wola(self, ctx):
        await ctx.send("Where my shit post command man")


    #mclean during the exam
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tthe x should be t",
        description="")
    
    async def mclean(self, ctx):
        await ctx.send("the x should be t")


        
class Notable_Quotes(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    def check_blacklist(ctx):
        return ctx.author.id not in blacklisted   
    
    #cyperone - check avenue lmfao
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tWhen in doubt...",
        description="")
    async def cyperone(self, ctx):
        await ctx.send("*check avenue*")

    #ekatris - check childsmath lol
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tIf you haven't already...",
        description="")
    
    async def ekatris(self, ctx):
        await ctx.send("*check childsmath*")

    #parth - check crowdmark lol
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tIf you haven't already...",
        description="")
    
    async def parth(self, ctx):
        await ctx.send("*check crowdmark lol*")


    #cutoffs - thick skulls
    
    @commands.check(check_blacklist)
    @commands.command(
        brief="\tA message for those with thick skulls",
        description="")
    
    async def cutoffs(self, ctx):
        await ctx.send("can you all please get it through your thick skulls that **past cutoffs are not indicative of future cutoffs**")


class Resources(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        #conflict free schedule
    @commands.command(
        brief="\tConflict Free Schedule goes brr",
        description="")
    async def conflict(self, ctx):
        await ctx.send("> A conflict-free timetable has been created for you and due to its complexity, swapping sections of lectures, labs, or tutorials of required courses will result in an enrollment error.")

    @commands.command(
        brief="\tHow to use MyTimetable",
        description="")
    async def timetable(self, ctx):
        await ctx.send("""__How to use MyTimetable__
    \nOverview: <https://youtu.be/MvZ0kqb00-8>
    \nCreating A Preferred Schedule: <https://youtu.be/wRjSN2P3liw>
    \nEnrolling Into Courses: <https://youtu.be/fX9j6bPBVC4>""")

    @commands.command(
        brief="\tEngineering Electives",
        description="")
    async def electives(self, ctx):
        await ctx.send("""
    Engineering Complementary Electives List:
    \nhttps://www.eng.mcmaster.ca/sites/default/files/uploads/booth/complementary_studies_electives_list.pdf""")

    @commands.command(
        brief="\tCo-op opt in form",
        description="")
    async def coop(self, ctx):
        await ctx.send("""Co-op opt-in form:
        \nhttps://www.eng.mcmaster.ca/sites/default/files/co-op_opt_in_form_june_2021_0.pdf""")

    #grades gpa calculator???
    @commands.command(
        brief="\tGPA Calculator",
        description="")
    async def gpa(self, ctx):
        await ctx.send("""> GPA Calculator: https://gradecalc.info/ca/on/mcmaster/gpa_calc.pl
    > GPA Tracker: https://docs.google.com/spreadsheets/d/1SKg4nY1L24kRSKYQmBm4cyEDEdCIXToAoq42OwLdQ2A/edit#gid=0
    """)

    #academic calendar
    @commands.command(
        brief="\tAcademic Calendar",
        description="")
    async def calendar(self, ctx):
        await ctx.send("""> McMaster Academic Calendar (2021-2022): \n\n https://academiccalendars.romcmaster.ca/index.php?catoid=44""")

    @commands.command(
        brief="\tImportant dates and deadlines",
        description="")
    async def dates(self, ctx):
        await ctx.send("""Important Dates & Deadlines:\n\nhttps://registrar.mcmaster.ca/dates-and-deadlines """)

    @commands.command(
        brief="\tDispute Form",
        description="")
    async def dispute(self, ctx):
        await ctx.send("""Dispute Form:\n\nTBA""")
        
    @commands.command(
        brief="\tstream selection",
        description="")
    async def stream(self, ctx):
        await ctx.send("""https://registrar.mcmaster.ca/build-degree/level-ii/\n\nAvailable **April 4th, 2022 @9AM** until **April 30th, 2022 @5PM**""")


bot.add_cog(Copypasta(bot))
bot.add_cog(Notable_Quotes(bot))
bot.add_cog(Resources(bot))
bot.run(TOKEN)
