import pandas as pd
# save filepath to variable for easier access
melbourne_file_path = r"C:\Users\user\OneDrive\デスクトップ\py\melb_data.csv"
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 
# print a summary of the data in Melbourne data
melbourne_data.describe()

melbourne_data.columns#选择建模数据
melbourne_data = melbourne_data.dropna(axis=0)#删除na值的行

y = melbourne_data.Price#选择预测目标
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']#选择 "特征" 列
X = melbourne_data[melbourne_features]
X.describe()#查看特征的统计信息
X.head()#查看前几行数据

#定义： 模型的类型是什么？决策树？其他类型的模型？还要指定模型类型的其他参数。
#拟合： 从提供的数据中捕捉模式。这是建模的核心。
#预测： 就像听起来一样
#评估： 确定模型预测的准确度。

#使用 scikit-learn 定义决策树模型并利用特征和目标变量进行拟合的示例。
from sklearn.tree import DecisionTreeRegressor

# 定义模型(决策树)。为 random_state 指定一个数字，以确保每次运行结果相同
melbourne_model = DecisionTreeRegressor(random_state=1)

#拟合模型
melbourne_model.fit(X, y)
print("Making predictions for the following 5 houses:")
print(X.head())#查看前5行特征
print("The predictions are")
print(melbourne_model.predict(X.head()))#预测前5行数据的房价

#验证模型
#在实际应用中，模型的随机性是不可避免的。去掉 random_state 参数可以让模型更接近实际应用场景，从而更好地评估模型在实际环境中的表现。
from sklearn.tree import DecisionTreeRegressor
# Define mode　定义模型
melbourne_model = DecisionTreeRegressor()
# Fit model训练模型
melbourne_model.fit(X, y)

#mean_absolute_error函数用于计算预测值与实际值之间的平均绝对误差。
from sklearn.metrics import mean_absolute_error
#使用已经训练好的 melbourne_model 模型对特征数据 X 进行预测，并将预测结果存储在 predicted_home_prices 变量中。
predicted_home_prices = melbourne_model.predict(X)
#mean_absolute_error 函数计算预测值与实际值 y 之间的平均绝对误差。
mean_absolute_error(y, predicted_home_prices)

#要衡量模型在未用于构建模型的数据上的性能。最直接的方法就是在建立模型的过程中排除一些数据
#然后用这些数据来测试模型在未见过的数据上的准确性。这些数据被称为验证数据。
#scikit-learn 库有一个 train_test_split 函数，用于将数据分成两部分。
#我们将使用其中的一些数据作为训练数据来拟合模型，并使用另一部分数据作为验证数据来计算均值绝对误差

from sklearn.model_selection import train_test_split
# 针对特征和目标，将数据分成训练数据和验证数据
# 分割基于随机数生成器。
# the random_state 能保证每次运行此脚本时都能获得相同的分割结果。
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))

#样本内数据的平均绝对误差约为 500 美元。而样本外数据的平均绝对误差则超过 25 万美元。
#这就是一个几乎完全正确的模型和一个无法用于大多数实际用途的模型之间的差别。

#欠拟合和过拟合
#微调您的模型以获得更好的性能。
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor

#定义函数，用于计算不同最大叶子节点数下的均值绝对误差
#定义了一个名为 get_mae 的函数，它接受五个参数,max_leaf_nodes：决策树模型的最大叶子节点数。
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)#创建一个决策树模型，并设置了两个参数：最大叶子节点数和随机数种子。
    model.fit(train_X, train_y)#模型训练
    preds_val = model.predict(val_X)#模型预测
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)
#通过这个函数，可以方便地评估不同最大叶子节点数对模型性能的影响，从而选择最优的模型参数。

# compare MAE with differing values of max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))
# %d 是格式化占位符，表示这里将插入一个整数。
# \t\t 是两个制表符，用于在输出中创建水平间距。
# %(max_leaf_nodes, my_mae) 这部分将变量 max_leaf_nodes 和 my_mae 插入到格式化字符串中。
#结论:500 是最佳的叶片数量。

