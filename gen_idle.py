"""选择点背后的待机循环：首尾帧都锁 masters/idle-key.jpg（开场确认版的最后一帧，Rowan 近景，问完“要不要重来”在等她回答），5 秒，静音循环播放。"""
import live_common as L
from pathlib import Path
D = Path(__file__).resolve().parent
P = ('固定机位，一镜到底：镜头像架在三脚架上，全程不移动、不切镜。首帧和尾帧是同一张画面，构图、姿势、表情全程和首帧一样，只有很细小的动作：呼吸、自然眨眼、发丝在海风里微动、嘴角带着期待的小笑。'
     'Rowan 一个人在画面里，近景，眼睛看着镜头左侧旁边的她（几乎贴着镜头），闭着嘴不说话，安静地等她回答；画面左边缘是她虚焦的一缕头发，不转身、不露脸。' + L.STYLE + '约束：无字幕，无文字，无旁白，画面里只有 Rowan 一个人正面出镜，没有背景音乐。')
c = L.W1Client(); U = c.upload(str(D / 'masters/idle-key.jpg'))['url']; print('key', U); out = D / 'docs/media/IDLE0.mp4'
r = c.run(prompt=P, duration=5, aspect_ratio='9:16', first_frame_image=U, last_frame_image=U, out=str(out))
print('ok', r['job_id'], r.get('generate_seconds'))
