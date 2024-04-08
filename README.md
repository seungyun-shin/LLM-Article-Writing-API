# LLM article authoring API : 기사작성 LLM모델 API
- Langchain, Fast API 활용하여 만들어진 기사 작성 API 서비스 입니다. 

## 💡 ENDPOINT
- 요청 POST : `/generate-text`
POST BODY 형식 예시
```bash
{
  "article_format" : "피라미드형",
  "category" : "생활/문화",
  "body_text" : "이번 전시 관람은 무료이나, 사전 예약을 통해 한정된 인원만 입장 가능하다는 점이 특징이다.헤리티지 존에서는 MINI 브랜드의 전통을 느낄 수 있으며, 현행 MINI의 다양한 라인업도 전시될 예정이다.비욘드 존에서는 새롭게 탄생한 MINI의 순수전기 모델들이 전시되며, 이 모델들은 특히 삼성 디스플레이와의 협업을 통해 개발된 최첨단 기술을 선보일 예정이다.",
  "highlight_text" : "'MINI 코리아는 29일부터 다음 달 21일까지 서울 강남구 신사동 K 현대미술관에서 'MINI 헤리티지 & 비욘드' 전시회를 진행한다.이번 전시에서는 MINI의 과거, 현재, 미래를 보여주는 세 개의 전시 구역으로 구성되어 있으며, MINI의 역사와 디자인 변화를 한눈에 살펴볼 수 있다.전시회에서는 오는 6월 이후 국내 출시 예정인 뉴 올-일렉트릭 MINI 쿠퍼와 뉴 올-일렉트릭 MINI 컨트리맨이 첫 공개된다. 이들 최신 순수전기 모델은 삼성 디스플레이와 협업해 전 세계 최초로 선보이는 자동차용 원형 OLED 디스플레이와 MINI OS 9를 탑재했다."
}
```

## 💡 DOCKER
- Dockerfile dir : `./Dockerfile`
```bash
$ docker build -t article_generate .
$ docker run -d -v "$(pwd)":/workspace --name article_generate_container -p 8000:8000 article_generate
```

