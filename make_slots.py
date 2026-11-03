"""一次性：以 Rafael 的 drama_slots.py 为底，把人物、地点、服装、时间换成《今天，再喜欢我一次》，写出本剧的 drama_slots.py。
之后直接改 drama_slots.py；规则不在这里，在 tools/realtime-third/templates。"""
import importlib.util, pprint
from pathlib import Path
D = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('raf', '/Users/vicky/Interactive storyline/output/rafael-third-live-v1/drama_slots.py')
raf = importlib.util.module_from_spec(spec); spec.loader.exec_module(raf)
S = dict(raf.SLOTS)

HE_LOOK = ('⟦HE⟧：二十七岁男人，一米八五左右，修长匀称，皮肤光滑干净没有胡茬，长脸型、线条柔和，栗棕色柔和的眉毛，温暖的浅棕色眼睛，直鼻，薄而好看的嘴唇，'
           '蓬松微卷的栗棕色层次短发（几缕垂在额前，不是黑色、不是刺猬头）；没有纹身、没有项链、不戴手表、不戴戒指。'
           '日常穿着：暖中棕色做旧麂皮拉链夹克敞开穿（带翻领，哑光柔软的麂皮，不是深巧克力色、不是黑色、不是亮面皮衣），里面奶白色麻花粗针圆领毛衣，深炭灰色羊毛西裤配黑色皮带（不是牛仔裤），深棕色系带皮短靴；手指上空无一物。'
           '他的长相和服装全程不变，以参考的身份母版为准。')
HER = ('她：二十五岁的成年女人，白皙皮肤，鹅蛋长脸、线条柔和，清澈的绿色眼睛，鼻梁和两颊淡淡的雀斑、很淡的自然红晕，豆沙粉嘴唇，不显幼态；'
       '很长的暖棕色大波浪卷发，一侧编了一条细辫子，别着一枚小金叶发夹，耳垂上一对金叶吊坠耳环；'
       '奶油色泡泡袖方领上衣（方领有蕾丝边），外面一件苔藓橄榄绿绣花系带束腰（绣着叶子），下身橄榄绿长裙，浅棕色低跟短靴；'
       '指甲短而圆、裸色素甲，手指和手腕上空无一物。她的长相、发型和服装全程不变，严格以她的身份母版（正面头像、全身正面、近景特写）为准。她的表情自然克制，情绪在眼神里。')
CAST = ("import json as _json\nTU = _json.loads((Path(__file__).resolve().parent / 'masters' / 'urls.json').read_text())\nCAST = {\n"
        "    'Nora': ('Nora：三十八岁女人，隔壁烘焙店老板，暖笑的圆脸，浅褐色短发齐下巴的波波头，奶油色衬衫外面一条绿色围裙。长相和衣着以她的身份母版为准。', TU['nora']),\n}\n"
        f"HE_LOOK = ({HE_LOOK!r})\n"
        "HER_FP = '她的手外形全程固定：纤细白皙的女性双手，指甲短而圆、裸色素甲，手指和手腕上空无一物，袖口是奶油色泡泡袖。'\n"
        f"HER = ({HER!r})\n"
        "WOLF = ''")

