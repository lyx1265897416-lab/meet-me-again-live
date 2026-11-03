import cv2,numpy as np,sys
for k in sys.argv[2:]:
    c=cv2.VideoCapture(f'{sys.argv[1]}/{k}.mp4');n=int(c.get(7));fps=c.get(5);r=[]
    for t in np.linspace(0,n-2,8).astype(int):
        c.set(1,int(t));ok,f=c.read()
        t2=cv2.resize(f,(180,320)) if ok else np.zeros((320,180,3),np.uint8);cv2.putText(t2,'%s %.1f'%(k,t/fps),(4,16),0,.45,(0,255,255),1);r.append(t2)
    cv2.imwrite(f'qa/sheet-{k}.jpg',np.hstack(r))
ims=[cv2.imread(f'qa/sheet-{k}.jpg') for k in sys.argv[2:]]
cv2.imwrite('qa/sheet.jpg',np.vstack(ims))
