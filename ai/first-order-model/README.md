# First Order Model

[First-order-model](https://github.com/AliaksandrSiarohin/first-order-model)

위의 코드를 가져왔다.



가장 먼저 requirments 설치 후

```
pip install -r requirments.txt
```



[파이토치 홈페이지](https://pytorch.org/)를 가서

![image](https://user-images.githubusercontent.com/34182908/86527336-f7555700-bed8-11ea-8577-6a467b08422d.png)

파이토치를 각 자의 컴퓨터 환경에 맞게 설치한다.



그 후

[First order google drive](https://drive.google.com/drive/folders/1kZ1gCnpfU0BnpdU47pLM_TQ6RypDDqgw)에 가서 .tar(모델파일)를 설치



```
python demo.py  --config config파일경로 --driving_video 동영상 --source_image 변환할 사진 --checkpoint .tar파일 --relative --adapt_scale
```

을 입력하면 result.mp4 파일로 파일이 생성된다.



예시

```
python demo.py  --config config/vox-256.yaml --driving_video 04.mp4 --source_image YEE.jpg --checkpoint vox-cpk.pth.tar --relative --adapt_scale
```

