from PIL import ImageDraw, Image, ImageFont

def CertificateGenerator(names_and_paths, certificate_path):


    for name, output_path in names_and_paths.items():
        certificate = Image.open(certificate_path)
        draw = ImageDraw.Draw(certificate)
        
        font = ImageFont.truetype("arial.ttf", 50)
        x = 690
        y = 608
        
        draw.text((x, y), name, fill="black", font=font)
        
        certificate.save(output_path)

# Example usage
if __name__ == "__main__":
    names_and_paths = {
        "Kiran Rao": "Kiran_Certificate.png",
        "Conner Beach": "Conner_Certificate.png",
        "Hailey Black": "Hailey_Certificate.png"
    }
    certificate_path = "AppreciationCertificate.png"  # Path to your certificate template image
    CertificateGenerator(names_and_paths, certificate_path)

