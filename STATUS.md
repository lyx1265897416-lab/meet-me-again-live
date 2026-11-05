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

## 网页播放卡（2026-11-05，同三真四假的修法）
- 结论：Pages 实测开场 38.7 秒（播放器 1.1 倍速）用 35.2 秒播完，0 次停顿；实时一轮 15+15（L0225070fd）两段 15.04+15.04 秒无停顿、两段之间无缝（第 2 段在第 1 段播到一半时已缓冲完），中转记 stall 0，发送到开播 80.6 秒。
- 改动（照搬三真四假）：docs/index.html 加 enough/bufEta/warm/pick/srcOf——开场缓冲够前面 8 秒才播；实时段一到就静音、0.0625 倍速在后台“播”（warm），浏览器才会一直下到结尾，开播时退回 0 秒、用回播放器倍速；每段真的缓冲到结尾才开播（不信 readyState 4）；开播时机算上浏览器下载第 2 段的时间。bufEta 比三真四假多一步：速度取“从开始加载算的平均速度（含首包等待）”和“最近测得的速度”里较慢的那个（Meet-me 实测 Vivix CDN 先快后慢，只看后者会提前开播，两段之间停 11.5 秒）。rt-player.js 不改 warm 视频的速度（共用源 tools/realtime-player/rt-player.js 已同步，备份 rt-player.before-warm.js）。改前备份在 backup-antistall/。
- 开场片原 5.0 Mbps → 压到 1.31 Mbps（6.4 MB，抽帧对比看不出差），GCS 新地址写进 CDN 和 cdn.json（build_site.py 的 _sig 已同步，重跑不会重传），docs/media/OPEN.mp4 换成同一份，原片 backup-antistall/OPEN.orig.mp4。
- 过程中的失败：第一次实时轮 L0220229da 第 1 段播完后停了 11.5 秒才接第 2 段（Vivix CDN 15 秒片要下 37–42 秒，两段同时下互相抢，旧 bufEta 估得太乐观）→ 改了 bufEta 后重测通过。GCS 新开场片第一次被读时开头停了两下共 0.8 秒，之后再测 0 停顿。
