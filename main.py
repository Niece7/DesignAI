import os
import discord
from keep_alive import keep_alive
from discord.ext import commands

# Explicitly enable all Intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd)
    print(f'Logged in as {bot.user.name}')
# قم بتحديد معرفات المستخدمين المرخص لهم
authorized_users = [413611451589328921, 874935399108186133,465153546808197130,924280105411412049]

@bot.command(name='skin')
async def skin_command(ctx, skin_number: int):
    # التحقق من أن المستخدم هو أحد المستخدمين المرخص لهم
    if ctx.author.id in authorized_users:
        if 0 <= skin_number <= 312:
            titles = {
                0: "cj",
                1: "truth",
                2: "maccer",
                3: "cdeput",
                4: "sfpdm1",
                5: "bb",
                6: "wfycrp",
                7: "male01",
                8: "wmycd2",
                9: "bfori",
                10: "bfost",
                11: "vbfycrp",
                12: "bfyri",
                13: "bfyst",
                14: "bmori",
                15: "bmost",
                16: "bmyap",
                17: "bmybu",
                18: "bmybe",
                19: "bmydj",
                20: "bmyri",
                21: "bmycr",
                22: "bmyst",
                23: "wmybmx",
                24: "wbdyg1",
                25: "wbdyg2",
                26: "wmybp",
                27: "wmycon",
                28: "bmydrug",
                29: "wmydrug",
                30: "hmydrug",
                31: "dwfolc",
                32: "dwmolc1",
                33: "dwmolc2",
                34: "dwmylc1",
                35: "hmogar",
                36: "wmygol1",
                37: "wmygol2",
                38: "hfori",
                39: "hfost",
                40: "hfyri",
                41: "hfyst",
                42: "suzie",
                43: "hmori",
                44: "hmost",
                45: "hmybe",
                46: "hmyri",
                47: "hmycr",
                48: "hmyst",
                49: "omokung",
                50: "wmymech",
                51: "bmymoun",
                52: "wmymoun",
                53: "ofori",
                54: "ofost",
                55: "ofyri",
                56: "ofyst",
                57: "omori",
                58: "omost",
                59: "omyri",
                60: "omyst",
                61: "wmyplt",
                62: "wmopj",
                63: "✋ اتق الله في نفسك يا اخي",
                64: "✋ اتق الله في نفسك يا اخي",
                65: "vwmyap",
                66: "bmypol1",
                67: "bmypol2",
                68: "wmoprea",
                69: "sbfyst",
                70: "wmosci",
                71: "wmysgrd",
                72: "swmyhp1",
                73: "swmyhp2",
                75: "✋ اتق الله في نفسك يا اخي",
                76: "wfystew",
                77: "swmotr1",
                78: "wmotr1",
                79: "bmotr1",
                80: "vbmybox",
                81: "vwmybox",
                82: "vhmyelv",
                83: "vbmyelv",
                84: "vimyelv",
                85: "✋ اتق الله في نفسك يا اخي",
                86: "vhfyst",
                87: "✋ اتق الله في نفسك يا اخي",
                88: "wfori",
                89: "wfost",
                90: "✋ اتق الله في نفسك يا اخي",
                91: "wfyri",
                92: "✋ اتق الله في نفسك يا اخي",
                93: "wfyst",
                94: "wmori",
                95: "wmost",
                96: "wmyjg",
                97: "wmylg",
                98: "wmyri",
                99: "wmyro",
                100: "wmycr",
                101: "wmyst",
                102: "ballas1",
                103: "ballas2",
                104: "ballas3",
                105: "fam1",
                106: "fam2",
                107: "fam3",
                108: "lsv1",
                109: "lsv2",
                110: "lsv3",
                111: "maffa",
                112: "maffb",
                113: "mafboss",
                114: "vla1",
                115: "vla2",
                116: "vla3",
                117: "triada",
                118: "triadb",
                119: "lvpdm1",
                120: "triboss",
                121: "dnb1",
                122: "dnb2",
                123: "dnb3",
                124: "vmaff1",
                125: "vmaff2",
                126: "vmaff3",
                127: "vmaff4",
                128: "dnmylc",
                129: "dnfolc1",
                130: "dnfolc2",
                131: "dnfylc",
                132: "dnmolc1",
                133: "dnmolc2",
                134: "sbmotr2",
                135: "swmotr2",
                136: "sbmytr3",
                137: "swmotr3",
                138: "✋ اتق الله في نفسك يا اخي",
                139: "✋ اتق الله في نفسك يا اخي",
                140: "✋ اتق الله في نفسك يا اخي",
                141: "sofybu",
                142: "sbmyst",
                143: "sbmycr",
                144: "bmycg",
                145: "✋ اتق الله في نفسك يا اخي",
                146: "hmycm",
                147: "wmybu",
                148: "bfybu",
                150: "wfybu",
                151: "✋ اتق الله في نفسك يا اخي",
                152: "✋ اتق الله في نفسك يا اخي",
                153: "wmyconb",
                154: "wmybe",
                155: "wmypizz",
                156: "bmobar",
                157: "cwfyhb",
                158: "cwmofr",
                159: "cwmohb1",
                160: "cwmohb2",
                161: "cwmyfr",
                162: "cwmyhb1",
                163: "bmyboun",
                164: "wmyboun",
                165: "wmomib",
                166: "bmymib",
                167: "wmybell",
                168: "bmochil",
                169: "sofyri",
                170: "somyst",
                171: "vwmybjd",
                172: "vwfycrp",
                173: "sfr1",
                174: "sfr2",
                175: "sfr3",
                176: "bmybar",
                177: "wmybar",
                178: "✋ اتق الله في نفسك يا اخي",
                179: "wmyammo",
                180: "bmytatt",
                181: "vwmycr",
                182: "vbmocd",
                183: "vbmycr",
                184: "vhmycr",
                185: "sbmyri",
                186: "somyri",
                187: "somybu",
                188: "swmyst",
                189: "wmyva",
                190: "copgrl3",
                191: "gungrl3",
                192: "mecgrl3",
                193: "nurgrl3",
                194: "crogrl3",
                195: "gangrl3",
                196: "cwfofr",
                197: "cwfohb",
                198: "cwfyfr1",
                199: "cwfyfr2",
                200: "cwmyhb2",
                201: "dwfylc2",
                202: "dwmylc2",
                203: "omykara",
                204: "wmykara",
                205: "wfyburg",
                206: "vwmycd",
                207: "✋ اتق الله في نفسك يا اخي",
                209: "omonood",
                210: "omoboat",
                211: "wfyclot",
                212: "vwmotr1",
                213: "vwmotr2",
                214: "✋ اتق الله في نفسك يا اخي",
                215: "sbfori",
                216: "swfyri",
                217: "wmyclot",
                218: "sbfost",
                219: "sbfyri",
                220: "sbmocd",
                221: "sbmori",
                222: "sbmost",
                223: "shmycr",
                224: "sofori",
                225: "sofost",
                226: "sofyst",
                227: "somobu",
                228: "somori",
                229: "somost",
                230: "swmotr5",
                231: "swfori",
                232: "swfost",
                233: "swfyst",
                234: "swmocd",
                235: "swmori",
                236: "swmost",
                237: "✋ اتق الله في نفسك يا اخي",
                238: "✋ اتق الله في نفسك يا اخي",
                239: "swmotr4",
                240: "swmyri",
                241: "smyst",
                242: "smyst2",
                243: "✋ اتق الله في نفسك يا اخي",
                244: "✋ اتق الله في نفسك يا اخي",
                245: "✋ اتق الله في نفسك يا اخي",
                246: "✋ اتق الله في نفسك يا اخي",
                247: "bikera",
                248: "bikerb",
                249: "bmypimp",
                250: "swmycr",
                251: "✋ اتق الله في نفسك يا اخي",
                252: "wmyva2",
                253: "bmosec",
                254: "bikdrug",
                255: "wmych",
                256: "✋ اتق الله في نفسك يا اخي",
                257: "✋ اتق الله في نفسك يا اخي",
                258: "heck1",
                259: "heck2",
                260: "bmycon",
                261: "wmycd1",
                262: "bmocd",
                263: "vwfywa2",
                264: "wmoice",
                265: "tenpen",
                266: "pulaski",
                267: "hern",
                268: "dwayne",
                269: "smoke",
                270: "sweet",
                271: "ryder",
                272: "forelli",
                273: "mediatr",
                274: "laemt1",
                275: "lvemt1",
                276: "sfemt1",
                277: "lafd1",
                278: "lvfd1",
                279: "sffd1",
                280: "lapd1",
                281: "sfpd1",
                282: "lvpd1",
                283: "csher",
                284: "lapdm1",
                285: "swat",
                286: "fbi",
                287: "army",
                288: "dsher",
                289: "somyap",
                290: "rose",
                291: "paul",
                292: "cesar",
                293: "ogloc",
                294: "wuzimu",
                295: "torino",
                296: "jizzy",
                297: "maddogg",
                298: "cat",
                299: "claude",
                300: "ryder2",
                301: "ryder3",
                302: "emmet",
                303: "andre",
                304: "kendl",
                305: "jethro",
                306: "zero",
                307: "tbone",
                308: "sindaco",
                309: "janitor",
                310: "bbthin",
                311: "smokev",
                312: "psycho"
            }
            images = {
                1: "https://i.ibb.co/5cB1sRV/image.png",
                2: "https://i.ibb.co/jTyXG6h/image.png",
                3: "https://i.ibb.co/TYynXvb/image.png",
                4: "https://i.ibb.co/p26Kn1Z/image.png",
                5: "https://i.ibb.co/FbsnKrZ/image.png",
                6: "https://i.ibb.co/P1gqsG8/Achraf-Vip.png",
                7: "https://i.ibb.co/DMrSZp5/Achraf-Vip.png",
                8: "https://i.ibb.co/Tbppvvg/Achraf-Vip.png",
                9: "https://i.ibb.co/kqGMXzv/Achraf-Vip.png",
                10: "https://i.ibb.co/hWGDYkR/Achraf-Vip.png",
                11: "https://i.ibb.co/c6k9GWC/Achraf-Vip.png",
                12: "https://i.ibb.co/tC7ZTLy/Achraf-Vip.png",
                13: "https://i.ibb.co/QmRLf7s/Achraf-Vip.png",
                14: "https://i.ibb.co/4s9gSGS/Achraf-Vip.png",
                15: "https://i.ibb.co/Yy1jqQt/Achraf-Vip.png",
                16: "https://i.ibb.co/64yDt2N/Achraf-Vip.png",
                17: "https://i.ibb.co/Mh92YwC/Achraf-Vip.png",
                18: "https://i.ibb.co/0GvH0jk/Achraf-Vip.png",
                19: "https://i.ibb.co/KVF88bs/Achraf-Vip.png",
                20: "https://i.ibb.co/NTvH5mQ/Achraf-Vip.png",
                21: "https://i.ibb.co/99CJzH4/Achraf-Vip.png",
                22: "https://i.ibb.co/LJ2mx1k/Achraf-Vip.png",
                23: "https://i.ibb.co/qgCfsxm/Achraf-Vip.png",
                24: "https://i.ibb.co/f9jfN5r/Achraf-Vip.png",
                25: "https://i.ibb.co/1bd63Gh/Achraf-Vip.png",
                26: "https://i.ibb.co/vJvGdBd/Achraf-Vip.png",
                27: "https://i.ibb.co/kmRYMvw/Achraf-Vip.png",
                28: "https://i.ibb.co/k9Rgy1x/Achraf-Vip.png",
                29: "https://i.ibb.co/XFSfFsB/Achraf-Vip.png",
                30: "https://i.ibb.co/4FBFPVD/Achraf-Vip.png",
                31: "https://i.ibb.co/rfK2g9M/Achraf-Vip.png",
                32: "https://i.ibb.co/F7VZvGy/Achraf-Vip.png",
                33: "https://i.ibb.co/G2Wr6Kb/Achraf-Vip.png",
                34: "https://i.ibb.co/KV7cd0X/Achraf-Vip.png",
                35: "https://i.ibb.co/pWv80WD/Achraf-Vip.png",
                36: "https://i.ibb.co/VQTx6jL/Achraf-Vip.png",
                37: "https://i.ibb.co/JQgD2qX/Achraf-Vip.png",
                38: "https://i.ibb.co/5Wgrpg4/Achraf-Vip.png",
                39: "https://i.ibb.co/99HrXRb/Achraf-Vip.png",
                40: "https://i.ibb.co/1rWFSKz/Achraf-Vip.png",
                41: "https://i.ibb.co/CbZ9MZq/Achraf-Vip.png",
                42: "https://i.ibb.co/jgYQZ7f/Achraf-Vip.png",
                43: "https://i.ibb.co/R0LxPJc/Achraf-Vip.png",
                44: "https://i.ibb.co/qBzXkRn/Achraf-Vip.png",
                45: "https://i.ibb.co/0fXzsnZ/Achraf-Vip.png",
                46: "https://i.ibb.co/K9Z1Tt9/Achraf-Vip.png",
                47: "https://i.ibb.co/F0Y8L0R/Achraf-Vip.png",
                48: "https://i.ibb.co/2SFKwDr/Achraf-Vip.png",
                49: "https://i.ibb.co/2ZZRHNN/Achraf-Vip.png",
                50: "https://i.ibb.co/Wxw7WFn/Achraf-Vip.png",
                51: "https://i.ibb.co/YNSMwZy/Achraf-Vip.png",
                52: "https://i.ibb.co/2NSDfBD/Achraf-Vip.png",
                53: "https://i.ibb.co/9q5McNS/Achraf-Vip.png",
                54: "https://i.ibb.co/wJg2k2b/Achraf-Vip.png",
                55: "https://i.ibb.co/jb1LK6C/Achraf-Vip.png",
                56: "https://i.ibb.co/GCR71QS/Achraf-Vip.png",
                57: "https://i.ibb.co/mXRCPd8/Achraf-Vip.png",
                58: "https://i.ibb.co/SX0h1rN/Achraf-Vip.png",
                59: "https://i.ibb.co/6sBCkVX/Achraf-Vip.png",
                60: "https://i.ibb.co/kyqYS86/Achraf-Vip.png",
                61: "https://i.ibb.co/0rR9jYm/Achraf-Vip.png",
                62: "https://i.ibb.co/bmR69Th/Achraf-Vip.png",
                63: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                64: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                65: "https://i.ibb.co/5vtc9fP/Achraf-Vip.png",
                66: "https://i.ibb.co/f1wfP9c/Achraf-Vip.png",
                67: "https://i.ibb.co/tsfQKC9/Achraf-Vip.png",
                68: "https://i.ibb.co/Nm65fb2/Achraf-Vip.png",
                69: "https://i.ibb.co/7CKmRD4/Achraf-Vip.png",
                70: "https://i.ibb.co/Mc5Nyfh/Achraf-Vip.png",
                71: "https://i.ibb.co/7KN84rC/Achraf-Vip.png",
                72: "https://i.ibb.co/3kVdfjX/Achraf-Vip.png",
                73: "https://i.ibb.co/b2dtCWv/Achraf-Vip.png",
                75: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                76: "https://i.ibb.co/JRdCF1J/Achraf-Vip.png",
                77: "https://i.ibb.co/gMxfbsG/Achraf-Vip.png",
                78: "https://i.ibb.co/fkRCbS6/Achraf-Vip.png",
                79: "https://i.ibb.co/Tgc9ffT/Achraf-Vip.png",
                80: "https://i.ibb.co/T2ZPBrh/Achraf-Vip.png",
                81: "https://i.ibb.co/dMvn9KC/Achraf-Vip.png",
                82: "https://i.ibb.co/NynQG1G/Achraf-Vip.png",
                83: "https://i.ibb.co/ggy3G4T/Achraf-Vip.png",
                84: "https://i.ibb.co/vhvwkdw/Achraf-Vip.png",
                85: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                86: "https://i.ibb.co/MSYnBnF/Achraf-Vip.png",
                87: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                88: "https://i.ibb.co/5TWKTdk/Achraf-Vip.png",
                89: "https://i.ibb.co/Q6Pn1cK/Achraf-Vip.png",
                90: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                91: "https://i.ibb.co/HY24WTC/Achraf-Vip.png",
                92: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                93: "https://i.ibb.co/ngBpwZ8/Achraf-Vip.png",
                94: "https://i.ibb.co/4YgHkMC/Achraf-Vip.png",
                95: "https://i.ibb.co/tpmkfPb/Achraf-Vip.png",
                96: "https://i.ibb.co/KFkMbwj/Achraf-Vip.png",
                97: "https://i.ibb.co/c3YcsVT/Achraf-Vip.png",
                98: "https://i.ibb.co/b7wFykh/Achraf-Vip.png",
                99: "https://i.ibb.co/F6BjBmf/Achraf-Vip.png",
                100: "https://i.ibb.co/3shrzwk/Achraf-Vip.png",
                101: "https://i.ibb.co/DzKjsVG/Achraf-Vip.png",
                102: "https://i.ibb.co/WHz4cg0/Achraf-Vip.png",
                103: "https://i.ibb.co/2Mn2Hqn/Achraf-Vip.png",
                104: "https://i.ibb.co/ydP8qXS/Achraf-Vip.png",
                105: "https://i.ibb.co/j6B7Bbn/Achraf-Vip.png",
                106: "https://i.ibb.co/8Dz00sJ/Achraf-Vip.png",
                107: "https://i.ibb.co/NLNLFyG/Achraf-Vip.png",
                108: "https://i.ibb.co/Mhr1cYn/Achraf-Vip.png",
                109: "https://i.ibb.co/8sknYkh/Achraf-Vip.png",
                110: "https://i.ibb.co/2WF3LzF/Achraf-Vip.png",
                111: "https://i.ibb.co/5KSRcg5/Achraf-Vip.png",
                112: "https://i.ibb.co/ZXc6H9M/Achraf-Vip.png",
                113: "https://i.ibb.co/WBqvPJ9/Achraf-Vip.png",
                114: "https://i.ibb.co/C9BNWnq/Achraf-Vip.png",
                115: "https://i.ibb.co/93Xq9mL/Achraf-Vip.png",
                116: "https://i.ibb.co/hBNDg7b/Achraf-Vip.png",
                117: "https://i.ibb.co/ggxL6Cd/Achraf-Vip.png",
                118: "https://i.ibb.co/zfBFQcS/Achraf-Vip.png",
                119: "https://i.ibb.co/jJWDp0v/Achraf-Vip.png",
                120: "https://i.ibb.co/xggy7Nb/Achraf-Vip.png",
                121: "https://i.ibb.co/cJxpNKD/Achraf-Vip.png",
                122: "https://i.ibb.co/rxppKpd/Achraf-Vip.png",
                123: "https://i.ibb.co/FKTbfKQ/Achraf-Vip.png",
                124: "https://i.ibb.co/SJcmX4H/Achraf-Vip.png",
                125: "https://i.ibb.co/0YcKzvy/Achraf-Vip.png",
                126: "https://i.ibb.co/zJXdfgJ/Achraf-Vip.png",
                127: "https://i.ibb.co/qrrVnX7/Achraf-Vip.png",
                128: "https://i.ibb.co/VLPh7dt/Achraf-Vip.png",
                129: "https://i.ibb.co/9nZRcNS/Achraf-Vip.png",
                130: "https://i.ibb.co/dLG4Zbd/Achraf-Vip.png",
                131: "https://i.ibb.co/wCRGRMM/Achraf-Vip.png",
                132: "https://i.ibb.co/HzX7SXQ/Achraf-Vip.png",
                133: "https://i.ibb.co/bF0NmNp/Achraf-Vip.png",
                134: "https://i.ibb.co/QmN5VCd/Achraf-Vip.png",
                135: "https://i.ibb.co/dmF2CKZ/Achraf-Vip.png",
                136: "https://i.ibb.co/1RcSYsY/Achraf-Vip.png",
                137: "https://i.ibb.co/9vpHVRN/Achraf-Vip.png",
                138: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                139: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                140: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                141: "https://i.ibb.co/CmNk1wH/Achraf-Vip.png",
                142: "https://i.ibb.co/LPnwHJX/Achraf-Vip.png",
                143: "https://i.ibb.co/GvDCBd7/Achraf-Vip.png",
                144: "https://i.ibb.co/q0T3g3B/Achraf-Vip.png",
                145: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                146: "https://i.ibb.co/jkLcbPC/Achraf-Vip.png",
                147: "https://i.ibb.co/KVhQ029/Achraf-Vip.png",
                148: "https://i.ibb.co/JCLzLDj/Achraf-Vip.png",
                150: "https://i.ibb.co/1zSw0XM/Achraf-Vip.png",
                151: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                152: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                153: "https://i.ibb.co/BqKsgZM/Achraf-Vip.png",
                154: "https://i.ibb.co/LZ58B33/Achraf-Vip.png",
                155: "https://i.ibb.co/JFF6dmZ/Achraf-Vip.png",
                156: "https://i.ibb.co/G756736/Achraf-Vip.png",
                157: "https://i.ibb.co/3h714MV/Achraf-Vip.png",
                158: "https://i.ibb.co/0YJcYR2/Achraf-Vip.png",
                159: "https://i.ibb.co/JtVKYnV/Achraf-Vip.png",
                160: "https://i.ibb.co/pLzb9SJ/Achraf-Vip.png",
                161: "https://i.ibb.co/d4kvxSC/Achraf-Vip.png",
                162: "https://i.ibb.co/MNCqn2R/Achraf-Vip.png",
                163: "https://i.ibb.co/3RcG58V/Achraf-Vip.png",
                164: "https://i.ibb.co/CwNwjK1/Achraf-Vip.png",
                165: "https://i.ibb.co/588NKPD/Achraf-Vip.png",
                166: "https://i.ibb.co/tHct9w0/Achraf-Vip.png",
                167: "https://i.ibb.co/TYgHVkv/Achraf-Vip.png",
                168: "https://i.ibb.co/z48h79K/Achraf-Vip.png",
                169: "https://i.ibb.co/rFXS0tD/Achraf-Vip.png",
                170: "https://i.ibb.co/QCHWnYG/Achraf-Vip.png",
                171: "https://i.ibb.co/9g4w0Cx/Achraf-Vip.png",
                172: "https://i.ibb.co/q9t9Y5x/Achraf-Vip.png",
                173: "https://i.ibb.co/1nbNmJh/Achraf-Vip.png",
                174: "https://i.ibb.co/GkdpzXP/Achraf-Vip.png",
                175: "https://i.ibb.co/PCFvHWQ/Achraf-Vip.png",
                176: "https://i.ibb.co/PFWqgk7/Achraf-Vip.png",
                177: "https://i.ibb.co/7J4P4D3/Achraf-Vip.png",
                178: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                179: "https://i.ibb.co/dmLNL3v/Achraf-Vip.png",
                180: "https://i.ibb.co/WxYrJbp/Achraf-Vip.png",
                181: "https://i.ibb.co/yF0cWHq/Achraf-Vip.png",
                182: "https://i.ibb.co/Z6NLYK1/Achraf-Vip.png",
                183: "https://i.ibb.co/HxK6r9v/Achraf-Vip.png",
                184: "https://i.ibb.co/X3sSd6j/Achraf-Vip.png",
                185: "https://i.ibb.co/LNgSvyM/Achraf-Vip.png",
                186: "https://i.ibb.co/9thdFT9/Achraf-Vip.png",
                187: "https://i.ibb.co/cQTzvm7/Achraf-Vip.png",
                188: "https://i.ibb.co/TKPfmcJ/Achraf-Vip.png",
                189: "https://i.ibb.co/vskf83d/Achraf-Vip.png",
                190: "https://i.ibb.co/nf97241/Achraf-Vip.png",
                191: "https://i.ibb.co/R6RhyCN/Achraf-Vip.png",
                192: "https://i.ibb.co/z5k0VY1/Achraf-Vip.png",
                193: "https://i.ibb.co/PMLJ6rs/Achraf-Vip.png",
                194: "https://i.ibb.co/BwzhWkt/Achraf-Vip.png",
                195: "https://i.ibb.co/JnTYYT0/Achraf-Vip.png",
                196: "https://i.ibb.co/6HGDc91/Achraf-Vip.png",
                197: "https://i.ibb.co/Trg7wTT/Achraf-Vip.png",
                198: "https://i.ibb.co/M7qSP1d/Achraf-Vip.png",
                199: "https://i.ibb.co/3pVgLS2/Achraf-Vip.png",
                200: "https://i.ibb.co/0CCBF1w/Achraf-Vip.png",
                201: "https://i.ibb.co/7NCvh2B/Achraf-Vip.png",
                202: "https://i.ibb.co/r5C4CJq/Achraf-Vip.png",
                203: "https://i.ibb.co/bJnGPpX/Achraf-Vip.png",
                204: "https://i.ibb.co/7YcXX1h/Achraf-Vip.png",
                205: "https://i.ibb.co/DGh6pWD/Achraf-Vip.png",
                206: "https://i.ibb.co/dLQLP23/Achraf-Vip.png",
                207: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                209: "https://i.ibb.co/8zThYQn/Achraf-Vip.png",
                210: "https://i.ibb.co/VVjNb62/Achraf-Vip.png",
                211: "https://i.ibb.co/drQ2QxG/Achraf-Vip.png",
                212: "https://i.ibb.co/TYDr7Dx/Achraf-Vip.png",
                213: "https://i.ibb.co/qyzC9vQ/Achraf-Vip.png",
                214: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                215: "https://i.ibb.co/cg46QDd/Achraf-Vip.png",
                216: "https://i.ibb.co/kXSXKtr/Achraf-Vip.png",
                217: "https://i.ibb.co/0YxPst3/Achraf-Vip.png",
                218: "https://i.ibb.co/D7VRpJ5/Achraf-Vip.png",
                219: "https://i.ibb.co/r44VVJr/Achraf-Vip.png",
                220: "https://i.ibb.co/93RvhtN/Achraf-Vip.png",
                221: "https://i.ibb.co/7Ytgk6Y/Achraf-Vip.png",
                222: "https://i.ibb.co/Yk4sWyk/Achraf-Vip.png",
                223: "https://i.ibb.co/0ndD5t5/Achraf-Vip.png",
                224: "https://i.ibb.co/Wy6zxBF/Achraf-Vip.png",
                225: "https://i.ibb.co/bbKYvth/Achraf-Vip.png",
                226: "https://i.ibb.co/NKgHPk6/Achraf-Vip.png",
                227: "https://i.ibb.co/26Gyrsc/Achraf-Vip.png",
                228: "https://i.ibb.co/XzgXZhj/Achraf-Vip.png",
                229: "https://i.ibb.co/gjWVD6p/Achraf-Vip.png",
                230: "https://i.ibb.co/bvX5rTD/Achraf-Vip.png",
                231: "https://i.ibb.co/XLmNRYs/Achraf-Vip.png",
                232: "https://i.ibb.co/Pwhk43d/Achraf-Vip.png",
                233: "https://i.ibb.co/t4RQCnc/Achraf-Vip.png",
                234: "https://i.ibb.co/41Zmgrw/Achraf-Vip.png",
                235: "https://i.ibb.co/dg3xWGM/Achraf-Vip.png",
                236: "https://i.ibb.co/1J4nbQD/Achraf-Vip.png",
                237: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                238: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                239: "https://i.ibb.co/2NPLjTm/Achraf-Vip.png",
                240: "https://i.ibb.co/27N86RT/Achraf-Vip.png",
                241: "https://i.ibb.co/SPKhNsV/Achraf-Vip.png",
                242: "https://i.ibb.co/P4WXmc5/Achraf-Vip.png",
                243: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                244: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                245: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                246: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                247: "https://i.ibb.co/R6GW85d/Achraf-Vip.png",
                248: "https://i.ibb.co/kKJSHLP/Achraf-Vip.png",
                249: "https://i.ibb.co/LRdBNBP/Achraf-Vip.png",
                250: "https://i.ibb.co/LdCKJXH/Achraf-Vip.png",
                251: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                252: "https://i.ibb.co/Z1fsW6j/Achraf-Vip.png",
                253: "https://i.ibb.co/0Dz0gbj/Achraf-Vip.png",
                254: "https://i.ibb.co/R6GW85d/Achraf-Vip.png",
                255: "https://i.ibb.co/3mF7SDs/Achraf-Vip.png",
                256: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                257: "https://i.ibb.co/rHMcZYK/Achraf-Vip.webp",
                258: "https://i.ibb.co/WgS42V9/Achraf-Vip.png",
                259: "https://i.ibb.co/tKDqfxw/Achraf-Vip.png",
                260: "https://i.ibb.co/LzZLNVP/Achraf-Vip.png",
                261: "https://i.ibb.co/80Pz0gH/Achraf-Vip.png",
                262: "https://i.ibb.co/JBD4g0H/Achraf-Vip.png",
                263: "https://i.ibb.co/PmvV6cz/Achraf-Vip.png",
                264: "https://i.ibb.co/zbnhxVV/Achraf-Vip.png",
                265: "https://i.ibb.co/xfrKGJp/Achraf-Vip.png",
                266: "https://i.ibb.co/GT1VHNx/Achraf-Vip.png",
                267: "https://i.ibb.co/fNx6GBp/Achraf-Vip.png",
                268: "https://i.ibb.co/fxrS2Sr/Achraf-Vip.png",
                269: "https://i.ibb.co/9b11SJx/Achraf-Vip.png",
                270: "https://i.ibb.co/xYDX22T/Achraf-Vip.png",
                271: "https://i.ibb.co/v3mzzTf/Achraf-Vip.png",
                272: "https://i.ibb.co/v1HbT16/Achraf-Vip.png",
                273: "https://i.ibb.co/p059s4B/Achraf-Vip.png",
                274: "https://i.ibb.co/HDJWWWd/Achraf-Vip.png",
                275: "https://i.ibb.co/f2mPXZP/Achraf-Vip.png",
                276: "https://i.ibb.co/P9hzQTP/Achraf-Vip.png",
                277: "https://i.ibb.co/xG0bdQx/Achraf-Vip.png",
                278: "https://i.ibb.co/X3bXTZ6/Achraf-Vip.png",
                279: "https://i.ibb.co/Zf42X15/Achraf-Vip.png",
                280: "https://i.ibb.co/chsV924/Achraf-Vip.png",
                281: "https://i.ibb.co/KWWfvNY/Achraf-Vip.png",
                282: "https://i.ibb.co/y6WScmK/Achraf-Vip.png",
                283: "https://i.ibb.co/YNGtdkX/Achraf-Vip.png",
                284: "https://i.ibb.co/6swB47b/Achraf-Vip.png",
                285: "https://i.ibb.co/NV9rcsW/Achraf-Vip.png",
                286: "https://i.ibb.co/7byMzny/Achraf-Vip.png",
                287: "https://i.ibb.co/qptWJKB/Achraf-Vip.png",
                288: "https://i.ibb.co/ZHtF7x3/Achraf-Vip.png",
                289: "https://i.ibb.co/3F2Jq1P/Achraf-Vip.png",
                290: "https://i.ibb.co/kGKcs9Q/Achraf-Vip.png",
                291: "https://i.ibb.co/ys7BjjP/Achraf-Vip.png",
                292: "https://i.ibb.co/nn9mpm0/Achraf-Vip.png",
                293: "https://i.ibb.co/FJHzhPD/Achraf-Vip.png",
                294: "https://i.ibb.co/VBtx2JK/Achraf-Vip.png",
                295: "https://i.ibb.co/F08wPsx/Achraf-Vip.png",
                296: "https://i.ibb.co/kxpwr3h/Achraf-Vip.png",
                297: "https://i.ibb.co/jzsHGpH/Achraf-Vip.png",
                298: "https://i.ibb.co/XD2W3ZD/Achraf-Vip.png",
                299: "https://i.ibb.co/2K8fb8v/Achraf-Vip.png",
                300: "https://i.ibb.co/v3mzzTf/Achraf-Vip.png",
                301: "https://i.ibb.co/xf6MDFc/Achraf-Vip.png",
                302: "https://i.ibb.co/GRt1R7Y/Achraf-Vip.png",
                303: "https://i.ibb.co/K2Yh8tL/Achraf-Vip.png",
                304: "https://i.ibb.co/G55TGCd/Achraf-Vip.png",
                305: "https://i.ibb.co/4N56hnH/Achraf-Vip.png",
                306: "https://i.ibb.co/gSvn7Y0/Achraf-Vip.png",
                307: "https://i.ibb.co/RCzRcXq/Achraf-Vip.png",
                308: "https://i.ibb.co/dgfWPkn/Achraf-Vip.png",
                309: "https://i.ibb.co/7YqVnCk/Achraf-Vip.png",
                310: "https://i.ibb.co/tcW8YbH/Achraf-Vip.png",
                311: "https://i.ibb.co/hc6xPMX/Achraf-Vip.png",
                312: "https://i.ibb.co/HV565HH/Achraf-Vip.png"
            }
            title = titles.get(skin_number, "Unknown Skin")
            image_url = images.get(skin_number, "https://example.com/unknown.jpg")

            embed = discord.Embed(title=title, description=f"\nID {skin_number}")
            embed.set_image(url=image_url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("الرجاء إدخال رقم جلد صالح (من 1 إلى 3)")
    else:
        embed = discord.Embed(
            title="التصريح ممنوع",
            description="ليس لديك الصلاحية للوصول إلى هذا الخيار.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

# Status Profile Bot
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="المبدع التلقائي للتصميم ✨"))
# استخدم توكن البوت المخزن في ملف secrets
keep_alive()
my_secret = os.environ['discord']
bot.run(my_secret)
