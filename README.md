ML is important！
# Machine-Learning

目录 | 描述
--|--
[XGBoost]() | 从xgboost调用XGBClassifier完成花卉的分类

## 集成学习
### Boosting和Bagging的区别
Boosting(提升方法) | Bagging 群体决策方法
--|--
**基分类器的生成**|
基分类器串行训练，训练好当前，再去训练下一个 | 基分类器并行训练，多个基分类器之间互不影响
**方差、偏差角度**|
侧重于出错的样本，致力于减小集成分类器的偏差 | 对训练样本多次采样（样本多分成多个子集，样本较少子集可能交叠），训练多个不同的模型，致力于平衡数据，减小集成分类器方差
**常用的算法**|
GBDT(工程实现为xgboost) | RandomForest
**合并基分类器的方式**|
stacking | voting

### GBDT和XGBoost的区别
GBDT(梯度提升决策数)|XGBoost
--|--
**关系**|xgboost是GBDT的工程实现
**基分类器**
CART|除CART还支持线性分类器
**优化**
|添加了正则项
训练时使用损失函数的一阶导数|对代价函数二阶泰勒展开，同时使用一阶导数和二阶导数
**数据**
每次迭代使用全部数据|支持对数据的采样
|对缺失值进行填充

## 树模型原理
### CART原理

### GBDT原理

### xgboost原理

### lightGBM原理

### catboost原理

## 监督学习经典方法
### svm(支持向量机)
### logistic regression（逻辑斯特回归）