#随机森林
#随机森林是一种集成学习方法，它结合了多个决策树的预测结果，以提高预测精度。
#scikit-learn 库提供了 RandomForestRegressor 类来实现随机森林。
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# 定义模型
forest_model = RandomForestRegressor(random_state=1)
# 训练模型
forest_model.fit(train_X, train_y)
# 预测
melb_preds = forest_model.predict(val_X)
# 计算均值绝对误差
print(mean_absolute_error(val_y, melb_preds))
#发现结果的均值绝对误差比决策树模型小很多。
#随机森林模型的最大特点之一是，即使不进行调整，它们一般也能合理地工作。


# 随机森林的优点：
# 2. 它能够处理缺失值，而决策树不能处理缺失值。
# 3. 它能够处理不平衡的数据，而决策树不行。
# 4. 它能够处理高维数据，而决策树不行。
# 5. 它能够处理多输出问题，而决策树不行。
# 6. 它能够处理多分类问题，而决策树不行。
# 7. 它能够处理多任务问题，而决策树不行。
# 8. 它能够处理时间序列问题，而决策树不行。
# 9. 它能够处理不相关特征，而决策树不行。

# 随机森林的缺点：
# 1. 它需要更多的计算资源，因为它需要训练多个决策树。
# 2. 它可能过拟合，因为它会训练太多决策树。
# 3. 它可能不稳定，因为它会随机选择特征。
# 4. 它可能不容易解释，因为它没有单一的决策树。
# 5. 它可能不适合处理高维数据，因为它需要更多的内存。
# 6. 它可能不适合处理不平衡的数据，因为它会偏向于较少的样本。
# 7. 它可能不适合处理多输出问题，因为它会产生多个预测值。

#处理缺失值
#随机森林可以处理缺失值，因为它使用了不同的算法来处理缺失值。
#scikit-learn 库提供了不同的算法来处理缺失值。
#一种方法是用平均值来填充缺失值。
#另一种方法是用众数来填充缺失值。
#我们将使用平均值填充缺失值。

#三种方法
#1) 简单选项： 删除缺失值列
#除非被删除列中的大部分值都是缺失的，否则采用这种方法后，模型将无法获取大量（可能有用的！）信息。
#2) 更好的选择： 估算
#估算是用一些数字填补缺失值。例如，填入每列的平均值。
#在大多数情况下，估算值不会完全正确，但通常会比完全放弃该列得到的模型更准确。
#3) 估算的扩展 添加一列新的列（身高列是估值：布尔值），显示估算条目的位置。

import pandas as pd
from sklearn.model_selection import train_test_split

# Load the data
data = pd.read_csv(r"C:\Users\user\OneDrive\デスクトップ\py\melb_data.csv")

# Select target
y = data.Price

# To keep things simple, we'll use only numerical predictors
melb_predictors = data.drop(['Price'], axis=1)
X = melb_predictors.select_dtypes(exclude=['object'])

# Divide data into training and validation subsets
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,
                                                      random_state=0)
#表示训练数据集占总数据集的 80% 验证数据集占总数据集的 20%。
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

#定义score_dataset() 函数,衡量比较处理缺失值的不同方法。该函数报告随机森林模型的平均绝对误差 (MAE)。
# Function for comparing different approaches
def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=10, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)

#方法 1 的得分（删除缺失值列）
#由于我们同时使用训练集和验证集，因此我们要注意在两个数据框中删除相同的列。

# 获取缺失值列的名称
#识别并列出训练数据 X_train 中存在缺失值的列名。通过遍历每一列并检查是否存在缺失值，最终生成一个包含所有存在缺失值列名的列表
cols_with_missing = [col for col in X_train.columns
                     if X_train[col].isnull().any()]


