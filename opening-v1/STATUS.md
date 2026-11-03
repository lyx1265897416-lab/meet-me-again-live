# 今天，再喜欢我一次 · 第三人称开场 V1（2026-11-02）· 待 Vicky 确认，未进文档，实时版未搭

交付：delivery/MMA3P_OPENING_V1.mp4（47.9 秒 · 720×1280 · 24fps · -17.8 LUFS）+ .zh-en.vtt + cues.json；字幕不烧进画面。
分轨：edit/dialogue.wav、ambience.wav、sfx.wav、bgm.wav。脚本：shots.py（分镜/提示词）、gen.py（plates/frames/takes/lip）、dub.py、edit.py。

- 女主：storyboard-v1/references/maisie.png（绿眼、雀斑、暖棕长发、金叶发夹耳环、奶油泡袖、橄榄绿绣花束腰）。男主：rowan.png + CANON-rowan-ep1.png（暖中棕麂皮夹克、奶白麻花毛衣、炭灰西裤黑皮带）。
- 台词：原第 1 集 01-02/03/04 的 D1/B 配音，七句未改。配乐：本剧 daylight.mp3。音效和环境声新生成。
- 方法：Seedance 2.5 只演不说（720p），sync/lipsync-3 按配音对口型，图用 gpt-image-2/edit，场地先出三张空镜母版（P_TWO/P_HER/P_HIM）。
- 空间：院内=她，院外=他，隔着关着的院门。喷壶只在她手里；招牌 S02 掉下→S04 他接住→S08 放到门后他那一侧；工具袋在门柱上。

补拍和原因：
- S01 地上多喷壶；S02 只留前段（后段招牌像飘在空中）；S05 景别远、色调灰；S06 招牌偏大（改用 S04 首帧作比例参考）；S08 招牌放到门顶、后面又没了（改用 S10 首帧作尾帧）。
- 首帧：双人镜站到院门同一侧（改成墙沿画面中线的机位）；单人镜点名对方会多出人（单人镜不再点名）。
- 双人镜对口型会选更正脸的人（把女主嘴做开了），裁切后又因纯侧脸变形，所以 M4 改到男主正面近景 S13，S12 双人不说话收尾。
- 教训：concat 分离器和 -ss/-t 会丢帧造成音画错位，改精确帧数 + concat 滤镜；重做片段要连 lip 缓存一起清。

待确认后：替换进文档（飞书「角色样例」目前没有本剧内容包，要问放哪）；按 tools/realtime-third 接入 drama_slots.py、资料包、母版（face_head、her_head），末帧 S12 作第 1 轮关键帧，给中英测试链接。

