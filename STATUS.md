# 今天，再喜欢我一次 · 第三视角实时版（2026-11-03）

开场 = 确认版 V12A（opening-v1/delivery/MMA3P_OPENING_确认版.mp4，38.6 秒），播完停在 Rowan 近景待机（docs/media/IDLE0.mp4，Seedance 首帧 + 正放倒放循环；Vivix 首尾锁同一帧会换衣服，见 qa/IDLE0-vivix-morph.mp4）。之后全部实时：auto 优先 5+15，轻量 5+10，Vivix ultrafast。

- 规则：第三视角共用模板 tools/realtime-third/templates；本剧内容 drama_slots.py（由 make_slots.py 从 Rafael 那份改写，之后直接改 drama_slots.py）。2026-11-03 模板加了三个槽位 l.BROWS、q.HER_HAIR_BAD、q.HER_HAIR_BAD2（原来写死的黑眉、发色判定），Magnus 和 Rafael 填原文，render --check 两部都无差异。
- 资料包 pack/build_pack.py → meet_pack.json：隐藏真相（她每天忘记新经历，他已每天来近三个月），K01–K13，揭晓不早于第 5 轮、她直接问他不撒谎。
- 母版 masters_build.py gen|upload：他用 rowan.png、头像裁图、白底半身服装图；她用 maisie.png + 白底全身 + 认可的特写合成三联；诺拉 nora-style-v2；站位图、第 1 轮关键帧 open-key（从院墙另一头拍，男左女右，院门在中间）、薄荷绿复古小摩托。地址在 masters/urls.json（不进仓库）。
- 开场里她在画面左、他在右；共用模板写死男左女右。衔接：开场停在他的单人近景，第 1 轮从院墙另一头的双人镜头重新交代空间。
- 中转 mma_third_relay.py 8905，launchd：com.vicky.realtime.meet-third、meet-third-tunnel、meet-third-sync（隧道地址变了自动写 docs/relay.json 并推送）。口令 token.txt 不进仓库。
- 公开仓库 lyx1265897416-lab/meet-me-again-live，Pages 从 docs/：https://lyx1265897416-lab.github.io/meet-me-again-live/ ，带 ?k=口令&lang=zh|en 才能实时生成。
- 播放页素材 build_site.py 传 GCS（cdn.json）并写开场字幕；等待配乐用本剧 daylight。
- 飞书「角色样例」7️⃣ Rowan 内容包（h2 doxcniDJRzJRzej8aycSN8rxbdg），脚本 feishu/。

## 测试（2026-11-03，模拟，Vicky 还没人工测）
- 导演层干跑 tests/dry_open.py：A 查工具袋、B 问诺拉、自由输入“你认不认识我”（他承认见过、不多说）都对。
- 本机冒烟 S0203094e4 3 轮（tests/smoke.py），每轮 60–66 秒：第 1 轮隔着院门的空间没守住（院门消失，像站在同一侧）；第 3 轮换场温室，第 2 段开头和结尾出现黑色铁艺大门、结尾回到门外。人物外形和服装稳定。
- Pages 线上 1 轮（选项 B）：点到开播 57 秒，5+15，诺拉出镜和母版一致。
- 待做：Vicky 人工测后复盘；院门两侧站位、换场空镜的门；Vivix 声线和开场 R1/W2 不同；测试记录页、即兴剧场 APP 还没加。
