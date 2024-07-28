import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.neighbors import LocalOutlierFactor

# 1. 데이터 준비
X, _ = make_blobs(n_samples=300, centers=1, cluster_std=0.60, random_state=0)
rng = np.random.RandomState(42)
X_outliers = rng.uniform(low=-6, high=6, size=(20, 2))

# 정상 데이터와 이상치를 합칩니다.
X_full = np.vstack([X, X_outliers])

# 2. LOF 적용
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
y_pred = lof.fit_predict(X_full)

# 3. 결과 시각화
plt.figure(figsize=(10, 7))

# 정상 데이터와 이상치 시각화
plt.scatter(X_full[:, 0], X_full[:, 1], c=y_pred, cmap='coolwarm', marker='o')
plt.title('Local Outlier Factor (LOF) Anomaly Detection')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar(label='Prediction (-1: anomaly, 1: normal)')
plt.show()
