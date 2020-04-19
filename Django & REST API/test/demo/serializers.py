from rest_framework import serializers
from demo.models import Book,Number,Character,Author

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Character
        fields = ["id",'name',]


class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Number
        fields = ['bal1',"id"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields = ["id",'name',"surname"]


class BookMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = ["id","Title",]


class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    characters = CharacterSerializer(many=True)
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book 
        fields = ["id","Title","Description","Status","Price","number","characters","authors"]

