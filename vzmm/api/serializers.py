from django.forms import widgets
from rest_framework import serializers
from snippets.models import Email


class EmailSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    user_name = serializers.CharField(required=True,
                                  max_length=100)
    user_email = serializers.EmailField(required=True)
    domain = serializers.CharField(required=False, 
                                max_length=50)
    url_path = serializers.CharField(required=False,
                                max_length=150)
    comment = serializers.CharField(widget=widgets.Textarea,
                                max_length=100000)


    def restore_object(self, attrs, instance=None):
        """
        Create or update a new email instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.user_name = attrs.get('user_name', instance.user_name)
            instance.user_email = attrs.get('user_email', instance.user_email)
            instance.domain = attrs.get('domain', instance.domain)
            instance.url_path = attrs.get('url_path', instance.url_path)
            instance.comment = attrs.get('comment', instance.comment)
            return instance

        # Create new instance
        return Email(**attrs)