# Drop columns in training and validation data
reduced_X_train = X_train.drop(cols_with_missing, axis=1)
reduced_X_valid = X_valid.drop(cols_with_missing, axis=1)

print("MAE from Approach 1 (Drop columns with missing values):")
print(score_dataset(reduced_X_train, reduced_X_valid, y_train, y_valid))
#183550.22137772635

#使用 SimpleImputer 用每列的平均值替换缺失值。
from sklearn.impute import SimpleImputer

# Imputation
my_imputer = SimpleImputer()
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))

# Imputation removed column names; put them back
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns

print("MAE from Approach 2 (Imputation):")
print(score_dataset(imputed_X_train, imputed_X_valid, y_train, y_valid))
#178166.46269899711
#方法 2 的 MAE 低于方法 1，因此方法 2 在该数据集上的表现更好。

#方法 3 的得分（估算的扩展） 对缺失值进行估算，同时添加一列新的列，记录哪些值已被估算。
# Make copy to avoid changing original data (when imputing)
X_train_plus = X_train.copy()
X_valid_plus = X_valid.copy()

#X_valid_plus 数据框中创建一个相同的新列，列名为 col + '_was_missing'，布尔值表示每个元素是否为缺失值
# Make new columns indicating what will be imputed
for col in cols_with_missing:
    X_train_plus[col + '_was_missing'] = X_train_plus[col].isnull()
    X_valid_plus[col + '_was_missing'] = X_valid_plus[col].isnull()

# 使用每列的平均值来填充缺失值。
my_imputer = SimpleImputer()
imputed_X_train_plus = pd.DataFrame(my_imputer.fit_transform(X_train_plus))#fit_transform 方法首先在训练数据 X_train_plus 上计算每列的平均值，来填充 X_train_plus 中的缺失值。
imputed_X_valid_plus = pd.DataFrame(my_imputer.transform(X_valid_plus))#transform 方法使用之前在训练数据上计算的平均值来填充验证数据 X_valid_plus 中的缺失值。

# 由于 SimpleImputer 的 fit_transform 和 transform 方法返回的是 NumPy 数组，而不是 DataFrame，因此列名会丢失。
# 这两行代码将原始 DataFrame 的列名重新赋值给填充后的 DataFrame，以确保列名的一致性。
imputed_X_train_plus.columns = X_train_plus.columns
imputed_X_valid_plus.columns = X_valid_plus.columns

print("MAE from Approach 3 (An Extension to Imputation):")
print(score_dataset(imputed_X_train_plus, imputed_X_valid_plus, y_train, y_valid))
#178927.503183954
#方法 3 的表现略逊于方法 2。
#训练数据有 10864 行和 12 列，其中三列包含缺失数据。在每一列中，缺失的条目不到一半。
# 因此，去掉这些列会删除很多有用的信息，所以估算的效果会更好。

# Shape of training data (num_rows, num_columns)
print(X_train.shape)

missing_val_count_by_column = (X_train.isnull().sum())#  每列训练数据中缺失值的数量
print(missing_val_count_by_column[missing_val_count_by_column > 0])
#结论：通常情况下，估算缺失值（方法 2 和方法 3）比简单删除缺失值列（方法 1）的结果要好。

#分类变量
#比较三种准备分类数据的方法。
#1) 删除分类变量
#处理分类变量最简单的方法就是从数据集中删除它们。这种方法只有在这些列不包含有用信息的情况下才能奏效。

#2) 排序编码
#序数编码将每个唯一值分配给不同的整数。
#这种方法假定对类别进行排序： "从不"（0）<"很少"（1）<"大多数日子"（2）<"每天"（3）。
#并不是所有的分类变量的值都有明确的排序但我们把那些有明确排序的变量称为顺序变量。
# 对于基于树的模型（如决策树和随机森林），我们可以期待序数编码在处理序数变量时效果良好。

