<h1 align="center">Rowan｜今天，再喜欢我一次</h1>
<p align="center"><b>Meet Me, Again</b> · 女性向第三视角开放式实时互动剧</p>
<p align="center"><a href="https://lyx1265897416-lab.github.io/meet-me-again-live/">▶ 打开体验页</a></p>

只有开场是预制的（38.6 秒）。之后每一段视频，都根据观众点的选项或自己打的一句话实时生成，故事一直往下演。

> 不带口令打开时只能看开场。实时生成要用带口令的测试链接，并且要这台 Mac 开着：中转和模型 key 都在本机，不在仓库里。

## 故事

海边温室的女主人麦溪，警惕地拦下一个来修招牌的陌生男人洛温；他看见她时，像早就认识她。真相是她事故后留不住新的记忆，而他已经这样每天重新认识她将近三个月。

## 组成

- 开场：`opening-v1/`（脚本），确认版是 V12A，`docs/media/OPEN.mp4`。
- 资料包：`pack/build_pack.py` → `pack/meet_pack.json`（人物、隐藏真相、地点、K01–K13、规则）。
- 这部剧的内容：`drama_slots.py`。`director.py`、`live_common.py`、`qa_guard.py`、`mma_third_relay.py` 由 `tools/realtime-third/render.py` 从第三视角共用模板合成，不要手改。
- 母版：`masters_build.py`（gen / upload），地址在 `masters/urls.json`。
- 播放页：`docs/index.html`（`build_site.py` 传 CDN、写开场字幕），待机循环 `gen_idle2.py`。