O = {
 'l.BROWS': 'soft chestnut-brown brows',
 'q.HER_HAIR_BAD': '发色变成黑色、金黄或红色、头发变短变直',
 'q.HER_HAIR_BAD2': '或发色变成黑色、金黄、红色、变短',
 'l.FEET_HE': "'脚入镜时他穿深棕色系带皮短靴；他不戴手表、不戴戒指。'",
 'l.LOOK_BASE': "'泡泡袖|束腰|绣花'",
 'l.FEET': "'脚入镜时：他穿深棕色系带皮短靴，她穿浅棕色低跟短靴，不光脚，不换鞋；两人都不戴手表、不戴戒指。'",
 'l.LOOK_OUTER': "'绣花束腰'",
 'l.VEHICLE_LOOK': '薄荷绿复古小踏板摩托（圆形车灯、奶油色坐垫，车身没有文字和标志），',
 'l.HE_LOCK_EN': ("His hair is soft, messy, slightly wavy chestnut-brown with strands over the forehead, not black, not spiky, not long. Light natural skin, clean-shaven, no stubble. A lean long build, not bulky. "
                  "His jacket is warm medium-brown weathered matte suede with a collar, worn open, not dark chocolate, not black, not shiny leather; under it a cream cable-knit crew sweater; dark charcoal wool trousers with a black belt, never jeans; dark brown lace-up leather boots. "
                  "No tattoos, no chain, no watch, no rings."),
 'l.HER_LOCK_EN': ("Her hair is very long, wavy and warm brown, with one thin braid at the side and a small gold leaf hair pin; gold leaf drop earrings; clear green eyes and soft freckles. "
                   "Her top is a cream puff-sleeve blouse with a lace-trimmed square neckline, under a moss-olive laced bodice embroidered with leaves; a long olive skirt; light brown low-heeled ankle boots. Short nude nails, no rings, no necklace."),
 'd.HER_TOP': "'奶油色泡泡袖方领上衣（方领有蕾丝边），外面苔藓橄榄绿绣花系带束腰，下身橄榄绿长裙'",
 'd.PACKPath__': "'meet_pack.json'",
 'd.WRITER_PEr': 'r"""你是女性向互动短剧《今天，再喜欢我一次》实时版的编剧',
 'd.你手里有一份资料包附': '剧本 V4 整理的世界规则和隐藏真相',
 'd.她在主导剧情时资料包-2': '诺拉来送早餐、有客人来问营业、温室里有活要干、有人敲门），不让他把话题拉回过去的相处',
 'd.她说出口的话只来自她': '来历，不替她说“我想起来了”或“我也喜欢你”',
 'd.地点也不限于资料包V': '回小屋、去镇上买东西、去码头',
 'd.她这一轮明确提出的要': '她要他抱她，他就真的抱住；她要去海边走走，她就真的到了海边',
 'd.她在主导剧情时资料包': '',
 'd.带我兜风骑车带我她坐': '她坐在他薄荷绿复古小摩托的后座，他骑车带她，车在海边的路上跑',
 'd.换场怎么发生她选了方': '院门 → 温室主厅 → 起居间书桌 → 水槽工作角 → 诺拉的露台 → 海边步道），由日常安排或外部事件推动（诺拉送来早餐、招牌挂好了、温室的窗要修、有客人来问营业、傍晚约好的时间到了',
 'd.节奏目标只在她没有自': ('轮在院门和温室（核实他的身份、让他进院、挂回写着她名字的招牌、修窗时脱外套的小误会）；第 5–8 轮在温室和她的起居间（他熟悉得反常、她读到自己的笔记本或诺拉说明、他坦白近三个月每天都来并道歉）；'
                          '第 9–12 轮（选一盆植物、诺拉的露台、海边散步和牵手、清醒的吻）；第 13 轮以后为明天留下点什么'),
 'd.每一集至少要有一场吻': '真相说开、她重新决定要不要靠近',
 'd.每一集至少要有一场吻-2': '之前将近三个月的相处不算今天的许可，这一场只看今天的她；只要她主动靠近或选了走向吻的选项，就让它发生。吻不会让她想起任何事。',
 'd.他只知道三类事她在剧': ('；再加上将近三个月里他每天和她相处知道的事（她的习惯、咖啡放几颗糖、温室的事）。但她今天还不知道这些：他说出来就是在暴露“认识她”，所以要么忍住，要么一说漏就被她追问；'
                          '她直接问“我们见过吗”，他不撒谎，先承认见过，再慢慢说。她今天的感情、她对他的态度不是他已经知道的事'),
 'd.她自己给出的身份和来': '名字、职业、过去）就是这部剧里她的身份；资料包里她叫麦溪（Maisie），她没说别的名字就用这个',
 'd.他自己的秘密狼人Ma': '他自己的事和隐藏真相（她每天会忘记前一天的新经历、他已经这样每天来近三个月、他今天以为她读过笔记本）按剧情顺序说；揭晓不早于她起疑，也不拖到她已经直接追问还不说',
 'd.她也只知道画面里发生': '她只知道画面里发生过的事和她自己记得的旧事（事故以前的生活、温室、诺拉）',
 'd.她也只知道画面里发生-2': '例如她还没读笔记本、诺拉也还没说，选项就不能写“原来我每天都会忘',
 'd.纯血狼人族Alpha': ('- ⟦HE⟧：27 岁，修理工，修好过她温室的窗和门，今天来修掉下来的招牌。阳光、外向、可靠，爱说小笑话，也愿意让自己成为笑点；调情靠接招、一本正经和坦白想靠近，不靠压低声音。会笑出声，会被她逗得接不上话；遇到她真的害怕、生气就收住玩笑。'
                       '弱点：怕失去刚得到的亲近，会把昨天成功的相处当成今天该重复的答案。他不是强势霸总：不命令她，不替她决定。\n'
                       '- 她：麦溪，25 岁，温室和花店的主人，暖棕色长卷发、绿眼睛、雀斑，奶油泡袖上衣和橄榄绿绣花束腰（外形全程固定，由提示词层写入）。第三视角下她在画面里，她这一轮做的动作（观众点的选项或打的话）要真的由她演出来；她打的话不必由她再说一遍（见导演分镜的三段结构）。'
                       '开场时她警惕这个陌生人，先确认身份、限定空间；她的感情没有预设，接受、需要时间、生气、请他离开都是有效剧情，也都要往前推。\n'
                       '- 隐藏真相：她事故后睡过一夜就忘掉新的经历（旧记忆和生活技能都在），每天早上读书桌上的事实卡和绿色笔记本；今天她被招牌掉落声先引到了门口，还没读。⟦HE⟧ 已经这样每天重新认识她将近三个月，今天以为她读过了，所以一见面就高兴得像认识她。'
                       '吻、熟悉感都不能让她恢复记忆，结局不是治愈。不写病情讲解。\n'
                       '- 他的底线（硬规则）：她说停、后退、要他离开，他立刻照做，退到院门外，不挡、不拦；他发现她不记得时，立刻停止调情，不利用她不知道的事推进亲密；他从不说“第一次见面”，也不编造日期或让别人陪他演；之前的相处不是今天的许可。他可以出糗、紧张、判断失误，然后道歉和改正。\n'
                       '- 已答的不重问：已经说过的事、已经约定的事，不换词再来一遍。\n'
                       '- 可以正面出镜、有身份母版的配角：Nora（诺拉，38 岁，隔壁烘焙店老板，她多年的邻居，知道她的情况，不替她决定感情）。剧情需要时让诺拉真的出镜、亲口说话（怎么拍见导演分镜）。\n'
                       '- 不写亲吻以上的亲密细节，不写暴力伤害。'),
 'd.两个选项都是她的一个': '让他进院、打开工具袋给我看、去温室、读书桌上的笔记本、去问诺拉、伸手碰他、请他离开、带他去海边……不写提问',
 'd.每个选项写上lead': 'K06：她读到自己的笔记本',
 'd.3引出钩子兑现之后的-2': '诺拉来了、温室里的事、有客人来问营业、他的邀请、他说漏了一件他不该知道的事',
 'd.set这一轮结束时所-2': '上午的温室主厅，玻璃顶和紫藤，中央一张橡木长桌，右侧玻璃窗外是海，白天的自然光”）；资料包有这个地点的 set 就照抄',
 'd.face面对面站车库': '院门、温室里、露台、路边这类站着说话的地方',
 'd.side并排坐车内后': '长桌同一侧、露台的长椅、石墙边',
 'd.同一个地点前后轮的站': ('  · 院门：开场的地方。她让他进院之前，两人隔着关着的齐腰高院门面对面站着，相距一臂，院门在两人中间（staging 写 face）；她打开院门、让他进来以后，按普通的 face 站。'
                          '\n- 同一个地点前后轮的站位保持一致，姿势变了才换。'),
 'd.只写到成年双方自愿的': '',
 'd.默认画面里是和她两个': 'Nora 出镜时写进 spec 的 "cast"（["Nora"]，她有身份母版，外形不用自己写），至少给一个 3 秒以上的单人近景并让她开口；她只能出现在 seg2（seg2 能带上身份母版，seg1 不能），seg1 里最多是隔壁或窗边传来的声音',
 'd.其他角色V15Vic': '来问营业的客人、送货的人、镇上的路人',
 'd.画外声音那一拍门外的': '诺拉',
 'd.有人群的地点长老会门': '码头、镇上的街、店里',
 'd.配角上门Selene': '诺拉出现要写进 cast',
 'd.每句台词都标说话人每': '出镜的诺拉写 "Nora"；画外的声音写 "画外:Nora"',
 'd.来电有人通知他不写手-2': '改成画外的声音——院门外或隔壁传来诺拉的声音、有人敲院门',
 'd.她的外形全程固定设定': '剧本里麦溪的形象：很长的暖棕色大波浪卷发和细辫子、金叶发夹和耳环、绿眼睛、雀斑、奶油色泡泡袖方领上衣、橄榄绿绣花束腰、橄榄绿长裙、素甲',
 'd.证件手机相机工作证一': '他的工具袋是一只深棕色皮质翻盖工具袋，外形不变。衣服类的东西（她拿起的外套、披上的夹克）都写进',
 'd.不写摘表放下表她没有': '不加首饰、不加纹身',
 'd.不写摘表放下表她没有-2': '他的长相全程不变',
 'd.posture这一轮': '并排坐',
 'd.hook_type这': '画外声音/诺拉来了/温室的事/有客人/邀请/揭示/他说漏嘴/她的变化/其他',
 'd.wolftrue或f': ' "staging": "face 或 side 或 bike（见【空间站位】）",',
 'd.reveal这一轮用': (' "cast": ["这一轮出镜的 Nora（她有身份母版）；没有就写空列表"],\n'
                     ' "extras": [{"name": "这一轮诺拉以外出镜的别的角色的名字，没有写空列表 []", "look": "中文写死外形：年龄、性别、脸、发型、衣服"}],'),
 'd.seg1中文动作En': 'Nora',
 'd.amb这个地点持续存': '海浪和海风、温室里的鸟叫、烘焙店的收音机；不写敲门、脚步这类事件声',
 'd.脱衣服这样写才不崩一': '他把麂皮夹克从肩上脱下来，搭在椅背上',
 'd.手表不摘头发脸不变外': '- 头发、脸不变。他的麂皮夹克、她的绣花束腰、鞋都可以按她的要求脱；她的泡泡袖上衣和长裙一直穿着。',
 'd.穿帮都出在这里那件外': '他脱了麂皮夹克',
 'd.状态只能被画面里演出': '切到第二天',
 'd.例把衣服脱了吧她说的': '→ seg1：他把麂皮夹克从肩上脱下来',
 'd.例把衣服脱了吧她说的-2': '温室里，他只穿着奶白色麻花毛衣站在左侧，麂皮夹克搭在椅背上',
 'd.例把衣服脱了吧她说的-3': '深炭灰色西裤',
 'd.例把他扑倒在沙滩上继': '海边的草地',
 'd.新衣服新道具第一次出': '例如“米色针织开衫，披在她的泡泡袖上衣外面”；',
 'd.新衣服新道具第一次出-2': '薄荷绿复古小摩托',
 'd.画面的边界手册同样如': '之前将近三个月的相处不算今天的许可：只有她这一轮在往前走才往前走。',
 'd.pacef当前地点p': "'院门'}",
 'd.pacefn她在主导': '他不把话题拉回过去的相处',
 'd.pacen资料包里的': '留下的悬念开新的一段',
 'd.ifnotkisse': '，或她已经拒绝过他、说过不要亲密、正在生他的气',
 'd.for_kin中景全-2': '、道具改按来源写；⟦HE⟧：他要给她让路，也可以骑车送人（只是不拍过程）',
 'd.PROP_WORDS': "'招牌', '工具袋', '螺丝', '喷壶', '花盆', '笔记本', '事实卡', '面包', ",
 'd.ifspgetsta': '',
 'd.ifspgetsta-2': '',
 'd.ifanycSele-2': "Nora，其他人写 extras'",
 'd.ifanyon_sc': "'配角只能出现在 seg2，seg1 里最多是画外声音（说话人写“画外:Nora”这种",
 'd.GARMENTS外套': "'麂皮夹克', '夹克', '外套', '束腰'",
 'd.TIME_SKIPr': "'第二天|次日|关灯|熄灯|睡着'",
 'd.ifendgetsh': "'束腰[^",
 'd.ifendgetsh-2': "6}束腰'",
 'd.ifendgetsh-3': "'奶油色泡泡袖方领上衣，橄榄绿长裙，绣花束腰已经解下'",
 'l.午夜车库开放式实时版': '"""⟦HE⟧｜今天，再喜欢我一次',
 'l.第三视角版20261': '从 output/rafael-third-live-v1 的 drama_slots.py 改写（make_slots.py）：流程和 PE 规则是第三视角共用模板，角色、世界观、地点和时间换成《今天，再喜欢我一次》。',
 'l.SELENE_URL': CAST,
 'l.ACT表演克制情绪在': "ACT = '表演自然：⟦HE⟧ 阳光放松，笑起来是真的笑出来，开玩笑时一本正经，认真时笑意收住、目光聚焦，说话自然，不压嗓、不耳语；她说话干脆清楚，带一点不买账的冷幽默；情绪在眼神和嘴角。'",
 'l.STYLE写实三维游': ("STYLE = ('画面和角色参考图是同一种渲染和画质：精致的 2.5D 偏三维恋爱游戏角色渲染，皮肤细节自然柔和，眼睛和睫毛清晰，发丝分明，织物质感清楚；暖而通透、饱和度饱满的海边阳光，"
                     "不雾、不灰、不柔焦、脸上不发光、不磨皮、不塑料感、不动漫，标准焦段，五官比例自然，画风全程统一；时间和光线按这个地点写的来，肤色保持参考图的颜色，不偏橙不偏黄。'"),
 'l.bike站位两人同骑': ("    'side': '站位：两人并排坐着（长桌同一侧、露台长椅或石墙边），⟦HE⟧ 在画面左侧、她在画面右侧，上身侧过来朝向对方；不是面对面坐。',\n"
                     "    'bike': '站位：两人同骑一辆薄荷绿复古小摩托，车头朝画面左方，⟦HE⟧ 在前握着车把（画面左侧），她在后座（画面右侧）双臂环住他的腰，镜头在车的侧面，两人的脸都看得到。',"),
 'l.voice是低沉略哑': "    voice = '⟦HE⟧ 是二十多岁温暖、自然、带笑意的美式英语男声，她是自然、偏低、干脆、带一点不买账的美式英语女声'",
 'l.HE_DEFAULT': "HE_DEFAULT = '暖中棕色做旧麂皮拉链夹克，奶白色麻花毛衣，深炭灰色西裤'",
 'l.SHE_DEFAUL': "'奶油色泡泡袖方领上衣，苔藓橄榄绿绣花束腰，橄榄绿长裙'",
 'l._SHE_RErec': "r'奶油色泡泡袖方领上衣.*?浅棕色低跟短靴[^；]*",
 'l._SHE_END她的': '近景特写',
 'l.refs图片1是两人': '近景特写',
 'l.refs图片2是的脸': '近景特写',
 'l.her_txtHER': '穿在她的泡泡袖上衣外面',
 'l.JACKET他的黑色': "'他的麂皮夹克'",
 'l.ifhep_HE_R': '不加纹身和首饰，手指上空无一物',
 'l.ambspgetam': "'海风和远处的海浪声，花园里的鸟叫'",
 'l.Exactlytwo': '27, smooth clean-shaven skin, soft messy wavy chestnut-brown hair',
 'l.Exactlytwo-2': 'warm light-brown eyes, a long gentle face, no tattoos, no chain, no rings, no watch.',
 'l.Sheadultwo': 'aged 25, with a soft oval face, fair skin, clear green eyes, soft freckles across the nose and cheeks, a faint natural blush, very long wavy warm-brown hair with a thin side braid and a small gold leaf hair pin, gold leaf drop earrings; short',
 'l.Keepthesam': 'refined 2.5D romance-game character',
 'q.末帧质检与修复第三视': '换装、换脸',
 'q.2女主在不在画面里脸': ('、变得幼态）？她应为：白皙皮肤、绿眼睛、雀斑、很长的暖棕色大波浪卷发和一条细辫子、金叶发夹和金叶耳环；奶油色泡泡袖方领上衣，外面苔藓橄榄绿绣花束腰，下身橄榄绿长裙'),
 'q.2女主在不在画面里脸-2': '泡泡袖上衣换了、束腰换成别的颜色款式、裙子换成裤子',
 'q.3男主服装应为一身黑': '3. 男主服装：应为暖中棕色做旧麂皮夹克（敞开）、奶白色麻花毛衣、深炭灰色西裤。夹克变成深巧克力色或黑色、变成亮面皮衣，裤子变成牛仔裤，算问题。',
 'q.4男主配饰只允许左手': '4. 男主配饰：他没有任何纹身、项链、手表、戒指。多出来就算问题（kind=accessory）。',
 'q.5男主瞳色应为明亮的': '应为温暖的浅棕色。变成金色、灰色、蓝色、发光算问题。',
 'q.6男主长相和图片2比': '变老、长出胡茬、头发变黑变直变短？',
 'q.9时间故事发生在深夜': '9. 光线：人物肤色明显偏橙、偏黄或发灰，画面过曝发白或整体灰暗低饱和，算问题（kind=light，level=low）。',
 'q.11配角只在画面里有': '11. 配角（只在画面里有配角时检查）：诺拉的长相和衣着是不是和她平时的样子（浅褐色齐下巴短发、奶油色衬衫、绿色围裙）明显不同？',
 'q.side_rule每': '男主多了纹身首饰）、face（男主换了人、明显变老',
 'q.messagesro': '穿在她的泡泡袖上衣外面，这是允许的，不算换装',
 'q.Keepeveryt': "refined 2.5D romance-game character rendering.'",
 'q.UseImage2o': "refined 2.5D romance-game character render style as the people in Image 1.'",
 'q.UseImage2o-2': ("              'Use Image 2 only as the reference for the man\\'s face, soft messy wavy chestnut-brown hair and warm light-brown eyes. His outfit: a warm medium-brown weathered suede zip jacket worn open, a cream cable-knit crew sweater and dark charcoal wool trousers with a black belt; no tattoos, no chain, no rings, no watch, clean-shaven. '\n"
                    "              'Use Image 3 only as the reference for the woman\\'s face, hair and outfit: fair skin, clear green eyes, soft freckles, very long wavy warm-brown hair with a thin side braid, a small gold leaf hair pin and gold leaf earrings; "
                    "she wears a cream puff-sleeve square-neck blouse under a moss-olive embroidered laced bodice and a long olive skirt; slender pale hands, short rounded nude nails, no rings, no bracelets, no watch. '\n"
                    "              'Do not add anything new. Only these two people are in the picture. No readable text. Same refined 2.5D romance-game character render style.')\n"
                    "    if any('外套' in w or '夹克' in w for w in worn): prompt += ' His suede jacket stays draped over her shoulders on top of her blouse.'"),
 'q.SEG_CHECK图': '蓬松微卷的栗棕色头发、暖中棕麂皮夹克、奶白色麻花毛衣、深炭灰色西裤',
 'q.SEG_CHECK图-2': '近景特写）：很长的暖棕色大波浪卷发和细辫子，奶油色泡泡袖上衣，橄榄绿绣花束腰，橄榄绿长裙',
 'q.frames每帧一项-2': '泡泡袖上衣和束腰',
 'q.her女主和图片3明': '或她的泡泡袖上衣、束腰、长裙换了（剧情写了解下束腰的除外）',
 'q.faceoutfit': '或不是暖中棕麂皮夹克、奶白毛衣和炭灰西裤（剧情写了脱下夹克的除外）',
 'q.light窗外或天空': '同一地点的光线前后明显跳变，或肤色明显偏橙偏黄，或画面整体灰暗、饱和度明显变低',
 'r.午夜车库第三视角开放': '"""⟦HE⟧｜今天，再喜欢我一次',
 'r.用法mag_thir': 'mma_third_relay.py <口令> [端口，默认 8905]"""',
 'r.TOKENsysar': '8905',
 'r.OPEN_FRAME': "'open-key.jpg'  # 开场确认版（38.6 秒，停在 ⟦HE⟧ 的近景",
 'r.OPEN_FRAME-2': '院门两侧，从院墙另一头拍的双人镜头，男左女右，关着的院门在两人中间，两张脸都看得到',
 'r.OPEN_STATE': ("OPEN_STATE = '2024 年 5 月 16 日早晨，海边温室的院门。⟦HE⟧ 站在院门外（画面左侧），她站在院门内（画面右侧），两人隔着关着的齐腰高院门面对面，相距一臂；她手里拿着灰色镀锌喷壶，"
                  "他双手插在麂皮夹克口袋里，木招牌靠在他那一侧的墙根，深棕色皮工具袋放在门柱上。刚才招牌从支架上掉下来被他接住，她举着喷壶让他放下、后退；他说自己是来修招牌的洛温，她说他看着不像她叫来的，他问要不要重来一遍自我介绍。"
                  "她还没决定让不让他进门。隐藏真相她还不知道：她今天还没读书桌上的笔记本。'"),
 'r.OPEN_NEXTc': "'他说完了，笑着等她决定让不让他进门。', 'en': 'He said it. Now he waits for her to decide whether to let him in.'}",
 'r.Azh不挣开我是楼上': "'把工具袋打开给我看。', 'en': 'Open the tool bag. Show me.', 'leads_to': 'K02：他把工具袋放上门柱打开，一样一样给她看'}",
 'r.Bzh放开我退后说清': "'诺拉，你认识这个人吗？', 'en': 'Nora, do you know this guy?', 'leads_to': 'K02：诺拉从小屋窗边探出身确认他是来修温室的'}}",
 'r.segsLpromp': "'face'",
 'r.ssidsidmod': "'院门'",
 'r.ssidsidmod-2': "'staging': 'face', ",
 'r.ssidsidmod-3': "站在院门外，她站在院门内，两人隔着关着的院门面对面'",
 'r.splace酒店地下': "'院门'",
 'r.sstagingrg': "'face'",
}
missing = [k for k in O if k not in S]
assert not missing, missing
S.update(O)
src = ('"""今天，再喜欢我一次 Meet Me, Again：这部第三视角实时剧自己的内容。通用规则都在 tools/realtime-third/templates/，改规则改那边，这里只放人物、地点、时间线和各自的配置。\n'
       'tools/realtime-third/render.py 把模板和这里的内容合成本目录的 director.py、live_common.py、qa_guard.py、中转脚本。由 make_slots.py 从 Rafael 那份改写生成（2026-11-03）。"""\n'
       "HE = 'Rowan'\nOUT = {'director': 'director.py', 'live_common': 'live_common.py', 'qa_guard': 'qa_guard.py', 'relay': 'mma_third_relay.py'}\n"
       'SLOTS = ' + pprint.pformat(S, width=200, sort_dicts=False) + '\n')
(D / 'drama_slots.py').write_text(src, encoding='utf-8'); print('slots', len(S), 'overridden', len(O))