#3) 一热编码
#一热编码创建新列，表示原始数据中每个可能值的存在（或不存在）。为了理解这一点，我们先看一个例子。
#在原始数据集中，"颜色 "是一个分类变量，有三个类别： "红色"、"黄色 "和 "绿色"。如果原始值为 "红色"，我们就在 "红色 "一栏中填入 1；
#如果原始值为 "黄色"，我们就在 "黄色 "一栏中填入 1，以此类推。我们将这种没有内在排序的分类变量称为名义变量。
#如果分类变量的取值较多（例如，取值超过 15 个的变量一般不会使用单热编码
import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data
data = pd.read_csv('../input/melbourne-housing-snapshot/melb_data.csv')

# Separate target from predictors
y = data.Price
X = data.drop(['Price'], axis=1)

# Divide data into training and validation subsets
X_train_full, X_valid_full, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,
                                                                random_state=0)

# Drop columns with missing values (simplest approach)
cols_with_missing = [col for col in X_train_full.columns if X_train_full[col].isnull().any()] 
X_train_full.drop(cols_with_missing, axis=1, inplace=True)
X_valid_full.drop(cols_with_missing, axis=1, inplace=True)

# "Cardinality" means the number of unique values in a column
# Select categorical columns with relatively low cardinality (convenient but arbitrary)
low_cardinality_cols = [cname for cname in X_train_full.columns if X_train_full[cname].nunique() < 10 and 
                        X_train_full[cname].dtype == "object"]

# Select numerical columns
numerical_cols = [cname for cname in X_train_full.columns if X_train_full[cname].dtype in ['int64', 'float64']]

# Keep selected columns only
my_cols = low_cardinality_cols + numerical_cols
X_train = X_train_full[my_cols].copy()
X_valid = X_valid_full[my_cols].copy()

X_train.head()
#获得训练数据中所有分类变量的列表。我们要检查每一列的数据类型（或 dtype）。
#对于本数据集，带文本的列表示分类变量。
# Get list of categorical variables
s = (X_train.dtypes == 'object')
object_cols = list(s[s].index)

print("Categorical variables:")
print(object_cols)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Function for comparing different approaches
def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)

#方法 1（删除分类变量）的得分 select_dtypes() 方法删除对象列。
drop_X_train = X_train.select_dtypes(exclude=['object'])
drop_X_valid = X_valid.select_dtypes(exclude=['object'])

print("MAE from Approach 1 (Drop categorical variables):")
print(score_dataset(drop_X_train, drop_X_valid, y_train, y_valid))
#175703.48185157913

#方法 2 的得分（顺序编码）
#Scikit-learn 有一个 OrdinalEncoder 类，可以用来获取顺序编码。我们对分类变量进行循环，并对每一列分别应用顺序编码器。
from sklearn.preprocessing import OrdinalEncoder

# Make copy to avoid changing original data 
label_X_train = X_train.copy()
label_X_valid = X_valid.copy()

# Apply ordinal encoder to each column with categorical data
ordinal_encoder = OrdinalEncoder()
label_X_train[object_cols] = ordinal_encoder.fit_transform(X_train[object_cols])
label_X_valid[object_cols] = ordinal_encoder.transform(X_valid[object_cols])

print("MAE from Approach 2 (Ordinal Encoding):") 
print(score_dataset(label_X_train, label_X_valid, y_train, y_valid))
#165936.40548390493

#方法 3 的得分（单热编码）
from sklearn.preprocessing import OneHotEncoder

# Apply one-hot encoder to each column with categorical data
OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(X_train[object_cols]))
OH_cols_valid = pd.DataFrame(OH_encoder.transform(X_valid[object_cols]))

# One-hot encoding removed index; put it back
OH_cols_train.index = X_train.index
OH_cols_valid.index = X_valid.index

# Remove categorical columns (will replace with one-hot encoding)
num_X_train = X_train.drop(object_cols, axis=1)
num_X_valid = X_valid.drop(object_cols, axis=1)

