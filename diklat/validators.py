from django.core.exceptions import ValidationError

def validate_nip(value):
	nip = value
	if nip == 123456:
		message = "NIP : " + nip + " sudah terdafnntar"
		raise ValidationError(message)
