from django.db import models

AVALABILITY = (("danger","午前中"),("info","午後"),("success","夜"))

class ProfileModel(models.Model):
    name = models.CharField("名前",max_length=20)
    age = models.IntegerField("年齢")
    avalability = models.CharField(
        max_length = 50,
        choices = AVALABILITY
        )
    description = models.TextField("説明")

    birhday = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "profile"


# クラスには、model と記入する

# Create your models here.

# モデルとは→データベースのテーブル定義
# →最初の②行は、Djaogoがもともと持っているものを使うと宣言しているだけ

# CharfieldとTextは、長さ指定の有無
        # db_table = "profile"で、テーブルの名前（定義しないと、Djaongが勝手に名前をつける）