# Add one-hot encoded columns to numerical features
OH_X_train = pd.concat([num_X_train, OH_cols_train], axis=1)
OH_X_valid = pd.concat([num_X_valid, OH_cols_valid], axis=1)

# Ensure all columns have string type
OH_X_train.columns = OH_X_train.columns.astype(str)
OH_X_valid.columns = OH_X_valid.columns.astype(str)

print("MAE from Approach 3 (One-Hot Encoding):") 
print(score_dataset(OH_X_train, OH_X_valid, y_train, y_valid))
#一般来说，单次编码（方法 3）的性能通常最好，而放弃分类列（方法 1）的性能通常最差，但具体情况具体分析。

#Pipeline用管道来清理建模代码。
#管道是让数据预处理和建模代码井井有条的一种简单方法。具体来说，管道捆绑了预处理和建模步骤，因此您可以像使用单一步骤一样使用整个捆绑。
#代码更整洁： 在预处理的每个步骤中对数据进行核算可能会变得混乱。有了管道，您就不需要在每个步骤中手动跟踪训练和验证数据了。
#错误更少： 错误应用步骤或忘记预处理步骤的机会更少。
#更易于生产： 要将一个模型从原型转变为可大规模部署的模型，可能会出乎意料地困难。我们不会在此讨论许多相关问题，但管道可以提供帮助。
#模型验证的更多选择： 您将在下一个教程中看到一个例子，其中涉及交叉验证。

#加载数据，得到训练集和验证集。
import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data
data = pd.read_csv('../input/melbourne-housing-snapshot/melb_data.csv')

# Separate target from predictors
y = data.Price
X = data.drop(['Price'], axis=1)

# Divide data into training and validation subsets
X_train_full, X_valid_full, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,
                                                                random_state=0)

# "Cardinality" means the number of unique values in a column
# Select categorical columns with relatively low cardinality (convenient but arbitrary)
categorical_cols = [cname for cname in X_train_full.columns if X_train_full[cname].nunique() < 10 and 
                        X_train_full[cname].dtype == "object"]

# Select numerical columns
numerical_cols = [cname for cname in X_train_full.columns if X_train_full[cname].dtype in ['int64', 'float64']]

# Keep selected columns only
my_cols = categorical_cols + numerical_cols
X_train = X_train_full[my_cols].copy()
X_valid = X_valid_full[my_cols].copy()

#数据既包含分类数据，也包含缺失值列。使用管道可以轻松处理这两种数据！
X_train.head()

#分三步构建完整的管道。
#步骤 1：定义预处理步骤
#与管道捆绑预处理和建模步骤的方式类似，我们使用 ColumnTransformer 类捆绑不同的预处理步骤。
#代码规则：计算数值数据中的缺失值，以及计算缺失值，并对分类数据进行单次编码。
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

# 数值数据的预处理
numerical_transformer = SimpleImputer(strategy='constant')

#分类数据的预处理
categorical_transformer = Pipeline(steps=[                #Pipeline用于将多个数据预处理步骤和模型训练步骤串联
    ('imputer', SimpleImputer(strategy='most_frequent')), #SimpleImputer 是一个用于填充缺失值的工具，strategy='most_frequent' 表示使用出现频率最高的值来填充缺失值。
    ('onehot', OneHotEncoder(handle_unknown='ignore'))   #定义了第二个步骤，名为 'onehot'，它使用 OneHotEncoder 类对分类数据进行独热编码。OneHotEncoder 将分类变量转换为二进制向量，以便机器学习模型能够处理这些数据。handle_unknown='ignore' 表示在遇到训练数据中未见过的类别时，忽略这些类别，不进行编码。#
])

#对数值数据和分类数据进行捆绑预处理
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),   #'num'：指定数值数据的预处理步骤，使用 numerical_transformer 处理 numerical_cols 列。
        ('cat', categorical_transformer, categorical_cols)
    ])

#步骤 2：定义模型
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, random_state=0)

