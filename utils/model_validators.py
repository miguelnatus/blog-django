from django.core.exceptions import ValidationError

def validate_icon(image):
    if not image.name.lower().endswith('.png'):
        raise ValidationError('A imagem precisa ser .png, .jpg ou .ico!')