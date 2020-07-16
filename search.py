import pandas as pd


df = pd.read_csv('서울특별시 공공자전거 대여소 정보_20191209_csv.csv', engine='python')
df = df.dropna(axis=0)
df = df[['대여소ID', '대여소명', '대여소주소', '위도', '경도']]
df['대여소ID'] = df['대여소ID'].astype('object')

def run():
    name = input("대여소 검색:")
    id_list = [int(df['대여소ID'][i]) for i, n in enumerate(df['대여소명']) if name in n]
    name_list = [df['대여소명'][i].split('.')[1].lstrip() for i, n in enumerate(df['대여소명']) if name in n]
    print()
    for i in range(len(id_list)):
        print("대여소ID:", id_list[i], "\t대여소명:", name_list[i])


if __name__ == '__main__':
    run()
