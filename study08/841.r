# 패키지 설치 및 로드
install.packages("randomForest")
library(randomForest)

# 데이터 생성
set.seed(123)
data <- data.frame(
  x1 = rnorm(100),
  x2 = rnorm(100),
  y = factor(sample(c("Yes", "No"), 100, replace = TRUE))
)

# 랜덤 포레스트 모델 생성
model <- randomForest(y ~ x1 + x2, data = data)

# 모델 요약
print(model)

# 예측
predictions <- predict(model, newdata = data)