#第 3 步：创建和评估管道¶ 。
#使用管道类来定义一个将预处理和建模步骤捆绑在一起的管道。
#有了管道，我们只需一行代码就能完成训练数据的预处理和模型拟合。
from sklearn.metrics import mean_absolute_error

# Bundle preprocessing and modeling code in a pipeline
my_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                              ('model', model)
                             ])

# Preprocessing of training data, fit model 
my_pipeline.fit(X_train, y_train)

# 预处理验证数据，获得预测结果
preds = my_pipeline.predict(X_valid)

# Evaluate the model
score = mean_absolute_error(y_valid, preds)
print('MAE:', score)

#XGBoost使用梯度提升技术构建和优化模型#
#梯度提升是一种集成学习方法，它通过将多个弱学习器（如决策树）的预测结果组合在一起，来构建一个强学习器（如随机森林）。
#它通过迭代的方式，逐步提升模型的性能。
#XGBoost 是一个开源的库，它实现了梯度提升算法。
#XGBoost 具有以下优点：
#1. 速度快：XGBoost 算法的速度非常快，它可以处理大数据集，并且在处理数据时不会过拟合。
#2. 准确性高：XGBoost 算法的准确性非常高，它可以处理高维度数据，并且可以自动处理缺失值。
#3. 灵活性强：XGBoost 算法的灵活性非常强，它可以处理不同的数据类型，并且可以自定义参数。
#4. 正则化：XGBoost 算法具有正则化功能，可以防止过拟合。
#5. 并行化：XGBoost 算法可以并行化处理数据，因此它可以提升处理速度。
#6. 便于使用：XGBoost 算法的使用非常简单，它只需要几行代码就可以实现模型的训练。
#7. 稳定性：XGBoost 算法的稳定性非常好，它可以处理各种类型的噪声，并且不会受到数据规模的影响。
#8. 适用于不同任务：XGBoost 算法可以用于分类、回归、排序和多类分类任务。

import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data
data = pd.read_csv(r"C:\Users\user\OneDrive\デスクトップ\py\melb_data.csv")
# Select subset of predictors
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]
# Select target
y = data.Price
# Separate data into training and validation sets
X_train, X_valid, y_train, y_valid = train_test_split(X, y)

from xgboost import XGBRegressor
my_model = XGBRegressor()
my_model.fit(X_train, y_train)

#对模型进行了预测和评估。
from sklearn.metrics import mean_absolute_error
predictions = my_model.predict(X_valid)
print("Mean Absolute Error: " + str(mean_absolute_error(predictions, y_valid)))

#参数调整  XGBoost几个参数会极大地影响准确性和训练速度。

#n_estimators
#设置集合中模型数量
my_model = XGBRegressor(n_estimators=500)
my_model.fit(X_train, y_train)
#n_estimators 指定了上述建模循环的次数。它等于我们在集合中包含的模型数量。
#数值太小会导致拟合不足，从而导致对训练数据和测试数据的预测都不准确。
#过高会导致过度拟合，从而导致对训练数据的预测准确，但对测试数据的预测不准确（这正是我们所关心的）。
#典型值范围在 100-1000 之间，不过这在很大程度上取决于下面讨论的学习率参数。

#early_stopping_rounds¶
#early_stopping_rounds 提供了一种自动寻找 n_estimators 理想值的方法。
# 早期停止会导致模型在验证得分停止提高时停止迭代，即使我们还没有达到 n_estimators 的硬停止值。
# 明智的做法是为 n_estimators 设置一个较高的值，然后使用 early_stopping_rounds 来找到停止迭代的最佳时间。
#由于随机机会有时会导致一轮验证分数没有提高，因此需要指定一个数字，说明在停止迭代之前允许多少轮分数直线下降。
# 设置 early_stopping_rounds=5 是一个合理的选择。在这种情况下，我们会在验证分数连续恶化 5 轮后停止。
#使用 early_stopping_rounds 时，还需要为计算验证分数预留一些数据，这可以通过设置 eval_set 参数来实现。
my_model = XGBRegressor(n_estimators=500)
my_model.fit(X_train, y_train, 
             early_stopping_rounds=5, 
             eval_set=[(X_valid, y_valid)],
             verbose=False)#不输出任何中间结果或进度信息