## V2（2026-11-02，Vicky：物品掉落后女主立马惊讶，下一秒切男主接住，节奏要快；音色重新设计一批供选择）
- 交付 delivery/MMA3P_OPENING_V2.mp4（44.8 秒）。开头：S01 空镜 1.6 秒 → S02 招牌掉落 0.9 秒 → S03b 她惊讶 1 秒（新拍）→ S04c 他接住（新拍，尾帧钉 S04 首帧，接住后部分 2.6 倍速）→ S04 抬头认出她（前段 3 倍速）。S03 退役，水声和旧招牌音效换成 sfx_snap、sfx_catch。
- 声音暂时仍是旧 D1/B。候选音色在 ../voices-v1/（minimax/voice-design，M1–M6、F1–F6，voice_id 在 manifest.json，提示词在 generate.py）；试听页 https://claude.ai/artifact/3uR1L48QMRDwmMjzxrJWi3 。
- Vicky 选定后：用选中的 voice_id 重新配七句（audio/F*.wav、M*.wav），按新时长调 shots.py 的开口时间和窗口，跑 dub.py、清 takes/*_ls.mp4 和 jobs/lip-*.json、gen.py lip、edit.py，出 V3。

## 音色第二轮（2026-11-02）
女主定 F5。男主往 M5 方向，新候选 M7–M12（../voices-v1/generate2.py）。等 Vicky 定男主后按上面的步骤出 V3。

## 音色第三轮（2026-11-02，Vicky：前两批都不好，太人机，要真实自然）
前两批都是 minimax/voice-design。第三批换路子比较，在 ../voices-v2/（generate.py）：Seedance 原生演出 R1 R2 W1 W2（视频在 video/）、Seed Audio R3 R4 W3、Eleven v4 预置 R5–R7 W5–W7、Gemini 3.8 导演式 R8 R9 W8 W9、Gemini 双人对戏 D1。VibeVoice（D2 D3）念错词且码率低，W4 过平过慢，都淘汰。客观指标（音高起伏、节奏）分不出人机感：被否的 M5 起伏也不低，所以只能靠 Vicky 听。选 Seedance 原生路子的话，开场对白镜头要重拍成原生演出，不再静默 + lipsync（见 vicky-drama natural-performance）。

## V3（2026-11-02，Vicky 选音色 R1 和 W2，都是 Seedance 原生）
- 7 个对白镜头（S05 S06 S07 S08 S10 S11 S13）全部重拍成原生演出（takes/*_n.mp4，gen.py native），不再静默 + lipsync。窗口在 shots.py NWIN，词时间在 qa/native_words.json。其余镜头沿用 V2。
- 两版同一画面，43.5 秒，-16 LUFS 左右，等 Vicky 听后定：delivery/MMA3P_OPENING_V3A.mp4 每镜原声（audio/raw-*）；V3B 变声到 R1/W2（chatterbox，audio/vc-*，voice_post.py）。V3B 包络相关度 S05 0.71、S07 0.76，低于规范 0.8；其余 ≥0.87。原声中位音高男 97–117 Hz（R1 110）、女 184–191 Hz（W2 198）。
- 没做 lipsync 精修，口型是模型原生。没有人耳听审。
- 实时版用 Vivix，声音和 Seedance 不是同一个；搭实时版时要解决声线衔接。

## V4（2026-11-02，Vicky：开头动态衔接不自然；最后不要定格在两人画面，停在男主镜头）
- 交付 delivery/MMA3P_OPENING_V4A.mp4（每镜原声）、V4B（变声），41.9 秒。A/B 她还没选。
- 开头：S01 空镜 → S02b 招牌特写（只有天空紫藤，不露院门，新拍）→ S03b 她惊呆 → S04a 他接住（S04n 前 1.3 秒，新拍）→ S03c 她的反应（S03b 1.3–2.0）→ S04b 他抬头认出她（S04n 3.75–6.4）→ S05。去掉全部加速和拼接；靠切回她跳过他盯招牌的 2 秒。
- S04n 第一版废弃（qa/rejected-takes/S04n-gatesplit.mp4）：招牌穿过脸融进手里，院门裂开露腿。教训：动作镜把院门移出画面，下落物写明从身前落下。
- 结尾：S12 双人只留 1.6 秒放在 M4 前，S13 男主说完后停 1.8 秒收尾。第 1 轮实时关键帧要用 S13 末帧，不是 S12。

## V5（2026-11-02，Vicky：女主惊讶要有声音，表情/动态都要有对应音效）
- delivery/MMA3P_OPENING_V5A.mp4、V5B，41.9 秒，画面同 V4（S01 短 0.25 秒，S02b 早 0.25 秒起，保留脱钩声）。A/B 她还没选。
- 根因：V1–V4 没台词的镜头只取画面，丢了 Seedance 原生声（她的惊呼、接住撞击、招牌落下）。现在每镜都留原生音（edit.py dlg）。
- 新增 14 条音效 sound/fx（gen_fx.py），放点在 edit.py BEATS、EFFORT：招牌吱呀、水声、喷壶、衣料、招牌靠墙、脚步、插兜、他呼气/吸气/轻笑、她憋笑/hm。
- 修了一个老 bug：bed() 的 amix normalize 让增益随片段结束而升高，V1–V4 后半段越来越响；改 normalize=0。配乐从 -14 降到 -20 dB。
- 没有人耳听审；几条气声是模型生成，不是 W2/R1 本人声线。

## V6（2026-11-02，Vicky 四条：①她松口气要往下看他的手 ②放招牌太僵太慢 ③她不要带笑的配音 ④两人就隔着门，单人镜显得站很远，改正反打）
- delivery/MMA3P_OPENING_V6A.mp4（原声）、V6B（变声），41.1 秒。A/B 她还没选。
- 对话段全部改过肩正反打（S05o–S13o，shots.py V6 块 OTS_HER/OTS_HIM）：拍她时前景是他的后脑和肩，拍他时前景是她的后脑和肩。双人远景 S12 删掉，结尾停在 S13o 他说完的过肩镜。
- S03d 新拍：招牌落到他手里，她眼睛往下看，一声松气（取 1.65–3.25 秒，前段招牌又掉一次不能用）。招牌在这镜是搭在门顶、他一只手扶着，和 S04a/S04b 他胸前双手拿着略有出入。
- S08o 第一版有隐藏切镜（钉了构图不同的 S10o 尾帧）→ 去掉尾帧重拍，1 秒内放下招牌。
- 去掉 f_exhale、f_hm。V6B 变声在最后一句前多出一声 "Pfft"（转写听到），A 版没有。
- 第 1 轮实时关键帧改用 S13o 末帧（过肩镜，两人都在）。

## V7（2026-11-02，Vicky：男主眼神要看向女主）
- delivery/MMA3P_OPENING_V7A.mp4、V7B，42.0 秒。A/B 她还没选。
- V6 他的过肩镜里眼睛常往下垂、笑时眯成缝或闭眼、往别处飘。S06/S08/S10/S13 重做：首帧在 V6 首帧上只改眼神和头的朝向（eyefix.py，EYE_EDIT），视频提示词加 EYE（全程看她、笑也睁眼，只在看招牌和弯腰放招牌时可离开）。新镜头 S06e/S08e/S10e/S13e。她比他矮，脸在他肩膀高度，所以视线略向左下是对的。
- 接住后抬头那镜 S04n 眼神本来朝她，没动。V7B 不再有 "Pfft"。

## V8（2026-11-02，Vicky：松口气那镜站位不对，改女主特写；整体色调统一成 S08e 那样，不要低饱和或偏色）
- delivery/MMA3P_OPENING_V8A.mp4、V8B，42.5 秒。A/B 她还没选。
- S03d 换成 S03f：她单人特写，轻呼一口气、眼睛往右下看（frame_s03f.py 用 S08e 当色调参考出首帧），原生气声音量 ×2.5。
- 调色 grade.py：以 S08e 为准，逐镜调感知饱和度（HSV，0.97–1.3）、白平衡（a/b 平移 ≤1.5）、亮度按脸部高光对齐（gamma 0.9–1.1）；过肩镜统计去掉前景人物；S02b 天空特写不动。参数在 qa/grade.json，edit.py 每段生成后自动套用。第一版按整幅画面统计被深色夹克带偏（反而降饱和压暗），已弃用。
- 各镜感知饱和度离散度 6.3 → 4.2，最低 64 → 67。

## V9（2026-11-03，Vicky：他的眼神还是没看着她，可以改男主正面特写，要有真实对话感；她的过肩镜色调不对、形象没保持）
- delivery/MMA3P_OPENING_V9A.mp4、V9B，40.0 秒。A/B 她还没选。
- 对话 8 镜全部改成近景单人（S05c–S13c，shots.py V9 块 CU_HIM/CU_HER）：脸居中近乎正对镜头，视线紧贴镜头一侧（他看镜头左、她看镜头右），画边留对方一缕虚焦的头发或肩膀。过肩镜的问题根源是他会看前景人物的后脑，视线自然偏离。
- 首帧 frames_v9.py：她用 REF_HER（S03f 认可的特写）+ maisie.png，色调参考 REF_COLOR（S08e 4.5 秒）。
- S08c、S11c 第一版中途拉远/跳景别 → 钉同景别尾帧重拍（S10c、S09c）。S08c 重拍后 5.42 秒仍有一帧推近：画面 5.38 切到她（S09c），他的台词在她脸上说完（atail 1.3）。
- S05c、S07c 转写把开口误判在 0 秒，按能量改成 1.4、1.3 秒（native_words.json onset_fixed_by_energy）。
- grade.py 参考仍是 S08e（V7 定义），新近景偏暖偏饱和，被小幅收回。

## V10（2026-11-03，Vicky：女主叹气太人机太慢太机械，男主反应也是；要自然真实、节奏快）
- delivery/MMA3P_OPENING_V10A.mp4、V10B，38.5 秒。A/B 她还没选。
- react.py 各拍两条（提示词写真人即时反应、不慢动作、不慢慢闭眼）：她用 S03g2 0.1–1.45（半秒内呼气、抬眼回戒备），他用 S04r2 1.75–3.6（抬眼即认出、亮起再收成半笑）。S03g1 仍慢慢闭眼、S04r1 抬眼太晚，弃用。
- 接住→她松气→他认出 从约 6 秒压到 4.5 秒。去掉生成的吸气音效，用原生呼吸。

## V11（2026-11-03，Vicky：他拿招牌说话那镜不要看到她抬着的手）
- delivery/MMA3P_OPENING_V11A.mp4、V11B，38.6 秒。A/B 她还没选。
- S06c 的手和喷壶是视频里从底部伸进来的（首帧没有）。retake06.py 用同一首帧加 NOHANDS 拍两条，选 S06d1（已复制为 takes/S06c_n.mp4，原片在 qa/rejected-takes/S06c_n-herhands.mp4）。其他男主镜头查过无此问题。

## V12（2026-11-03，Vicky：S08c 那段音效嘈杂，噪声/摩擦音效删除或优化）
- delivery/MMA3P_OPENING_V12A.mp4、V12B，38.6 秒，画面同 V11。A/B 她还没选。
- 对白镜头开口前 0.12 秒之前的原声静音（gate，去掉放招牌的刮擦声等），全部原生音轨加 afftdn=nf=-30 轻度降噪（4 kHz 以上占比约减半）。
- 对白镜头里后加的衣料摩擦声全部删除；S08c 只留一声 -50% 的木牌落地；开头动作戏（S03b、S04a）的拟音保留。
- 教训：改 edit.py 的批量替换要先 assert 每段原文都在；失败那次 V11 被重跑却没做响度统一，已补做。

## 确认版（2026-11-03）
Vicky 选 V12A（每镜原声），存为 delivery/MMA3P_OPENING_确认版.mp4。末帧是 S13c 他的近景。
