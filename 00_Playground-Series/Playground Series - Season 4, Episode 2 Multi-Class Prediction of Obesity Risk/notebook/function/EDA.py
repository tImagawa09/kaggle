import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(df, target_column=None):
    # 基本統計量の表示
    print("基本統計量:")
    print(df.describe(include='all'))
    
    # データ型と欠損値の確認
    print("\nデータ型と欠損値:")
    print(df.info())

    # 欠損値の可視化
    print("\n欠損値の可視化:")
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.title('Missing values in the dataset')
    plt.show()

    # 各列のユニーク値の確認
    for column in df.columns:
        print(f"\n{column} のユニーク値の数: {df[column].nunique()}")

    # カテゴリカルデータと数量データの分布の可視化
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    numerical_columns = df.select_dtypes(exclude=['object', 'category']).columns

    for column in categorical_columns:
        plt.figure(figsize=(10, 5))
        sns.countplot(x=column, data=df)
        plt.title(f'{column} の分布')
        plt.xticks(rotation=45)
        plt.show()

    for column in numerical_columns:
        plt.figure(figsize=(10, 5))
        sns.histplot(df[column], kde=True)
        plt.title(f'{column} のヒストグラム')
        plt.show()

    # 目的変数が指定されている場合、目的変数との関係を可視化
    if target_column and target_column in df.columns:
        if target_column in numerical_columns:
            for column in numerical_columns:
                if column != target_column:
                    plt.figure(figsize=(10, 5))
                    sns.scatterplot(x=column, y=target_column, data=df)
                    plt.title(f'{column} と {target_column} の関係')
                    plt.show()

        if target_column in categorical_columns:
            for column in categorical_columns:
                if column != target_column:
                    plt.figure(figsize=(10, 5))
                    sns.boxplot(x=column, y=target_column, data=df)
                    plt.title(f'{column} と {target_column} の関係')
                    plt.xticks(rotation=45)
                    plt.show()