#如果以后想用所有数据拟合模型，可将 n_estimators 设为在提前停止运行时发现的最佳值。

#学习率 XGBoost 默认设置 learning_rate=0.1。
my_model = XGBRegressor(n_estimators=1000, learning_rate=0.05)
my_model.fit(X_train, y_train, 
             early_stopping_rounds=5, 
             eval_set=[(X_valid, y_valid)], 
             verbose=False)
#我们可以将每个模型的预测值乘以一个小数（称为学习率），然后再将它们加在一起，而不是简单地将每个组件模型的预测值相加。
#这意味着我们添加到集合中的每一棵树对我们的帮助都会减少。因此，我们可以为 n_estimators 设置一个较高的值，而不会过度拟合。
# 如果我们使用早期停止，那么合适的树数量就会自动确定。
#一般来说，较小的学习率和较多的估计器数量会产生更精确的 XGBoost 模型，但由于模型的迭代周期较长，因此训练时间也会更长。

#n_jobs¶
#通常将参数 n_jobs 设置为机器的内核数。在大型数据集上，如果不进行微优化，拟合命令的等待时间会很长，这时微优化就很有用了。
my_model = XGBRegressor(n_estimators=1000, learning_rate=0.05, n_jobs=4)
my_model.fit(X_train, y_train, 
             early_stopping_rounds=5, 
             eval_set=[(X_valid, y_valid)], 
             verbose=False)

#交叉验证 衡量模型性能。
#通常会保留约 20% 的数据作为验证数据集，即 1000 行。但这样在确定模型得分时会留下一些随机机会。
# 也就是说，一个模型可能在一组 1000 行数据上表现出色，但在另外 1000 行数据上却不准确。
#一般来说，验证集越大，我们衡量模型质量的随机性（又称 "噪音"）就越小，也就越可靠。
# 不幸的是，我们只能通过删除训练数据中的行来获得较大的验证集，而较小的训练数据集意味着较差的模型！

#我们可以先将数据分成 5 份，每份占整个数据集的 20%。在这种情况下，我们可以说已经将数据分成了 5 个 "折叠"。
#在实验 1 中，我们将第一个折叠数据作为验证（或保留）集，将其他所有数据作为训练数据。这样，我们就能根据 20% 的保留集来衡量模型质量。
#在实验 2 中，我们保留了第二个折叠的数据（并使用除第二个折叠以外的所有数据来训练模型）。然后使用保留集对模型质量进行第二次估计。
#我们重复这一过程，将每个折叠数据作为保留集使用一次。综上所述，100% 的数据都会在某个时刻被用作保留集，我们最终会得到基于数据集中所有行的模型质量度量（即使我们没有同时使用所有行）。

#对于小数据集来说，额外的计算负担并不是什么大问题，您应该运行交叉验证。
#对于较大的数据集，单个验证集就足够了。你的代码运行速度会更快，而且你可能拥有足够多的数据，几乎不需要重复使用其中的一些数据来进行保留。
#什么是大数据集，什么是小数据集，并没有一个简单的界限。但如果你的模型运行时间只需几分钟或更短，那么就值得改用交叉验证。

import pandas as pd
# Read the data
data = pd.read_csv(r"C:\Users\user\OneDrive\デスクトップ\py\melb_data.csv")
# Select subset of predictors
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]
# Select target
y = data.Price

#创建管道填充缺失值，并拟合模型。
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
my_pipeline = Pipeline(steps=[('preprocessor', SimpleImputer()),
                              ('model', RandomForestRegressor(n_estimators=50,
                                                              random_state=0))
                             ])

