import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from models import EmailRequest

class EmailService:
    def __init__(self):
        self.smtp_host = os.getenv("SMTP_HOST", "")
        self.smtp_port = int(os.getenv("SMTP_PORT", "587"))
        self.smtp_user = os.getenv("SMTP_USER", "")
        self.smtp_password = os.getenv("SMTP_PASSWORD", "")
        self.from_email = os.getenv("FROM_EMAIL", "")
        self.enabled = all([self.smtp_host, self.smtp_user, self.smtp_password])
    
    async def send_compliment(self, email_request: EmailRequest) -> dict:
        """Send a compliment via email."""
        
        if not self.enabled:
            return {
                "success": False,
                "message": "Email service not configured"
            }
        
        try:
            # Create email
            message = MIMEMultipart("alternative")
            message["Subject"] = f"A Nurtured Heart Compliment for {email_request.recipient_name}"
            message["From"] = self.from_email
            message["To"] = email_request.recipient_email
            
            # Email body
            html = f"""
            <html>
                <body style="font-family: Arial, sans-serif; padding: 20px; max-width: 600px; margin: 0 auto;">
                    <h2 style="color: #4a5568;">You've received a Nurtured Heart compliment! 💙</h2>
                    <p style="font-size: 14px; color: #718096;">From: {email_request.sender_name}</p>
                    
                    <div style="background-color: #f7fafc; border-left: 4px solid #4299e1; padding: 20px; margin: 20px 0;">
                        <p style="font-size: 16px; line-height: 1.6; color: #2d3748; font-style: italic;">
                            {email_request.compliment}
                        </p>
                    </div>
                    
                    <p style="font-size: 14px; color: #718096; margin-top: 30px;">
                        This compliment was generated with care using the Nurtured Heart Approach.
                    </p>
                </body>
            </html>
            """
            
            text = f"""
            You've received a Nurtured Heart compliment!
            
            From: {email_request.sender_name}
            
            {email_request.compliment}
            
            ---
            This compliment was generated with care using the Nurtured Heart Approach.
            """
            
            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")
            message.attach(part1)
            message.attach(part2)
            
            # Send email
            await aiosmtplib.send(
                message,
                hostname=self.smtp_host,
                port=self.smtp_port,
                username=self.smtp_user,
                password=self.smtp_password,
                start_tls=True
            )
            
            return {
                "success": True,
                "message": f"Compliment sent to {email_request.recipient_email}"
            }
            
        except Exception as e:
            return {
                "success": False,
                "message": f"Failed to send email: {str(e)}"
            }

email_service = EmailService()

