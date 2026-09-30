import qrcode as qr
from PIL import Image, ImageDraw

upi_id = input("Enter your UPI ID :-")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

phonepe_upi = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_upi = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

google_pay_upi = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

phonepe_qr = qr.make(phonepe_upi)
paytm_qr = qr.make(paytm_upi)
google_qr = qr.make(google_pay_upi)

phonepe_qr.save("phonepe_qr.png")

phonepe_qr.show()
