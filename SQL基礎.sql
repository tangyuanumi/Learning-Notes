select* from テーブル　*は全ての列　全検索
select 列名　from　テーブル　where　条件　--条件つき検索
insert into テーブル (列名1,列名2,)　values ("追加数値")　--按列追加データ　
insert into テーブル 　values ("追加数値")　--追加一整行データ　
update テーブル　set a列＝数値　where b列＝数値　--データの更新
delete from テーブル　where 条件　--データ削除
select* from テーブル as 別名　--asを使って別名を定義

delete from テーブル　where 条件 --where条件
= < > >= <= <>或=!　null 空集合
select 列名　from　テーブル　where　列名 is not null　--is null
--%・・・任意の0文字以上の文字   _・・任意の1文字
select 列名　from　テーブル　where　列名 like'%文字%'--likeで文字列を探す
/*betweenで範囲検索 */　
select* from テーブル　where 列名　between 100 and 200
--IN 演算子は、指定されたリスト内の値と一致する行を選択します。
SELECT * FROM table_name WHERE column_name IN (value1, value2, ...)
--not in 指定されたリスト内の値と一致しない行を選択します。
SELECT * FROM table_name WHERE column_name NOT IN (value1, value2, ...);
--any all　演算子
--優先順位
SELECT * FROM table_name WHERE (列名１='数値1'OR　列名1='数値2')
AND(列名2='数値3'OR 列名2='数値4')
--distinct 重複行除外
select distinct 列名 from テーブル
--order by　並び替え
select * from テーブル　order by 列名　--昇順
select * from テーブル　order by 列名 desc --降順
select * from テーブル　order by 列名 desc,列名2　desc --前後がある複数列の並び替え
select * from テーブル　order by 2 desc,3　desc --列番号指定の複数列の並び替え
--行数を限定して取得
select 列名　from テーブル　order by 列名
offset 先頭から除外する行数　rows
fetch next 取得行数　rows only
集合
select 列名a,列名b,列名c from テーブル　
union　　　　　　　　　　　　　　--和集合(except差集合）(intersect重複結合）
select 列名a,列名b,列名c from テーブルa
order by 2,3,1

--選択列リスト　
select 列名1,列名2　from テーブル
--case演算子
select 列名　case when 条件１/値１　then 返す値 case when 条件2/値2　then 返す値
else 値の設定 end as 返す値の列名　from テーブル　where 条件
--length/len関数 文字列の長さを表す
select 列名,length(列名) as 別名　from　テーブル
--空白除去関数 trim ltrim rtrim(左右、左、右）
select 列名,trim(列名) as 別名　from　テーブル
--replace 文字列の置き換え関数
update テーブル　set 列名=replace(列名,'文字列1','文字列2')
--文字列一部の抽出
WHERE substring/substr (列名,抽出開始位置,抽出文字数) LIKE　%'文字列'%
--文字列連結
select concat (列名1,列名2) from	テーブル
--round関数
round(列名,四捨五入の桁数）正は小数点以下桁数、負は整数桁数
--trunc関数 指定桁を切り捨てる
 trunc (列名,切り捨ての桁数）正は小数点以下桁数、負は整数桁数
 --power関数　べき乗の計算
 power(列名,	次方数)
--日付関数 
current_timestamp 秒到年 current_time 年月日 current_date 时分秒 只代表数值
--cast関数 データ型を変換
cast(値　as 変換する型)
--coalesce関数　最初に登場するnullでない値を返す
select coalesce (null,'B','C'); --結果はＢ
sum(列名) as　新列名 --sum 集計
--他の集計関数 max min avg count行数
distinct(列名)　重複除外
--nullをゼロとして平均値
select avg(cloaesce(列名,0))　as 新列名　from テーブル
--列名でグループ化してそれぞれの合計を求め
select 列名,sum(数字列) as 合計額　from テーブル(where 条件)　
　group by 行　having(集計結果に対する絞り込み条件) order by 列名
--in条件式
select*　from	テーブル　where 列名 in(項目)
--副問い合わせからnullを除外する
select*　from　テーブル　where 列名　in(select 列名　from テーブル where 列名　is not null)
select*　from　テーブル　where 列名　in(select coalesce(費目,'不明')from　テーブル)
--テーブル結合方法
select 選択列リスト　from テーブル１　join　デーブル２ on 結合条件
--左外部結合（LEFT OUTER JOIN）
SELECT * FROM table1
LEFT OUTER JOIN table2 ON table1.column = table2.column;
--右外部結合（RIGHT OUTER JOIN）
SELECT *FROM table1
RIGHT OUTER JOIN table2 ON table1.column = table2.column;
--完全外部結合（FULL OUTER JOIN）左右のテーブルのすべての行を結合
SELECT *FROM table1
FULL OUTER JOIN table2 ON table1.column = table2.column;
--内部結合（INNER JOIN）: 共通する行のみを結合
SELECT *FROM table1
INNER JOIN table2 ON table1.column = table2.column;

--共有ロック
BEGIN TRANSACTION; -- トランザクションの開始
SELECT * FROM products FOR SHARE; -- トランザクションの開始
COMMIT; -- ロックの解放とトランザクションの終了
--排他ロック
BEGIN TRANSACTION; -- トランザクションの開始
SELECT * FROM orders WHERE order_id = 12345 FOR UPDATE; -- 排他ロックの取得
UPDATE orders SET quantity = 10 WHERE order_id = 12345; -- データの更新（例えば、数量の変更）
COMMIT;
--テーブルのロック
begin
lock table テーブル名　in モード名　mode
commit
--行ロック
select 行名　for update(nowait)
--表ロック(排他ロックexclusive,共有ロックshare)
lock table テーブル名　in モード名 mode(nowait)
--権限の付与と剝奪
grant 権限名 to ユーザー名
revoke 権限名　from ユーザー名

--テーブルの作成と削除
CREATE TABLE テーブル名 (
    列名1 データ型1,
    列名2 データ型2,
    ...
	);

CREATE TABLE テーブル名 (
列名1 データ型1 DEFAULT デフォルト値1,
列名2 データ型2 DEFAULT デフォルト値2,
 ...
);

drop table テーブル名
--テーブルの列の追加と削除
ALTER TABLE テーブル名 ADD 列名 データ型;
ALTER TABLE テーブル名 DROP COLUMN 列名;
--テーブルの存在を確認してから作成と削除
create table if not exists テーブル名;
drop table if exists テーブル名;
create or replace table テーブル名;
--制約指定を含むテーブルの作成
-- NOT NULL 制約 列に :NULL 値が挿入されないことを保証します。
CREATE TABLE テーブル名 (         
    列名1 データ型1 NOT NULL,
    列名2 データ型2,
    ...
);
--UNIQUE 制約: 列に一意の値が含まれることを保証します。
CREATE TABLE テーブル名 (
    列名1 データ型1 UNIQUE,
    列名2 データ型2,
    ...
);
--CHECK 制約: 列に挿入できる値の範囲や条件を指定します。
CREATE TABLE テーブル名 (
    列名1 データ型1 CHECK (条件),
    列名2 データ型2,
    ...
);
--主キー制約 (PRIMARY KEY): テーブル内の行を一意に識別するための列または列の組み合わせを指定します。
CREATE TABLE テーブル名 (
    列名1 データ型1 PRIMARY KEY,
    列名2 データ型2,
    ...
);
--複合主キー
CREATE TABLE テーブル名 (
    列名1 データ型1 UNIQUE,
    列名2 データ型2,
    PRIMARY KEY(列名1,列名2)
);
--外部キー制約 (FOREIGN KEY): 他のテーブルの列に対する参照整合性を強制します。
CREATE TABLE テーブル名 (
    列名1 データ型1 REFERENCES 参照テーブル名(参照列名),
    列名2 データ型2 REFERENCES 参照テーブル名(参照列名),
    ,
    ...
);
--インデックスの作成と削除
CREATE INDEX インデックス名 ON テーブル名 (列名);
drop index インデックス名
