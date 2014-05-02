
from rest_framework import serializers
from api.models import Email


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('id', 'user_name', 'user_email', 'domain', 'url_path', 'comment')