#使用 scikit-learn 的 cross_val_score() 函数获取交叉验证得分。使用 cv 参数设置折叠数。
from sklearn.model_selection import cross_val_score
# 乘以-1，因为 sklearn 计算的 MAE 为*负值
scores = -1 * cross_val_score(my_pipeline, X, y,
                              cv=5,
                              scoring='neg_mean_absolute_error')#负的平均绝对误差
print("MAE scores:\n", scores)
print("Average MAE score (across experiments):")
print(scores.mean())
#取实验的平均值，衡量模型质量。277707.3795913405


#深度学习是一种以深度计算堆栈为特征的机器学习方法。
#凭借其强大的功能和可扩展性，神经网络已成为深度学习的定义模型。
#神经网络由神经元组成，每个神经元只能单独进行简单的计算。神经网络的强大功能来自于这些神经元所能形成的复杂连接。

#线性单元
#让我们从神经网络的基本组成部分开始：单个神经元。
#训练一个以 "糖"（每份食物的糖克数）为输入、"卡路里"（每份食物的卡路里）为输出的模型，
# 我们可能会发现偏差为 b=90，权重为 w=2.5。我们可以这样估算每份含 5 克糖的麦片的卡路里含量：

#多重输入
#为神经元添加更多的输入连接，每增加一个特征就添加一个。为了找到输出，我们会将每个输入乘以其连接权重，然后将它们相加。

#Keras 中的线性单元
#在 Keras 中创建模型的最简单方法是通过 keras.Sequential，它将神经网络创建为一个层栈。
#我们可以像这样定义一个线性模型，接受三个输入特征（"糖"、"纤维 "和 "蛋白质"）并产生一个输出（"卡路里"）：
from tensorflow import keras
from tensorflow.keras import layers

# 创建一个有 1 个线性单元的网络
model = keras.Sequential([
    layers.Dense(units=1, input_shape=[3])#接受三个输入特征
])

#深度神经网络
#关键思想是模块化，即从较简单的功能单元构建复杂的网络。
#神经网络通常将神经元分为若干层。当我们将具有一组共同输入的线性单元集合在一起时，就会得到一个密集层。
#激活功能
#如果没有激活函数，神经网络只能学习线性关系。为了拟合曲线，我们需要使用激活函数。
#激活函数就是我们应用于每一层输出（激活）的函数。最常见的是整流函数 max(0,x)
#当我们将整流器连接到线性单元时，就得到了整流线性单元或 ReLU。(因此，整流函数通常被称为 "ReLU 函数"）。
# 将 ReLU 激活应用于线性单元，意味着输出变为 max(0，w * x + b)
#堆叠密集图层
#输出层之前的层有时被称为隐藏层，因为我们无法直接看到它们的输出。
#最后（输出）层是一个线性单元（即没有激活函数）。这使得该网络适用于回归任务，即我们试图预测某个任意数值。
#构建顺序模型  第一层获取输入，最后一层产生输出。
from tensorflow import keras
from tensorflow.keras import layers
# 创建一个有 2 个隐藏层的网络
model = keras.Sequential([
    # the hidden ReLU layers
    layers.Dense(units=4, activation='relu', input_shape=[2]),
    layers.Dense(units=3, activation='relu'), 
    layers.Dense(units=1), #线性输出层
])

#随机梯度下降
#训练数据中的每个示例都包含一些特征（输入）和一个预期目标（输出）。训练网络意味着调整其权重，使其能够将特征转化为目标。
#除了训练数据，我们还需要:衡量网络预测结果好坏的 "损失函数"。一个 "优化器"，告诉网络如何改变权重。
#损失函数 告诉网络要解决什么问题。
#损失函数衡量的是目标真实值与模型预测值之间的差距。

#回归问题常用的损失函数是平均绝对误差或 MAE。
#对于每个预测结果 y_pred，MAE 用绝对差值 abs（y_true - y_pred）来衡量与真实目标 y_true 之间的差距。
#数据集的总 MAE 损失是所有这些绝对差值的平均值。