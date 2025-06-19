from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import seaborn as sns


n_estimators = 100
random_state = 0

data = sns.load_dataset('titanic')
data = data.drop(columns=['deck', 'alive'])
data = data.dropna()
cat_cols = data.select_dtypes(include=['object', 'category']).columns

le = LabelEncoder()
for col in cat_cols:
    data[col] = data[col].astype(str)
    data[col] = le.fit_transform(data[col])

X_train, X_test, y_train, y_test = train_test_split(
    data.drop(columns='survived'), data.survived, test_size=0.2, random_state=42
)

random_forest_classifier = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
random_forest_classifier.fit(X_train, y_train)
y_pred = random_forest_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision_recall_fscore = precision_recall_fscore_support(y_test, y_pred, average='binary')
