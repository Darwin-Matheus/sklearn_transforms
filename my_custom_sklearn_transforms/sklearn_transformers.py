from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

rm_columns = DropColumns(
columns=["NAME", "Unnamed: 0"])

    rm_columns.fit(X=df_data_1)


df_data_2 = pd.DataFrame.from_records(
    data=rm_columns.transform(
        X=df_data_1
    ),
)

si = SimpleImputer(
    missing_values=np.nan,
    strategy='constant',  
    fill_value=1,
    verbose=0,
    copy=True
)


si.fit(X=df_data_2)


df_data_3 = pd.DataFrame.from_records(
    data=si.transform(
        X=df_data_2
    ),
    columns=df_data_2.columns
)
df_data_3.head()


colum = [
    "USER_ID","HOURS_DATASCIENCE", "HOURS_BACKEND", "HOURS_FRONTEND",
    "NUM_COURSES_BEGINNER_DATASCIENCE", "NUM_COURSES_BEGINNER_BACKEND", "NUM_COURSES_BEGINNER_FRONTEND",
    "NUM_COURSES_ADVANCED_DATASCIENCE", "NUM_COURSES_ADVANCED_BACKEND", "NUM_COURSES_ADVANCED_FRONTEND",
    "AVG_SCORE_DATASCIENCE", "AVG_SCORE_BACKEND", "AVG_SCORE_FRONTEND"
]
datos=df_data_3[colum]
print(df_data_3.shape)

scaler=preprocessing.RobustScaler()
colu=scaler.fit(X=datos)

df_data_4 = pd.DataFrame.from_records(
    data=colu.transform(
       X=datos
   ),
    columns=datos.columns
)

datos=df_data_4
print(datos.shape)

scaler2=preprocessing.StandardScaler()
colu2=scaler2.fit(X=datos)

df_data_5 = pd.DataFrame.from_records(
   data=colu2.transform(
        X=datos
    ),
    columns=datos.columns
)			
	
